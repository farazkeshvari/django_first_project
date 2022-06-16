from django.db import models
from django.shortcuts import redirect ,reverse

STATUS_CHOICE = (
    ("pub", "published"),
    ("drf", "draft")
)


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_edited = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=3)

    def get_absolute_url(self):
        return reverse("page_one")

