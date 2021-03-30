from django.contrib.auth.models import User
from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.city_name


class Theatre(models.Model):
    name = models.CharField(max_length=50, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.TextField(null=False)
    no_of_screen = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) + "-" + str(self.address) + "-" + str(self.city)


class Movie(models.Model):
    lang_choice = (
        ('ENGLISH', 'English'),
        ('BENGALI', 'Bengali'),
        ('HINDI', 'Hindi'),
        ('TAMIL', 'Tamil'),
        ('TELUGU', 'Telugu'),
    )
    rating_choice = (
        ('U', 'U'),
        ('UA', 'U/A'),
        ('A', 'A'),
        ('R', 'R'),
    )
    name = models.CharField(max_length=20, null=True, blank=True)
    cast = models.CharField(max_length=100, null=True, blank=True)
    director = models.CharField(max_length=20, null=True, blank=True)
    language = models.CharField(max_length=10, choices=lang_choice)
    run_length = models.IntegerField(help_text="Enter run length in minutes", null=True, blank=True)
    certificate = models.CharField(max_length=2, choices=rating_choice)
    trailer = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True, upload_to='media')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    screen = models.IntegerField(default=1)
    date_time = models.DateTimeField(null=False)
    no_of_seat = models.PositiveIntegerField(default=1)
    seat_left = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.movie) + "-" + str(self.theatre) + "-" + str(self.date) + "-" + str(self.time)


class Booking(models.Model):
    timestamp = models.DateTimeField(null=True, blank=True)
    book_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Seat(models.Model):
    no_of_seat = models.CharField(max_length=3, null=True, blank=False)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('no_of_seat', 'show')

    def __str__(self):
        return str(self.no) + str(self.show)


class BookedSeat(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('seat', 'booking')

    def __str__(self):
        return str(self.seat) + '|' + str(self.booking)
