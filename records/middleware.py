import json
from .models import AuditLog


class AuditLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        try:
            user = request.user if hasattr(request, 'user') and request.user.is_authenticated else None
            action = self.get_action(request)

            should_log = action is not None

            if should_log:
                AuditLog.objects.create(
                    user=user,
                    username=self.get_username(request, user),
                    role=self.get_role(request, user),
                    action=action,
                    status='SUCCESS' if response.status_code < 400 else 'FAILED',
                    endpoint=request.path,
                    method=request.method,
                    ip_address=self.get_client_ip(request),
                    user_agent=request.META.get('HTTP_USER_AGENT'),
                    request_data=self.get_request_data(request),
                    response_data=self.get_response_data(response)
                )

        except Exception as e:
            print('Audit Log Error:', e)

        return response

    def get_action(self, request):
        path = request.path.lower()

        if 'login' in path:
            return 'LOGIN'

        if 'register' in path:
            return 'REGISTER'

        if 'refresh' in path:
            return 'TOKEN_REFRESH'

        if 'summary' in path:
            return 'SUMMARY_VIEW'

        if request.method == 'POST':
            return 'CREATE'

        if request.method in ['PUT', 'PATCH']:
            return 'UPDATE'

        if request.method == 'DELETE':
            return 'DELETE'

        return None

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()

        return request.META.get('REMOTE_ADDR')

    def get_request_data(self, request):
        try:
            if request.body:
                body = json.loads(request.body.decode('utf-8'))

                sensitive_fields = [
                    'password',
                    'confirm_password',
                    'token',
                    'access',
                    'refresh',
                    'otp'
                ]

                for field in sensitive_fields:
                    if field in body:
                        body[field] = '***hidden***'

                return body

        except Exception:
            return None

        return None

    def get_response_data(self, response):
        try:
            data = {
                'status_code': response.status_code
            }

            if hasattr(response, 'data'):
                response_data = response.data

                sensitive_fields = [
                    'password',
                    'token',
                    'access',
                    'refresh',
                    'otp'
                ]

                if isinstance(response_data, dict):
                    for field in sensitive_fields:
                        if field in response_data:
                            response_data[field] = '***hidden***'

                data['body'] = response_data

            return data

        except Exception:
            return {
                'status_code': response.status_code
            }

    def get_username(self, request, user):
        if user:
            if hasattr(user, 'username') and user.username:
                return user.username

            if hasattr(user, 'email') and user.email:
                return user.email

        try:
            body = self.get_request_data(request)

            if body:
                return (
                    body.get('username') or
                    body.get('email') or
                    body.get('phone')
                )

        except Exception:
            pass

        return None

    def get_role(self, request, user):
        if user:
            if hasattr(user, 'role'):
                return user.role

            if hasattr(user, 'user_type'):
                return user.user_type

            if hasattr(user, 'is_superuser') and user.is_superuser:
                return 'Admin'

            return 'User'

        return None