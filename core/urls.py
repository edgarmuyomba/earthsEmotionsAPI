from django.urls import path
from .views import PolarityNow, PolarityOnThisDay, PolarityTrends

app_name = 'core'

urlpatterns = [
    path('polarity-now/', PolarityNow.as_view(), name="polarity-now"),
    path('polarity-on-this-day/<str:date>/', PolarityOnThisDay.as_view(), name="polarity-on-this-day"),
    path('polarity-trends/', PolarityTrends.as_view(), name='polarity-trends'),
]