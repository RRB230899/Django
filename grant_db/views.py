from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Book, Rating
from .serializers import BookSerializer, RatingSerializer, UserSerializer

# import io
# from django.http import FileResponse
# from reportlab.pdfgen import canvas

# Create your views here.


# @staff_member_required
# def generatePDF(request, id):
#     buffer = io.BytesIO()
#     x = canvas.Canvas(buffer)
#     x.drawString(100, 100, "Let's generate this pdf file.")
#     x.showPage()
#     x.save()
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='attempt1.pdf')

def firstFunction(request):
    return render(request, 'first_app_temp.html', {'data': 'Something'})


class DjangoSolution(View):
    books_obj = Book.objects.all()
    output = ''

    for i, book in enumerate(books_obj):
        output += f"{i + 1}. {book.title}\n"

    def get(self, request):
        return render(request, 'first_app_temp.html', {'data': f"We have the following books in our Grant DB:\n" + self.output})


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def rate_book(self, request, pk=None):

        if 'stars' in request.data:
            book = Book.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            print(f"User: {user}")
            print(f"Book title: {book.title} was rated {stars} by {user.username}")

            try:
                rating = Rating.objects.get(user=user.id, book=book.id)
                rating.rating = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': "Rating updated", 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

            except:
                Rating.objects.create(user=user, book=book, rating=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': "Rating created", 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'Please rate the movie'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

