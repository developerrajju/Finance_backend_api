from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FinancialRecordViewSet
from .dashboard import DashboardSummaryView 

# Create a router (automatically generates CRUD URLs)
router = DefaultRouter()

# Register the ViewSet with router
# This will create endpoints like:
# GET    /records/        → list records
# POST   /records/        → create record
# GET    /records/{id}/   → retrieve single record
# PUT    /records/{id}/   → update record
# DELETE /records/{id}/   → delete record
router.register(r'records', FinancialRecordViewSet)

urlpatterns = [
    # Include all router-generated URLs
    path('', include(router.urls)),

    # Custom API endpoint for dashboard summary
    # Example: GET /summary/
    path('summary/', DashboardSummaryView.as_view()),
]