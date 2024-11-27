from django.urls import path

from .views import index, detail, category

app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:id>/", detail, name="post_detail"),
    path("category/<slug:category_slug>/", category, name="category_posts"),
]
