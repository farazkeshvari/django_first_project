from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from .forms import Create


class PostListView(generic.ListView) :
    template_name = "blog/post_list.html"
    context_object_name = "all_post"

    def get_queryset(self):
        return Post.objects.filter(status="pub").order_by("-datetime_create")


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "all_post"


class PostCreateView(generic.CreateView):
    form_class = Create
    template_name = "blog/post_create.html"


class PostUpdateView(generic.UpdateView) :
    model = Post
    form_class = Create
    template_name = "blog/post_create.html"


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("page_one")


