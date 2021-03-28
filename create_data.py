
import os
import sys

import django


sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booking_system.settings")
if __name__ == "__main__":
    django.setup()

from booking import models as book_model
from account import models as account_model

account_model.Role.objects.create(role_name="Admin")
account_model.Role.objects.create(role_name="Normal Use")

book_model.City.objects.create(city_name='Delhi')
book_model.City.objects.create(city_name='Kolkata')
book_model.City.objects.create(city_name='Mumbai')
book_model.City.objects.create(city_name='Chennai')