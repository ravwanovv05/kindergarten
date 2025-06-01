from rest_framework.permissions import BasePermission

class ManagerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'manager'
