# Event Management API 🗓️

A backend service for managing events (conferences, meetups, etc.), featuring user registrations, advanced search and filtering, and automated email notifications.

---

## 🛠 Tech Stack
* **Python** / **Django** / **DRF**
* **PostgreSQL**
* **Docker** & **Docker Compose**
* **django-filter** (Advanced Search & Filtering)
* **drf-spectacular** (Swagger UI)

---

## 📡 API Endpoints

- **POST /api/login/** - Obtain auth token using username and password.
- **GET /api/events/** - List all events (supports `search`, `location`, and `date` filters).
- **POST /api/events/** - Create a new event (Authenticated organizers only).
- **GET /api/events/{id}/** - Get detailed information about a specific event.
- **PUT / PATCH / DELETE /api/events/{id}/** - Update or delete an event (Event organizer only).
- **GET /api/registrations/** - List user event registrations.
- **POST /api/registrations/** - Register for an event (Triggers automated console email notification).

---

## 📁 Project Structure
```text
core/                        # Project settings & routing
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
events/                      # Main application
│   ├── migrations/          # Database migrations
│   ├── __init__.py
│   ├── admin.py             # Admin panel setup
│   ├── apps.py
│   ├── models.py            # Database models (Event, Registration)
│   ├── serializers.py       # DRF Serializers
│   ├── tests.py             # Unit tests
│   ├── urls.py              # App routing
│   └── views.py             # API ViewSets & Business logic
├── .env.example             # Environment template
├── Dockerfile               # Docker setup
├── docker-compose.yml       # Docker services
├── manage.py                # Django CLI
└── requirements.txt         # Project dependencies
```

---

## 🚀 How to Run
### 1. Prepare Environment
Copy the example environment file to create your active `.env`:
```bash
cp .env.example .env
```

### 2. Launch Application
Build and start the containers:
```bash
docker-compose up --build
```

### 3. Run Migrations & Create Admin Account
Apply database migrations and create your superuser:
```bash
docker compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

---

## 📖 API & Monitoring
* **Swagger UI:** http://localhost:8000/api/docs/ - Full interactive API documentation.
* **Admin Panel:** http://localhost:8000/admin/ - Manage users, events, and registrations.

---
## ⚙️ Key Requirements & Bonus Features Met
* **Event Management:** Full CRUD operations for events with role-based restrictions (only organizers can edit/delete their events).
* **Authentication:** Secure Token-based authentication via Django REST Framework.
* **Event Registrations:** Users can securely register for upcoming events.
* **Advanced Filtering:** API supports filtering events by `location` and `date`, plus full-text search across `title` and `description`.
* **Email Notifications:** Automated email notifications sent to users upon successful event registration (routed to Docker console for instant testing).
* **API Access:** Fully documented and tested interactively via Swagger UI.
