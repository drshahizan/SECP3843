from django.shortcuts import render
from django.contrib import messages
import pymongo
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

def index(request):
    
    if request.method == 'POST':
        myclient = pymongo.MongoClient()
        mydb = myclient["mflix"]
        mycol = mydb["movies"]

        mydoc = mycol.find()

        df = pd.DataFrame(list(mydoc))
        
        titles = df['title']
        indices = pd.Series(df.index, index=df['title'].str.lower())
        title = request.POST.get('title')
        title = title.lower()
        
        if title in indices.index:
        
            df['fullplot'] = df['fullplot'].fillna('')
            
            tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
            tfidf_matrix = tf.fit_transform(df['fullplot'])
            
            cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
            idxlist = []
            metas = []
            desc = []
            results = []
            idx = indices[title]
            if(isinstance(idx, np.integer)):
                idxlist.append(idx)
                idx = idxlist
            for i in idx:
                sim_scores = list(enumerate(cosine_sim[i]))
                sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
                sim_scores = sim_scores[1:21]
                movie_indices = [i[0] for i in sim_scores]
                meta = str(titles.iloc[i]) + ' (' + str(df.iloc[i]['year']) + ') ' + str(df.iloc[i]['countries'])
                metas.append(meta)
                desc.append(df.iloc[i]['fullplot'])
                tdf = titles.iloc[movie_indices].head(20).tolist()
                results.append(tdf)
            return render(request, 'recommender/index.html', {'recommendations': zip(metas, desc, results), "title": title})
        else:
            messages.error(request, 'Movie not found.')
            return render(request, 'recommender/index.html', {"title": title})
    return render(request, 'recommender/index.html')
