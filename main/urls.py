from django.urls import path
from main.views import homepage, about

app_name = 'main'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about.html', about, name='about'),
]