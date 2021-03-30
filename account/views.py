from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from account import models as auth_models, utils
from account.jwt import create_token
from account.serializers import SignUpSerializer


class UserSignUp(generics.CreateAPIView):
    """
       :purpose: Added employee details into the database role wise
       :input:{"name":<name>,"role_id":<role_id>}
       :models: Employee,User,User permission
       :Output: added single employee into databasen
       """
    permission_classes = []
    serializer_class = SignUpSerializer

    def check_user_exists(self):
        if auth_models.UserDetail.objects.filter(user__username=self.request.data.get('phone_no')).exists():
            self.mode = 'phone number'
            return True
        elif auth_models.UserDetail.objects.filter(email=self.request.data.get('email')).exists():
            self.mode = 'email'
            return True
        elif auth_models.UserDetail.objects.filter(phone_no=self.request.data.get('phone_no')).exists():
            self.mode = 'phone number'
            return True
        return False

    def create(self, request, *args, **kwargs):
        request_data = self.request.data
        self.mode = None
        if not self.check_user_exists():
            try:
                get_or_create_auth_user = User.objects.get(username=request_data.get('phone_no'))
            except User.DoesNotExist:
                get_or_create_auth_user = User(
                    username=request_data.get('phone_no'),
                    first_name=request_data.get('name'),
                )
                get_or_create_auth_user.set_password(request_data.get('password'))
                get_or_create_auth_user.save()
            request_data['user'] = get_or_create_auth_user.id
            request_data['role'] = utils.get_normal_user_id()
            serializer = self.get_serializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response = {
                'status_code': status.HTTP_201_CREATED,
                'message': "Signup successful",
                'result': serializer.data
            }
            return Response(response)
        response = {
            'status_code': status.HTTP_409_CONFLICT,
            'message': f"This {self.mode} is already registered",
            'result': {}
        }
        return Response(response)


class AdminSignUp(generics.CreateAPIView):
    """
       :purpose: Added employee details into the database role wise
       :input:{"name":<name>,"role_id":<role_id>}
       :models: Employee,User,User permission
       :Output: added single employee into databasen
       """
    serializer_class = SignUpSerializer

    def check_user_exists(self):
        if auth_models.UserDetail.objects.filter(user__username=self.request.data.get('phone_no')).exists():
            self.mode = 'phone number'
            return True
        elif auth_models.UserDetail.objects.filter(email=self.request.data.get('email')).exists():
            self.mode = 'email'
            return True
        elif auth_models.UserDetail.objects.filter(phone_no=self.request.data.get('phone_no')).exists():
            self.mode = 'phone number'
            return True
        return False

    def create(self, request, *args, **kwargs):
        request_data = self.request.data
        self.mode = None
        if not self.check_user_exists():
            try:
                get_or_create_auth_user = User.objects.get(username=request_data.get('phone_no'))
            except User.DoesNotExist:
                get_or_create_auth_user = User(
                    username=request_data.get('phone_no'),
                    first_name=request_data.get('name'),
                )
                get_or_create_auth_user.set_password(request_data.get('password'))
                get_or_create_auth_user.save()
            request_data['user'] = get_or_create_auth_user.id
            request_data['role'] = request_data.get('role')
            serializer = self.get_serializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response = {
                'status_code': status.HTTP_201_CREATED,
                'message': "Signup successful",
                'result': serializer.data
            }
            return Response(response)
        response = {
            'status_code': status.HTTP_409_CONFLICT,
            'message': f"This {self.mode} is already registered",
            'result': {}
        }
        return Response(response)


@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    """
        :purpose: this function is used to authenticate
            the user and generating jwt token and
            storing all the user information in the payaload .
        :input: username and password of
         the user who is authenticating from the form.
        :Output: Generating jwt token and
            storing all the user data in the payload.
        :Output Example:
        """

    if "password" in request.data:
        password = request.data["password"]
    else:
        return Response({"status": "Password not found"}, status=401)

    if "username" in request.data:
        username = request.data["username"]
        user = authenticate(username=username, password=password)
        if not user:
            try:
                user_detail_obj = auth_models.UserDetail.objects.get(
                    Q(phone_no=request.data["username"]) | Q(email=request.data["username"]))
            except auth_models.UserDetail.DoesNotExist:
                return Response({"status": "Username not found"}, status=401)

            user = authenticate(username=user_detail_obj.user.username, password=password)

    else:
        return Response({"status": "Username not found"}, status=401)

    if user is not None:

        if not user.is_active:
            return Response({"status": "User is not Active"}, status=401)

        user_detail = create_token(user)
        if not user_detail:
            return Response({"status": "User Detail not match. please contact to admistration"}, status=401)

        response = Response(
            {
                "status": "success",
                "message": "successfully logged in",
                "success": True,
                "user_detail": user_detail,
            }
        )
        return response
    else:
        return Response({"status": "The username or password you entered is incorrect"}, status=401)
