from rest_framework import serializers

from booking.models import City, Theatre, Movie, Show, BookedSeat, Seat, Booking


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = "__all__"


class SeatSerializer(serializers.ModelSerializer):
    show = ShowSerializer()

    class Meta:
        model = Seat
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class BookedSeatSerializer(serializers.ModelSerializer):
    seat = SeatSerializer()
    booking = BookingSerializer()

    class Meta:
        model = BookedSeat
        fields = "__all__"
