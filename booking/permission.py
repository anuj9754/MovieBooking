from rest_framework.permissions import BasePermission

from account.models import UserPermissions


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            role = UserPermissions.objects.get(user_id=request.user.id)
            print(role, 'ddd')
            return role.role.role_name == "Admin"
        except:
            return None


class IsNormal(BasePermission):
    def has_permission(self, request, view):
        try:
            role = UserPermissions.objects.get(user_id=request.user.id)
            return role.role.role_name == "Normal User"
        except:
            return None
