from django.urls import path
from . import views   #"Import views.py from the same folder where this file lives" (blog) "

urlpatterns = [
    path('', views.home, name='blog-home'), #The '' just means "nothing after blog" — it's the homepage of the blog section
     path('about/', views.about, name='blog-about'),
]
                            # 'blog/'  +  ''       →  /blog/
                            # 'blog/'  +  'about/' →  /blog/about/