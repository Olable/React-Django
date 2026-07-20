# API Documentation

## Authentication

### Signup
Register a new user account.

**Endpoint:** `POST /api/auth/signup/`

**Request Body:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepass123",
  "password_confirm": "securepass123",
  "first_name": "John",
  "last_name": "Doe"
}
```

**Response (201 Created):**
```json
{
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "bio": null,
    "profile_picture": null,
    "created_at": "2026-07-20T12:00:00Z"
  },
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Login
Login with username and password.

**Endpoint:** `POST /api/auth/login/`

**Request Body:**
```json
{
  "username": "john_doe",
  "password": "securepass123"
}
```

**Response (200 OK):**
```json
{
  "user": { ... },
  "refresh": "...",
  "access": "..."
}
```

### Refresh Token
Get a new access token using refresh token.

**Endpoint:** `POST /api/auth/token/refresh/`

**Request Body:**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Response (200 OK):**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

## Servers

### List Servers
Get all servers or filter by category.

**Endpoint:** `GET /api/server/`

**Query Parameters:**
- `category` (optional): Filter by category ID

**Response:**
```json
[
  {
    "id": 1,
    "name": "Gaming Central",
    "owner": {
      "id": 1,
      "username": "john_doe",
      "email": "john@example.com"
    },
    "category": 1,
    "description": "A server for gamers",
    "members": [],
    "channels": [
      {
        "id": 1,
        "name": "general",
        "owner": { ... },
        "topic": "General discussion",
        "server": 1,
        "messages_count": 5
      }
    ],
    "created_at": "2026-07-20T12:00:00Z",
    "updated_at": "2026-07-20T12:00:00Z"
  }
]
```

### Create Server
Create a new server.

**Endpoint:** `POST /api/server/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "name": "My Gaming Community",
  "category": 1,
  "description": "Welcome to our gaming community!"
}
```

**Response (201 Created):**
```json
{
  "id": 2,
  "name": "My Gaming Community",
  "owner": { ... },
  "category": 1,
  "description": "Welcome to our gaming community!",
  "members": [],
  "channels": [],
  "created_at": "2026-07-20T13:00:00Z",
  "updated_at": "2026-07-20T13:00:00Z"
}
```

### Get Server
Get server details by ID.

**Endpoint:** `GET /api/server/{id}/`

**Response:** Server object

### Update Server
Update server details (owner only).

**Endpoint:** `PATCH /api/server/{id}/`

**Request Body:**
```json
{
  "name": "Updated Server Name",
  "description": "Updated description"
}
```

**Response:** Updated server object

### Delete Server
Delete a server (owner only).

**Endpoint:** `DELETE /api/server/{id}/`

**Response:** 204 No Content

### Get Server Channels
Get all channels in a server.

**Endpoint:** `GET /api/server/{id}/channels/`

**Response:** Array of channel objects

## Channels

### List Channels
Get all channels or filter by server.

**Endpoint:** `GET /api/channel/`

**Query Parameters:**
- `server` (optional): Filter by server ID

### Create Channel
Create a new channel in a server.

**Endpoint:** `POST /api/channel/`

**Request Body:**
```json
{
  "name": "announcements",
  "server": 1,
  "topic": "Important announcements"
}
```

**Response:** Channel object

### Get Channel Messages
Get all messages in a channel.

**Endpoint:** `GET /api/channel/{id}/messages/`

**Response:** Array of message objects

## Messages

### List Messages
Get all messages or filter by channel.

**Endpoint:** `GET /api/message/`

**Query Parameters:**
- `channel` (optional): Filter by channel ID

### Create Message
Post a new message to a channel.

**Endpoint:** `POST /api/message/`

**Request Body:**
```json
{
  "channel": 1,
  "content": "Hello everyone!"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "author": {
    "id": 1,
    "username": "john_doe"
  },
  "channel": 1,
  "content": "Hello everyone!",
  "created_at": "2026-07-20T13:05:00Z",
  "updated_at": "2026-07-20T13:05:00Z"
}
```

### Update Message
Edit a message (author only).

**Endpoint:** `PATCH /api/message/{id}/`

**Request Body:**
```json
{
  "content": "Updated message content"
}
```

### Delete Message
Delete a message (author only).

**Endpoint:** `DELETE /api/message/{id}/`

## Error Responses

### 400 Bad Request
```json
{
  "field_name": ["Error message"]
}
```

### 401 Unauthorized
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 403 Forbidden
```json
{
  "detail": "Only the owner can update this server."
}
```

### 404 Not Found
```json
{
  "detail": "Server not found."
}
```

## Authentication

All protected endpoints require a JWT token in the Authorization header:

```
Authorization: Bearer <access_token>
```

Obtain tokens from:
- `/api/auth/signup/` - Signup endpoint
- `/api/auth/login/` - Login endpoint
- `/api/auth/token/` - Token endpoint

## Rate Limiting

Currently no rate limiting is implemented. For production, consider adding:
- Django-ratelimit
- DRF throttling

## Pagination

Currently no pagination is implemented. For large datasets, consider adding:
- DRF pagination classes
- Cursor-based pagination for real-time applications
