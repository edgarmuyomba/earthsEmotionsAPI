from django.shortcuts import render
from rest_framework.views import APIView
from datetime import datetime as dt, timedelta
from .models import Article
from django.db.models import Avg
from rest_framework.response import Response
from .serializers import ArticleSerializer
import re
from rest_framework import status


class PolarityNow(APIView):
    def get(self, request):
        seven_days_ago = dt.now() - timedelta(days=7)
        articles = Article.objects.filter(
            datetime__range=[seven_days_ago, dt.now()])
        average_polarity = articles.aggregate(Avg('polarity'))['polarity__avg']
        top_articles = articles.order_by('-polarity')[:7]
        bottom_articles = articles.order_by('polarity')[:7]
        top_serializer = ArticleSerializer(top_articles, many=True)
        bottom_serializer = ArticleSerializer(bottom_articles, many=True)
        return Response({
            'average_polarity': average_polarity,
            'top_articles': top_serializer.data,
            'bottom_articles': bottom_serializer.data
        })


class PolarityOnThisDay(APIView):
    def get(self, request, date):
        date_pattern = r"\d{4}\-\d{2}\-\d{2}&\d{2}\:\d{2}:\d{2}"
        if not re.search(date_pattern, date):
            return Response({
                "error": "Invalid date format"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            date_query = dt.strptime(date, "%Y-%m-%d&%H:%M:%S")
            seven_days_ago = date_query - timedelta(days=7)
            articles = Article.objects.filter(
                datetime__range=[seven_days_ago, date_query])
            average_polarity = articles.aggregate(Avg('polarity'))['polarity__avg']
            top_articles = articles.order_by('-polarity')[:7]
            bottom_articles = articles.order_by('polarity')[:7]
            top_serializer = ArticleSerializer(top_articles, many=True)
            bottom_serializer = ArticleSerializer(bottom_articles, many=True)
            return Response({
                'average_polarity': average_polarity,
                'top_articles': top_serializer.data,
                'bottom_articles': bottom_serializer.data
            })
