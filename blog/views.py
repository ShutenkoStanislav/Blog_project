from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    context = {
        "post_list": posts,
    }
    return render(
        request,
        "Myblog/post_list.html",
        context=context,
    )

