from django.urls import path
from .views import (PostDetailView, 
                    PostListView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView)
from . import views
urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
]
#naming convention post_form for createpost
# post_detail for details
