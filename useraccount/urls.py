from django.urls import path
from useraccount.views import login_view

app_name='user'

urlpatterns=[ 
    path('', login_view, name='login')
]