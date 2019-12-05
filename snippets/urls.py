# from .views import snippet_detail, snippet_list
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetListApi, SnippetDetailApi

urlpatterns = [
    path('', SnippetListApi.as_view(), name="snippet_list"),
    path('<int:pk>/', SnippetDetailApi.as_view(), name="snippet_list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)