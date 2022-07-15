from django.urls import path
from polls.views import *

urlpatterns = [
    path('', index, name='index'),
    path('vote', vote, name='vote'),
    path('result', result, name='result')
]
