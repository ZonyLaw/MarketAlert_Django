from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def get_ticker(request):
    return render(request, 'marketApi/market_ticker.html')
