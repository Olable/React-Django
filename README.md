# React Django

A modern full-stack integration project combining **React** frontend with **Django REST Framework** backend. This project demonstrates best practices for building scalable web applications with separated frontend and backend architectures.

![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-5.0+-darkgreen.svg)
![React](https://img.shields.io/badge/react-16.0+-brightblue.svg)
![DRF](https://img.shields.io/badge/DRF-3.16+-red.svg)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Development Workflow](#development-workflow)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

React Django is a full-stack web application template showcasing:
- **Modern Frontend** with React and component-based architecture
- **Robust Backend** with Django REST Framework API
- **Separated Concerns** - independent frontend and backend
- **Best Practices** - clean code, proper architecture, comprehensive testing
- **Scalability** - designed for growth and maintainability
- **Security** - CORS, authentication, permission handling

Perfect for learning full-stack development or as a starting point for production applications.

---

## ✨ Features

### Backend (Django REST Framework)
- ✅ RESTful API design
- ✅ User authentication and authorization
- ✅ Permission and role management
- ✅ Token-based authentication (JWT/DRF Tokens)
- ✅ Database ORM with Django models
- ✅ API documentation (Swagger/ReDoc)
- ✅ Comprehensive error handling
- ✅ Pagination and filtering
- ✅ Request/response validation with serializers

### Frontend (React)
- ✅ Component-based architecture
- ✅ React Hooks for state management
- ✅ Axios HTTP client with interceptors
- ✅ Responsive design
- ✅ Client-side routing
- ✅ Error boundaries and error handling
- ✅ Loading states and spinners
- ✅ Form validation
- ✅ Local storage integration

### Full-Stack Features
- ✅ User authentication flow
- ✅ Session management
- ✅ CORS configuration
- ✅ Environment-based configuration
- ✅ Development and production builds
- ✅ Docker support ready
- ✅ Code quality tools (Black, Flake8, MyPy)

---

## 🛠 Tech Stack

### Backend
| Component | Technology | Version |
|-----------|-----------|---------|
| **Framework** | Django | 5.2.8 |
| **API** | Django REST Framework | 3.16.1 |
| **Python** | Python | 3.8+ |
| **Database** | SQLite / PostgreSQL | - |
| **Code Quality** | Black, Flake8, MyPy | Latest |
| **Environment** | python-dotenv | 1.2.1 |

### Frontend
| Component | Technology |
|-----------|-----------|
| **UI Framework** | React | 16.0+ |
| **HTTP Client** | Axios |
| **Routing** | React Router |
| **State Management** | React Context API / Hooks |
| **Styling** | CSS3 / Tailwind (optional) |
| **Build Tool** | Create React App / Vite |

---

## 📁 Project Structure

```
React-Django/
├── djchat/                          # Main backend directory
│   ├── account/                     # User account app
│   │   ├── models.py               # User models
│   │   ├── views.py                # Account views
│   │   ├── serializers.py          # DRF serializers
│   │   ├── urls.py                 # Account endpoints
│   │   └── admin.py                # Admin configuration
│   │
│   ├── server/                      # Server/content app
│   │   ├── models.py               # Server models
│   │   ├── views.py                # Server views
│   │   ├── serializers.py          # Serializers
│   │   ├── urls.py                 # Server endpoints
│   │   └── admin.py                # Admin setup
│   │
│   ├── djchat/                      # Project settings
│   │   ├── settings.py             # Configuration
│   │   ├── urls.py                 # Main URL routing
│   │   ├── wsgi.py                 # WSGI config
│   │   └── asgi.py                 # ASGI config
│   │
│   ├── templates/                   # HTML templates (if needed)
│   ├── static/                      # Static files
│   ├── manage.py                    # Django CLI
│   ├── requirements.txt             # Python dependencies
│   ├── schema.yml                   # API schema
│   └── .env.example                 # Environment template
│
├── frontend/                        # React application (if separate)
│   ├── public/
│   │   └── index.html              # HTML entry point
│   ├── src/
│   │   ├── components/             # React components
│   │   │   ├── Layout.jsx
│   │   │   ├── Navigation.jsx
│   │   │   └── ...
│   │   ├── pages/                  # Page components
│   │   │   ├── HomePage.jsx
│   │   │   ├── LoginPage.jsx
│   │   │   └── ...
│   │   ├── services/               # API services
│   │   │   ├── api.js
│   │   │   └── auth.js
│   │   ├── hooks/                  # Custom React hooks
│   │   ├── context/                # Context API setup
│   │   ├── App.jsx                 # Main app component
│   │   └── index.js                # Entry point
│   ├── package.json                # Dependencies
│   ├── .env.example                # Environment template
│   └── .gitignore
│
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git ignore rules
├── .env.example                     # Environment variables
└── README.md                        # This file
```

---

## 🚀 Quick Start

### Prerequisites

**Backend:**
- Python 3.8+
- pip package manager
- PostgreSQL (optional, SQLite for dev)

**Frontend:**
- Node.js 14+
- npm or yarn

---

## 🔧 Backend Setup (Django)

### Installation

1. **Clone repository**
```bash
git clone https://github.com/Olable/React-Django.git
cd React-Django
```

2. **Navigate to backend**
```bash
cd djchat
```

3. **Create virtual environment**
```bash
# macOS/Linux
python3 -m venv env
source env/bin/activate

# Windows
python -m venv env
env\Scripts\activate
```

4. **Install dependencies**
```bash
pip install -r ../requirements.txt
```

5. **Configure environment**
```bash
cp .env.example .env
```

6. **Update .env file**
```env
DEBUG=True
SECRET_KEY=your_secret_key_here
ALLOWED_HOSTS=localhost,127.0.0.1
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# CORS Configuration
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
```

7. **Run migrations**
```bash
python manage.py migrate
```

8. **Create superuser**
```bash
python manage.py createsuperuser
```

9. **Start backend server**
```bash
python manage.py runserver
```

Backend available at: `http://localhost:8000`

---

## 💻 Frontend Setup (React)

### Installation

1. **Navigate to frontend** (if separated)
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Create environment file**
```bash
cp .env.example .env
```

4. **Configure .env**
```env
REACT_APP_API_URL=http://localhost:8000
REACT_APP_API_TIMEOUT=10000
```

5. **Start development server**
```bash
npm start
```

Frontend available at: `http://localhost:3000`

### Build for Production
```bash
npm run build
```

---

## ⚙️ Configuration

### Django Settings

**Database Configuration**
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'react_django_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**CORS Configuration**
```python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
    'https://yourdomain.com',
]
```

**REST Framework Configuration**
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

### React Configuration

**API Service Setup**
```javascript
// src/services/api.js
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
    baseURL: API_URL,
    timeout: parseInt(process.env.REACT_APP_API_TIMEOUT || '10000'),
});

// Add token to requests
api.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
        config.headers.Authorization = `Token ${token}`;
    }
    return config;
});

export default api;
```

---

## 🔌 API Documentation

### Authentication Endpoints
```
POST   /api/auth/login/              # User login
POST   /api/auth/logout/             # User logout
POST   /api/auth/register/           # User registration
GET    /api/auth/user/               # Get current user
POST   /api/auth/refresh/            # Refresh token
```

### Account Endpoints
```
GET    /api/account/profile/         # Get user profile
PUT    /api/account/profile/         # Update profile
POST   /api/account/change-password/ # Change password
GET    /api/account/settings/        # Get settings
```

### Server Endpoints
```
GET    /api/server/                  # List servers
POST   /api/server/                  # Create server
GET    /api/server/<id>/             # Get server detail
PUT    /api/server/<id>/             # Update server
DELETE /api/server/<id>/             # Delete server
GET    /api/server/<id>/members/     # Get members
POST   /api/server/<id>/members/     # Add member
```

### Response Format
```json
{
    "status": "success",
    "data": { /* endpoint-specific data */ },
    "message": "Operation successful"
}
```

### Error Response Format
```json
{
    "status": "error",
    "message": "Error description",
    "errors": { /* field-specific errors */ }
}
```

---

## 🔄 Development Workflow

### Running Both Servers

**Terminal 1 - Backend**
```bash
cd djchat
source env/bin/activate
python manage.py runserver
```

**Terminal 2 - Frontend**
```bash
cd frontend
npm start
```

### Database Migrations

```bash
# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations
```

### Code Quality

**Format code with Black**
```bash
black . --line-length 88
```

**Lint with Flake8**
```bash
flake8 .
```

**Type checking with MyPy**
```bash
mypy .
```

---

## 🚀 Deployment

### Backend Deployment (Django)

1. **Environment Setup**
```bash
DEBUG=False
SECRET_KEY=your_production_key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DB_ENGINE=django.db.backends.postgresql
```

2. **Collect static files**
```bash
python manage.py collectstatic --noinput
```

3. **Run migrations**
```bash
python manage.py migrate --noinput
```

4. **Deploy with Gunicorn**
```bash
pip install gunicorn
gunicorn djchat.wsgi:application --bind 0.0.0.0:8000
```

### Frontend Deployment (React)

1. **Build production bundle**
```bash
npm run build
```

2. **Deploy to Vercel/Netlify**
```bash
# Using Vercel CLI
vercel deploy
```

3. **Deploy to static hosting (S3)**
```bash
aws s3 sync build/ s3://your-bucket-name
```

---

## 🐛 Troubleshooting

### CORS Errors
```
Access to XMLHttpRequest blocked by CORS policy
```

**Solution:** Update CORS_ALLOWED_ORIGINS in Django settings

### API 404 Errors
- Verify backend URL in React .env
- Check API endpoint paths in Django
- Ensure backend is running

### Port Already in Use
```bash
# Backend - use different port
python manage.py runserver 8001

# Frontend - use different port
PORT=3001 npm start
```

### Database Errors
```bash
# Reset database (development only)
rm db.sqlite3
python manage.py migrate
```

### Authentication Failures
- Check token storage in localStorage
- Verify token format in headers
- Check DRF authentication settings

---

## 🤝 Contributing

1. **Fork repository**
2. **Create feature branch**
```bash
git checkout -b feature/amazing-feature
```
3. **Commit changes**
```bash
git commit -m 'Add amazing feature'
```
4. **Push to branch**
```bash
git push origin feature/amazing-feature
```
5. **Open Pull Request**

---

## 📚 Learning Resources

### Django & DRF
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [DRF Tutorial](https://www.django-rest-framework.org/tutorial/quickstart/)

### React
- [React Official Docs](https://react.dev)
- [React Hooks](https://react.dev/reference/react/hooks)
- [React Router](https://reactrouter.com/)

### Full-Stack
- [Building APIs with Django REST](https://www.django-rest-framework.org/)
- [React + Django Integration](https://www.fullstackpython.com/django.html)
- [CORS Explained](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 🔗 Related Projects

- [Django E-commerce](https://github.com/Olable/django-ecommerce) - Full-featured e-commerce platform
- [Django Simple E-commerce](https://github.com/Olable/django-simple-ecommerce) - Beginner-friendly e-commerce
- [React Chat Channel](https://github.com/Olable/React-and-Django-Chat-Channel) - Real-time chat with WebSockets

---

## 🎓 Key Concepts

This project demonstrates:
- ✅ Frontend-backend separation of concerns
- ✅ RESTful API design principles
- ✅ Token-based authentication
- ✅ CORS and security best practices
- ✅ React component lifecycle and hooks
- ✅ Django ORM and models
- ✅ Request/response serialization
- ✅ Error handling and validation
- ✅ Environment-based configuration
- ✅ Development and production workflows

---

<div align="center">

**Made with ❤️ by [Olable](https://github.com/Olable)**

⭐ **If you found this helpful, star the repository!**

[⬆ Back to Top](#react-django)

</div>
