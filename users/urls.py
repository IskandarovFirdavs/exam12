from django.urls import path
from users.views import login_view, registration_view, logout_view

app_name = 'users'
urlpatterns = [
    path('', login_view, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
