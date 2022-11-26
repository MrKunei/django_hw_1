from rest_framework import permissions
from user.models import User

class AdUpdateDeletePermission(permissions.BasePermission):
    message = 'The owner, moderator or admin can update or delete an ad.'

    def has_permission(self, request, view):
        if request.ad.author == request.user.id:
            return True
        elif request.user.role == User.AMIN or request.user.role == User.MODERATOR:
            return True
        else:
            return False