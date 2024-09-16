from django.shortcuts import render
from rest_framework.views import APIView
from datetime import datetime as dt, timedelta
from .models import Article
from django.db.models import Q, Avg
from rest_framework.response import Response
from .serializers import ArticleSerializer


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
