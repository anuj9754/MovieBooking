from account.models import Role


def get_normal_user_id():
    """
        get student id
    """
    role_id = Role.objects.get(
        role_name="Normal User"
    ).id
    return role_id