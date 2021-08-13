from rest_framework import permissions
from rest_framework.permissions import (
    BasePermission, IsAuthenticated, SAFE_METHODS)
from rest_framework.response import Response
from rest_framework.views import APIView


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class ExampleView(APIView):
    permission_classes = [IsAuthenticated | ReadOnly]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
