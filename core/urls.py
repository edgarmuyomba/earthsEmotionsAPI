from django.urls import path
from .views import PolarityNow

app_name = 'core'

urlpatterns = [
    path('polarity-now/', PolarityNow.as_view(), name="polarity-now"),
]