from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Posts"),
    path('post/create/', views.create_post, name='post-create'),
    # path('about/', views.about, name='about'),
]
