# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.core.paginator import Paginator
from datetime import datetime
from pymongo import MongoClient
import json
import re

mongodb_client = MongoClient('mongodb+srv://cluster0.cpy5tdw.mongodb.net', username='peiyu', password='1')
db = mongodb_client["test"]
collection = db["tweets"]

@login_required(login_url="/login/")
def dashboard(request):
    documents = list(collection.find())
    total_count = len(documents)

    avg_favourites = collection.aggregate([
        {
            "$group": {
                "_id": None,
                "avg_favourites": {
                    "$avg": {
                        "$toInt": "$user.favourites_count"
                    }
                }
            }
        }
    ])

    avg_followers = collection.aggregate([
        {
            "$group": {
                "_id": None,
                "avg_followers": {
                    "$avg": {
                        "$toInt": "$user.followers_count"
                    }
                }
            }
        }
    ])

    avg_friends = collection.aggregate([
        {
            "$group": {
                "_id": None,
                "avg_friends": {
                    "$avg": {
                        "$toInt": "$user.friends_count"
                    }
                }
            }
        }
    ])

    avg_favourites = int(list(avg_favourites)[0]['avg_favourites'])
    avg_followers = int(list(avg_followers)[0]['avg_followers'])
    avg_friends = int(list(avg_friends)[0]['avg_friends'])

    pipeline = [
    {
        "$group": {
            "_id": {
                "$dateToString": {
                    "format": "%Y-%m",
                    "date": {
                        "$toDate": "$user.created_at"
                    }
                }
            },
            "total_users": {
                "$addToSet": "$user.id"
            }
        }
    },
    {
        "$sort": {
            "_id": 1
        }
    },
    {
        "$project": {
            "_id": 1,
            "user_count": {
                "$size": "$total_users"
            }
        }
    }
]

    result = collection.aggregate(pipeline)

    # Extract the dates and user counts from the aggregation result
    dates = []
    user_counts = []

    for doc in result:
        dates.append(doc['_id'])
        user_counts.append(doc['user_count'])
    dates_json = json.dumps(dates)
    user_counts_json = json.dumps(user_counts)

    # Pie
    pipeline = [
        {
            "$group": {
                "_id": {
                    "$cond": {
                        "if": { "$eq": ["$source", "web"] },
                        "then": "web",
                        "else": "others"
                    }
                },
                "count": { "$sum": 1 }
            }
        },
        {
            "$project": {
                "_id": 0,
                "source": "$_id",
                "count": 1
            }
        }
    ]

    result = list(collection.aggregate(pipeline))

    if result:
        sources = [doc['source'] for doc in result]
        counts = [doc['count'] for doc in result]

        sources_json = json.dumps(sources)
        counts_json = json.dumps(counts)
    else:
        sources_json = "[]"
        counts_json = "[]"

    pipeline = [
        {
            "$match": {
                "user.location": {"$ne": ""}
            }
        },
        {
            "$group": {
                "_id": "$user.location",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 11
        }
    ]

    result = collection.aggregate(pipeline)

    labels = []
    data = []

    for item in result:
        location = item['_id']
        count = item['count']

        if location != None:
            labels.append(location)
            data.append(count)

    labels = labels[:10]
    data = data[:10]

    pipeline = [
        {
            "$sort": {"user.followers_count": -1}
        },
        {
            "$limit": 5
        },
        {
            "$project": {
                "_id": "$user.id",
                "followers_count": "$user.followers_count",
                "screen_name": "$user.screen_name",
                "location": "$user.location"
            }
        }
    ]

    top_users = list(collection.aggregate(pipeline))

    pipeline = [
        {
            "$unwind": "$entities.hashtags"
        },
        {
            "$group": {
                "_id": "$entities.hashtags.text",
                "count": { "$sum": 1 }
            }
        },
        {
            "$sort": { "count": -1 }
        },
        {
            "$limit": 5
        }
    ]

    hashtag_result = collection.aggregate(pipeline)

    hashtag_counts = [(doc['_id'], doc['count']) for doc in hashtag_result]

    totalcount = sum(count for _, count in hashtag_counts)

    hashtag_counts = [(hashtag, count, round((count / totalcount) * 100, 2)) for hashtag, count in hashtag_counts]

    context = {
        'segment': 'index',
        'total_count': total_count,
        'avg_favourites': avg_favourites,
        'avg_followers': avg_followers,
        'avg_friends': avg_friends,
        'dates': dates_json,
        'user_counts': user_counts_json,
        'sources': sources_json,
        'counts': counts_json,
        'labels': labels,
        'data': data,
        'top_users': top_users,
        'hashtag_counts': hashtag_counts,
    }

    return render(request, 'home/dashboard.html', context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
