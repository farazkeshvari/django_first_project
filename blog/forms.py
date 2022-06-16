from django import forms
from .models import Post


class Create(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text", "author", "status"]

