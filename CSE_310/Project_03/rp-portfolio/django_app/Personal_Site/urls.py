from django.urls import path
from . import views 

### The code below creates a path to get accessed to the web page.
### Line 8 is  the default path. The pattern matches to an empty route so it can be the home page.

urlpatterns = [
    path('', views.home, name='Personal_Site-home'),
    path('summary/', views.summary, name='Personal_Site-summary'),
    path('posts/', views.post, name='Personal_Site-posts'),
]
