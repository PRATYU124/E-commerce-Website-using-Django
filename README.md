# 🛒 Django E-Commerce Website

This is a fully functional e-commerce web application built using **Django**. It includes features like product listings, shopping cart, checkout, user authentication, and admin management. Ideal for learning or adapting to real-world commerce applications.

## 🚀 Features

- User registration and authentication (login/logout)
- Product catalog with search and category filtering
- Add to cart / remove from cart
- Cart persistence for logged-in users
- Checkout and order summary
- Admin panel for product and order management
- Responsive design using Bootstrap or TailwindCSS

## 🛠 Tech Stack

### Backend
- **Python 3.8+**
- **Django 4.x**
- **SQLite** (for development) or **PostgreSQL/MySQL** (for production)
- **Django Admin** for backend management

### Frontend
- **HTML5/CSS3**
- **Bootstrap 5** / TailwindCSS
- **JavaScript** for dynamic cart updates

### Tools & Libraries
- **Django REST Framework** (optional for APIs)
- **Stripe/PayPal API** (optional for payment integration)
- **Celery & Redis** (optional for async tasks like email)
- **Docker** (optional for deployment)
- **Git & GitHub** for version control

## 📦 Project Structure
ecommerce/
├── ecommerce/ # Project settings
├── store/ # Core app (products, cart, orders)
├── users/ # Custom user auth
├── templates/ # HTML templates
├── static/ # Static files (CSS/JS)
├── media/ # Uploaded images
├── manage.py
