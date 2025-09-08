from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite.models import Post
from datetime import datetime
from typing import Any
from django.db.models.query import QuerySet


class HomePageView:
    """
    主页面的显示
    """

    def __init__(self):
        pass

    @staticmethod
    def homepage(request) -> HttpResponse:
        """
        从Post中获取具体的显示内容
        """
        posts: QuerySet = Post.objects.all()
        now: datetime = datetime.now()
        post_lis: list = list()
        return render(request, "index.html", locals())

    @staticmethod
    def showpost(request, slug) -> HttpResponse:
        """
        点击URL显示的具体内容
        """
        try:
            post: QuerySet = Post.objects.get(slug=slug)
            if post is not None:
                return render(request=request, template_name="post.html", context={"post": post})
        except Post.DoesNotExist:
            return redirect('/')