"""
Data Handler Module - File Management and CRUD Operations
Handle all data files for read/write operations (JSON format)
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class DataHandler:
    """Handle all data files"""
    
    DATA_DIR = "data"
    BOOKS_FILE = os.path.join(DATA_DIR, "books.txt")
    USERS_FILE = os.path.join(DATA_DIR, "users.txt")
    ADMINS_FILE = os.path.join(DATA_DIR, "admins.txt")
    ISSUED_FILE = os.path.join(DATA_DIR, "issued.txt")
    FINES_FILE = os.path.join(DATA_DIR, "fines.txt")
    RESERVATIONS_FILE = os.path.join(DATA_DIR, "reservations.txt")
    
    @staticmethod
    def initialize():
        """Initialize - create folders and files if they don't exist"""
        if not os.path.exists(DataHandler.DATA_DIR):
            os.makedirs(DataHandler.DATA_DIR)
        
        # If files don't exist, create them (with empty arrays)
        if not os.path.exists(DataHandler.BOOKS_FILE):
            DataHandler._write_file(DataHandler.BOOKS_FILE, [])
        
        if not os.path.exists(DataHandler.USERS_FILE):
            DataHandler._write_file(DataHandler.USERS_FILE, [])
        
        if not os.path.exists(DataHandler.ADMINS_FILE):
            DataHandler._write_file(DataHandler.ADMINS_FILE, [])
        
        if not os.path.exists(DataHandler.ISSUED_FILE):
            DataHandler._write_file(DataHandler.ISSUED_FILE, [])
        
        if not os.path.exists(DataHandler.FINES_FILE):
            DataHandler._write_file(DataHandler.FINES_FILE, [])
        
        if not os.path.exists(DataHandler.RESERVATIONS_FILE):
            DataHandler._write_file(DataHandler.RESERVATIONS_FILE, [])
    
    @staticmethod
    def _write_file(filepath: str, data: List) -> None:
        """Write data to file in JSON format"""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error writing file {filepath}: {e}")
    
    @staticmethod
    def _read_file(filepath: str) -> List:
        """Read JSON data from file"""
        try:
            if not os.path.exists(filepath):
                return []
            
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except Exception as e:
            print(f"Error reading file {filepath}: {e}")
            return []
    
    # ======================== ADMIN OPERATIONS ========================
    
    @staticmethod
    def add_admin(admin_data: Dict) -> tuple:
        """Add new admin - returns (success: bool, message: str)"""
        try:
            admins = DataHandler._read_file(DataHandler.ADMINS_FILE)
            
            # Check duplicate email
            if any(admin['email'] == admin_data['email'] for admin in admins):
                return False, "This email is already registered as admin."
            
            admin_data['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            admins.append(admin_data)
            DataHandler._write_file(DataHandler.ADMINS_FILE, admins)
            return True, "Admin account created successfully!"
        except Exception as e:
            print(f"Error adding admin: {e}")
            return False, f"Error: {str(e)}"
    
    @staticmethod
    def get_admin(email: str, password: str) -> Optional[Dict]:
        """Find admin by email and password (for login)"""
        try:
            admins = DataHandler._read_file(DataHandler.ADMINS_FILE)
            for admin in admins:
                if admin['email'] == email and admin['password'] == password:
                    return admin
            return None
        except Exception as e:
            print(f"Error getting admin: {e}")
            return None
    
    @staticmethod
    def admin_exists(email: str) -> bool:
        """Check if admin already exists"""
        admins = DataHandler._read_file(DataHandler.ADMINS_FILE)
        return any(admin['email'] == email for admin in admins)
    
    @staticmethod
    def verify_admin_password(password: str) -> bool:
        """Verify if password matches any existing admin's password"""
        try:
            admins = DataHandler._read_file(DataHandler.ADMINS_FILE)
            # If no admins exist yet, allow signup
            if not admins:
                return True
            # Check if password matches any admin
            return any(admin['password'] == password for admin in admins)
        except Exception as e:
            print(f"Error verifying admin password: {e}")
            return False
    
    @staticmethod
    def get_all_admins() -> List[Dict]:
        """Get all admins"""
        return DataHandler._read_file(DataHandler.ADMINS_FILE)
    
    @staticmethod
    def get_admin_by_email(email: str) -> Optional[Dict]:
        """Get admin by email"""
        admins = DataHandler.get_all_admins()
        for admin in admins:
            if admin['email'] == email:
                return admin
        return None
    
    @staticmethod
    def is_first_admin(email: str) -> bool:
        """Check if admin is the first admin (created first)"""
        admins = DataHandler.get_all_admins()
        if not admins:
            return False
        # First admin is the one who appears first in the list (created first)
        return admins[0]['email'] == email
    
    @staticmethod
    def delete_admin(email: str) -> tuple:
        """Delete admin - returns (success: bool, message: str)"""
        try:
            admins = DataHandler._read_file(DataHandler.ADMINS_FILE)
            
            # Check if admin exists
            admin_to_delete = None
            for admin in admins:
                if admin['email'] == email:
                    admin_to_delete = admin
                    break
            
            if not admin_to_delete:
                return False, "Admin not found!"
            
            # Check if trying to delete the first admin
            if admins[0]['email'] == email:
                return False, "Cannot delete the first admin!"
            
            # Remove admin
            admins = [admin for admin in admins if admin['email'] != email]
            DataHandler._write_file(DataHandler.ADMINS_FILE, admins)
            return True, "Admin deleted successfully!"
        except Exception as e:
            print(f"Error deleting admin: {e}")
            return False, f"Error: {str(e)}"
    
    # ======================== BOOK OPERATIONS ========================
    
    @staticmethod
    def add_book(book_data: Dict) -> tuple:
        """Add new book - returns (success: bool, message: str)"""
        try:
            books = DataHandler._read_file(DataHandler.BOOKS_FILE)
            
            # Check duplicate ISBN
            if any(book['isbn'] == book_data['isbn'] for book in books):
                return False, "This ISBN already exists in the library."
            
            book_data['id'] = len(books) + 1
            book_data['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            book_data['available_copies'] = book_data.get('total_copies', 1)
            
            books.append(book_data)
            DataHandler._write_file(DataHandler.BOOKS_FILE, books)
            return True, "Book added successfully!"
        except Exception as e:
            print(f"Error adding book: {e}")
            return False, f"Error: {str(e)}"
    
    @staticmethod
    def get_all_books() -> List[Dict]:
        """List of all books"""
        return DataHandler._read_file(DataHandler.BOOKS_FILE)
    
    @staticmethod
    def get_book(book_id: int) -> Optional[Dict]:
        """Find book by ID"""
        books = DataHandler.get_all_books()
        for book in books:
            if book['id'] == book_id:
                return book
        return None
    
    @staticmethod
    def update_book(book_id: int, updated_data: Dict) -> bool:
        """Update book details"""
        try:
            books = DataHandler._read_file(DataHandler.BOOKS_FILE)
            
            for i, book in enumerate(books):
                if book['id'] == book_id:
                    books[i].update(updated_data)
                    DataHandler._write_file(DataHandler.BOOKS_FILE, books)
                    return True
            return False
        except Exception as e:
            print(f"Error updating book: {e}")
            return False
    
    @staticmethod
    def delete_book(book_id: int) -> bool:
        """Delete book"""
        try:
            books = DataHandler._read_file(DataHandler.BOOKS_FILE)
            books = [book for book in books if book['id'] != book_id]
            DataHandler._write_file(DataHandler.BOOKS_FILE, books)
            return True
        except Exception as e:
            print(f"Error deleting book: {e}")
            return False
    
    @staticmethod
    def search_books(query: str, search_by: str = "title") -> List[Dict]:
        """Search books (title, author, isbn, category)"""
        books = DataHandler.get_all_books()
        query = query.lower()
        
        results = []
        for book in books:
            if search_by in book:
                if query in str(book[search_by]).lower():
                    results.append(book)
        
        return results
    
    # ======================== USER/MEMBER OPERATIONS ========================
    
    @staticmethod
    def register_member(member_data: Dict) -> tuple:
        """Register new member - returns (success: bool, message: str)"""
        try:
            users = DataHandler._read_file(DataHandler.USERS_FILE)
            
            # Check duplicate email
            if any(user['email'] == member_data['email'] for user in users):
                return False, "This email is already registered. Please use a different email."
            # Check duplicate member ID
            if any(user.get('member_id') == member_data.get('member_id') for user in users):
                return False, "This Member ID already exists. Please use a different ID."
            
            member_data['id'] = len(users) + 1
            member_data['registered_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            users.append(member_data)
            DataHandler._write_file(DataHandler.USERS_FILE, users)
            return True, "Member registered successfully!"
        except Exception as e:
            print(f"Error registering member: {e}")
            return False, f"Error: {str(e)}"
    
    @staticmethod
    def get_member(email: str, password: str) -> Optional[Dict]:
        """Find member by email and password (for login)"""
        try:
            users = DataHandler._read_file(DataHandler.USERS_FILE)
            for user in users:
                if user['email'] == email and user['password'] == password:
                    return user
            return None
        except Exception as e:
            print(f"Error getting member: {e}")
            return None
    
    @staticmethod
    def member_exists(email: str) -> bool:
        """Check if member already exists"""
        users = DataHandler._read_file(DataHandler.USERS_FILE)
        return any(user['email'] == email for user in users)
    
    @staticmethod
    def get_all_members() -> List[Dict]:
        """List of all members"""
        return DataHandler._read_file(DataHandler.USERS_FILE)
    
    @staticmethod
    def get_member_by_id(member_id: int) -> Optional[Dict]:
        """Find member by ID"""
        users = DataHandler.get_all_members()
        for user in users:
            if user['id'] == member_id:
                return user
        return None
    
    @staticmethod
    def update_member(member_id: int, updated_data: Dict) -> bool:
        """Update member details"""
        try:
            users = DataHandler._read_file(DataHandler.USERS_FILE)
            
            for i, user in enumerate(users):
                if user['id'] == member_id:
                    users[i].update(updated_data)
                    DataHandler._write_file(DataHandler.USERS_FILE, users)
                    return True
            return False
        except Exception as e:
            print(f"Error updating member: {e}")
            return False
    
    @staticmethod
    def delete_member(member_id: int) -> bool:
        """Delete member"""
        try:
            users = DataHandler._read_file(DataHandler.USERS_FILE)
            users = [user for user in users if user['id'] != member_id]
            DataHandler._write_file(DataHandler.USERS_FILE, users)
            return True
        except Exception as e:
            print(f"Error deleting member: {e}")
            return False
    
    # ======================== ISSUE/RETURN OPERATIONS ========================
    
    @staticmethod
    def issue_book(book_id: int, member_id: int, due_date: str) -> bool:
        """Issue book to member"""
        try:
            # Check if book is available
            book = DataHandler.get_book(book_id)
            if not book or book['available_copies'] <= 0:
                return False
            
            issued = DataHandler._read_file(DataHandler.ISSUED_FILE)
            
            issue_record = {
                'id': len(issued) + 1,
                'book_id': book_id,
                'member_id': member_id,
                'issue_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'due_date': due_date,
                'return_date': None,
                'status': 'issued'  # issued, returned
            }
            
            issued.append(issue_record)
            DataHandler._write_file(DataHandler.ISSUED_FILE, issued)
            
            # Update book available copies
            book['available_copies'] -= 1
            DataHandler.update_book(book_id, book)
            
            return True
        except Exception as e:
            print(f"Error issuing book: {e}")
            return False
    
    @staticmethod
    def return_book(issue_id: int) -> bool:
        """Return book"""
        try:
            issued = DataHandler._read_file(DataHandler.ISSUED_FILE)
            
            for i, record in enumerate(issued):
                if record['id'] == issue_id:
                    # Mark as returned
                    issued[i]['status'] = 'returned'
                    issued[i]['return_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    DataHandler._write_file(DataHandler.ISSUED_FILE, issued)
                    
                    # Update book available copies
                    book = DataHandler.get_book(record['book_id'])
                    if book:
                        book['available_copies'] += 1
                        DataHandler.update_book(record['book_id'], book)
                    
                    return True
            return False
        except Exception as e:
            print(f"Error returning book: {e}")
            return False
    
    @staticmethod
    def get_member_issued_books(member_id: int) -> List[Dict]:
        """All issued books by member (not yet returned)"""
        issued = DataHandler._read_file(DataHandler.ISSUED_FILE)
        member_books = []
        
        for record in issued:
            if record['member_id'] == member_id and record['status'] == 'issued':
                book = DataHandler.get_book(record['book_id'])
                if book:
                    record['book_title'] = book['title']
                    record['author'] = book['author']
                    member_books.append(record)
        
        return member_books
    
    @staticmethod
    def get_member_history(member_id: int) -> List[Dict]:
        """Complete borrowing history of member"""
        issued = DataHandler._read_file(DataHandler.ISSUED_FILE)
        history = []
        
        for record in issued:
            if record['member_id'] == member_id:
                book = DataHandler.get_book(record['book_id'])
                if book:
                    record['book_title'] = book['title']
                    record['author'] = book['author']
                    history.append(record)
        
        return history
    
    @staticmethod
    def get_all_issued_books() -> List[Dict]:
        """All issued books (for admin)"""
        issued = DataHandler._read_file(DataHandler.ISSUED_FILE)
        result = []
        
        for record in issued:
            if record['status'] == 'issued':
                book = DataHandler.get_book(record['book_id'])
                member = DataHandler.get_member_by_id(record['member_id'])
                if book and member:
                    record['book_title'] = book['title']
                    record['member_name'] = member['name']
                    result.append(record)
        
        return result
    
    # ======================== ANALYTICS/STATS ========================
    
    @staticmethod
    def get_dashboard_stats() -> Dict:
        """Stats for admin dashboard"""
        books = DataHandler.get_all_books()
        members = DataHandler.get_all_members()
        issued = DataHandler._read_file(DataHandler.ISSUED_FILE)
        
        total_issued = sum(1 for record in issued if record['status'] == 'issued')
        
        return {
            'total_books': len(books),
            'total_members': len(members),
            'total_issued': total_issued,
            'total_available': sum(book.get('available_copies', 0) for book in books)
        }
    
    # ======================== FINE OPERATIONS ========================
    
    @staticmethod
    def create_fine(member_id: int, issue_id: int, amount: float, reason: str) -> bool:
        """Create a fine for member"""
        try:
            fines = DataHandler._read_file(DataHandler.FINES_FILE)
            
            fine_record = {
                'id': len(fines) + 1,
                'member_id': member_id,
                'issue_id': issue_id,
                'amount': amount,
                'reason': reason,
                'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'status': 'unpaid',  # unpaid, paid
                'paid_at': None
            }
            
            fines.append(fine_record)
            DataHandler._write_file(DataHandler.FINES_FILE, fines)
            return True
        except Exception as e:
            print(f"Error creating fine: {e}")
            return False
    
    @staticmethod
    def get_member_fines(member_id: int) -> List[Dict]:
        """Get all fines for a member"""
        fines = DataHandler._read_file(DataHandler.FINES_FILE)
        member_fines = []
        
        for fine in fines:
            if fine['member_id'] == member_id:
                member_fines.append(fine)
        
        return member_fines
    
    @staticmethod
    def get_pending_fines(member_id: int) -> List[Dict]:
        """Get unpaid fines for a member"""
        fines = DataHandler._read_file(DataHandler.FINES_FILE)
        pending = []
        
        for fine in fines:
            if fine['member_id'] == member_id and fine['status'] == 'unpaid':
                pending.append(fine)
        
        return pending
    
    @staticmethod
    def get_all_fines() -> List[Dict]:
        """Get all fines (for admin)"""
        return DataHandler._read_file(DataHandler.FINES_FILE)
    
    @staticmethod
    def get_overdue_books() -> List[Dict]:
        """Get all overdue issued books"""
        issued = DataHandler._read_file(DataHandler.ISSUED_FILE)
        overdue = []
        
        for record in issued:
            if record['status'] == 'issued':
                due_date = datetime.strptime(record['due_date'], "%Y-%m-%d")
                if due_date < datetime.now():
                    book = DataHandler.get_book(record['book_id'])
                    member = DataHandler.get_member_by_id(record['member_id'])
                    if book and member:
                        record['book_title'] = book['title']
                        record['member_name'] = member['name']
                        overdue.append(record)
        
        return overdue
    
    @staticmethod
    def pay_fine(fine_id: int) -> bool:
        """Mark fine as paid"""
        try:
            fines = DataHandler._read_file(DataHandler.FINES_FILE)
            
            for i, fine in enumerate(fines):
                if fine['id'] == fine_id:
                    fines[i]['status'] = 'paid'
                    fines[i]['paid_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    DataHandler._write_file(DataHandler.FINES_FILE, fines)
                    return True
            return False
        except Exception as e:
            print(f"Error paying fine: {e}")
            return False
    
    # ======================== RESERVATION OPERATIONS ========================
    
    @staticmethod
    def reserve_book(book_id: int, member_id: int) -> tuple:
        """Reserve a book - returns (success: bool, message: str)"""
        try:
            book = DataHandler.get_book(book_id)
            if not book:
                return False, "Book not found!"
            
            # Check if book is available
            if book['available_copies'] > 0:
                return False, "Book is currently available. You can request it from the librarian."
            
            reservations = DataHandler._read_file(DataHandler.RESERVATIONS_FILE)
            
            # Check if already reserved by this member
            if any(r['book_id'] == book_id and r['member_id'] == member_id and r['status'] == 'pending' 
                   for r in reservations):
                return False, "You have already reserved this book!"
            
            reservation = {
                'id': len(reservations) + 1,
                'book_id': book_id,
                'member_id': member_id,
                'reserved_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'status': 'pending'  # pending, cancelled, issued
            }
            
            reservations.append(reservation)
            DataHandler._write_file(DataHandler.RESERVATIONS_FILE, reservations)
            return True, "Book reserved successfully! You will be notified when it's available."
        except Exception as e:
            print(f"Error reserving book: {e}")
            return False, f"Error: {str(e)}"
    
    @staticmethod
    def get_member_reservations(member_id: int) -> List[Dict]:
        """Get all reservations by a member"""
        reservations = DataHandler._read_file(DataHandler.RESERVATIONS_FILE)
        member_reservations = []
        
        for res in reservations:
            if res['member_id'] == member_id and res['status'] == 'pending':
                book = DataHandler.get_book(res['book_id'])
                if book:
                    res['book_title'] = book['title']
                    res['author'] = book['author']
                    member_reservations.append(res)
        
        return member_reservations
    
    @staticmethod
    def cancel_reservation(reservation_id: int) -> bool:
        """Cancel a book reservation"""
        try:
            reservations = DataHandler._read_file(DataHandler.RESERVATIONS_FILE)
            
            for i, res in enumerate(reservations):
                if res['id'] == reservation_id:
                    reservations[i]['status'] = 'cancelled'
                    DataHandler._write_file(DataHandler.RESERVATIONS_FILE, reservations)
                    return True
            return False
        except Exception as e:
            print(f"Error cancelling reservation: {e}")
            return False
    
    @staticmethod
    def get_book_reservations(book_id: int) -> List[Dict]:
        """Get all pending reservations for a book"""
        reservations = DataHandler._read_file(DataHandler.RESERVATIONS_FILE)
        book_reservations = []
        
        for res in reservations:
            if res['book_id'] == book_id and res['status'] == 'pending':
                member = DataHandler.get_member_by_id(res['member_id'])
                if member:
                    res['member_name'] = member['name']
                    book_reservations.append(res)
        
        return book_reservations
