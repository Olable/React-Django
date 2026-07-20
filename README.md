# DJChat - Discord-like Chat Application

## Overview

DJChat is a full-stack chat application built with **Django REST Framework** (backend) and **React** (frontend), inspired by Discord. It allows users to create servers, channels, and exchange messages in real-time with a modern, responsive interface.

### Key Features

✅ **User Authentication**
- JWT-based authentication
- Secure signup and login
- Token refresh mechanism

✅ **Server Management**
- Create, read, update, delete servers
- Organize servers by categories
- Manage server members

✅ **Channel Management**
- Create channels within servers
- Organize conversations by topic
- Channel messaging

✅ **Real-time Messaging**
- Send and receive messages
- Edit and delete messages
- Message timestamps

✅ **Admin Dashboard**
- Django admin interface for content management
- User, server, channel, and message administration

✅ **API Documentation**
- Interactive Swagger UI
- ReDoc documentation
- Full OpenAPI 3.0 schema

## Tech Stack

### Backend
- **Framework:** Django 5.2 + Django REST Framework 3.16
- **Database:** SQLite (Development), PostgreSQL (Production-ready)
- **Authentication:** JWT (Simple JWT)
- **CORS:** django-cors-headers
- **API Docs:** drf-spectacular
- **Code Quality:** Black, Flake8, MyPy

### Frontend
- **Framework:** React 18
- **State Management:** Redux Toolkit / Context API
- **HTTP Client:** Axios
- **UI Library:** Tailwind CSS / Material-UI
- **Build Tool:** Vite / Create React App

## Project Structure

```
React-Django/
├── djchat/                      # Django project root
│   ├── manage.py
│   ├── djchat/                  # Project settings
│   │   ├── settings.py          # Django configuration
│   │   ├── urls.py              # URL routing
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── account/                 # User authentication app
│   │   ├── models.py            # Custom Account model
│   │   ├── views.py             # Auth views (signup, login)
│   │   ├── serializer.py        # Account serializers
│   │   ├── admin.py             # Admin configuration
│   │   └── tests.py             # Auth tests
│   │
│   ├── server/                  # Chat server app
│   │   ├── models.py            # Server, Channel, Message models
│   │   ├── views.py             # API viewsets
│   │   ├── serializer.py        # Model serializers
│   │   ├── admin.py             # Admin configuration
│   │   └── tests.py             # API tests
│   │
│   └── requirements.txt          # Python dependencies
│
├── frontend/                    # React application
│   ├── public/
│   ├── src/
│   │   ├── components/          # Reusable React components
│   │   ├── pages/               # Page components
│   │   ├── services/            # API integration
│   │   ├── hooks/               # Custom React hooks
│   │   ├── context/             # Context providers
│   │   ├── App.jsx
│   │   └── index.jsx
│   ├── package.json
│   └── vite.config.js
│
├── README.md                    # This file
├── SETUP.md                     # Setup instructions
└── API.md                       # API documentation
```

## Getting Started

### Prerequisites
- Python 3.10+
- Node.js 16+ & npm
- Git

### Backend Setup

1. **Clone and navigate to backend:**
   ```bash
   git clone https://github.com/Olable/React-Django.git
   cd React-Django/djchat
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   ```bash
   cp djchat/.env-example djchat/.env
   # Edit .env and add your SECRET_KEY
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server:**
   ```bash
   python manage.py runserver
   ```

   Backend will be available at: `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend:**
   ```bash
   cd ../frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start development server:**
   ```bash
   npm start
   ```

   Frontend will be available at: `http://localhost:3000`

## API Endpoints

### Authentication
- `POST /api/auth/signup/` - Register new user
- `POST /api/auth/login/` - Login user
- `POST /api/auth/token/` - Obtain JWT tokens
- `POST /api/auth/token/refresh/` - Refresh access token

### Servers
- `GET /api/server/` - List all servers
- `POST /api/server/` - Create server
- `GET /api/server/{id}/` - Get server details
- `PATCH /api/server/{id}/` - Update server (owner only)
- `DELETE /api/server/{id}/` - Delete server (owner only)
- `GET /api/server/{id}/channels/` - Get server channels

### Channels
- `GET /api/channel/` - List all channels
- `POST /api/channel/` - Create channel
- `GET /api/channel/{id}/` - Get channel details
- `PATCH /api/channel/{id}/` - Update channel (owner only)
- `DELETE /api/channel/{id}/` - Delete channel (owner only)
- `GET /api/channel/{id}/messages/` - Get channel messages

### Messages
- `GET /api/message/` - List all messages
- `POST /api/message/` - Create message
- `GET /api/message/{id}/` - Get message details
- `PATCH /api/message/{id}/` - Update message (author only)
- `DELETE /api/message/{id}/` - Delete message (author only)

### Documentation
- `GET /api/schema/` - OpenAPI schema
- `GET /api/schema/swagger-ui/` - Swagger UI
- `GET /api/schema/redoc/` - ReDoc documentation

## Running Tests

### Backend Tests
```bash
cd djchat
python manage.py test
```

### Run specific test module
```bash
python manage.py test account.tests
python manage.py test server.tests
```

### Test coverage
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

## Code Quality

### Format with Black
```bash
black .
```

### Lint with Flake8
```bash
flake8 .
```

### Type checking with MyPy
```bash
mypy .
```

## Deployment

### Backend (Production)

1. **Environment variables:**
   ```bash
   SECRET_KEY=your-secret-key
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

2. **Database:** Configure PostgreSQL in settings.py

3. **Static files:**
   ```bash
   python manage.py collectstatic
   ```

4. **Deploy with Gunicorn:**
   ```bash
   gunicorn djchat.wsgi:application
   ```

### Frontend (Production)

1. **Build for production:**
   ```bash
   npm run build
   ```

2. **Deploy to Netlify/Vercel/AWS:**
   - Connect your repository
   - Set build command: `npm run build`
   - Set publish directory: `dist/`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Project Status

✅ **Completed:**
- Backend API with full CRUD operations
- JWT authentication system
- Admin dashboard
- Comprehensive tests
- API documentation

🚀 **Planned:**
- React frontend UI
- Real-time messaging with WebSockets
- File uploads
- User mentions and notifications
- Search functionality
- User profiles
- Direct messaging

## License

MIT License - see LICENSE file for details

## Author

**Olable** - [GitHub](https://github.com/Olable)

## Support

For issues and questions:
1. Check existing issues on GitHub
2. Create a new issue with detailed description
3. Include steps to reproduce and environment details

## Acknowledgments

- Django and DRF community
- React community
- Discord for inspiration
