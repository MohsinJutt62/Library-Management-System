"""
Admin Dashboard - Library Manager Control Panel
"""

import customtkinter as ctk
from data_handler import DataHandler
from datetime import datetime, timedelta
import tkinter as tk


class AdminDashboard(ctk.CTk):
    """Admin Dashboard - Control Center"""
    
    def __init__(self, admin_user: dict):
        super().__init__()
        
        self.admin_user = admin_user
        
        self.title("Library Management - Admin Dashboard")
        self.geometry("1200x700")
        
        # Color scheme
        self.bg_color = "#0a0a0a"
        self.fg_color = "#ffffff"
        self.primary_color = "#007bff"
        self.success_color = "#28a745"
        self.danger_color = "#dc3545"
        self.dark_gray = "#1a1a1a"
        
        self.configure(fg_color=self.bg_color)
        
        # Current screen
        self.current_screen = "home"
        
        # Create layout
        self.create_layout()
        self.show_home_screen()
    
    def create_layout(self):
        """Main layout - Sidebar + Content Area"""
        
        # ==================== SIDEBAR ====================
        self.sidebar = ctk.CTkFrame(self, fg_color=self.dark_gray, width=250)
        self.sidebar.pack(side="left", fill="y", padx=0)
        self.sidebar.pack_propagate(False)
        
        # Header
        header = ctk.CTkLabel(
            self.sidebar,
            text="🎓 LIBRARY",
            font=("Helvetica", 22, "bold"),
            text_color=self.primary_color
        )
        header.pack(pady=25)
        
        admin_name = ctk.CTkLabel(
            self.sidebar,
            text=f"👤 {self.admin_user['name']}",
            font=("Helvetica", 14),
            text_color="#cccccc"
        )
        admin_name.pack(pady=(0, 20))
        
        # Navigation buttons
        self.nav_buttons = {}
        
        nav_items = [
            ("🏠 Home", "home"),
            ("📚 Manage Books", "books"),
            ("👥 Manage Members", "members"),
            ("📋 Issued Books", "issued"),
            ("📊 Reports", "reports"),
        ]
        
        # Add Manage Admins option only for first admin
        if DataHandler.is_first_admin(self.admin_user['email']):
            nav_items.append(("👨‍💼 Manage Admins", "admins"))
        
        for label, screen in nav_items:
            btn = ctk.CTkButton(
                self.sidebar,
                text=label,
                font=("Helvetica", 13),
                height=50,
                fg_color="transparent",
                text_color=self.fg_color,
                hover_color=self.primary_color,
                command=lambda s=screen: self.switch_screen(s)
            )
            btn.pack(pady=6, padx=10, fill="x")
            self.nav_buttons[screen] = btn
        
        # Logout button
        ctk.CTkButton(
            self.sidebar,
            text="🚪 Logout",
            font=("Helvetica", 13, "bold"),
            height=50,
            fg_color=self.danger_color,
            hover_color="#c82333",
            command=self.logout
        ).pack(pady=(50, 10), padx=10, fill="x", side="bottom")
        
        # ==================== CONTENT AREA ====================
        self.content = ctk.CTkFrame(self, fg_color=self.bg_color)
        self.content.pack(side="right", fill="both", expand=True, padx=20, pady=20)
        
        # Content container (Show different screens here)
        self.content_frame = ctk.CTkFrame(self.content, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True)
    
    def clear_content(self):
        """Clear content area"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def switch_screen(self, screen_name: str):
        """Switch between different screens"""
        # Reset previous button
        if hasattr(self, 'current_screen'):
            if self.current_screen in self.nav_buttons:
                self.nav_buttons[self.current_screen].configure(fg_color="transparent")
        
        # Highlight new button
        self.nav_buttons[screen_name].configure(fg_color=self.primary_color)
        self.current_screen = screen_name
        
        self.clear_content()
        
        if screen_name == "home":
            self.show_home_screen()
        elif screen_name == "books":
            self.show_books_screen()
        elif screen_name == "members":
            self.show_members_screen()
        elif screen_name == "issued":
            self.show_issued_screen()
        elif screen_name == "reports":
            self.show_reports_screen()
        elif screen_name == "admins":
            self.show_admins_screen()
    
    # ======================== HOME SCREEN ========================
    
    def show_home_screen(self):
        """Dashboard Home - Summary stats"""
        self.nav_buttons["home"].configure(fg_color=self.primary_color)
        
        # Title
        title = ctk.CTkLabel(
            self.content_frame,
            text="📊 Dashboard Overview",
            font=("Helvetica", 32, "bold"),
            text_color=self.primary_color
        )
        title.pack(pady=(0, 35))
        
        # Get stats
        stats = DataHandler.get_dashboard_stats()
        
        # Stats Cards
        cards_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        cards_frame.pack(fill="x", pady=20)
        
        # Card 1: Total Books
        self.create_stat_card(
            cards_frame,
            "📚 Total Books",
            str(stats['total_books']),
            self.primary_color
        )
        
        # Card 2: Total Members
        self.create_stat_card(
            cards_frame,
            "👥 Total Members",
            str(stats['total_members']),
            "#28a745"
        )
        
        # Card 3: Books Issued
        self.create_stat_card(
            cards_frame,
            "📤 Books Issued",
            str(stats['total_issued']),
            "#ffc107"
        )
        
        # Card 4: Available Books
        self.create_stat_card(
            cards_frame,
            "✅ Available",
            str(stats['total_available']),
            "#17a2b8"
        )
        
        # Quick Actions
        quick_frame = ctk.CTkFrame(self.content_frame, fg_color=self.dark_gray, corner_radius=10)
        quick_frame.pack(fill="x", pady=20)
        
        quick_title = ctk.CTkLabel(
            quick_frame,
            text="⚡ Quick Actions",
            font=("Helvetica", 16, "bold"),
            text_color=self.fg_color
        )
        quick_title.pack(pady=(15, 10), padx=15, anchor="w")
        
        buttons_frame = ctk.CTkFrame(quick_frame, fg_color="transparent")
        buttons_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        ctk.CTkButton(
            buttons_frame,
            text="➕ Add New Book",
            font=("Helvetica", 11, "bold"),
            fg_color=self.success_color,
            command=lambda: self.switch_screen("books")
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            buttons_frame,
            text="➕ Register Member",
            font=("Helvetica", 11, "bold"),
            fg_color=self.success_color,
            command=lambda: self.switch_screen("members")
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            buttons_frame,
            text="📋 View Issued Books",
            font=("Helvetica", 11, "bold"),
            fg_color=self.primary_color,
            command=lambda: self.switch_screen("issued")
        ).pack(side="left", padx=5)
    
    def create_stat_card(self, parent, title: str, value: str, color: str):
        """Create stat card"""
        card = ctk.CTkFrame(parent, fg_color=self.dark_gray, corner_radius=10)
        card.pack(side="left", fill="x", expand=True, padx=10)
        
        card_title = ctk.CTkLabel(
            card,
            text=title,
            font=("Helvetica", 14),
            text_color="#cccccc"
        )
        card_title.pack(pady=(18, 8), padx=15)
        
        card_value = ctk.CTkLabel(
            card,
            text=value,
            font=("Helvetica", 40, "bold"),
            text_color=color
        )
        card_value.pack(pady=(0, 18), padx=15)
    
    # ======================== BOOKS SCREEN ========================
    
    def show_books_screen(self):
        """Manage Books - Add/Edit/Delete"""
        self.nav_buttons["books"].configure(fg_color=self.primary_color)
        
        # Title
        title = ctk.CTkLabel(
            self.content_frame,
            text="📚 Manage Books",
            font=("Helvetica", 20, "bold"),
            text_color=self.primary_color
        )
        title.pack(pady=(0, 20))
        
        # Button frame
        btn_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        btn_frame.pack(fill="x", pady=10)
        
        ctk.CTkButton(
            btn_frame,
            text="➕ Add New Book",
            font=("Helvetica", 12, "bold"),
            fg_color=self.success_color,
            command=self.show_add_book_dialog
        ).pack(side="left", padx=5)
        
        # Books list
        books = DataHandler.get_all_books()
        
        if not books:
            empty_label = ctk.CTkLabel(
                self.content_frame,
                text="No books found. Add a new book.",
                font=("Helvetica", 14),
                text_color="#cccccc"
            )
            empty_label.pack(pady=50)
            return
        
        # Scrollable list
        list_frame = ctk.CTkScrollableFrame(self.content_frame, fg_color="transparent")
        list_frame.pack(fill="both", expand=True, pady=10)
        
        for book in books:
            self.create_book_card(list_frame, book)
    
    def create_book_card(self, parent, book: dict):
        """Create book card"""
        card = ctk.CTkFrame(parent, fg_color=self.dark_gray, corner_radius=8)
        card.pack(fill="x", pady=10, padx=5)
        
        # Left side - Book info
        info_frame = ctk.CTkFrame(card, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True, padx=15, pady=15)
        
        title_label = ctk.CTkLabel(
            info_frame,
            text=f"📕 {book['title']}",
            font=("Helvetica", 14, "bold"),
            text_color=self.fg_color
        )
        title_label.pack(anchor="w")
        
        author_label = ctk.CTkLabel(
            info_frame,
            text=f"✍️ Author: {book['author']} | ISBN: {book['isbn']}",
            font=("Helvetica", 12),
            text_color="#cccccc"
        )
        author_label.pack(anchor="w", pady=(6, 0))
        
        copies_label = ctk.CTkLabel(
            info_frame,
            text=f"📦 Total: {book.get('total_copies', 1)} | Available: {book.get('available_copies', 0)}",
            font=("Helvetica", 10),
            text_color="#aaaaaa"
        )
        copies_label.pack(anchor="w", pady=(2, 0))
        
        # Right side - Buttons
        btn_frame = ctk.CTkFrame(card, fg_color="transparent")
        btn_frame.pack(side="right", padx=15, pady=12)
        
        ctk.CTkButton(
            btn_frame,
            text="✏️ Edit",
            font=("Helvetica", 11),
            width=75,
            fg_color=self.primary_color,
            command=lambda: self.show_edit_book_dialog(book)
        ).pack(side="left", padx=3)
        
        ctk.CTkButton(
            btn_frame,
            text="🗑️ Delete",
            font=("Helvetica", 11),
            width=75,
            fg_color=self.danger_color,
            command=lambda: self.delete_book(book['id'])
        ).pack(side="left", padx=3)
    
    def show_add_book_dialog(self):
        """Show dialog to add new book"""
        # Top-level window
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add New Book")
        dialog.geometry("500x600")
        dialog.resizable(False, False)
        dialog.configure(fg_color=self.bg_color)
        
        # Title
        title = ctk.CTkLabel(
            dialog,
            text="📕 Add New Book",
            font=("Helvetica", 16, "bold"),
            text_color=self.primary_color
        )
        title.pack(pady=15)
        
        # Form
        form_frame = ctk.CTkScrollableFrame(dialog, fg_color="transparent")
        form_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Title
        ctk.CTkLabel(form_frame, text="Book Title:", font=("Helvetica", 11)).pack(anchor="w")
        title_entry = ctk.CTkEntry(form_frame, height=35, font=("Helvetica", 11))
        title_entry.pack(fill="x", pady=(0, 12))
        
        # Author
        ctk.CTkLabel(form_frame, text="Author:", font=("Helvetica", 11)).pack(anchor="w")
        author_entry = ctk.CTkEntry(form_frame, height=35, font=("Helvetica", 11))
        author_entry.pack(fill="x", pady=(0, 12))
        
        # ISBN
        ctk.CTkLabel(form_frame, text="ISBN:", font=("Helvetica", 11)).pack(anchor="w")
        isbn_entry = ctk.CTkEntry(form_frame, height=35, font=("Helvetica", 11))
        isbn_entry.pack(fill="x", pady=(0, 12))
        
        # Publisher
        ctk.CTkLabel(form_frame, text="Publisher:", font=("Helvetica", 11)).pack(anchor="w")
        publisher_entry = ctk.CTkEntry(form_frame, height=35, font=("Helvetica", 11))
        publisher_entry.pack(fill="x", pady=(0, 12))
        
        # Category
        ctk.CTkLabel(form_frame, text="Category:", font=("Helvetica", 11)).pack(anchor="w")
        category_entry = ctk.CTkEntry(form_frame, height=35, font=("Helvetica", 11))
        category_entry.pack(fill="x", pady=(0, 12))
        
        # Total Copies
        ctk.CTkLabel(form_frame, text="Total Copies:", font=("Helvetica", 11)).pack(anchor="w")
        copies_entry = ctk.CTkEntry(form_frame, height=35, font=("Helvetica", 11))
        copies_entry.insert(0, "1")
        copies_entry.pack(fill="x", pady=(0, 20))
        
        # Status label
        status_label = ctk.CTkLabel(form_frame, text="", font=("Helvetica", 10))
        status_label.pack(pady=10)
        
        # Buttons
        btn_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        btn_frame.pack(fill="x", pady=10)
        
        def save_book():
            title_val = title_entry.get().strip()
            author_val = author_entry.get().strip()
            isbn_val = isbn_entry.get().strip()
            publisher_val = publisher_entry.get().strip()
            category_val = category_entry.get().strip()
            copies_val = copies_entry.get().strip()
            
            if not all([title_val, author_val, isbn_val, publisher_val, category_val, copies_val]):
                status_label.configure(text="❌ Fill all fields!", text_color=self.danger_color)
                return
            
            try:
                copies = int(copies_val)
                if copies < 1:
                    raise ValueError
            except:
                status_label.configure(text="❌ Copies must be a number", text_color=self.danger_color)
                return
            
            book_data = {
                'title': title_val,
                'author': author_val,
                'isbn': isbn_val,
                'publisher': publisher_val,
                'category': category_val,
                'total_copies': copies
            }
            
            success, message = DataHandler.add_book(book_data)
            if success:
                status_label.configure(text=f"✅ {message}", text_color=self.success_color)
                dialog.after(800, lambda: [dialog.destroy(), self.show_books_screen()])
            else:
                status_label.configure(text=f"❌ {message}", text_color=self.danger_color)
        
        ctk.CTkButton(
            btn_frame,
            text="💾 Save Book",
            font=("Helvetica", 12, "bold"),
            fg_color=self.success_color,
            command=save_book
        ).pack(fill="x", pady=5)
        
        ctk.CTkButton(
            btn_frame,
            text="Cancel",
            font=("Helvetica", 12),
            fg_color="#6c757d",
            command=dialog.destroy
        ).pack(fill="x")
    
    def show_edit_book_dialog(self, book: dict):
        """Edit book"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Edit Book")
        dialog.geometry("500x500")
        dialog.resizable(False, False)
        dialog.configure(fg_color=self.bg_color)
        
        # Title
        title = ctk.CTkLabel(
            dialog,
            text="📕 Edit Book",
            font=("Helvetica", 16, "bold"),
            text_color=self.primary_color
        )
        title.pack(pady=15)
        
        # Form
        form_frame = ctk.CTkScrollableFrame(dialog, fg_color="transparent")
        form_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Title
        ctk.CTkLabel(form_frame, text="Title:", font=("Helvetica", 11)).pack(anchor="w")
        title_entry = ctk.CTkEntry(form_frame, height=35)
        title_entry.insert(0, book['title'])
        title_entry.pack(fill="x", pady=(0, 10))
        
        # Author
        ctk.CTkLabel(form_frame, text="Author:", font=("Helvetica", 11)).pack(anchor="w")
        author_entry = ctk.CTkEntry(form_frame, height=35)
        author_entry.insert(0, book['author'])
        author_entry.pack(fill="x", pady=(0, 10))
        
        # Total Copies
        ctk.CTkLabel(form_frame, text="Total Copies:", font=("Helvetica", 11)).pack(anchor="w")
        copies_entry = ctk.CTkEntry(form_frame, height=35)
        copies_entry.insert(0, str(book.get('total_copies', 1)))
        copies_entry.pack(fill="x", pady=(0, 20))
        
        # Status
        status_label = ctk.CTkLabel(form_frame, text="", font=("Helvetica", 10))
        status_label.pack(pady=10)
        
        # Buttons
        btn_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        btn_frame.pack(fill="x", pady=10)
        
        def update_book():
            try:
                title = title_entry.get().strip()
                author = author_entry.get().strip()
                copies_str = copies_entry.get().strip()
                
                if not all([title, author, copies_str]):
                    status_label.configure(text="❌ All fields are required!", text_color=self.danger_color)
                    return
                
                try:
                    copies = int(copies_str)
                    if copies < 1:
                        status_label.configure(text="❌ Total copies must be at least 1!", text_color=self.danger_color)
                        return
                except ValueError:
                    status_label.configure(text="❌ Total copies must be a valid number!", text_color=self.danger_color)
                    return
                
                updated = {
                    'title': title,
                    'author': author,
                    'total_copies': copies
                }
                
                if DataHandler.update_book(book['id'], updated):
                    status_label.configure(text="✅ Book updated successfully!", text_color=self.success_color)
                    dialog.after(800, lambda: [dialog.destroy(), self.show_books_screen()])
                else:
                    status_label.configure(text="❌ Failed to update book!", text_color=self.danger_color)
            except Exception as e:
                status_label.configure(text=f"❌ Error: {str(e)}", text_color=self.danger_color)
        
        ctk.CTkButton(
            btn_frame,
            text="💾 Update",
            fg_color=self.primary_color,
            command=update_book
        ).pack(fill="x", pady=5)
        
        ctk.CTkButton(
            btn_frame,
            text="Cancel",
            fg_color="#6c757d",
            command=dialog.destroy
        ).pack(fill="x")
    
    def delete_book(self, book_id: int):
        """Delete book"""
        if DataHandler.delete_book(book_id):
            self.show_books_screen()
    
    # ======================== MEMBERS SCREEN ========================
    
    def show_members_screen(self):
        """Manage Members"""
        self.nav_buttons["members"].configure(fg_color=self.primary_color)
        
        # Title
        title = ctk.CTkLabel(
            self.content_frame,
            text="👥 Manage Members",
            font=("Helvetica", 20, "bold"),
            text_color=self.primary_color
        )
        title.pack(pady=(0, 20))
        
        # Button
        ctk.CTkButton(
            self.content_frame,
            text="➕ Add New Member",
            font=("Helvetica", 12, "bold"),
            fg_color=self.success_color,
            command=self.show_add_member_dialog
        ).pack(pady=10)
        
        # Members list
        members = DataHandler.get_all_members()
        
        if not members:
            empty = ctk.CTkLabel(
                self.content_frame,
                text="No members found.",
                font=("Helvetica", 14),
                text_color="#cccccc"
            )
            empty.pack(pady=50)
            return
        
        list_frame = ctk.CTkScrollableFrame(self.content_frame, fg_color="transparent")
        list_frame.pack(fill="both", expand=True, pady=10)
        
        for member in members:
            self.create_member_card(list_frame, member)
    
    def create_member_card(self, parent, member: dict):
        """Create member card"""
        card = ctk.CTkFrame(parent, fg_color=self.dark_gray, corner_radius=8)
        card.pack(fill="x", pady=10, padx=5)
        
        info = ctk.CTkFrame(card, fg_color="transparent")
        info.pack(side="left", fill="both", expand=True, padx=15, pady=15)
        
        name = ctk.CTkLabel(
            info,
            text=f"👤 {member['name']}",
            font=("Helvetica", 14, "bold"),
            text_color=self.fg_color
        )
        name.pack(anchor="w")
        
        email = ctk.CTkLabel(
            info,
            text=f"📧 {member['email']} | ID: {member['member_id']}",
            font=("Helvetica", 11),
            text_color="#cccccc"
        )
        email.pack(anchor="w", pady=(4, 0))
        
        # Buttons
        btn_frame = ctk.CTkFrame(card, fg_color="transparent")
        btn_frame.pack(side="right", padx=15, pady=12)
        
        ctk.CTkButton(
            btn_frame,
            text="📋 History",
            font=("Helvetica", 10),
            width=80,
            fg_color=self.primary_color,
            command=lambda: self.show_member_history(member)
        ).pack(side="left", padx=2)
        
        ctk.CTkButton(
            btn_frame,
            text="✏️ Edit",
            font=("Helvetica", 10),
            width=60,
            fg_color="#ffc107",
            command=lambda: self.show_edit_member_dialog(member)
        ).pack(side="left", padx=2)
        
        ctk.CTkButton(
            btn_frame,
            text="🗑️ Delete",
            font=("Helvetica", 10),
            width=70,
            fg_color=self.danger_color,
            command=lambda: self.delete_member(member['id'])
        ).pack(side="left", padx=2)
    
    def show_add_member_dialog(self):
        """Show dialog to add new member"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add Member")
        dialog.geometry("400x500")
        dialog.configure(fg_color=self.bg_color)
        
        title = ctk.CTkLabel(dialog, text="👥 Add Member", font=("Helvetica", 16, "bold"), text_color=self.primary_color)
        title.pack(pady=15)
        
        form = ctk.CTkScrollableFrame(dialog, fg_color="transparent")
        form.pack(fill="both", expand=True, padx=20)
        
        ctk.CTkLabel(form, text="Name:", font=("Helvetica", 11)).pack(anchor="w")
        name_entry = ctk.CTkEntry(form, height=35)
        name_entry.pack(fill="x", pady=(0, 10))
        
        ctk.CTkLabel(form, text="Email:", font=("Helvetica", 11)).pack(anchor="w")
        email_entry = ctk.CTkEntry(form, height=35)
        email_entry.pack(fill="x", pady=(0, 10))
        
        ctk.CTkLabel(form, text="Member ID:", font=("Helvetica", 11)).pack(anchor="w")
        id_entry = ctk.CTkEntry(form, height=35)
        id_entry.pack(fill="x", pady=(0, 10))
        
        ctk.CTkLabel(form, text="Phone:", font=("Helvetica", 11)).pack(anchor="w")
        phone_entry = ctk.CTkEntry(form, height=35)
        phone_entry.pack(fill="x", pady=(0, 10))
        
        ctk.CTkLabel(form, text="Password:", font=("Helvetica", 11)).pack(anchor="w")
        pass_entry = ctk.CTkEntry(form, height=35, show="●")
        pass_entry.pack(fill="x", pady=(0, 20))
        
        status = ctk.CTkLabel(form, text="", font=("Helvetica", 10))
        status.pack()
        
        def save():
            if not all([name_entry.get(), email_entry.get(), id_entry.get(), pass_entry.get()]):
                status.configure(text="❌ Fill all required fields!", text_color=self.danger_color)
                return
            
            member_data = {
                'name': name_entry.get().strip(),
                'email': email_entry.get().strip(),
                'member_id': id_entry.get().strip(),
                'password': pass_entry.get(),
                'phone': phone_entry.get().strip(),
                'address': '',
                'status': 'active'
            }
            
            success, message = DataHandler.register_member(member_data)
            if success:
                status.configure(text=f"✅ {message}", text_color=self.success_color)
                dialog.after(800, lambda: [dialog.destroy(), self.show_members_screen()])
            else:
                status.configure(text=f"❌ {message}", text_color=self.danger_color)
        
        btn_frame = ctk.CTkFrame(form, fg_color="transparent")
        btn_frame.pack(fill="x", pady=10)
        
        ctk.CTkButton(btn_frame, text="💾 Save", fg_color=self.success_color, command=save).pack(fill="x", pady=5)
        ctk.CTkButton(btn_frame, text="Cancel", fg_color="#6c757d", command=dialog.destroy).pack(fill="x")
    
    def show_edit_member_dialog(self, member: dict):
        """Edit member"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Edit Member")
        dialog.geometry("400x400")
        dialog.configure(fg_color=self.bg_color)
        
        title = ctk.CTkLabel(dialog, text="✏️ Edit Member", font=("Helvetica", 16, "bold"), text_color=self.primary_color)
        title.pack(pady=15)
        
        form = ctk.CTkScrollableFrame(dialog, fg_color="transparent")
        form.pack(fill="both", expand=True, padx=20)
        
        ctk.CTkLabel(form, text="Name:", font=("Helvetica", 11)).pack(anchor="w")
        name_entry = ctk.CTkEntry(form, height=35)
        name_entry.insert(0, member['name'])
        name_entry.pack(fill="x", pady=(0, 10))
        
        ctk.CTkLabel(form, text="Phone:", font=("Helvetica", 11)).pack(anchor="w")
        phone_entry = ctk.CTkEntry(form, height=35)
        phone_entry.insert(0, member.get('phone', ''))
        phone_entry.pack(fill="x", pady=(0, 20))
        
        status = ctk.CTkLabel(form, text="", font=("Helvetica", 10))
        status.pack()
        
        def update():
            name = name_entry.get().strip()
            phone = phone_entry.get().strip()
            
            if not name:
                status.configure(text="❌ Name cannot be empty!", text_color=self.danger_color)
                return
            
            updated = {'name': name, 'phone': phone}
            if DataHandler.update_member(member['id'], updated):
                status.configure(text="✅ Member updated successfully!", text_color=self.success_color)
                dialog.after(800, lambda: [dialog.destroy(), self.show_members_screen()])
            else:
                status.configure(text="❌ Failed to update member!", text_color=self.danger_color)
        
        btn = ctk.CTkFrame(form, fg_color="transparent")
        btn.pack(fill="x", pady=10)
        ctk.CTkButton(btn, text="💾 Update", fg_color=self.primary_color, command=update).pack(fill="x", pady=5)
        ctk.CTkButton(btn, text="Cancel", fg_color="#6c757d", command=dialog.destroy).pack(fill="x")
    
    def show_member_history(self, member: dict):
        """Member borrowing history"""
        history = DataHandler.get_member_history(member['id'])
        
        win = ctk.CTkToplevel(self)
        win.title(f"{member['name']} - Borrowing History")
        win.geometry("600x500")
        win.configure(fg_color=self.bg_color)
        
        title = ctk.CTkLabel(win, text=f"📋 {member['name']} - History", font=("Helvetica", 16, "bold"), text_color=self.primary_color)
        title.pack(pady=15)
        
        if not history:
            empty = ctk.CTkLabel(win, text="No history available", font=("Helvetica", 12), text_color="#cccccc")
            empty.pack(pady=50)
            return
        
        frame = ctk.CTkScrollableFrame(win, fg_color="transparent")
        frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        for record in history:
            card = ctk.CTkFrame(frame, fg_color=self.dark_gray, corner_radius=8)
            card.pack(fill="x", pady=8)
            
            info = ctk.CTkLabel(
                card,
                text=f"📕 {record['book_title']} | Issued: {record['issue_date']} | Due: {record['due_date']}",
                font=("Helvetica", 11),
                text_color=self.fg_color
            )
            info.pack(padx=15, pady=10, anchor="w")
            
            status_text = "✅ Returned" if record['status'] == 'returned' else "📤 Active"
            status = ctk.CTkLabel(card, text=status_text, font=("Helvetica", 10), text_color="#aaaaaa")
            status.pack(padx=15, pady=(0, 10), anchor="w")
    
    def delete_member(self, member_id: int):
        """Member delete"""
        if DataHandler.delete_member(member_id):
            self.show_members_screen()
    
    # ======================== ISSUED BOOKS SCREEN ========================
    
    def show_issued_screen(self):
        """List of issued books"""
        self.nav_buttons["issued"].configure(fg_color=self.primary_color)
        
        title = ctk.CTkLabel(
            self.content_frame,
            text="📤 Issued Books",
            font=("Helvetica", 28, "bold"),
            text_color=self.primary_color
        )
        title.pack(pady=(0, 25))
        
        issued = DataHandler.get_all_issued_books()
        
        if not issued:
            empty = ctk.CTkLabel(
                self.content_frame,
                text="No books issued yet.",
                font=("Helvetica", 14),
                text_color="#cccccc"
            )
            empty.pack(pady=50)
            return
        
        frame = ctk.CTkScrollableFrame(self.content_frame, fg_color="transparent")
        frame.pack(fill="both", expand=True, pady=10)
        
        for record in issued:
            card = ctk.CTkFrame(frame, fg_color=self.dark_gray, corner_radius=8)
            card.pack(fill="x", pady=8, padx=5)
            
            info = ctk.CTkFrame(card, fg_color="transparent")
            info.pack(side="left", fill="both", expand=True, padx=15, pady=12)
            
            ctk.CTkLabel(
                info,
                text=f"📕 {record['book_title']}",
                font=("Helvetica", 12, "bold"),
                text_color=self.fg_color
            ).pack(anchor="w")
            
            ctk.CTkLabel(
                info,
                text=f"👤 {record['member_name']} | Due: {record['due_date']}",
                font=("Helvetica", 10),
                text_color="#cccccc"
            ).pack(anchor="w", pady=(3, 0))
            
            btn = ctk.CTkFrame(card, fg_color="transparent")
            btn.pack(side="right", padx=15, pady=12)
            
            ctk.CTkButton(
                btn,
                text="✅ Return",
                font=("Helvetica", 10),
                fg_color=self.success_color,
                command=lambda r=record: self.return_book_action(r)
            ).pack()
    
    def return_book_action(self, record: dict):
        """Return book"""
        if DataHandler.return_book(record['id']):
            self.show_issued_screen()
    
    # ======================== REPORTS SCREEN ========================
    
    def show_reports_screen(self):
        """Reports and analytics"""
        self.nav_buttons["reports"].configure(fg_color=self.primary_color)
        
        title = ctk.CTkLabel(
            self.content_frame,
            text="📊 Reports & Analytics",
            font=("Helvetica", 20, "bold"),
            text_color=self.primary_color
        )
        title.pack(pady=(0, 30))
        
        frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        frame.pack(fill="both", expand=True)
        
        # Stats
        stats = DataHandler.get_dashboard_stats()
        
        report_data = [
            ("📚 Total Books in Library", str(stats['total_books'])),
            ("👥 Total Registered Members", str(stats['total_members'])),
            ("📤 Books Currently Issued", str(stats['total_issued'])),
            ("✅ Books Available", str(stats['total_available'])),
        ]
        
        for label, value in report_data:
            card = ctk.CTkFrame(frame, fg_color=self.dark_gray, corner_radius=10)
            card.pack(fill="x", pady=10)
            
            ctk.CTkLabel(
                card,
                text=f"{label}: {value}",
                font=("Helvetica", 14),
                text_color=self.fg_color
            ).pack(padx=20, pady=15, anchor="w")
    
    # ======================== LOGOUT ========================
    
    def logout(self):
        """Logout and return to login screen"""
        self.destroy()
        from auth import AuthWindow
        app = AuthWindow()
        app.mainloop()


if __name__ == "__main__":
    # Test
    dummy_admin = {'name': 'Test Admin', 'email': 'admin@test.com', 'password': '1234'}
    app = AdminDashboard(dummy_admin)
    app.mainloop()
