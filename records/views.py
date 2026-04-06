""" from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from .permissions import RoleBasedPermission 

class FinancialRecordViewSet(ModelViewSet):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer
    permission_classes = [IsAuthenticated,RoleBasedPermission]

    def get_queryset(self):
        # Only show logged-in user's records
        return FinancialRecord.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign user
        serializer.save(created_by=self.request.user) """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from .permissions import RoleBasedPermission 

# ViewSet automatically handles CRUD operations (Create, Read, Update, Delete)
class FinancialRecordViewSet(ModelViewSet):
    
    # Default queryset (can be overridden by get_queryset)
    queryset = FinancialRecord.objects.all()
    
    # Serializer to convert data ↔ JSON and validate input
    serializer_class = FinancialRecordSerializer
    
    # Permissions:
    # IsAuthenticated → user must be logged in
    # RoleBasedPermission → controls access based on user role
    permission_classes = [IsAuthenticated, RoleBasedPermission]

    # Control which data each user can see
    def get_queryset(self):
        user = self.request.user

        # Admin & Analyst → can see all records
        if user.role in ['admin', 'analyst']:
            return FinancialRecord.objects.all()

        # Viewer → can see only their own records
        return FinancialRecord.objects.filter(created_by=user)

    # Automatically assign logged-in user when creating a record
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)