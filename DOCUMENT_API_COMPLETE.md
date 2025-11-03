# Document API - Complete Endpoint Reference

## 📋 All Available Endpoints

### 1. **CREATE** - Create a new document
```http
POST /Dijkstra/v1/document/create
```

**Request Body:**
```json
{
  "github_username": "AbdulWahab938",
  "latex": "\\documentclass{article}...",
  "base_structure": {
    "personal_info": {...},
    "experience": [...],
    "education": [...]
  }
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid-here",
  "profile_id": "auto-fetched-uuid",
  "latex": "...",
  "base_structure": {...},
  "created_at": "2025-11-03T...",
  "updated_at": "2025-11-03T..."
}
```

---

### 2. **UPDATE** - Update existing document ✨ NEW
```http
PUT /Dijkstra/v1/document/{document_id}
```

**Request Body:** (All fields optional - update only what you need)
```json
{
  "latex": "\\documentclass{article}...UPDATED...",
  "base_structure": {
    "personal_info": {
      "email": "new-email@example.com"
    }
  }
}
```

**Response:** `200 OK`
```json
{
  "id": "same-uuid",
  "profile_id": "same-profile-id",
  "latex": "...UPDATED...",
  "base_structure": {...UPDATED...},
  "created_at": "2025-11-03T...",
  "updated_at": "2025-11-03T...NEWER..."
}
```

**Use Cases:**
- User edits their resume
- Auto-save draft changes
- Update LaTeX after JSON changes
- Update JSON after LaTeX changes

---

### 3. **GET BY ID** - Get a specific document
```http
GET /Dijkstra/v1/document/{document_id}
```

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "profile_id": "uuid",
  "latex": "...",
  "base_structure": {...},
  "created_at": "...",
  "updated_at": "..."
}
```

---

### 4. **GET ALL FOR USER** - List all documents ✨ NEW
```http
GET /Dijkstra/v1/document/user/{github_username}
```

**Example:**
```
GET /Dijkstra/v1/document/user/AbdulWahab938
```

**Response:** `200 OK`
```json
[
  {
    "id": "uuid-1",
    "profile_id": "uuid",
    "latex": "...version 1...",
    "base_structure": {...},
    "created_at": "2025-11-01T...",
    "updated_at": "2025-11-01T..."
  },
  {
    "id": "uuid-2",
    "profile_id": "uuid",
    "latex": "...version 2...",
    "base_structure": {...},
    "created_at": "2025-11-02T...",
    "updated_at": "2025-11-03T..."
  }
]
```

**Use Cases:**
- Show resume history
- List all saved versions
- Resume version management

---

### 5. **DELETE** - Delete a document ✨ NEW
```http
DELETE /Dijkstra/v1/document/{document_id}
```

**Response:** `200 OK`
```json
{
  "message": "Document {uuid} deleted successfully."
}
```

---

## 🔄 Common Workflows

### Workflow 1: Create and Edit Resume
```bash
# 1. Create initial version
curl -X POST http://localhost:8000/Dijkstra/v1/document/create \
  -H "Content-Type: application/json" \
  -d '{
    "github_username": "AbdulWahab938",
    "latex": "...",
    "base_structure": {...}
  }'

# Response includes document_id

# 2. User edits resume
curl -X PUT http://localhost:8000/Dijkstra/v1/document/{document_id} \
  -H "Content-Type: application/json" \
  -d '{
    "latex": "...UPDATED...",
    "base_structure": {...UPDATED...}
  }'
```

### Workflow 2: Auto-save Draft
```bash
# Update only changed fields (partial update)
curl -X PUT http://localhost:8000/Dijkstra/v1/document/{document_id} \
  -H "Content-Type: application/json" \
  -d '{
    "base_structure": {
      "personal_info": {
        "email": "new@example.com"
      }
    }
  }'
# LaTeX remains unchanged!
```

### Workflow 3: View Resume History
```bash
# Get all versions for a user
curl http://localhost:8000/Dijkstra/v1/document/user/AbdulWahab938
```

---

## 🎯 API Summary Table

| Method | Endpoint | Purpose | Request Body |
|--------|----------|---------|--------------|
| POST | `/create` | Create new document | `github_username`, `latex`, `base_structure` |
| PUT | `/{document_id}` | Update document | `latex` (optional), `base_structure` (optional) |
| GET | `/{document_id}` | Get single document | None |
| GET | `/user/{github_username}` | Get all user documents | None |
| DELETE | `/{document_id}` | Delete document | None |

---

## 🧪 Testing

### Quick Test - Full CRUD
```bash
python3 test_update_document.py
```

This will:
1. ✅ Create a document
2. ✅ Update it (full)
3. ✅ Retrieve it
4. ✅ List all for user
5. ✅ Partial update

### Manual cURL Tests

**Create:**
```bash
curl -X POST http://localhost:8000/Dijkstra/v1/document/create \
  -H "Content-Type: application/json" \
  -d @test_data.json
```

**Update:**
```bash
curl -X PUT http://localhost:8000/Dijkstra/v1/document/{YOUR_DOC_ID} \
  -H "Content-Type: application/json" \
  -d '{
    "latex": "Updated LaTeX",
    "base_structure": {"version": 2}
  }'
```

**Get User's Documents:**
```bash
curl http://localhost:8000/Dijkstra/v1/document/user/AbdulWahab938
```

**Delete:**
```bash
curl -X DELETE http://localhost:8000/Dijkstra/v1/document/{YOUR_DOC_ID}
```

---

## 💡 Notes

- **Partial Updates**: You can update only `latex`, only `base_structure`, or both
- **Automatic Timestamps**: `updated_at` is automatically set on updates
- **Multiple Versions**: Users can have multiple documents (different resume versions)
- **No Username in DB**: Documents are stored with `profile_id`, not `github_username`
- **404 Errors**: Returned if document/user/profile doesn't exist
