import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from booking import models as book_model
from booking.pagination import CustomPagination
from booking.permission import IsAdmin, IsNormal
from booking import serializers


class CityDetails(generics.CreateAPIView, generics.UpdateAPIView):
    """api for City details """

    permission_classes = [IsAdmin, ]
    serializer_class = serializers.CitySerializer

    def create(self, request, *args, **kwargs):
        try:
            request_data = self.request.data
            serializer = self.get_serializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response = {
                'status_code': status.HTTP_201_CREATED,
                'message': "Successful Created",
                'result': serializer.data
            }
            return Response(response)

        except Exception as e:
            message = str(e)
            response = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': "Issued Raised",
                'result': message
            }
            return Response(response)

    def update(self, request, *args, **kwargs):
        try:
            city_id = int(request.data['id'])
            instance = book_model.City.objects.get(id=city_id)

            serializer = self.get_serializer(instance, request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response = {
                'status_code': status.HTTP_201_CREATED,
                'message': "City Updated Successfully",
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            message = str(e)
            response = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': "Issued Raised",
                'result': message
            }
            return Response(response)


class RetrieveCities(generics.ListAPIView):
    """
    :purpose: fetching all cities from database
    :input:NULL
    :Output: {
        "city": ""
    },
    """
    permission_classes = []
    serializer_class = serializers.CitySerializer
    queryset = book_model.City.objects.order_by('id')


class TheatreDetails(generics.ListCreateAPIView, generics.UpdateAPIView):
    """api for Theatre details """

    permission_classes = [IsAdmin, ]
    serializer_class = serializers.TheatreSerializer

    def create(self, request, *args, **kwargs):
        try:
            request_data = self.request.data
            serializer = self.get_serializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response = {
                'status_code': status.HTTP_201_CREATED,
                'message': "Successful Created",
                'result': serializer.data
            }
            return Response(response)

        except Exception as e:
            message = str(e)
            response = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': "Issued Raised",
                'result': message
            }
            return Response(response)

    def update(self, request, *args, **kwargs):
        try:
            theatre_id = int(request.data['id'])
            instance = book_model.Theatre.objects.get(id=theatre_id)

            serializer = self.get_serializer(instance, request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response = {
                'status_code': status.HTTP_201_CREATED,
                'message': "City Updated Successfully",
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            message = str(e)
            response = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': "Issued Raised",
                'result': message
            }
            return Response(response)

    def list(self, request, *args, **kwargs):
        paginator = CustomPagination()
        if 'city_id' in self.request.query_params:
            queryset = book_model.Theatre.objects.filter(city_id=self.request.query_params('city_id'))
        else:
            queryset = book_model.Theatre.objects.all()

        page = paginator.paginate_queryset(queryset, self.request)
        serializer = serializers.TheatreSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class RetrieveTheatre(generics.ListAPIView):
    """
    :purpose: fetching all theatre from database
    :input:NULL
    :Output: {
        "Theatre": ""
    },
    """
    permission_classes = []

    def list(self, request, *args, **kwargs):
        paginator = CustomPagination()
        if 'city_id' in self.request.query_params:
            queryset = book_model.Theatre.objects.filter(city_id=self.request.query_params('city_id'))
        else:
            queryset = book_model.Theatre.objects.all()

        page = paginator.paginate_queryset(queryset, self.request)
        serializer = serializers.TheatreSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class MovieDetails(generics.ListCreateAPIView, generics.UpdateAPIView):
    """api for Movie details """

    permission_classes = [IsAdmin, ]
    serializer_class = serializers.MovieSerializer

    def create(self, request, *args, **kwargs):
        try:
            request_data = self.request.data
            serializer = self.get_serializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response = {
                'status_code': status.HTTP_201_CREATED,
                'message': "Successful Created",
                'result': serializer.data
            }
            return Response(response)

        except Exception as e:
            message = str(e)
            response = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': "Issued Raised",
                'result': message
            }
            return Response(response)

    def update(self, request, *args, **kwargs):
        try:
            movie_id = int(request.data['id'])
            instance = book_model.Movie.objects.get(id=movie_id)

            serializer = self.get_serializer(instance, request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response = {
                'status_code': status.HTTP_201_CREATED,
                'message': "City Updated Successfully",
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            message = str(e)
            response = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': "Issued Raised",
                'result': message
            }
            return Response(response)

    def list(self, request, *args, **kwargs):
        paginator = CustomPagination()

        queryset = book_model.Movie.objects.all()

        page = paginator.paginate_queryset(queryset, self.request)
        serializer = serializers.MovieSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class RetrieveMovie(generics.ListAPIView):
    """
    :purpose: fetching all theatre from database
    :input:NULL
    :Output: {
        "Movie": ""
    },
    """
    permission_classes = []

    def list(self, request, *args, **kwargs):
        paginator = CustomPagination()

        queryset = book_model.Movie.objects.filter(is_acitve=False)

        page = paginator.paginate_queryset(queryset, self.request)
        serializer = serializers.MovieSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class ShowDetails(generics.ListCreateAPIView, generics.UpdateAPIView):
    """api for Show details """

    permission_classes = [IsAdmin, ]
    serializer_class = serializers.ShowSerializer

    def create(self, request, *args, **kwargs):
        try:
            request_data = self.request.data
            serializer = self.get_serializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response = {
                'status_code': status.HTTP_201_CREATED,
                'message': "Successful Created",
                'result': serializer.data
            }
            return Response(response)

        except Exception as e:
            message = str(e)
            response = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': "Issued Raised",
                'result': message
            }
            return Response(response)

    def update(self, request, *args, **kwargs):
        try:
            show_id = request.data['id']
            instance = book_model.Show.objects.get(id=show_id)

            serializer = self.get_serializer(instance, request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response = {
                'status_code': status.HTTP_201_CREATED,
                'message': "City Updated Successfully",
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            message = str(e)
            response = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': "Issued Raised",
                'result': message
            }
            return Response(response)

    def list(self, request, *args, **kwargs):
        paginator = CustomPagination()
        movie_id = self.request.query_params.get('movie', None)
        theatre_id = self.request.query_params.get('theatre', None)
        queryset = book_model.Movie.objects.all()

        if movie_id is not None:
            queryset = queryset.filter(movie_id=movie_id)

        if theatre_id is not None:
            queryset = queryset.filter(theatre_id=theatre_id)

        page = paginator.paginate_queryset(queryset, self.request)
        serializer = serializers.MovieSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class RetrieveShow(generics.ListAPIView):
    """
    :purpose: fetching all theatre from database
    :input:NULL
    :Output: {
        "show": ""
    },
    """
    permission_classes = []

    def list(self, request, *args, **kwargs):
        paginator = CustomPagination()
        movie_id = self.request.query_params.get('movie', None)
        theatre_id = self.request.query_params.get('theatre', None)
        queryset = book_model.Movie.objects.filter(is_active=True)

        if movie_id is not None:
            queryset = queryset.filter(movie_id=movie_id)

        if theatre_id is not None:
            queryset = queryset.filter(theatre_id=theatre_id)

        page = paginator.paginate_queryset(queryset, self.request)
        serializer = serializers.MovieSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class MovieBooking(APIView):
    permission_classes = [IsNormal]

    def post(self, request, *args, **kwargs):
        try:
            request_data = self.request.data
            show_id = request_data['show_id']
            no_of_seat = int(request_data['no_of_seat'])
            user_id = self.request.user.id

            show_obj = book_model.Show.objects.get(is_active=True, id=show_id, date_time__lte=datetime.datetime.now())

            if show_obj.seat_left < 1:
                response = {
                    'status_code': status.HTTP_409_CONFLICT,
                    'message': f"No Seat left",
                    'result': {}
                }
                return Response(response)

            if show_obj.seat_left < no_of_seat:
                response = {
                    'status_code': status.HTTP_409_CONFLICT,
                    'message': "Only {} Left".format(show_obj.seat_left),
                    'result': {}
                }
                return Response(response)

            show_obj.seat_left = show_obj.seat_left - no_of_seat
            show_obj.save()
            booking_obj = book_model.Booking.objects.create(timestamp=datetime.datetime.now(), book_by_id=user_id)
            seat_obj = book_model.Seat.objects.create(no_of_seat=no_of_seat, show_id=show_obj.id)
            book_model.BookedSeat.objects.create(seat_id=seat_obj.id, booking_id=booking_obj.id)
            response = {
                'status_code': status.HTTP_201_CREATED,
                'message': "Booked successful",
            }
            return Response(response)

        except book_model.Show.DoesNotExist:
            response = {
                'status_code': status.HTTP_409_CONFLICT,
                'message': f"This Show is already Expire",
                'result': {}
            }
            return Response(response)


class BookingDetail(generics.ListAPIView):
    permission_classes = [IsNormal]

    def list(self, request, *args, **kwargs):
        paginator = CustomPagination()
        queryset = book_model.BookedSeat.objects.filter(booking__book_by_id=self.request.user.id).select_related('seat', 'booking').order_by('booking__timestamp')

        page = paginator.paginate_queryset(queryset, self.request)
        serializer = serializers.BookedSeatSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
