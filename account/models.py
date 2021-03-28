from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Role(models.Model):
    """RoleList model."""

    role_name = models.CharField(max_length=222, blank=True, null=True, unique=True)

    class Meta:
        """Meta."""

        managed = True
        db_table = "role_list"
        ordering = ["pk"]

    def __str__(self):
        """__str__."""
        return self.role_name


class UserPermissions(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        managed = True
        ordering = ['pk']
        unique_together = ['role', 'user']

    def __str__(self):
        """Return role id and user id."""
        return str(self.role) + " | " + str(self.user)


class UserDetail(UserPermissions):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_no = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True)
    email = models.EmailField(help_text="Enter a valid email", max_length=50, blank=True, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        """Meta."""
        managed = True
        ordering = ["pk"]

    def __str__(self):
        """__str__."""
        return str(self.user) + " || " + str(self.name) + " || " + str(self.role)
