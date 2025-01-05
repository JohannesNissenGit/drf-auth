from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        is_staff = bool(request.user and request.user.is_staff)

        return is_staff or request.method in SAFE_METHODS

class IsNotNamedBob(BasePermission):
    def has_permission(self, request, view):
        return request.user.username != 'bob'
