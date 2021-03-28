from rest_framework.permissions import BasePermission

from account.models import UserPermissions


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        role = UserPermissions.objects.get(user_id=request.user.id)
        return role.emp_role.role_name == "Admin"


class IsNormal(BasePermission):
    def has_permission(self, request, view):
        role = UserPermissions.objects.get(user_id=request.user.id)
        return role.emp_role.role_name == "Normal Use"
