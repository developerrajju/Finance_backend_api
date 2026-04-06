from django.db import models
from django.conf import settings


class FinancialRecord(models.Model):
    TYPE_CHOICES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='records'
    )

    def __str__(self):
        return f"{self.type} - {self.amount}"


class AuditLog(models.Model):
    ACTION_CHOICES = (
        ('LOGIN', 'Login'),
        ('REGISTER', 'Register'),
        ('TOKEN_REFRESH', 'Token Refresh'),
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
        ('SUMMARY_VIEW', 'Summary View'),
    )

    STATUS_CHOICES = (
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='audit_logs'
    )

    username = models.CharField(max_length=150, null=True, blank=True)
    role = models.CharField(max_length=50, null=True, blank=True)

    action = models.CharField(max_length=30, choices=ACTION_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    endpoint = models.CharField(max_length=255)
    method = models.CharField(max_length=10)

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)

    request_data = models.JSONField(null=True, blank=True)
    response_data = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.action} - {self.status}"