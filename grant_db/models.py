from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Book(models.Model):
    payment_status = [
        ('0', 'Unknown'),
        ('1', 'Processed'),
        ('2', 'Paid'),
    ]

    title = models.CharField(max_length=36, blank=False, unique=True, default='')
    description = models.TextField(max_length=250, blank=True)
    price = models.FloatField(default=0)
    published = models.BooleanField(default=False)
    current_payment_status = models.CharField(max_length=24, null=False, default='', choices=payment_status)

    def __str__(self):
        return self.title

    def no_of_ratings(self):
        ratings = Rating.objects.filter(book=self)
        return len(ratings)

    def avg_ratings(self):
        ratings = Rating.objects.filter(book=self)
        sum_of_ratings = 0
        for i in ratings:
            sum_of_ratings += i.rating

        if len(ratings) > 0:
            avg_rating = sum_of_ratings / len(ratings)
            return avg_rating

        else:
            return 0


class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'book'),)
        index_together = (('user', 'book'),)
