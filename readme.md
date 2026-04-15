# 🧠 Genderize API — Production-Ready Django Service

A robust, production-ready REST API built with Django and Django REST Framework that predicts gender from a given name using the **Genderize.io** service.

Designed with clean architecture, proper validation, and deployment-readiness in mind.

---

## ✨ Overview

The Genderize API provides a simple interface for predicting gender based on names. It integrates with an external service, applies validation, and enriches responses with confidence metrics and metadata.

This project demonstrates:

* Clean API design principles
* External API integration
* Structured error handling
* Deployment-ready configuration

---

## ⚙️ Architecture

```
Client → Django API → External Service (Genderize.io) → Processed Response
```

* **Django REST Framework** handles request/response lifecycle
* **Requests** library manages external API communication
* **Custom logic layer** enriches and validates responses

---

## 📡 API Endpoints

### 🔹 Health Check

**GET `/api/`**

```json
{
  "status": "success",
  "message": "Welcome to the Genderize API"
}
```

---

### 🔹 Classify Name

**GET `/api/classify/?name={name}`**

#### Example Request

```bash
curl "http://localhost:8000/api/classify/?name=tolu"
```

#### Successful Response

```json
{
  "status": "success",
  "data": {
    "name": "tolu",
    "gender": "female",
    "probability": 0.87,
    "sample_size": 1234,
    "is_confident": true,
    "processed_at": "2026-04-14T12:00:00Z"
  }
}
```

---

## 🧪 Error Handling

The API follows structured error responses:

| Scenario          | Status Code | Response                             |
| ----------------- | ----------- | ------------------------------------ |
| Missing parameter | 400         | `"Missing or empty name parameter"`  |
| Invalid data      | 422         | `"name must be a string"`            |
| No prediction     | 422         | `"No prediction available"`          |
| Upstream failure  | 502         | `"Upstream service error"`           |
| Network failure   | 500         | `"Failed to reach upstream service"` |

---

## 🧠 Decision Logic

Confidence is derived using:

* `probability ≥ 0.7`
* `sample_size ≥ 100`

```text
is_confident = True if both conditions are met
```

---

## 🛠️ Tech Stack

* **Python 3.11+**
* **Django**
* **Django REST Framework**
* **Requests**
* **WhiteNoise** (static file serving)
* **Gunicorn** (production server)

---

## 🚀 Getting Started

### 1. Clone repository

```bash
git clone https://github.com/Douglasemmanuel/HNG14-STAGE-0.git
cd hng_stage0
```

### 2. Setup virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run development server

```bash
python manage.py runserver
```

---

## 🧩 Configuration

### Environment Variables (optional)

| Variable        | Description               |
| --------------- | ------------------------- |
| `DEBUG`         | Enable/disable debug mode |
| `ALLOWED_HOSTS` | Allowed domains           |

---

## 📦 Deployment

* **Vercel** (serverless)
* **Render** (recommended)
* **Railway**

### Notes

* No database required
* Stateless architecture
* External dependency: `https://api.genderize.io`

---

## 📁 Project Structure

```
.
├── hng_stage0/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── app/
│   ├── views.py
│   ├── urls.py
├── manage.py
├── requirements.txt

```

---



## 🔐 Security Considerations

* Input validation enforced
* External request timeout configured
* No sensitive data stored

---



## 📄 License

MIT License — free to use and modify.
