from django.shortcuts import render
import requests

API_KEY = '403d62707f8f4cdf816f7b2e27b4a469'


def home(request):

    country = request.GET.get('country')
    category = request.GET.get('category')


    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'articles': articles,
        }

    return render(request, 'newsApp/home.html', context)