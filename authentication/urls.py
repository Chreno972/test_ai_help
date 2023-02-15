from django.urls import path, include
from .views import register_page, login_page, home_page, logout_user, user_dashboard

app_name = 'authentication'

urlpatterns = [
    path('', home_page, name='home'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('dashboard/', user_dashboard, name='dashboard'),
]
