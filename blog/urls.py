from django.urls import path, include
from .views import PostListView, PostDetailView , PostCreateView ,PostUpdateView , PostDeleteView
urlpatterns = [
    path("", PostListView.as_view(), name="page_one"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/update",PostUpdateView.as_view(), name="post_update"),
    path("<int:pk>/delete",PostDeleteView.as_view(), name="post_delete")
]

