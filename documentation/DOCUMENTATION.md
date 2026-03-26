# Project Structure Documentation

## Overview

This project follows a modular Django architecture, separating concerns into:

* **Core project configuration**
* **Applications (features)**
* **Reusable UI components**
* **Global static and templates**

This structure is designed for scalability, maintainability, and reusability.

---

## Root Structure

```
source/
└── django/
    └── core/
```

* `source/django/core/` is the main Django project root.

---

## 1. Core Configuration

```
core/app/
```

Contains the main Django project configuration:

* `settings.py` → global configuration
* `urls.py` → root routing
* `wsgi.py` / `asgi.py` → deployment entry points

---

## 2. Applications (Feature Modules)

```
core/applications/
```

Each folder here represents a **feature-specific Django app**.

### Example apps:

#### `account/`

Handles authentication logic:

* Handlers (custom logic)
* Templates
* Static files

#### `core/`

General-purpose logic shared across the app.

#### `employeemanager/`

Feature module for employee management:

* Views
* Templates (`templates/employeemanager/`)
* Static files (`static/employeemanager/`)
* Migrations

### Pattern

Each app follows:

```
app_name/
├── migrations/
├── static/
│   └── app_name/
├── templates/
│   └── app_name/
├── views.py
├── models.py
```

This ensures:

* No naming conflicts
* Clear ownership per feature

---

## 3. Components (Reusable UI System)

```
core/components/
```

This is a **custom component system** (similar to frontend frameworks).

### Structure:

```
components/core/
├── button/
├── header/
├── footer/
```

Each component contains:

```
component/
├── templates/
│   └── core/
├── static/
│   └── core/
├── apps.py
```

### Purpose

* Reusable UI elements (like buttons, headers, footers)
* Shared across multiple apps
* Encourages DRY design

### Usage

Components are included in templates using:

```
{% include "core/button.html" %}
```

---

## 4. Global Static Files

```
core/static/
```

Used for **global styles and assets**:

```
static/
└── styles/
    └── pages/
```

This is for:

* Page-level styles
* Shared CSS not tied to a specific app

---

## 5. Global Templates

```
core/templates/
```

Used for **project-wide templates**, such as:

```
templates/
└── pages/
```

Examples:

* Base layouts
* Shared pages

---

## 6. Template Resolution

Django loads templates from:

1. Each app’s `templates/` folder
2. Global `core/templates/`

Because `APP_DIRS = True`, all templates are accessible globally.

### Best Practice

Always namespace templates:

```
app_name/template.html
```

Example:

```
employeemanager/employeemanager.html
```

---

## 7. Static File Resolution

Static files follow:

```
static/app_name/...
```

Example:

```
employeemanager/styles/employeemanager.css
```

Usage in templates:

```
{% load static %}
<link href="{% static 'employeemanager/styles/employeemanager.css' %}" />
```

---

## Design Principles

### 1. Separation of Concerns

* Applications handle features
* Components handle UI
* Core handles configuration

### 2. Reusability

* Components are shared across apps
* Avoid duplication

### 3. Scalability

* Easy to add new apps without breaking structure

### 4. Consistency

* Each app follows the same internal structure

---

## Summary

* `applications/` → feature logic
* `components/` → reusable UI
* `static/` → global assets
* `templates/` → global templates
* `app/` → Django configuration

This structure allows the project to grow cleanly while keeping code organized and maintainable.
