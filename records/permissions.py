#we have this permissions file to give permissions based on rbac and object level permisiions
from rest_framework.permissions import BasePermission

class RoleBasedPermission(BasePermission):
#   here we put permission where the specific role can access the specific method as post ,put,get and delete   
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        # Admin → full access
        if user.role == 'admin':
            return True

        # Analyst → read-only
        if user.role == 'analyst':
            return request.method == 'GET'

        # User → CRUD allowed
        if user.role == 'viewer':
            return request.method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

        return False

#here we define that object level permisiions where the viewer can view his records and update likethat
    def has_object_permission(self, request, view, obj):
        user = request.user

        # Admin → full access
        if user.role == 'admin':
            return True

        # Analyst → only read
        if user.role == 'analyst':
            return request.method == 'GET'

        # User → only their own records
        if user.role == 'viewer':
            return obj.created_by == user

        return False