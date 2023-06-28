from django.urls import path
from django.urls import re_path
from .views import index,customer, technical_worker, senior_management,top_5_topic,top_5_by_comments


urlpatterns = [
    path('', index, name='index'),
    path('customer/', customer, name='customer'),
    path('technical_worker/', technical_worker, name='technical_worker'),
    path('senior_management/', senior_management, name='senior_management'),
    path('top_5_topic/', top_5_topic, name='top_5_topic'),
    path('top_5_by_comments/', top_5_by_comments, name='top_5_by_comments'),

]