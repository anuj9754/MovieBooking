from django.urls import path

from booking import views

urlpatterns = [
    path("city/", views.CityDetails.as_view()),
    path("city-list/", views.RetrieveCities.as_view()),
    path("theater/", views.TheatreDetails.as_view()),
    path("theater-list/", views.RetrieveTheatre.as_view()),
    path("movie/", views.MovieDetails.as_view()),
    path("movie-list/", views.RetrieveMovie.as_view()),
    path("show/", views.ShowDetails.as_view()),
    path("show-list/", views.RetrieveShow.as_view()),
    path("movie-booking/", views.MovieBooking.as_view()),
    path("booking-detail/", views.BookingDetail.as_view()),

]
