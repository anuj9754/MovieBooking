from django.conf import settings
from rest_framework_jwt.serializers import (
    jwt_payload_handler,
    VerifyJSONWebTokenSerializer,
)
import jwt

from account.models import UserPermissions


def create_token(user):
    try:
        role = UserPermissions.objects.get(user_id=user.id)

        payload = jwt_payload_handler(user)
        token = jwt.encode(payload, settings.SECRET_KEY)

        user_details = {"user_id": user.id, "first_name": user.first_name, "token": token,
                        "role": role.role.role_name}
        return user_details
    except UserPermissions.DoesNotExist:
        return None