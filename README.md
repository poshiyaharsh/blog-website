
# BlogSpot - Django Blogging Platform

BlogSpot is a full‑featured multi‑user blogging system built using **Django**.  
It includes user authentication, blog creation, comments, profile management, and a clean responsive UI.

---

## 🚀 Features

### ✔ User Module  
- User Signup / Login / Logout  
- Profile View & Edit  
- Secure authentication via Django Auth

### ✔ Blog Module  
- Create, Edit, Delete blog posts  
- Add image to posts  
- Categories  
- View all blogs  
- Like posts  
- Recent posts & top‑liked posts sections

### ✔ Comments Module  
- Add comments  
- Delete comments  
- Comment counter

### ✔ Contact Module  
- Contact form  
- Stores user messages in database

### ✔ Other  
- Fully responsive UI  
- Static & media file handling  
- Clean, modern blog layout  
- Multi‑app Django project structure

---

## 📁 Project Structure

```
blog/
 ├── blog/                 # Main project
 ├── users/                # Authentication & Profile
 ├── blogapp/              # Homepage + Blog listing
 ├── post/                 # Post create/edit/delete
 ├── contact/              # Contact form
 ├── templates/            # All HTML files
 ├── static/               # CSS / JS / Images
 └── media/                # Uploaded images
```

---

## 🛠 Technology Stack

- **Python 3**
- **Django 4+**
- **SQLite3** (default DB)
- **HTML, CSS, Bootstrap**
- **FontAwesome Icons**

---

## 🔧 Installation Guide

### 1️⃣ Create Virtual Environment  
```
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 2️⃣ Install Dependencies  
```
pip install django
```

### 3️⃣ Run Migrations  
```
python manage.py migrate
```

### 4️⃣ Start Server  
```
python manage.py runserver
```

---

## 🔑 Default URLs

| Path | Description |
|------|-------------|
| `/` | Home Page |
| `/blog` | All blogs |
| `/signin` | Login |
| `/signup` | Register |
| `/create` | Create blog post |
| `/post/<id>` | Blog details |
| `/profile/<id>` | User profile |

---

## 📌 Developer

**Harsh Poshiya**  
🔗 GitHub: https://github.com/poshiyaharsh  
🔗 LinkedIn: https://www.linkedin.com/in/harshposhiya  

---

## 📜 License  
Open‑source for educational use.

