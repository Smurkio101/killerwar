from django.shortcuts import render
import requests
import json


def home(request):
    res = requests.get(f"https://api.jikan.moe/v4/anime/")
    Data = res.json()
    context = {
           "page": "home",
           "data": Data,
    }
    return render (request, "app/pages/home.html", context=context)
  

def anime(request):
    res = request.get(f"https://api.jikan.moe/v4/anime/{id}/moreinfo")
    Data= res.json()
    context ={
           "page":"anime",
           "data":"data",
    }
    return render (request, "app/pages/anime.html")





