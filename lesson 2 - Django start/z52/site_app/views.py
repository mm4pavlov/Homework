from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class MainPage(View):
    def get(self, request):
        return HttpResponse(status=401)
