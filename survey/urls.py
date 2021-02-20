"""survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

import api.views

survey_data_router = DefaultRouter()
survey_data_router.register(r'data', api.views.SurveyDataViewset, basename='survey-data')

router = DefaultRouter()
router.register(r'survey', api.views.SurveyViewset, basename='survey')
router.register(r'survey-data-type', api.views.SurveyDataTypeViewset)
router.register(r'question-data', api.views.QuestionDataViewset)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("api/", include(router.urls)),
    path("api/survey/<int:survey>/", include(survey_data_router.urls)),
    path("", api.views.default),
    path("<str:a>/", api.views.default),
    path("<str:a>/<str:b>/", api.views.default),
]
