from rest_framework import serializers
from .models import FinancialRecord

# This serializer converts FinancialRecord model data ↔ JSON (API format)
class FinancialRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinancialRecord  # Link serializer to FinancialRecord model
        
        # Include all fields from the model in API
        fields = '__all__'
        
        # This field cannot be set by user manually (read-only)
        # It will be automatically assigned in the view (perform_create)
        read_only_fields = ['created_by'] 

    # Custom validation for "amount" field
    def validate_amount(self, value):
        
        # Check if amount is less than or equal to 0
        if value <= 0:
            # Raise error if invalid
            raise serializers.ValidationError("Amount must be positive")
        
        # If valid, return the value
        return value