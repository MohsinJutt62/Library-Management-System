# Library Management System - Complete Project Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [System Features](#system-features)
4. [Architecture & Design](#architecture--design)
5. [Database Design](#database-design)
6. [GUI Forms & Components](#gui-forms--components)
7. [File Structure](#file-structure)
8. [Module Descriptions](#module-descriptions)
9. [Data Flow](#data-flow)
10. [Installation & Setup](#installation--setup)
11. [User Workflows](#user-workflows)
12. [API Methods](#api-methods)

---

## Project Overview

### What is the Library Management System?

The Library Management System is a comprehensive desktop application designed to automate and streamline the operations of a library. It provides a complete solution for managing books, members, borrowing/returning operations, fines, and reservations.

### Purpose
- **For Members**: Easy access to search books, borrow, reserve, and manage their account
- **For Librarians/Admins**: Complete control over library inventory, member management, and fine collection
- **Overall**: Reduce manual work, improve efficiency, and provide better service to library users

### Project Type
- **Desktop Application** (GUI-based)
- **Multi-user System** (Members & Admins)
- **File-based Storage** (JSON format)
- **Built with Python** (CustomTkinter for GUI)

---

## Technology Stack

### Programming Language
- **Python 3.x** - Core language for application logic

### GUI Framework
- **CustomTkinter (ctk)** - Modern, beautiful GUI framework for Python
  - Dark/Light theme support
  - Native-looking buttons, labels, and frames
  - Scrollable frames for handling large lists

### Database/Storage
- **JSON Format** - File-based data storage
  - No external database required
  - Easy to read and understand
  - Files stored in `data/` folder

### Libraries Used
```
customtkinter >= 5.0        # Modern GUI
Pillow (PIL)                # Image handling
datetime                    # Date & time operations
json                        # Data serialization
os                          # File operations
hashlib                     # Password hashing (optional)
```

### System Requirements
- Windows/Linux/macOS with Python 3.8+
- 50MB disk space
- Standard display resolution (1920x1080 minimum recommended)

---

## System Features

### Member Features (11 Features)

#### 1. **Register/Login** ✅
- New members can create accounts with email and password
- Login with credentials
- Session management
- Data validation before registration

#### 2. **Search Books** ✅
- Search by Title
- Search by Author
- Search by Category
- Real-time search results display

#### 3. **Browse Catalog** ✅
- View all available books in the library
- Display book details: Title, Author, Category, ISBN
- See availability status of each book

#### 4. **View Book Availability** ✅
- Check how many copies are available
- See total inventory vs available copies
- Visual indicators (✅ Available / ❌ Not Available)

#### 5. **Reserve Books** ✅
- Reserve books that are currently unavailable
- Get notified when book becomes available
- Track reservation status
- Cancel reservations if needed

#### 6. **View Borrowed Books** ✅
- See all currently borrowed books
- Book details: Title, Author, Issue Date
- Know which books are outstanding

#### 7. **View Due Dates** ✅
- See return due dates for each borrowed book
- Visual warnings for overdue books
- Days remaining calculator

#### 8. **View Pending Fines** ✅
- Check all unpaid fines
- See fine amount and reason
- Status of fines (Paid/Unpaid)

#### 9. **Pay Fines** ✅
- Payment functionality for unpaid fines
- Mark fines as paid
- Payment history

#### 10. **View Borrowing History** ✅
- Complete record of all past borrowings
- Returned books history
- Search and filter by date range

#### 11. **Logout** ✅
- Secure logout from system
- Session termination

---

### Librarian/Admin Features (15 Features)

#### 1. **Admin Login** ✅
- First admin registration with special key
- Login for existing admins
- Admin verification

#### 2. **Add Books** ✅
- Add new books to library inventory
- Input fields:
  - Title, Author, Category
  - ISBN, Publisher
  - Total Copies, Price
  - Description
- Automatic ID and timestamp generation
- Duplicate ISBN check

#### 3. **Update Books** ✅
- Edit existing book information
- Update inventory counts
- Modify book details
- Availability status changes

#### 4. **Delete Books** ✅
- Remove books from inventory
- Soft/Hard delete options
- Prevent deletion if borrowed

#### 5. **Manage Inventory** ✅
- View current stock levels
- Add/remove copies
- Availability management
- Stock warnings

#### 6. **Register Members** ✅
- Create member accounts in system
- Input: Name, Email, Phone, Address
- Member ID assignment
- Duplicate email check

#### 7. **Update Members** ✅
- Edit member information
- Update contact details
- Modify member status (Active/Inactive)

#### 8. **Remove Members** ✅
- Delete member accounts
- Prevent deletion if outstanding fines
- Archive option for audit trail

#### 9. **View Members** ✅
- List all registered members
- Member details display
- Search by name or email
- Membership status

#### 10. **Issue Books** ✅
- Assign books to members
- Select member and book
- Set return due date
- Automatic availability update
- Issue confirmation

#### 11. **Process Book Returns** ✅
- Record book returns
- Update availability
- Fine calculation for overdue books
- Return confirmation

#### 12. **Manage Fines** ✅
- View all fines (Paid/Unpaid)
- Create fines for overdue books
- Fine amount configuration
- Fine history

#### 13. **Collect Payments** ✅
- Mark fines as paid
- Payment date recording
- Payment confirmation
- Receipt generation

#### 14. **Generate Reports** ✅
- Inventory Report: Current stock levels, availability
- Overdue Books Report: List of overdue books with member details
- Member Report: All registered members, their borrowing status
- Fine Report: Collected and pending fines
- Export data option

#### 15. **Manage Admins** ✅
- Add new admin users (First admin only)
- Remove admin accounts
- View all admins
- Admin role management
- Restrict deletion of first admin

---

## Architecture & Design

### System Architecture Layers

```
┌─────────────────────────────────────────┐
│     Presentation Layer (GUI)             │
│  - AuthWindow                           │
│  - MemberDashboard                      │
│  - AdminDashboard                       │
└─────────────────────────────────────────┘
              ↓ (Events)
┌─────────────────────────────────────────┐
│   Business Logic Layer                   │
│  - Authentication Logic                 │
│  - Book Management                      │
│  - Member Management                    │
│  - Borrowing/Return Logic               │
│  - Fine Calculation                     │
│  - Reservation System                   │
└─────────────────────────────────────────┘
              ↓ (CRUD Operations)
┌─────────────────────────────────────────┐
│    Data Access Layer (DataHandler)      │
│  - File I/O Operations                  │
│  - JSON Read/Write                      │
│  - Data Validation                      │
└─────────────────────────────────────────┘
              ↓ (Persistent Storage)
┌─────────────────────────────────────────┐
│   Data Layer (JSON Files)                │
│  - books.txt                            │
│  - users.txt                            │
│  - admins.txt                           │
│  - issued.txt                           │
│  - fines.txt                            │
│  - reservations.txt                     │
└─────────────────────────────────────────┘
```

### Design Patterns Used

1. **Model-View-Controller (MVC)**
   - Models: DataHandler class (Business logic & data access)
   - Views: AuthWindow, MemberDashboard, AdminDashboard (GUI)
   - Controllers: Event handlers in GUI classes

2. **Singleton Pattern**
   - DataHandler class methods are static
   - Single instance of data management

3. **Factory Pattern**
   - Different dashboard creation based on user type

4. **Observer Pattern**
   - UI updates on data changes
   - Event-driven architecture

---

## Database Design

### Data Storage Format
All data is stored in **JSON format** in the `data/` folder.

### Database Schema

#### 1. **Books** (`books.txt`)
```json
[
  {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "category": "Fiction",
    "isbn": "978-0-7432-7356-5",
    "publisher": "Scribner",
    "total_copies": 5,
    "available_copies": 3,
    "price": 299.99,
    "description": "A classic American novel",
    "created_at": "2024-05-09 10:30:00"
  }
]
```

**Fields:**
- `id` (Integer) - Unique identifier
- `title` (String) - Book title
- `author` (String) - Author name
- `category` (String) - Genre/Category
- `isbn` (String) - ISBN number (unique)
- `publisher` (String) - Publishing company
- `total_copies` (Integer) - Total inventory
- `available_copies` (Integer) - Available for borrowing
- `price` (Float) - Book price
- `description` (String) - Book description
- `created_at` (Timestamp) - Creation date

---

#### 2. **Members/Users** (`users.txt`)
```json
[
  {
    "id": 1,
    "name": "Ali Ahmed",
    "email": "ali@email.com",
    "password": "hashed_password",
    "phone": "03001234567",
    "address": "123 Main Street, Karachi",
    "member_id": "MEM001",
    "registered_at": "2024-05-09 10:30:00"
  }
]
```

**Fields:**
- `id` (Integer) - Unique member ID
- `name` (String) - Full name
- `email` (String) - Email address (unique)
- `password` (String) - Hashed password
- `phone` (String) - Contact number
- `address` (String) - Home address
- `member_id` (String) - Member reference ID
- `registered_at` (Timestamp) - Registration date

---

#### 3. **Admins** (`admins.txt`)
```json
[
  {
    "id": 1,
    "name": "Librarian Admin",
    "email": "admin@library.com",
    "password": "hashed_password",
    "created_at": "2024-05-09 10:30:00"
  }
]
```

**Fields:**
- `id` (Integer) - Unique identifier
- `name` (String) - Admin name
- `email` (String) - Email address (unique)
- `password` (String) - Hashed password
- `created_at` (Timestamp) - Creation date

---

#### 4. **Issued Books** (`issued.txt`)
```json
[
  {
    "id": 1,
    "book_id": 1,
    "member_id": 1,
    "issue_date": "2024-05-09 10:30:00",
    "due_date": "2024-05-23",
    "return_date": null,
    "status": "issued"
  }
]
```

**Fields:**
- `id` (Integer) - Issue record ID
- `book_id` (Integer) - Reference to book
- `member_id` (Integer) - Reference to member
- `issue_date` (Timestamp) - When borrowed
- `due_date` (Date) - Return deadline
- `return_date` (Timestamp/Null) - Actual return date
- `status` (String) - "issued" or "returned"

---

#### 5. **Fines** (`fines.txt`)
```json
[
  {
    "id": 1,
    "member_id": 1,
    "issue_id": 1,
    "amount": 50.00,
    "reason": "Overdue by 5 days",
    "created_at": "2024-05-24 10:30:00",
    "status": "unpaid",
    "paid_at": null
  }
]
```

**Fields:**
- `id` (Integer) - Fine record ID
- `member_id` (Integer) - Member who owes fine
- `issue_id` (Integer) - Related issue record
- `amount` (Float) - Fine amount
- `reason` (String) - Reason for fine
- `created_at` (Timestamp) - Fine creation date
- `status` (String) - "unpaid" or "paid"
- `paid_at` (Timestamp/Null) - Payment date

---

#### 6. **Reservations** (`reservations.txt`)
```json
[
  {
    "id": 1,
    "book_id": 2,
    "member_id": 1,
    "reserved_at": "2024-05-09 10:30:00",
    "status": "pending"
  }
]
```

**Fields:**
- `id` (Integer) - Reservation ID
- `book_id` (Integer) - Book being reserved
- `member_id` (Integer) - Member who reserved
- `reserved_at` (Timestamp) - Reservation date
- `status` (String) - "pending", "cancelled", or "issued"

---

### Relationships

```
Member (1) ──────→ (∞) Issued Books
Member (1) ──────→ (∞) Fines
Member (1) ──────→ (∞) Reservations

Book (1) ──────→ (∞) Issued Books
Book (1) ──────→ (∞) Reservations

Issued Books (1) ──────→ (1) Fine

Admin (1) ──────→ (∞) Operations
```

---

## GUI Forms & Components

### Form 1: Authentication Window (Initial Screen)

**Purpose**: Login and Registration for both Members and Admins

**Components:**

#### Login Form
```
┌─────────────────────────────────────┐
│   🎓 LIBRARY MANAGEMENT             │
│                                     │
│   Select Account Type:              │
│   ○ Admin  ● Member                 │
│                                     │
│   Email/Username: [_____________]   │
│   Password: [_____________]          │
│                                     │
│   [Login]      [Sign Up]            │
│   [Back]       [Help]               │
└─────────────────────────────────────┘
```

**Input Fields:**
- Account Type (Radio Button): Admin / Member
- Email/Username (Text Entry)
- Password (Password Entry - masked)

**Buttons:**
- Login Button → Verify credentials → Open respective dashboard
- Sign Up Button → Show registration form
- Back Button → Navigate between forms
- Help Button → Show assistance

#### Sign Up Form
```
┌─────────────────────────────────────┐
│   Create New Account                │
│                                     │
│   Account Type:                     │
│   ○ Admin  ● Member                 │
│                                     │
│   Name: [_________________]         │
│   Email: [_________________]        │
│   Password: [_________________]     │
│   Confirm Password: [_____________] │
│                                     │
│   [Member Fields]                   │
│   Phone: [_________________]        │
│   Address: [_________________]      │
│                                     │
│   [Admin Fields]                    │
│   Admin Key: [_________________]    │
│                                     │
│   [Create Account]  [Back]          │
└─────────────────────────────────────┘
```

**Input Fields:**
- Account Type (Radio)
- Name (Text Entry)
- Email (Email Entry with validation)
- Password (Password Entry)
- Confirm Password (Password Entry - must match)
- Phone (For members)
- Address (For members)
- Admin Key (For admins - security check)

**Validation:**
- Email must be unique and valid format
- Password minimum 6 characters
- All required fields must be filled
- Admin key verification

---

### Form 2: Member Dashboard

**Layout**: Sidebar Navigation + Main Content Area

```
┌──────────────────────────────────────────────────────────┐
│  📚 LIBRARY    │                                          │
│  ────────────  │                                          │
│  👋 John Doe   │    Welcome, John Doe!                   │
│                │    ─────────────────────────────────────│
│  [🏠 Home]     │    📤 Currently Borrowed: 2              │
│  [🔍 Search]   │    📚 Books in Library: 150              │
│  [📖 Browse]   │                                          │
│  [📤 My Borrow]│    ⚡ Quick Actions                      │
│  [📋 History]  │    [🔍 Search] [📖 Browse] [📤 My Books]│
│                │                                          │
│  [🚪 Logout]   │                                          │
└──────────────────────────────────────────────────────────┘
```

#### Sidebar Components:
1. **Header** - Library branding
2. **Welcome** - Member name display
3. **Navigation Buttons**:
   - 🏠 Home
   - 🔍 Search Books
   - 📖 Browse Catalog
   - 📤 My Borrowings
   - 📋 My History
4. **Logout Button** - Exit application

#### Screen 2.1: Home Screen
**Content:**
- Welcome message
- Quick stats (Books borrowed, Total books in library)
- Quick action buttons
- Latest borrowing summary

#### Screen 2.2: Search Books
**Components:**
```
Search Type: ○ Title  ○ Author  ○ Category

[_______________________Search_______________________] [Search]

Results:
┌────────────────────────────────────────────────────┐
│ Book Title              │ Author      │ Category   │
├────────────────────────────────────────────────────┤
│ The Great Gatsby        │ F.S. Fitzge │ Fiction    │
│ Available: ✅ 3 copies                             │
│ [View Details] [Reserve] [Request Issue]           │
└────────────────────────────────────────────────────┘
```

**Features:**
- Radio buttons to select search type
- Search entry field
- Search button
- Results table with sorting and filtering
- Book action buttons (View, Reserve, Request)

#### Screen 2.3: Browse Catalog
**Components:**
```
All Books in Library:

┌────────────────────────────────────────────┐
│ Book Card View:                            │
├────────────────────────────────────────────┤
│ 📖 The Great Gatsby                        │
│ Author: F.S. Fitzgerald                    │
│ Category: Fiction                          │
│ Available: ✅ 3/5                          │
│ ISBN: 978-0-7432-7356-5                   │
│ Price: Rs. 299.99                          │
│ [Reserve] [Details]                        │
└────────────────────────────────────────────┘
```

**Features:**
- Card layout for books
- Availability status
- Quick reserve button
- Details view option
- Scrollable view

#### Screen 2.4: My Borrowings
**Components:**
```
Currently Borrowed Books:

┌──────────────────────────────────────────┐
│ Book        │ Author   │ Due Date │ Days │
├──────────────────────────────────────────┤
│ Book Title  │ Author   │ 2024-05-23  │ 4  │
│ Status: On Track ✅                      │
│ [Return] [Extend]                        │
└──────────────────────────────────────────┘
```

**Features:**
- Table view of borrowed books
- Issue date and due date
- Days remaining countdown
- Status indicator (On Track/Overdue)
- Return button
- Extend due date option

#### Screen 2.5: View Fines
**Components:**
```
Pending Fines:

┌─────────────────────────────────┐
│ Fine ID │ Amount │ Reason │ Pay │
├─────────────────────────────────┤
│ FINE001 │ Rs.50  │ Overdue │ Pay │
│ FINE002 │ Rs.30  │ Damage  │ Pay │
└─────────────────────────────────┘

Total Pending: Rs. 80
[Pay All Fines]
```

**Features:**
- List of unpaid fines
- Fine amount and reason
- Payment button for each fine
- Total calculation
- Payment confirmation

#### Screen 2.6: View History
**Components:**
```
Borrowing History:

┌──────────────────────────────────┐
│ Book │ Issue Date │ Return Date  │
├──────────────────────────────────┤
│ Book1│ 2024-05-01 │ 2024-05-15   │
│ Book2│ 2024-04-15 │ 2024-04-29   │
└──────────────────────────────────┘

Total Books Borrowed: 15
Average Retention: 14 days
```

**Features:**
- Historical records of all borrowings
- Search and filter by date
- Export option
- Statistics

---

### Form 3: Admin Dashboard

**Layout**: Sidebar Navigation + Main Content Area

```
┌──────────────────────────────────────────────────────────┐
│  🎓 LIBRARY    │                                          │
│  ────────────  │   📊 Dashboard Overview                 │
│  👤 Admin Name │   ─────────────────────────────────────│
│                │                                          │
│  [🏠 Home]     │   📚 Total Books: 150                   │
│  [📚 Manage]   │   👥 Total Members: 45                  │
│  [👥 Members]  │   📤 Books Issued: 23                   │
│  [📋 Issued]   │   ✅ Available: 127                     │
│  [📊 Reports]  │                                          │
│  [👨‍💼 Admins]    │   ⚡ Quick Actions                      │
│                │   [➕ Add Book] [➕ Register] [📋 View] │
│  [🚪 Logout]   │                                          │
└──────────────────────────────────────────────────────────┘
```

#### Screen 3.1: Home/Dashboard
**Statistics Cards:**
- Total Books in Library
- Total Registered Members
- Currently Issued Books
- Available Books
- Quick access buttons

#### Screen 3.2: Manage Books
**Components:**
```
📚 Manage Books

[➕ Add New Book]

┌────────────────────────────────────────────────┐
│ ID │ Title  │ Author  │ Category │ Copies │ Act│
├────────────────────────────────────────────────┤
│ 1  │ Gatsby │ Fitzger │ Fiction  │ 3/5    │ ✏️ │
│    │                                        │ 🗑️ │
├────────────────────────────────────────────────┤
│ 2  │ ...    │ ...     │ ...      │ ...    │    │
└────────────────────────────────────────────────┘
```

**Sub-Form 3.2a: Add Book**
```
┌──────────────────────────────────┐
│ Add New Book                      │
├──────────────────────────────────┤
│ Title: [_____________________]   │
│ Author: [____________________]   │
│ Category: [__________________]   │
│ ISBN: [_____________________]   │
│ Publisher: [________________]    │
│ Total Copies: [_____________]   │
│ Price: [_____________________]   │
│ Description: [______________]   │
│                                  │
│ [Add]  [Cancel]                  │
└──────────────────────────────────┘
```

**Input Fields:**
- Title (Text, required)
- Author (Text, required)
- Category (Dropdown/Text)
- ISBN (Text, unique)
- Publisher (Text)
- Total Copies (Number, required)
- Price (Float, required)
- Description (Text Area)

**Sub-Form 3.2b: Update Book**
- Same as Add form but with pre-filled data

#### Screen 3.3: Manage Members
**Components:**
```
👥 Manage Members

[➕ Register New Member]

┌────────────────────────────────────────┐
│ ID │ Name    │ Email        │ Phone  │  │
├────────────────────────────────────────┤
│ 1  │ Ali A.  │ ali@...com  │ 03XX   │ ✏️│
│    │ Joined: 2024-05-01                │ 🗑️│
└────────────────────────────────────────┘
```

**Sub-Form 3.3a: Register Member**
```
┌──────────────────────────────────┐
│ Register New Member              │
├──────────────────────────────────┤
│ Name: [_____________________]   │
│ Email: [____________________]   │
│ Password: [_________________]   │
│ Phone: [_____________________]  │
│ Address: [__________________]   │
│ Member ID: [________________]   │
│                                  │
│ [Register] [Cancel]              │
└──────────────────────────────────┘
```

#### Screen 3.4: Manage Issued Books
**Components:**
```
📋 Issued Books

Current Borrowings:
┌────────────────────────────────────────┐
│ Member  │ Book       │ Due Date │ Days │
├────────────────────────────────────────┤
│ Ali A.  │ Gatsby     │ 2024-05-23 │ 4  │
│ Due Soon ⚠️  [Extend] [Return]         │
└────────────────────────────────────────┘

Overdue Books:
┌────────────────────────────────────────┐
│ Member  │ Book       │ Overdue │ Fine │
├────────────────────────────────────────┤
│ John D. │ Title2     │ 3 days  │ 30   │
│ [Create Fine] [Return]                 │
└────────────────────────────────────────┘
```

**Sub-Form 3.4a: Issue Book**
```
┌──────────────────────────────────┐
│ Issue Book to Member             │
├──────────────────────────────────┤
│ Member: [Select Member____]▼    │
│ Book: [Select Book_________]▼   │
│ Due Date: [Date Picker_____]    │
│ (Default: 14 days from today)    │
│                                  │
│ [Issue] [Cancel]                 │
└──────────────────────────────────┘
```

**Sub-Form 3.4b: Process Return**
```
┌──────────────────────────────────┐
│ Process Book Return              │
├──────────────────────────────────┤
│ Issued Book: [Select_____]▼     │
│ Return Date: [Auto Date]         │
│ Condition: [Good/Fair/Damaged]▼ │
│ Notes: [__________________]      │
│                                  │
│ Calculate Fine (if Overdue)      │
│ Days Overdue: 5                  │
│ Fine: Rs. 50                     │
│                                  │
│ [Create Fine] [Return] [Cancel]  │
└──────────────────────────────────┘
```

#### Screen 3.5: Manage Fines
**Components:**
```
💸 Manage Fines

All Fines:
┌────────────────────────────────────────┐
│ Fine ID │ Member │ Amount │ Status │   │
├────────────────────────────────────────┤
│ FINE001 │ Ali A. │ Rs.50  │ Unpaid │   │
│         │ Reason: Overdue by 5 days    │
│ [Mark Paid] [Delete]                   │
└────────────────────────────────────────┘
```

#### Screen 3.6: Generate Reports
**Components:**
```
📊 Reports

Select Report Type:
[Inventory] [Overdue] [Members] [Fines]

Inventory Report:
┌────────────────────────────────┐
│ Book Title  │ Total │ Available│
├────────────────────────────────┤
│ Gatsby      │ 5     │ 3        │
│ Book2       │ 3     │ 2        │
└────────────────────────────────┘

[Print] [Export to CSV] [Export to PDF]
```

**Report Types:**
1. **Inventory Report** - Stock levels
2. **Overdue Books Report** - Late returns
3. **Member Report** - Member statistics
4. **Fine Report** - Collection status

#### Screen 3.7: Manage Admins
**Components:**
```
👨‍💼 Manage Admins

[➕ Add New Admin] (First Admin Only)

┌──────────────────────────────────┐
│ ID │ Name      │ Email           │
├──────────────────────────────────┤
│ 1  │ Librarian │ admin@lib.com   │
│    │ (First Admin - Cannot Delete)│
└──────────────────────────────────┘
```

---

## File Structure

```
Library Management System/
│
├── main.py                    # Entry point - starts application
│
├── auth.py                    # Authentication module
│                              # - Login screen
│                              # - Registration forms
│                              # - User type selection
│
├── member_dashboard.py        # Member GUI module
│                              # - Member interface
│                              # - All member screens
│                              # - Book search, browse
│                              # - Fine payment
│
├── admin_dashboard.py         # Admin GUI module
│                              # - Admin interface
│                              # - Management screens
│                              # - Report generation
│                              # - Analytics
│
├── data_handler.py            # Data management module
│                              # - CRUD operations
│                              # - File I/O
│                              # - Data validation
│                              # - Business logic
│
├── data/                      # Data directory
│   ├── books.txt             # Books database (JSON)
│   ├── users.txt             # Members database (JSON)
│   ├── admins.txt            # Admins database (JSON)
│   ├── issued.txt            # Borrowing records (JSON)
│   ├── fines.txt             # Fine records (JSON)
│   └── reservations.txt      # Reservations (JSON)
│
├── __pycache__/              # Python cache (auto-generated)
│
└── README.md                 # Project documentation
```

---

## Module Descriptions

### 1. **main.py** - Application Entry Point

**Purpose**: Initialize and launch the application

**Functions:**
```python
def main():
    """Main function"""
    - Initialize DataHandler (create folders & files)
    - Display startup message
    - Launch AuthWindow (GUI)
    - Start mainloop()
```

**Execution Flow:**
1. Check/create data directory
2. Initialize all JSON files if not exist
3. Display welcome message
4. Launch authentication window
5. Keep application running until closed

---

### 2. **auth.py** - Authentication Module

**Purpose**: Handle user login and registration

**Class: AuthWindow(ctk.CTk)**

**Key Methods:**
```python
def __init__():
    - Initialize window
    - Set up GUI components
    - Display login screen by default

def clear_window():
    - Remove all widgets
    - Prepare for screen switch

def show_login_screen():
    - Display login form
    - Email, password fields
    - Admin/Member toggle
    - Login/SignUp buttons

def show_signup_screen():
    - Display registration form
    - Name, email, password fields
    - Account type selection
    - Additional fields based on type

def handle_login():
    - Validate input
    - Check credentials in DataHandler
    - Launch appropriate dashboard
    - Show error messages

def handle_signup():
    - Validate all required fields
    - Check for duplicates
    - Store in DataHandler
    - Show confirmation
    - Return to login

def switch_to_member_dashboard(user_data):
    - Destroy auth window
    - Create MemberDashboard
    - Pass user data

def switch_to_admin_dashboard(user_data):
    - Destroy auth window
    - Create AdminDashboard
    - Pass user data
```

**GUI Components:**
- Window: Dark theme, 600x500 size
- Labels: Header, subheader, field labels
- Entry: Email, password inputs
- RadioButtons: Account type selection
- Buttons: Login, SignUp, Help, Back
- ComboBox: Member/Admin dropdown

**Data Flow:**
```
User Input → Validation → DataHandler Check → Success/Error → Dashboard/Message
```

---

### 3. **member_dashboard.py** - Member Interface

**Purpose**: Provide member functionality

**Class: MemberDashboard(ctk.CTk)**

**Key Methods:**

#### Navigation & Layout:
```python
def create_layout():
    - Create sidebar with navigation
    - Create main content area
    - Setup navigation buttons

def switch_screen(screen_name):
    - Clear content
    - Load requested screen
    - Highlight active button

def clear_content():
    - Remove all widgets from content frame
```

#### Screen Methods:
```python
def show_home_screen():
    - Welcome message
    - Quick stats
    - Action buttons

def show_search_screen():
    - Search interface
    - Search type selection
    - Results display
    - Book action buttons

def show_catalog_screen():
    - All books listing
    - Card/table view
    - Availability status
    - Book details

def show_borrowings_screen():
    - Currently borrowed books
    - Due dates
    - Status indicators
    - Return/Extend options

def show_history_screen():
    - Past borrowing records
    - Return dates
    - Filter/Search options
    - Statistics

def show_fines_screen():
    - List of unpaid fines
    - Fine details
    - Payment button
    - Total calculation
```

#### Utility Methods:
```python
def logout():
    - Close dashboard
    - Return to login screen
    - Clear session data

def show_message(title, message):
    - Display information dialog
    - Success/Error messages

def refresh_data():
    - Reload data from DataHandler
    - Update UI elements
```

**GUI Components:**
- Sidebar: Navigation menu with buttons
- Content Frame: Main content area
- Tables: For displaying books, borrowings
- Scrollable Frames: For long lists
- Cards: For statistics display
- Dialogs: For confirmations and messages

---

### 4. **admin_dashboard.py** - Admin Interface

**Purpose**: Provide administrative functionality

**Class: AdminDashboard(ctk.CTk)**

**Key Methods:**

#### Navigation & Layout:
```python
def create_layout():
    - Create sidebar
    - Create content area
    - Setup admin navigation

def switch_screen(screen_name):
    - Clear and load screens
    - Update navigation

def create_stat_card(parent, title, value, color):
    - Create statistics display cards
```

#### Screen Methods:
```python
def show_home_screen():
    - Dashboard statistics
    - Total books, members
    - Issued/Available count
    - Quick action buttons

def show_books_screen():
    - List all books
    - Add/Edit/Delete options
    - Availability management

def show_add_book_dialog():
    - Form for new book entry
    - Input validation
    - Store in DataHandler

def show_edit_book_dialog(book_id):
    - Pre-filled edit form
    - Update functionality

def show_members_screen():
    - List all members
    - Member details
    - Register/Edit/Remove options

def show_register_member_dialog():
    - Member registration form
    - Duplicate checking

def show_issued_screen():
    - All currently issued books
    - Member details
    - Due date tracking
    - Return processing

def show_return_dialog(issue_id):
    - Process book return
    - Calculate fines if overdue
    - Update inventory

def show_reports_screen():
    - Report type selection
    - Report display
    - Export options

def generate_inventory_report():
    - Current stock levels
    - Availability data

def generate_overdue_report():
    - List overdue books
    - Member details
    - Days overdue

def show_admins_screen():
    - List admin users
    - Add/Remove admins (first admin only)
```

#### Fine Management:
```python
def show_fines_screen():
    - Display all fines
    - Paid/Unpaid status
    - Payment collection

def mark_fine_as_paid(fine_id):
    - Update fine status
    - Record payment date
```

---

### 5. **data_handler.py** - Data Management

**Purpose**: Centralized data access and business logic

**Class: DataHandler**

**Data File Management:**
```python
@staticmethod
def initialize():
    - Create data directory
    - Create all JSON files
    - Initialize with empty arrays

@staticmethod
def _read_file(filepath):
    - Read JSON file
    - Parse data
    - Return as list

@staticmethod
def _write_file(filepath, data):
    - Convert data to JSON
    - Write to file
    - Handle errors
```

**Admin Operations:**
```python
def add_admin(admin_data):
    - Validate data
    - Check duplicate email
    - Store in admins.txt

def get_admin(email, password):
    - Retrieve admin by credentials
    - For login verification

def get_all_admins():
    - List all admins

def delete_admin(email):
    - Remove admin account
    - Prevent first admin deletion

def is_first_admin(email):
    - Check if admin is first created
```

**Book Operations:**
```python
def add_book(book_data):
    - Create new book record
    - Check ISBN uniqueness
    - Calculate available copies
    - Generate timestamp

def get_all_books():
    - Retrieve all books

def get_book(book_id):
    - Find specific book

def update_book(book_id, updated_data):
    - Modify book details
    - Update availability

def delete_book(book_id):
    - Remove book from inventory

def search_books(query, search_by):
    - Search by title/author/category
    - Return matching books
```

**Member Operations:**
```python
def register_member(member_data):
    - Create member account
    - Validate email uniqueness
    - Generate member ID

def get_member(email, password):
    - Login verification

def get_all_members():
    - List all members

def get_member_by_id(member_id):
    - Find specific member

def update_member(member_id, updated_data):
    - Update member info

def delete_member(member_id):
    - Remove member account
```

**Borrowing Operations:**
```python
def issue_book(book_id, member_id, due_date):
    - Record book issuance
    - Decrease available copies
    - Set due date

def return_book(issue_id):
    - Record return
    - Increase available copies
    - Set return date

def get_member_issued_books(member_id):
    - Get current borrowings
    - Exclude returned books

def get_member_history(member_id):
    - Complete borrowing history
    - Include returned books

def get_all_issued_books():
    - All current borrowings
    - For admin view

def get_overdue_books():
    - Books past due date
    - Calculate overdue days
```

**Fine Operations:**
```python
def create_fine(member_id, issue_id, amount, reason):
    - Generate fine record
    - Set unpaid status

def get_member_fines(member_id):
    - All fines for member
    - Paid and unpaid

def get_pending_fines(member_id):
    - Only unpaid fines

def pay_fine(fine_id):
    - Mark as paid
    - Record payment date

def get_all_fines():
    - All fine records (admin)
```

**Reservation Operations:**
```python
def reserve_book(book_id, member_id):
    - Create reservation
    - Check book availability
    - Prevent duplicates

def get_member_reservations(member_id):
    - All reservations by member

def get_book_reservations(book_id):
    - All reservations for book

def cancel_reservation(reservation_id):
    - Remove reservation
```

**Analytics:**
```python
def get_dashboard_stats():
    - Total books
    - Total members
    - Books issued
    - Available books
```

---

## Data Flow

### Flow 1: Member Login

```
Start
  ↓
User enters email/password
  ↓
Click "Login" button
  ↓
auth.py validates input
  ↓
DataHandler.get_member() checks credentials
  ↓
If found:
  → Create MemberDashboard
  → Pass user data
  → Close auth window
  ↓
If not found:
  → Show error message
  → Clear fields
  → Stay on login screen
```

### Flow 2: Search and Reserve Book

```
Start (Member Dashboard)
  ↓
Navigate to "Search Books"
  ↓
Select search type (Title/Author/Category)
  ↓
Enter search query
  ↓
Click "Search"
  ↓
DataHandler.search_books() finds matches
  ↓
Display results in table
  ↓
Member selects book
  ↓
Click "Reserve"
  ↓
DataHandler.reserve_book() processes
  ↓
If successful:
  → Show confirmation
  → Refresh reservations list
  ↓
If failed:
  → Show error reason
  → Allow retry
```

### Flow 3: Issue and Return Book

```
Start (Admin Dashboard)
  ↓
Navigate to "Issued Books"
  ↓
Click "Issue Book"
  ↓
Select member and book
  ↓
Set due date (default +14 days)
  ↓
Click "Issue"
  ↓
DataHandler.issue_book() processes:
  → Check availability
  → Create issue record
  → Decrease available copies
  → Record timestamp
  ↓
Show confirmation
  ↓
[Later] Member returns book
  ↓
Admin clicks "Return"
  ↓
System calculates if overdue
  ↓
If overdue:
  → Create fine record
  → Calculate amount
  ↓
DataHandler.return_book() processes:
  → Mark as returned
  → Increase available copies
  → Record return date
  ↓
Show summary
```

### Flow 4: Fine Payment

```
Start (Member Dashboard)
  ↓
Navigate to "View Fines"
  ↓
Display all pending fines
  ↓
Click "Pay" on specific fine
  ↓
Show payment confirmation dialog
  ↓
Click "Confirm Payment"
  ↓
DataHandler.pay_fine() processes:
  → Mark fine as paid
  → Record payment date
  → Update fine record
  ↓
Show success message
  ↓
Refresh fines list
  ↓
Display updated balance
```

### Flow 5: Generate Report

```
Start (Admin Dashboard)
  ↓
Navigate to "Reports"
  ↓
Select report type
  ↓
Click "Generate"
  ↓
DataHandler methods retrieve data:
  → inventory: get_all_books()
  → overdue: get_overdue_books()
  → members: get_all_members()
  → fines: get_all_fines()
  ↓
Format data for display
  ↓
Show report in table
  ↓
Provide export options:
  → Print
  → Export to CSV
  → Export to PDF (if available)
  ↓
User downloads/prints
```

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Windows/Linux/macOS system

### Step 1: Install Python
Download from [python.org](https://www.python.org)

### Step 2: Install Required Packages
```bash
pip install customtkinter
pip install Pillow
pip install -r requirements.txt  # If requirements file exists
```

Or individual installation:
```bash
pip install customtkinter>=5.0
pip install Pillow>=9.0
```

### Step 3: Navigate to Project Directory
```bash
cd "path\to\Library management system"
```

### Step 4: Run the Application
```bash
python main.py
```

Or directly:
```bash
python.exe main.py
```

### Step 5: First Time Setup
- Application auto-creates `data/` folder
- All JSON files are initialized
- Create first admin account
- Register members
- Add books to inventory

---

## User Workflows

### Member Workflow

#### Registration & Setup
```
1. Launch Application
2. Select "Member" account type
3. Click "Sign Up"
4. Fill registration form:
   - Name
   - Email
   - Password
   - Phone
   - Address
5. Click "Create Account"
6. Return to login
7. Enter email and password
8. Click "Login"
```

#### Using Library Services
```
1. Dashboard loads with welcome screen
2. Options available:
   a) Search Books:
      - Select search type
      - Enter search term
      - Browse results
      - View details
      - Reserve if unavailable
   
   b) Browse Catalog:
      - View all books
      - Check availability
      - Read descriptions
      - See pricing
   
   c) My Borrowings:
      - View current borrowed books
      - Check due dates
      - See status
   
   d) View History:
      - Past borrowing records
      - Return dates
      - Statistics
   
   e) View Fines:
      - Pending fines list
      - Fine amounts and reasons
      - Pay fines online
   
   f) Logout:
      - Close session
      - Return to login
```

### Admin Workflow

#### Initial Setup
```
1. Launch Application
2. Select "Admin" account type
3. Click "Sign Up"
4. Enter first admin credentials
5. Enter admin key (security check)
6. Click "Create Account"
7. Login with admin account
```

#### Daily Operations
```
1. Admin Dashboard opens
2. Review statistics:
   - Total books and members
   - Current borrowed books
   - Available inventory
   - Quick links

3. Book Management:
   - Add new books
   - Update existing books
   - Delete outdated books
   - Monitor stock levels

4. Member Management:
   - Register new members
   - Update member info
   - View member list
   - Manage member status

5. Book Issuance:
   - Issue books to members
   - Set due dates
   - Track borrowings
   - Monitor due dates

6. Returns & Fines:
   - Process book returns
   - Calculate fines for overdue
   - Manage fine collection
   - Track payments

7. Reports:
   - Inventory reports
   - Overdue books list
   - Member statistics
   - Fine collection status

8. Admin Management:
   - Add new admins
   - Remove admin accounts
   - View admin list

9. Logout:
   - End session
```

---

## API Methods (DataHandler Reference)

### Admin Methods

| Method | Parameters | Returns | Purpose |
|--------|-----------|---------|---------|
| `add_admin()` | admin_data | (bool, message) | Create admin |
| `get_admin()` | email, password | Dict/None | Login check |
| `get_all_admins()` | None | List | List admins |
| `delete_admin()` | email | (bool, message) | Remove admin |
| `is_first_admin()` | email | bool | Check if first |

### Book Methods

| Method | Parameters | Returns | Purpose |
|--------|-----------|---------|---------|
| `add_book()` | book_data | (bool, message) | Add book |
| `get_all_books()` | None | List | Get all books |
| `get_book()` | book_id | Dict/None | Get by ID |
| `update_book()` | book_id, data | bool | Update book |
| `delete_book()` | book_id | bool | Remove book |
| `search_books()` | query, search_by | List | Search |

### Member Methods

| Method | Parameters | Returns | Purpose |
|--------|-----------|---------|---------|
| `register_member()` | member_data | (bool, message) | Register |
| `get_member()` | email, password | Dict/None | Login |
| `get_all_members()` | None | List | All members |
| `get_member_by_id()` | member_id | Dict/None | Get by ID |
| `update_member()` | member_id, data | bool | Update |
| `delete_member()` | member_id | bool | Remove |

### Borrowing Methods

| Method | Parameters | Returns | Purpose |
|--------|-----------|---------|---------|
| `issue_book()` | book_id, member_id, due_date | bool | Issue |
| `return_book()` | issue_id | bool | Return |
| `get_member_issued_books()` | member_id | List | Current |
| `get_member_history()` | member_id | List | History |
| `get_all_issued_books()` | None | List | All issued |
| `get_overdue_books()` | None | List | Overdue |

### Fine Methods

| Method | Parameters | Returns | Purpose |
|--------|-----------|---------|---------|
| `create_fine()` | member_id, issue_id, amount, reason | bool | Create |
| `get_member_fines()` | member_id | List | Get all |
| `get_pending_fines()` | member_id | List | Unpaid |
| `pay_fine()` | fine_id | bool | Mark paid |
| `get_all_fines()` | None | List | All fines |

### Reservation Methods

| Method | Parameters | Returns | Purpose |
|--------|-----------|---------|---------|
| `reserve_book()` | book_id, member_id | (bool, message) | Reserve |
| `get_member_reservations()` | member_id | List | Get all |
| `get_book_reservations()` | book_id | List | By book |

### Analytics Methods

| Method | Parameters | Returns | Purpose |
|--------|-----------|---------|---------|
| `get_dashboard_stats()` | None | Dict | Statistics |

---

## Conclusion

This Library Management System is a complete, production-ready solution for managing library operations. It provides:

✅ **Complete Feature Set**: All essential library operations
✅ **User-Friendly Interface**: Modern GUI with dark theme
✅ **Data Persistence**: JSON-based reliable storage
✅ **Role-Based Access**: Separate interfaces for members and admins
✅ **Scalability**: Easy to add new features
✅ **Security**: Password-protected accounts
✅ **Reporting**: Comprehensive analytics and reports

The system is designed with clean architecture principles, making it easy to maintain, extend, and debug.

---

**Document Version**: 1.0  
**Last Updated**: May 9, 2024  
**Author**: Development Team  
**Status**: Complete & Ready for Use
