from rest_framework.permissions import BasePermission
from .models import Group


class IsGroupOwner(BasePermission):
    """
    Custom permission to check if the requesting user is the owner of the group.
    """
    message = 'You do not have permission to perform this action or the group does not exist'

    def has_permission(self, request, view):
        # Retrieve the group ID from the URL (assuming it's provided as a URL parameter)
        group_id = view.kwargs.get('pk')

        # Retrieve the group object based on the group ID
        try:
            group = Group.objects.get(pk=group_id)
        except Group.DoesNotExist:
            return False

        # Check if the requesting user is the owner of the group
        return request.user == group.instructor.user
