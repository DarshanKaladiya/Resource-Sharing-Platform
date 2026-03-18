# Resource-Sharing Platform 🚀

[](https://www.python.org/)
[](https://www.djangoproject.com/)
[](https://opensource.org/licenses/MIT)

A robust, **Django-based web application** designed to facilitate seamless academic resource sharing. This platform allows educators and students to upload, categorize, and manage study materials in a secure, organized environment—similar to Google Classroom but tailored for custom institutional needs.

-----

## 🌟 Key Features

  * **Role-Based Access Control (RBAC):** Distinct functionalities for Administrators, Teachers (Uploaders), and Students (Viewers).
  * **Secure File Management:** Integrated handling of PDFs, Documents, and Images with categorized storage.
  * **Interactive Dashboard:** User-specific views to track recently accessed or uploaded resources.
  * **Search & Filter:** Advanced querying to find resources by subject, date, or author.
  * **Responsive UI:** Fully optimized for mobile and desktop using **Bootstrap 5**.

-----

## 🛠️ Tech Stack

  * **Backend:** Python, Django
  * **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
  * **Database:** SQLite (Development)
  * **Environment Management:** Python Dotenv (for security)

-----

## 🚀 Getting Started

### Prerequisites

  * Python 3.x installed
  * Pip (Python package manager)

### Installation

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/DarshanKaladiya/Resource-Sharing-Platform.git
    cd Resource-Sharing-Platform
    ```

2.  **Install Dependencies**
    *(Note: It is recommended to use a virtual environment)*

    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Setup**
    Create a `.env` file in the root directory and add your secrets:

    ```env
    DEBUG=True
    SECRET_KEY=your_secret_key_here
    DATABASE_URL=your_database_url
    ```

4.  **Database Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Run the Server**

    ```bash
    python manage.py runserver
    ```

    Access the application at `http://127.0.0.1:8000/`.

-----

## 📂 Project Structure

```text
├── core/               # Project configurations and settings
├── resources/          # Main application logic (Models, Views, Templates)
├── media/              # User-uploaded files (Git ignored in production)
├── static/             # CSS, JavaScript, and Images
├── templates/          # Global HTML templates
├── .gitignore          # Files to be excluded from Git
├── manage.py           # Django command-line utility
└── requirements.txt    # List of project dependencies
```

-----

## 🛡️ Security & Best Practices

  * **Environment Variables:** Sensitive data is managed via `.env` to prevent credential leaks.
  * **CSRF Protection:** All forms are secured using Django’s built-in Cross-Site Request Forgery protection.
  * **Input Validation:** Strict server-side validation for all file uploads.

-----

## ✉️ Contact

**Darshan Kaladiya** - www.linkedin.com/in/darshan-kaladiya-968093346 

Project Link: [https://github.com/DarshanKaladiya/Resource-Sharing-Platform](https://www.google.com/search?q=https://github.com/DarshanKaladiya/Resource-Sharing-Platform)
