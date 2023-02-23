from django.shortcuts import render
from django.db.models import Avg
from . models import *
from .serializers import ReviewSerializer
from .serializers import BookSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.


# def get_average_rating(request):
#     average_rating = Review.objects.all().aggregate(Avg('rating'))
#     return render(request, 'average_rating.html',{'average_rating': average_rating})

@api_view(['GET'])
def get_average_rating(request):
    average_rating = Review.objects.all().aggregate(Avg('rating'))
    return JsonResponse({'average_rating': average_rating['rating__avg']})


@api_view(['GET', 'POST'])
def book_review(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = {
            'book': request.data.get('book'),
            'rating': request.data.get('rating')
        }
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
