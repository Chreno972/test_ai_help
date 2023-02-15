from django.urls import path
from authentication.views import user_dashboard

app_name = 'dashboard'

urlpatterns = [
    path('', user_dashboard, name='dashboard'),
]
