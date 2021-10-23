from django.http.response import HttpResponse
from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv
# Create your views here.
load_dotenv()


def home(request):
    # return HttpResponse('home')
    newskey = os.getenv('NEWS_API_KEY')
    weatherKey = os.getenv('WEATHER_API_KEY')
    newsUrl = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey="+newskey

    newsResponse = requests.get(newsUrl).json()

    # for i in newsResponse['articles']:
    #     print((i['author']+"\n"))
    return render(request, 'home.html', {'response': newsResponse['articles'], })
    # return render(request, 'home.html', )
