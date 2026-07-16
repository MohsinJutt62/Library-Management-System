<div align="center">
  <h1>📚 Library Management System</h1>
  <p><strong>A modern, comprehensive desktop application for automating library operations.</strong></p>

  <!-- Badges -->
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-brightgreen.svg" alt="GUI Framework">
  <img src="https://img.shields.io/badge/Architecture-MVC-orange.svg" alt="Architecture">
  <img src="https://img.shields.io/badge/Storage-JSON-yellow.svg" alt="Database">
</div>

<br>

## 📖 Project Overview

The **Library Management System** is a robust, multi-user desktop application designed to streamline the daily operations of a library. Built with a focus on clean software engineering principles, it provides an intuitive interface for both library members and administrators to manage inventory, track borrowings, handle fine payments, and automate reservations without the need for an external database server.

## ✨ Key Features

### 👤 Member Dashboard
* **Smart Catalog:** Real-time search by Title, Author, or Category with availability status.
* **Borrowing & Returns:** Track active borrowings, view due dates with visual indicators, and monitor borrowing history.
* **Reservation System:** Reserve currently unavailable books and track reservation status.
* **Fine Management:** Transparent tracking and payment system for overdue fines.

### 🛡️ Admin Dashboard
* **Inventory Control:** Comprehensive tools to add, update, and remove books from the library catalog.
* **Member Management:** Register new users, manage active memberships, and maintain compliance.
* **Circulation Management:** Issue books, process returns, calculate dynamic fines, and track overdue items.
* **Analytics & Reporting:** Generate detailed inventory, overdue, member, and financial reports.

## 🛠️ Technology Stack

* **Programming Language:** Python 3.x
* **GUI Framework:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (Provides a modern, responsive, and themeable UI)
* **Data Storage:** File-based JSON architecture (No SQL/external servers required)
* **Design Patterns:** Model-View-Controller (MVC), Singleton, Factory, and Observer patterns

## 🏗️ Architecture & File Structure

The application is strictly modularized to separate presentation, business logic, and data access layers:

```text
Library Management System/
├── main.py                 # Application entry point
├── auth.py                 # Authentication & Session Management
├── member_dashboard.py     # Member GUI & Interactions
├── admin_dashboard.py      # Administrator GUI & Reporting
├── data_handler.py         # Business Logic, Validation & JSON File I/O
└── data/                   # JSON storage (books, users, issues, fines, etc.)
```

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Library-Management-System.git
   cd "Library Management System"
   ```

2. **Install dependencies:**
   Ensure you have Python 3.8+ installed. Then run:
   ```bash
   pip install customtkinter Pillow
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```
   *Note: On the first run, the system will automatically generate the required `/data` directory and JSON files.*

## 📸 Screenshots
> - Login/Authentication Screen
> - Admin Dashboard Overview
> - Member Search & Catalog View
> - Book Issuance / Return Processing Dialog

<div align="center">

<img width="748" height="663" alt="{DB43D860-A85A-46BC-8F4D-5454C01349E8}" src="https://github.com/user-attachments/assets/ccdd535a-bf9e-4582-9f02-c7fb44272268" />
<img width="1384" height="869" alt="{8C7B8E94-641F-4B1E-8897-D4280F133EEB}" src="https://github.com/user-attachments/assets/9dcaec5f-c244-4604-bcce-3aa844e31b61" />
<img width="1379" height="581" alt="{CBE7FA5C-5F0B-4FA6-A101-D460F3660510}" src="https://github.com/user-attachments/assets/ef0f8b70-c42b-4bf0-a94e-a318807fcddd" />
<img width="1069" height="437" alt="{B59EB58F-FF38-492D-B2BB-DF6EC2E2564C}" src="https://github.com/user-attachments/assets/8a2ff71d-1304-4fa2-bd25-532fe11e702c" />

## Admin Dashboard
<img width="1503" height="932" alt="{931AA4F5-CA6A-49FE-8BE3-234C32DF95AF}" src="https://github.com/user-attachments/assets/cf24f24a-e07f-4492-8eaf-d09f602178f6" />
<img width="1471" height="548" alt="{969AED98-477D-4D35-AED7-9E63BAD69315}" src="https://github.com/user-attachments/assets/49e8218e-3691-406e-9098-6743832d5a91" />
<img width="1441" height="732" alt="{57EBFB49-FEFE-49A6-B868-157731052492}" src="https://github.com/user-attachments/assets/40b75dba-3b7e-45bf-b4b7-90581e55ddb0" />
<img width="1296" height="329" alt="{E44112EF-EB04-44F7-B827-88CE5C7EA3A7}" src="https://github.com/user-attachments/assets/045da836-3d5c-4a19-a9dc-eefb2a539a89" />


  
</div>

## 👨‍💻 Developer / Author

Developed by **Muhammad Mohsin Sajjad**  
*Software Engineering | Python Developer*

---
⭐ *If you found this project helpful, please consider giving it a star on GitHub!*
