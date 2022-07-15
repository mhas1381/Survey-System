from django.urls import path
from polls.views import *
app_name='polls'

urlpatterns = [
    path('poll', index, name='polls'),
    path('vote', vote, name='vote'),
    path('result', result, name='result')
]
