from rest_framework.permissions import BasePermission
from store_app.models import User

class IsAdmin(BasePermission):
    """
    Custom permission to allow only users in the "Admin" group to create stores,
    and allow read-only access for others.
    """
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.groups.filter(name='ADMIN').exists()