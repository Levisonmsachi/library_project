# 📚 Library Management System

<div align="center">

[![Django](https://img.shields.io/badge/Django-5.2-darkgreen?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)](/)

A **modern, scalable, and intuitive** library management web application built with Django. Designed for seamless book catalog management, availability tracking, and intelligent search capabilities.

[🚀 Quick Start](#-quick-start) • [✨ Features](#-features) • [📖 Documentation](#-documentation) • [🤝 Contributing](#-contributing)

</div>

---

## ✨ Features

### 📊 Comprehensive Dashboard
- **Real-time Statistics**: Track total books, available inventory, and recent additions
- **Visual Analytics**: Monitor library metrics at a glance
- **Smart Dashboard**: Displays curated recent books for quick access

### 🔍 Intelligent Search & Filtering
- **Full-text Search**: Search books by title with case-insensitive matching
- **Status Filtering**: Filter books by availability status
  - Available books
  - Checked out books
- **Advanced Queries**: Efficient database queries with Django ORM

### 📖 Book Management
- **Detailed Book Profiles**: Each book features:
  - Title & Author information
  - Comprehensive descriptions
  - ISBN tracking (unique identifiers)
  - Availability status
  - Creation & modification timestamps
- **Scalable Model**: Built for future expansion (users, borrowing history, etc.)

### 🎨 Modern User Interface
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Django Templates**: Clean, maintainable template architecture
- **Professional Styling**: Modern aesthetic with excellent UX/UI

---

## 🛠 Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Framework** | Django | 5.2.7 |
| **Language** | Python | 3.8+ |
| **Database** | SQLite | Built-in |
| **Frontend** | Django Templates | HTML5 + CSS |
| **Architecture** | Class-Based Views | Django Built-in |

---

## 🚀 Quick Start

### Prerequisites
- **Python** 3.8 or higher
- **pip** (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Levisonmsachi/library_project.git
cd library_project
```

2. **Create and activate virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install django==5.2.7
```

4. **Apply database migrations**
```bash
python manage.py migrate
```

5. **Create superuser (admin account)**
```bash
python manage.py createsuperuser
```

6. **Run development server**
```bash
python manage.py runserver
```

7. **Access the application**
```
http://127.0.0.1:8000/
```

---

## 📋 Available Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page with library statistics |
| `/books/` | GET | List all books with search & filter |
| `/books/?search=keyword` | GET | Search books by title |
| `/books/?status=available` | GET | Filter available books |
| `/books/?status=checked_out` | GET | Filter checked out books |
| `/books/<id>/` | GET | View detailed book information |
| `/admin/` | GET/POST | Django admin panel |

---

## 📂 Project Structure

```
library_project/
├── books/                          # Main application
│   ├── migrations/                 # Database migrations
│   │   └── 0001_initial.py        # Initial schema
│   ├── templates/books/            # HTML templates
│   │   ├── home.html              # Homepage
│   │   ├── book_list.html         # Books listing page
│   │   └── book_detail.html       # Individual book details
│   ├── admin.py                   # Admin configuration
│   ├── apps.py                    # App configuration
│   ├── models.py                  # Database models
│   ├── urls.py                    # URL routing
│   ├── views.py                   # View logic
│   └── tests.py                   # Unit tests
├── library_project/                # Project settings
│   ├── settings.py                # Django configuration
│   ├── urls.py                    # Root URL configuration
│   ├── wsgi.py                    # WSGI configuration
│   └── asgi.py                    # ASGI configuration
├── manage.py                       # Django CLI
├── db.sqlite3                      # SQLite database
└── README.md                       # This file
```

---

## 🔐 Model Architecture

### Book Model
```python
class Book(models.Model):
    title           # CharField (max 200 chars)
    author          # CharField (max 100 chars)
    description     # TextField (unlimited)
    isbn            # CharField (13 digits, unique)
    is_available    # BooleanField (default: True)
    created_at      # DateTimeField (auto-set on creation)
    updated_at      # DateTimeField (auto-updated)
```

---

## 🎯 Usage Examples

### Adding a New Book via Admin Panel
1. Navigate to `http://localhost:8000/admin/`
2. Log in with superuser credentials
3. Click on "Books"
4. Click "Add Book"
5. Fill in the details and save

### Searching for Books
Visit the books listing page and use the search bar:
```
http://localhost:8000/books/?search=Django
```

### Filtering by Availability
```
# View only available books
http://localhost:8000/books/?status=available

# View only checked out books
http://localhost:8000/books/?status=checked_out
```

---

## 🚦 Development

### Run Tests
```bash
python manage.py test
```

### Database Migrations
```bash
# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration history
python manage.py showmigrations
```

### Django Shell
```bash
python manage.py shell

# Example queries
from books.models import Book
Book.objects.all()
Book.objects.filter(is_available=True).count()
```

---

## 🔮 Future Enhancements

- [ ] **User Accounts**: Implement user authentication and profiles
- [ ] **Borrowing System**: Track book checkouts and returns
- [ ] **Reservation System**: Allow users to reserve unavailable books
- [ ] **Review System**: Add user ratings and reviews
- [ ] **API**: Build REST API for third-party integrations
- [ ] **Advanced Search**: Implement full-text search and filters
- [ ] **Email Notifications**: Reminder emails for due dates
- [ ] **Mobile App**: Native mobile application
- [ ] **Analytics Dashboard**: Advanced library analytics
- [ ] **Multi-language Support**: i18n implementation

---

## 📧 Configuration

### Environment Variables
Create a `.env` file in the project root:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### Database Setup
The project uses SQLite by default. To switch to PostgreSQL:

1. Install psycopg2:
```bash
pip install psycopg2-binary
```

2. Update `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
```bash
git clone https://github.com/Levisonmsachi/library_project.git
```

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

### Code Standards
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) Python style guide
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Library Project Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 🆘 Support & Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'django'`
```bash
# Solution: Install Django
pip install django==5.2.7
```

**Issue**: Database locked error
```bash
# Solution: Delete db.sqlite3 and remake migrations
rm db.sqlite3
python manage.py migrate
```

**Issue**: Port 8000 already in use
```bash
# Solution: Use different port
python manage.py runserver 8001
```

### Getting Help
- 📖 [Django Documentation](https://docs.djangoproject.com/)
- 🐛 [Issue Tracker](https://github.com/Levisonmsachi/library_project/issues)
- 💬 [Discussions](https://github.com/Levisonmsachi/library_project/discussions)

---

## 📞 Contact & Social

| Contact | Link |
|---------|------|
| **Email** | levisonmsachi03@gmail.com |
| **GitHub** | [@Levisonmsachi](https://github.com/Levisonmsachi) |
| **Twitter** | [@levvie-livvie](https://twitter.com/Levisonmsachi) |

---

<div align="center">

**Made with ❤️ by LEVVIE-LIVVIE**

⭐ If you find this project helpful, please give it a star!

[Back to top ↑](#-library-management-system)

</div>
