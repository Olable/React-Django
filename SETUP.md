# Setup Instructions

## Prerequisites

- **Python 3.10+**
- **Node.js 16+ and npm**
- **Git**
- **Virtual environment tool** (venv or conda)

## Backend Setup (Django)

### Step 1: Clone Repository

```bash
git clone https://github.com/Olable/React-Django.git
cd React-Django/djchat
```

### Step 2: Create Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r ../requirements.txt
```

### Step 4: Environment Configuration

Copy the example environment file:
```bash
cp djchat/.env-example djchat/.env
```

Edit `djchat/.env` and update:
```env
SECRET_KEY=your-secret-key-here  # Generate a strong key
DEBUG=True                         # Set to False in production
```

### Step 5: Database Migrations

Create and apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser (Optional)

Create an admin user for Django admin:
```bash
python manage.py createsuperuser
```

Follow the prompts to set username, email, and password.

### Step 7: Create Initial Data (Optional)

Create sample categories and servers:
```bash
python manage.py shell
```

Inside the shell:
```python
from server.models import Category
Category.objects.create(name='Gaming', description='Gaming servers')
Category.objects.create(name='Study', description='Study groups')
Category.objects.create(name='Social', description='Social hangouts')
exit()
```

### Step 8: Run Development Server

```bash
python manage.py runserver
```

The backend will be available at: **http://localhost:8000**

#### Useful endpoints:
- Admin: http://localhost:8000/admin/
- API: http://localhost:8000/api/
- Swagger UI: http://localhost:8000/api/schema/swagger-ui/
- ReDoc: http://localhost:8000/api/schema/redoc/

## Frontend Setup (React)

### Step 1: Navigate to Frontend Directory

```bash
cd ../frontend
```

### Step 2: Install Dependencies

```bash
npm install
```

### Step 3: Environment Configuration

Create `.env` file in the frontend directory:
```env
VITE_API_URL=http://localhost:8000/api
```

### Step 4: Start Development Server

```bash
npm run dev
```

The frontend will be available at: **http://localhost:3000**

## Running Tests

### Backend Tests

```bash
cd djchat
python manage.py test
```

**Run specific test file:**
```bash
python manage.py test account.tests
python manage.py test server.tests
```

**Run with verbose output:**
```bash
python manage.py test --verbosity=2
```

**Test coverage:**
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generates HTML report in htmlcov/
```

### Frontend Tests

```bash
cd ../frontend
npm test
```

## Code Quality

### Python Code Formatting

**Black (Code formatter):**
```bash
cd djchat
black .
```

**Flake8 (Linter):**
```bash
flake8 .
```

**MyPy (Type checker):**
```bash
mypy .
```

### JavaScript Code Formatting

**ESLint:**
```bash
cd frontend
npm run lint
```

**Prettier:**
```bash
npm run format
```

## Troubleshooting

### Python Errors

**`ModuleNotFoundError: No module named 'django'`**
- Solution: Ensure virtual environment is activated and dependencies are installed
  ```bash
  source venv/bin/activate  # macOS/Linux
  pip install -r requirements.txt
  ```

**`django.core.exceptions.ImproperlyConfigured`**
- Solution: Check that `.env` file is properly configured with `SECRET_KEY`

**Port 8000 already in use**
- Solution: Run on different port
  ```bash
  python manage.py runserver 8001
  ```

### Node/React Errors

**`npm ERR! code ERESOLVE`**
- Solution: Clear npm cache and reinstall
  ```bash
  npm cache clean --force
  rm -rf node_modules package-lock.json
  npm install
  ```

**Port 3000 already in use**
- Solution: Run on different port
  ```bash
  PORT=3001 npm run dev
  ```

### CORS Errors

**Error: Access to XMLHttpRequest blocked by CORS**
- Solution: Ensure `CORS_ALLOWED_ORIGINS` in `settings.py` includes your frontend URL
  ```python
  CORS_ALLOWED_ORIGINS = [
      "http://localhost:3000",
      "http://127.0.0.1:3000",
  ]
  ```

## Production Deployment

### Backend Deployment

1. **Set environment variables:**
   ```env
   SECRET_KEY=your-production-secret-key
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   DATABASE_URL=postgresql://user:password@host:port/dbname
   ```

2. **Collect static files:**
   ```bash
   python manage.py collectstatic --noinput
   ```

3. **Deploy with Gunicorn:**
   ```bash
   gunicorn djchat.wsgi:application --bind 0.0.0.0:8000
   ```

4. **Use a process manager (Supervisor, systemd)** to keep the app running

### Frontend Deployment

1. **Build for production:**
   ```bash
   npm run build
   ```

2. **Deploy to Netlify, Vercel, or AWS S3:**
   - Connect your repository
   - Build command: `npm run build`
   - Publish directory: `dist`

## Development Workflow

### Making Changes

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```

2. Make your changes

3. Run tests:
   ```bash
   python manage.py test  # Backend
   npm test               # Frontend
   ```

4. Format code:
   ```bash
   black .     # Backend
   npm run format  # Frontend
   ```

5. Commit changes:
   ```bash
   git add .
   git commit -m "Add your feature"
   ```

6. Push to repository:
   ```bash
   git push origin feature/your-feature
   ```

7. Create Pull Request on GitHub

## Next Steps

- Read the [README.md](README.md) for project overview
- Check [API.md](API.md) for API documentation
- Explore the Django admin at http://localhost:8000/admin/
- Test API endpoints using Swagger UI at http://localhost:8000/api/schema/swagger-ui/
