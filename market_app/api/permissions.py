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

class IsAdminForDeleteOrPatchAndReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == "DELETE": ## variant example for multiple methods: request.method in ['DELETE', 'PATCH']:
            return bool(request.user and request.user.is_superuser)
        else:
            return bool(request.user and request.user.is_staff)