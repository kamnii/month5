from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer
from .models import Director, Movie, Review


@api_view(['GET', 'POST'])
def directors_view(request):
    try:
        directors = Director.objects.all()
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Directors not found!'})

    if request.method == 'GET':
        serializers = DirectorSerializer(directors, many=True)
        return Response(data=serializers.data)

    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        director.save()
        return Response(data={'message': 'Data received',
                              'director': DirectorSerializer(director).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def directors_detail_view(request, **kwargs):
    try:
        director = Director.objects.get(id=kwargs['id'])
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Director not found!'})

    if request.method == 'GET':
        serializer = DirectorSerializer(director, many=False)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data={'message': 'Data received!',
                              'director': DirectorSerializer(director).data},
                        status=status.HTTP_201_CREATED)

    else:
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'Data deleted!'})


@api_view(['GET', 'POST'])
def movies_view(request):
    try:
        movies = Movie.objects.all()
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Movies not found!'})

    if request.method == 'GET':
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director)
        movie.save()
        return Response(data={'message': 'Data received!',
                              'movie': MovieSerializer(movie).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail_view(request, **kwargs):
    try:
        movie = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Movie not found!'})

    if request.method == 'GET':
        serializer = MovieSerializer(movie, many=False)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director')
        movie.save()
        return Response(data={'message': 'Data received!',
                              'movie': MovieSerializer(movie).data},
                        status=status.HTTP_201_CREATED)

    else:
        movie.delete()
        return Response(data={'message': 'Data deleted'},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reviews_view(request):
    try:
        reviews = Review.objects.all()
    except Review.DoesNotExist:
        return Response(data={'message': 'Reviews not found!'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)

    else:
        text = request.data.get('text')
        movie = request.data.get('movie')
        grade = request.data.get('grade')
        review = Review.objects.create(text=text, movie_id=movie, grade=grade)
        review.save()
        return Response(data={'message': 'Data received!',
                              'review': ReviewSerializer(review).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_view(request, **kwargs):
    try:
        review = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(data={'message': 'Review not found!'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(review, many=False)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie')
        review.grade = request.data.get('grade')
        review.save()
        return Response(data={'message': 'Data received!',
                              'review': ReviewSerializer(review).data},
                        status=status.HTTP_201_CREATED)

    else:
        review.delete()
        return Response(data={'message': 'Data deleted!'},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def movies_reviews_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()

        serializer = MovieReviewSerializer(movie, many=True)

        return Response(data=serializer.data)
