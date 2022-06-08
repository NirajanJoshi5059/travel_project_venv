from django.urls import path
from useraccount.views import login_view, register_view,dashboard

app_name='user'

urlpatterns=[ 
    path('login/', login_view, name='login'),
    path('register/',register_view, name='register'),
    path('dashboard/',dashboard, name='dashboard'),
]