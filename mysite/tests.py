from django.test import TestCase
# Create your tests here.

from django.shortcuts import render


class TestView:
    def __init__(self):
        pass
    @staticmethod
    def test_view(request):
        print("test")
        return render(request, "nd-2_2.html")
