
import os
import sys

import django

sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booking_system.settings")
if __name__ == "__main__":
    django.setup()
from django.contrib.auth.models import User


from booking import models as book_model
from account import models as account_model

user_role = account_model.Role.objects.create(role_name="Admin")
account_model.Role.objects.create(role_name="Normal User")

book_model.City.objects.create(city_name='Delhi')
book_model.City.objects.create(city_name='Kolkata')
book_model.City.objects.create(city_name='Mumbai')
book_model.City.objects.create(city_name='Chennai')


get_or_create_auth_user = User(
                    username="admin",
                    first_name="admin",
                )
get_or_create_auth_user.set_password("admin@1232")
get_or_create_auth_user.save()


account_model.UserDetail.objects.create(user_id=get_or_create_auth_user.id,role_id=user_role.id,name='admin', email='admin@gmail.com', phone_no='3123121212' )