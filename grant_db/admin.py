from django.contrib import admin
from .models import Book, Rating

# Register your models here.


@admin.register(Book)
class bookAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'price', 'published', 'current_payment_status']
    list_display = ['title', 'price']
    list_filter = ['published', 'current_payment_status']
    search_fields = ['title']


@admin.register(Rating)
class ratingAdmin(admin.ModelAdmin):
    fields = ['book', 'user', 'rating']
    list_display = ['book', 'rating']
    list_filter = ['rating']
    search_fields = ['book']

