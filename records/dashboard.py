""" from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from .models import FinancialRecord


class DashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        records = FinancialRecord.objects.filter(created_by=user)

        total_income = records.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        total_expense = records.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

        net_balance = total_income - total_expense

        category_data = records.values('category').annotate(total=Sum('amount'))

        recent = records.order_by('-date')[:5].values()

        return Response({
            "total_income": total_income,
            "total_expense": total_expense,
            "net_balance": net_balance,
            "category_breakdown": category_data,
            "recent_transactions": recent
        }) """

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum

#from finance_backend import records
from .models import FinancialRecord


class DashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # 🔥 Role-based data filtering
        if user.role in ['admin', 'analyst']:
            # Admin & Analyst → see all records
            records = FinancialRecord.objects.all()
        else:
            # Viewer → only own records
            records = FinancialRecord.objects.filter(created_by=user)

        # ✅ Total income
        total_income = (
            records.filter(type='income')
            .aggregate(Sum('amount'))['amount__sum'] or 0
        )

        # ✅ Total expense
        total_expense = (
            records.filter(type='expense')
            .aggregate(Sum('amount'))['amount__sum'] or 0
        )

        # ✅ Net balance
        net_balance = total_income - total_expense

        # ✅ Category-wise breakdown
        category_data = records.values('category').annotate(total=Sum('amount'))

        # ✅ Last 5 transactions
        recent = records.order_by('updated_at')[:5].values()

        return Response({
            "total_income": total_income,
            "total_expense": total_expense,
            "net_balance": net_balance,
            "category_breakdown": category_data,
            "recent_transactions": recent
        })