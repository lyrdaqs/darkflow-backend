from rest_framework.permissions import BasePermission



class BlocklistPermission(BasePermission):

    def has_permission(self, request, view):
        pass