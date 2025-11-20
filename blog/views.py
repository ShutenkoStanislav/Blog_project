from django.shortcuts import render
from blog.models import Post, Comment

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

def post_info(request, post_id):
    post_infa = Post.objects.get(id=post_id)
    comment_infa = Comment.objects.filter(post=post_infa)  
    context = {
        "post_infa": post_infa,
        "comment_infa": comment_infa,
    }
    return render(
        request,
        "Myblog/post_info.html",
        context=context,
    )

def author_post(request, author_name):
    author_to_post = Post.objects.filter(author__name=author_name)
    context = {
        "author": author_name,
        "posts": author_to_post,
    }
    return render(
        request,
        "Myblog/author_posts.html",
        context=context,
    )




# Детальна сторінка посту: Створіть нове представлення, яке відображає деталі
# конкретного посту:  назва, зміст, дата публікації та автор.

