from django.test import TestCase
# Create your tests here.
from django.shortcuts import render
from django.http import HttpResponse

class TestView:
    def __init__(self):
        pass
    @staticmethod
    def test_view(request) ->HttpResponse:
        """
        厨艺主题网页
        """
        return render(request, "nd-2_2.html")
    @staticmethod
    def test2_view(request) ->HttpResponse:
        """
        生活主题网页
        """
        return render(request, "nd-2_1.html")
    @staticmethod
    def show_nd23_view(request) ->HttpResponse:
        """
        好书推荐网页
        """
        return render(request, "nd-2_3.html")
