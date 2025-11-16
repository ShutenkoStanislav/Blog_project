from django.shortcuts import render
from blog.models import Post

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

def post_infornation(request, post_id):
    post_infa = Post.objects.get(id=post_id)
    context = {
        "post_infa": post_infa,
    }
    return render(
        request,
        "MyBlog/post_info.html",
        context=context,

    )




# Детальна сторінка посту: Створіть нове представлення, яке відображає деталі
# конкретного посту:  назва, зміст, дата публікації та автор.

