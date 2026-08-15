# djchat-api

A Django REST Framework backend for a Discord-style chat service — servers organised by category, each containing channels, with a custom user model.

Early-stage work in progress. This repository is **backend only**; there is no frontend in it.

**Stack:** Django 5.2 · Django REST Framework · drf-spectacular · SQLite

---

## Data model

| Model | Fields |
|---|---|
| `Account` | Custom user extending `AbstractUser` |
| `Category` | `name`, `description` |
| `Server` | `name`, `owner` (FK user), `category` (FK), `description`, `members` (M2M user) |
| `Channel` | `name` (lower-cased on save), `owner`, `topic`, `server` (FK) |

Three migrations applied. `AUTH_USER_MODEL` is swapped to the custom `Account` model.

---

## API

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/server/list/` | List servers (registered via DRF `DefaultRouter`) |
| `GET` | `/api/schema/` | OpenAPI schema |
| `GET` | `/api/schema/swagger-ui/` | Swagger UI |

Implemented with a DRF `ViewSet` and serialised by `ServerSerializer`.

---

## Running locally

```bash
git clone https://github.com/Olable/djchat-api.git
cd djchat-api
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cd djchat
cp djchat/.env-example djchat/.env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

API at `http://localhost:8000/api/server/list/`, admin at `/admin/`, Swagger UI at `/api/schema/swagger-ui/`.

---

## Current status

Built so far:

- [x] Custom user model
- [x] Server / Category / Channel models and migrations
- [x] Server list endpoint via `DefaultRouter`
- [x] Django admin registration
- [x] OpenAPI schema generation with drf-spectacular

Known issues and next steps:

- [ ] **Category filtering is a no-op** — the queryset filter result is discarded rather than reassigned
- [ ] Authentication endpoints (JWT)
- [ ] Channel and message endpoints
- [ ] WebSocket layer for real-time messaging (Django Channels)
- [ ] Tests
- [ ] Frontend client

---

## Note on this repository

Previously named `React-Django`, with a README describing a full-stack chat application that was never implemented. Renamed and rewritten to describe only what the code actually contains.

---

## Author

**Akeem Olayemi Yekeen** — Lagos, Nigeria
[GitHub](https://github.com/Olable) · [LinkedIn](https://www.linkedin.com/in/olayemi-akeem-1140b31b1)
