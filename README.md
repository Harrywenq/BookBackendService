# 📚 Book Management API

## 🧾 Giới thiệu

**Book Management API** là một RESTful API được xây dựng bằng **FastAPI**, dùng để quản lý **sách**, **tác giả** và **thể loại**.  
Dự án được thiết kế theo cấu trúc rõ ràng, dễ mở rộng, phù hợp cho việc học tập, thực hành backend hoặc làm nền tảng cho các hệ thống lớn hơn.

API sử dụng **SQLAlchemy ORM** để thao tác cơ sở dữ liệu và **Alembic** để quản lý migration, đi kèm tài liệu API tự động thông qua **Swagger (OpenAPI)**.

---

## 🚀 Công nghệ sử dụng

- **Python 3.9+**
- **FastAPI** – Framework xây dựng API hiệu năng cao
- **SQLAlchemy** – ORM cho Python
- **Alembic** – Database migration tool
- **SQLite** – Database mặc định
- **Uvicorn** – ASGI server
- **Swagger UI / OpenAPI** – Tài liệu API tự động

---

## 📂 Cấu trúc thư mục
```
BookService/
├── app/
│ ├── api/
│ │ ├── endpoints/
│ │ │ ├── authors.py
│ │ │ ├── books.py
│ │ │ └── categories.py
│ │ └── deps.py
│ │
│ ├── core/
│ │ └── config.py
│ │
│ ├── db/
│ │ ├── base.py
│ │ ├── session.py
│ │ └── models/
│ │ ├── author.py
│ │ ├── book.py
│ │ └── category.py
│ │
│ ├── schemas/
│ │
│ ├── main.py
│ └── static/
│ └── covers/
│
├── alembic/
│ ├── versions/
│ └── env.py
│
├── alembic.ini
├── requirements.txt
└── README.md
```

---

## 🗃️ Database schema
```
### 📖 Books
- id
- title
- description
- published_year
- author_id
- category_id
- cover_image
- created_at
- updated_at

### ✍️ Authors
- id
- name
- bio

### 🏷️ Categories
- id
- name
- description
```
---

## ⚙️ Cài đặt & chạy dự án

### 1️⃣ Clone repository
```
git clone https://github.com/your-username/book-management-api.git
cd book-management-api
```
2️⃣ Tạo virtual environment
```
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```
3️⃣ Cài đặt dependencies
```
pip install -r requirements.txt
Khuyến nghị version:

fastapi==0.95.2
pydantic==1.10.x
sqlalchemy<2.0
alembic
```
4️⃣ Khởi tạo database
```
alembic upgrade head
```
5️⃣ Chạy server
```
uvicorn app.main:app --reload
📘 API Documentation
Sau khi server chạy, truy cập:

Swagger UI:
http://127.0.0.1:8000/docs

OpenAPI JSON:
http://127.0.0.1:8000/openapi.json
```

🎯 Mục tiêu dự án
Thực hành xây dựng REST API với FastAPI

Áp dụng SQLAlchemy ORM và relationship

Sử dụng Alembic để quản lý migration

Làm nền tảng cho các dự án backend thực tế
