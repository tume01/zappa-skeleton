from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ListLicensePlates

urlpatterns = [
    path('', ListLicensePlates.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
