
# Finance Backend API

A secure finance management backend API built with **Django REST Framework** for handling financial records, user roles, dashboard analytics, and audit logging. 

This project includes JWT authentication, role-based access control, record filtering, dashboard summaries, pagination, and a clean modular API architecture.

## 🚀 Features

* **Authentication & Security:** JWT Authentication, Sensitive data masking in logs.
* **Role-Based Access Control (RBAC):** Distinct permissions for Viewer, Analyst, and Admin.
* **Financial Management:** Full CRUD for records with filtering (category, date, type).
* **Analytics Dashboard:** Monthly/Weekly trends, category-wise totals, and net balance summaries.
* **Audit System:** Middleware for tracking user activity, IP addresses, and request/response logs.
* **Robustness:** Pagination, comprehensive validation, and error handling.

## 🛠 Tech Stack

* **Language:** Python
* **Framework:** Django & Django REST Framework (DRF)
* **Database:** SQLite (Default)
* **Auth:** SimpleJWT

## 📂 Folder Structure

```text
Finance_backend_api/
│
├── config/             # Project settings and WSGI/ASGI configuration
├── users/              # User models, authentication, and RBAC logic
├── records/            # Financial records and dashboard logic
├── manage.py
├── requirements.txt
├── db.sqlite3
├── README.md
└── LICENSE
````

## 🔐 Roles and Permissions

| Role    | View Records | Create Records | Update Records | Delete Records | View Dashboard | Manage Users |
| :------ | :----------: | :------------: | :------------: | :------------: | :------------: | :----------: |
| Viewer  | ✅           | ❌             | ❌             | ❌             | ✅             | ❌           |
| Analyst | ✅           | ❌             | ❌             | ❌             | ✅             | ❌           |
| Admin   | ✅           | ✅             | ✅             | ✅             | ✅             | ✅           |

## 🛣 API Endpoints

### Authentication

  * `POST /api/auth/register/` - Register a new user
  * `POST /api/auth/login/` - Obtain JWT Pair
  * `POST /api/auth/refresh/` - Refresh Access Token

### Financial Records

  * `GET /api/records/` - List records (with filtering)
  * `POST /api/records/` - Add new record
  * `PUT /api/records/{id}/` - Update existing record
  * `DELETE /api/records/{id}/` - Remove record

### Dashboard & Logs

  * `GET /api/summary/` - Total income, expense, and balance
    

## ⚙️ Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/developerrajju/Finance_backend_api.git](https://github.com/developerrajju/Finance_backend_api.git)
    cd Finance_backend_api
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Start the server:**

    ```bash
    python manage.py runserver
    ```

## 🛡 Validation & Error Handling

  * **Required Fields:** API returns `400 Bad Request` with specific field errors.
  * **Unauthorized Access:** Uses DRF permissions to return `403 Forbidden` for restricted roles.
  * **Protected Records:** Prevents deletion or modification of records without proper ownership or Admin rights.

## 🔮 Future Improvements

  * [ ] Export reports to CSV/PDF.
  * [ ] Swagger/OpenAPI Documentation integration.
  * [ ] Docker Support (Dockerfile & docker-compose).
  * [ ] Redis Caching for dashboard analytics.
  * [ ] Email Notifications for budget alerts.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE] [MIT](https://choosealicense.com/licenses/mit/)file for details.

```
```
