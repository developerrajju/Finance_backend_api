```markdown
# Finance Backend API

A secure finance management backend API built with Django REST Framework for handling financial records, user roles, dashboard analytics, and audit logging.

This project includes JWT authentication, role-based access control, record filtering, dashboard summaries, pagination, and clean modular API architecture.

## Features

- JWT Authentication
- User Registration and Login
- Role-Based Access Control
- User Status Management
- Financial Records CRUD
- Dashboard Summary APIs
- Monthly and Weekly Trends
- Category Wise Totals
- Audit Logging Middleware
- Request and Response Logging
- Sensitive Data Masking
- Pagination and Filtering
- Validation and Error Handling

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- JWT Authentication

## Folder Structure

```
Finance_backend_api/
│
├── config/
├── users/
├── records/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── README.md
└── LICENSE
```

## Roles and Permissions

| Role   | View Records | Create Records | Update Records | Delete Records | View Dashboard | Manage Users | View Admin Panel |
|--------|--------------|----------------|---------------|----------------|---------------|--------------|------------------|
| Viewer | Yes          | No             | No            | No             | Yes           | No           | No               |
| Analyst| Yes          | No             | No            | No             | Yes           | No           | No               |
| Admin  | Yes          | Yes            | Yes           | Yes            | Yes           | Yes          | Yes              |

**Note:** Only **Admin** role can access user management endpoints and the Django admin panel (`/admin/`) to view/manage users.

## Main Modules

### Authentication
- User registration
- Login
- JWT token generation
- Token refresh

### Users
- User creation
- Role assignment
- Active / inactive status
- User management

### Financial Records
- Create records
- Update records
- Delete records
- Filter by category, date, and type

### Dashboard
- Total income
- Total expenses
- Net balance
- Category-wise summary
- Recent activity
- Monthly trends

### Audit Logs
- User activity tracking
- Request logging
- Response logging
- IP address tracking
- User agent tracking
- Sensitive field masking

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/developerrajju/Finance_backend_api.git
   cd Finance_backend_api
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment:**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the server:**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints (Local Host)

All endpoints are accessible at `http://127.0.0.1:8000/` after running `python manage.py runserver`

### Authentication

| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `POST /api/auth/register/` | POST | User registration | No |
| `POST /api/auth/login/` | POST | User login & JWT token | No |
| `POST /api/auth/refresh/` | POST | Refresh JWT token | Yes (JWT) |

### Users

| Endpoint | Method | Description | Auth Required | Role Required |
|----------|--------|-------------|---------------|---------------|
| `GET /api/users/` | GET | List all users | Yes (JWT) | Admin |
| `POST /api/users/` | POST | Create new user | Yes (JWT) | Admin |
| `PATCH /api/users/{id}/` | PATCH | Update user | Yes (JWT) | Admin |

**Note:** Only **Admin** role can access user endpoints and view users in admin panel

### Financial Records

| Endpoint | Method | Description | Auth Required | Role Required |
|----------|--------|-------------|---------------|---------------|
| `GET /api/records/` | GET | List financial records (with filtering) | Yes (JWT) | Viewer, Analyst, Admin |
| `POST /api/records/` | POST | Create financial record | Yes (JWT) | Admin |
| `PATCH /api/records/{id}/` | PATCH | Update financial record | Yes (JWT) | Admin |
| `DELETE /api/records/{id}/` | DELETE | Delete financial record | Yes (JWT) | Admin |

**Filtering Examples:**
```
GET /api/records/?category=food
GET /api/records/?type=expense
GET /api/records/?start_date=2026-04-01&end_date=2026-04-06
GET /api/records/?category=food&type=expense&start_date=2026-04-01
```

### Dashboard

| Endpoint | Method | Description | Auth Required | Role Required |
|----------|--------|-------------|---------------|---------------|
| `GET /api/summary/` | GET | Total income, expenses, net balance, category summary | Yes (JWT) | Viewer, Analyst, Admin |




## HTTP Request Examples

### 1. User Registration

**POST** `http://127.0.0.1:8000/api/auth/register/`

**Headers:**
```
Content-Type: application/json
```

**Body (JSON):**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepass123",
  "role": "viewer"
}
```

---

### 2. User Login (Get JWT Token)

**POST** `http://127.0.0.1:8000/api/auth/login/`

**Headers:**
```
Content-Type: application/json
```

**Body (JSON):**
```json
{
  "username": "john_doe",
  "password": "securepass123"
}
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

---

### 3. Create Financial Record (Admin Only)

**POST** `http://127.0.0.1:8000/api/records/`

**Headers:**
```
Content-Type: application/json
Authorization: Bearer YOUR_ACCESS_TOKEN
```

**Body (JSON):**
```json
{
  "category": "food",
  "amount": 500,
  "type": "expense",
  "date": "2026-04-06",
  "description": "Grocery shopping"
}
```

---

### 4. Get Dashboard Summary

**GET** `http://127.0.0.1:8000/api/dashboard/summary/`

**Headers:**
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

### 5. Get Financial Records with Filtering

**GET** `http://127.0.0.1:8000/api/records/?type=expense&category=food`

**Headers:**
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

### 6. Get Audit Logs (Admin Only)

**GET** `http://127.0.0.1:8000/api/audit-logs/`

**Headers:**
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---


### 6. Delete Financial Record (Admin Only)

**DELETE** `http://127.0.0.1:8000/api/records/{id}/`

**Headers:**
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## API Documentation

View the interactive API documentation in Postman:  
[Finance Backend API - Postman Documentation](https://documenter.postman.com/preview/53774568-cdad1f8b-ecdc-415f-88d7-003bca113faf?versionTag=latest&apiName=CURRENT&version=latest&top-bar=FFFFFF&right-sidebar=303030&highlight=FF6C37&top-bar-dark=212121&right-sidebar-dark=303030&highlight-dark=FF6C37&documentationLayout=classic-single-column&documentationTheme=light&logo=https://res.cloudinary.com/postman/image/upload/t_team_logo/v1/team/anonymous_team&logoDark=https://res.cloudinary.com/postman/image/upload/t_team_logo/v1/team/anonymous_team)

## Validation and Error Handling

- Required field validation
- Invalid date handling
- Unauthorized access protection
- Proper HTTP status codes
- Invalid record protection
- Role-based restrictions

## Future Improvements

- Export reports to CSV/PDF
- Swagger API Documentation
- Docker Support
- Redis Caching
- Budget Tracking
- Soft Delete Support
- Unit Tests
- Email Notifications

## License

This project is licensed under the [MIT License](LICENSE).
```
