# Deployment Guide (Vercel)

## Overview

This project is deployed on **Vercel** using its Python runtime.
Since Vercel is optimized for serverless environments, Django requires some configuration, especially for:

* Environment variables
* Static files
* Database connection

---

## REQUIREMENTS
* postgressql
* python 1.12 runtime
* vercel account

## 1. Environment Variables

Set the following variables in Vercel:

```env
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,monografico-tarea2.vercel.app

DJANGO_ENVIRONMENT=production

DJANGO_CDN_URL=yourpseudocdn.vercel.app

POSTGRESQL_DATABASE_NAME=postgres
POSTGRESQL_DATABASE_USER=postgres.zdnh
POSTGRESQL_DATABASE_PASSWORD=YOUR_PASSWORD
POSTGRESQL_DATABASE_HOST=project.pooler.yourpostgresqlhost.com
POSTGRESQL_DATABASE_PORT=6543
```

### Notes

* `DJANGO_ENVIRONMENT`

  * `development` → enables debug mode
  * `production` → disables debug and enables CDN usage

* `DJANGO_ALLOWED_HOSTS`

  * Must include your Vercel domain

---

## 2. Static Files (Important)

Vercel does **not serve Django static files automatically**, so you must use a CDN.

### Step 1 — Collect static files

```bash
python manage.py collectstatic --no-input
```

This generates:

```bash
staticfiles/
```

---

### Step 2 — Upload to CDN

* Go inside `staticfiles/`
* Upload all files to your CDN root
* Set:

```env
DJANGO_CDN_URL=your-cdn-domain.vercel.app
```

---

### Step 3 — Django config behavior

In production:

```python
STATIC_URL = f"https://{CDN_HOST}/"
```

So all static assets are loaded from the CDN.

---

## 3. Vercel Configuration

The project already includes a `vercel.json` file inside:

```bash
source/django/core/
```

So no additional configuration is required.

Vercel will:

* Detect Python runtime
* Install dependencies
* Run the app automatically

---

## 4. Database

This project uses PostgreSQL.

Make sure:

* Your database allows external connections
* Credentials match the environment variables

note: you can use supabase postgresql

---

## 5. Deployment Steps

### 1. create a fork of the project

In github press the fock button

---

### 2. Import project in Vercel

* Go to Vercel dashboard
* Import your repository
* Set environment variables
* set root folder to /source/django/core

---

### 3. Deploy

Vercel will:

* Install dependencies
* Build the project
* Deploy automatically

---

## 6. Common Issues

### Static files not loading

* Check `DJANGO_CDN_URL`
* Ensure files were uploaded correctly

---

### App not loading / 500 error

* Check logs in Vercel dashboard
* Verify environment variables
* Ensure `ALLOWED_HOSTS` includes your domain

---

### Database connection errors

* Verify host, port, and credentials
* Ensure database allows external connections

---

## Summary

* Django runs on Vercel via Python runtime
* Static files must be served from a CDN
* Environment variables control behavior
* PostgreSQL is used for persistence

This setup enables a serverless deployment of Django using Vercel.
