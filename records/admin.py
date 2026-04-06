from django.contrib import admin
from .models import FinancialRecord, AuditLog


@admin.register(FinancialRecord)
class FinancialRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'amount', 'category', 'created_by', 'created_at')


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'role',
        'action',
        'status',
        'method',
        'endpoint',
        'created_at'
    )

    list_filter = ('action', 'status', 'method')
    search_fields = ('user__username', 'endpoint', 'ip_address')