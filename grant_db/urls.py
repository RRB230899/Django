from django.contrib import admin
from django.urls import path, include
from .views import firstFunction, DjangoSolution, BookViewSet
from rest_framework import routers
# from first_app.views import generatePDF

router = routers.DefaultRouter()
router.register('books', BookViewSet)


urlpatterns = [
    path('firstMessage', firstFunction),
    path('grantDB', DjangoSolution.as_view()),
    path('', include(router.urls))
]
