"""
Member Dashboard - Student/Regular User Interface
"""

import customtkinter as ctk
from data_handler import DataHandler
from datetime import datetime, timedelta


class MemberDashboard(ctk.CTk):
    """Member Dashboard - Browse & Borrow Books"""
    
    def __init__(self, member_user: dict):
        super().__init__()
        
        self.member_user = member_user
        
        self.title("Library Management - Member Dashboard")
        self.geometry("1100x650")
        
        # Color scheme
        self.bg_color = "#0a0a0a"
        self.fg_color = "#ffffff"
        self.primary_color = "#007bff"
        self.success_color = "#28a745"
        self.danger_color = "#dc3545"
        self.dark_gray = "#1a1a1a"
        
        self.configure(fg_color=self.bg_color)
        
        self.current_screen = "home"
        
        self.create_layout()
        self.show_home_screen()
    
    def create_layout(self):
        """Sidebar + Content layout"""
        
        # ==================== SIDEBAR ====================
        self.sidebar = ctk.CTkFrame(self, fg_color=self.dark_gray, width=220)
        self.sidebar.pack(side="left", fill="y", padx=0)
        self.sidebar.pack_propagate(False)
        
        # Header
        header = ctk.CTkLabel(
            self.sidebar,
            text="📚 LIBRARY",
            font=("Helvetica", 18, "bold"),
            text_color=self.primary_color
        )
        header.pack(pady=20)
        
        # Welcome
        welcome = ctk.CTkLabel(
            self.sidebar,
            text=f"👋 {self.member_user['name']}",
            font=("Helvetica", 14),
            text_color="#cccccc",
            wraplength=190
        )
        welcome.pack(pady=(0, 20), padx=10)
        
        # Navigation
        self.nav_buttons = {}
        
        nav_items = [
            ("🏠 Home", "home"),
            ("🔍 Search Books", "search"),
            ("📖 Browse Catalog", "catalog"),
            ("📤 My Borrowings", "borrowings"),
            ("📋 My History", "history"),
        ]
        
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
            btn.pack(pady=4, padx=8, fill="x")
            self.nav_buttons[screen] = btn
        
        # Logout
        ctk.CTkButton(
            self.sidebar,
            text="🚪 Logout",
            font=("Helvetica", 13, "bold"),
            height=50,
            fg_color=self.danger_color,
            hover_color="#c82333",
            command=self.logout
        ).pack(pady=(50, 10), padx=8, fill="x", side="bottom")
        
        # ==================== CONTENT ====================
        self.content = ctk.CTkFrame(self, fg_color=self.bg_color)
        self.content.pack(side="right", fill="both", expand=True, padx=20, pady=20)
        
        self.content_frame = ctk.CTkFrame(self.content, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True)
    
    def clear_content(self):
        """Clear content"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def switch_screen(self, screen_name: str):
        """Switch screen"""
        # Highlight button
        if hasattr(self, 'current_screen') and self.current_screen in self.nav_buttons:
            self.nav_buttons[self.current_screen].configure(fg_color="transparent")
        
        self.nav_buttons[screen_name].configure(fg_color=self.primary_color)
        self.current_screen = screen_name
        
        self.clear_content()
        
        if screen_name == "home":
            self.show_home_screen()
        elif screen_name == "search":
            self.show_search_screen()
        elif screen_name == "catalog":
            self.show_catalog_screen()
        elif screen_name == "borrowings":
            self.show_borrowings_screen()
        elif screen_name == "history":
            self.show_history_screen()
    
    # ======================== HOME SCREEN ========================
    
    def show_home_screen(self):
        """Welcome screen"""
        self.nav_buttons["home"].configure(fg_color=self.primary_color)
        
        # Title
        title = ctk.CTkLabel(
            self.content_frame,
            text=f"👋 Welcome, {self.member_user['name']}!",
            font=("Helvetica", 36, "bold"),
            text_color=self.primary_color
        )
        title.pack(pady=(0, 12))
        
        subtitle = ctk.CTkLabel(
            self.content_frame,
            text="Welcome to Library Management System",
            font=("Helvetica", 18),
            text_color="#cccccc"
        )
        subtitle.pack(pady=(0, 40))
        
        # Quick Info
        info_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        info_frame.pack(fill="x", pady=20)
        
        # Current borrowings count
        borrowings = DataHandler.get_member_issued_books(self.member_user['id'])
        
        card1 = ctk.CTkFrame(info_frame, fg_color=self.dark_gray, corner_radius=10)
        card1.pack(side="left", fill="x", expand=True, padx=10)
        
        ctk.CTkLabel(
            card1,
            text="📤 Currently Borrowed",
            font=("Helvetica", 16),
            text_color="#cccccc"
        ).pack(pady=(18, 8), padx=15)
        
        ctk.CTkLabel(
            card1,
            text=str(len(borrowings)),
            font=("Helvetica", 48, "bold"),
            text_color=self.primary_color
        ).pack(pady=(0, 18), padx=15)
        
        # Total books in library
        all_books = DataHandler.get_all_books()
        
        card2 = ctk.CTkFrame(info_frame, fg_color=self.dark_gray, corner_radius=10)
        card2.pack(side="left", fill="x", expand=True, padx=10)
        
        ctk.CTkLabel(
            card2,
            text="📚 Books in Library",
            font=("Helvetica", 16),
            text_color="#cccccc"
        ).pack(pady=(18, 8), padx=15)
        
        ctk.CTkLabel(
            card2,
            text=str(len(all_books)),
            font=("Helvetica", 32, "bold"),
            text_color=self.success_color
        ).pack(pady=(0, 15), padx=15)
        
        # Quick Actions
        actions_frame = ctk.CTkFrame(self.content_frame, fg_color=self.dark_gray, corner_radius=10)
        actions_frame.pack(fill="x", pady=30)
        
        ctk.CTkLabel(
            actions_frame,
            text="⚡ Quick Actions",
            font=("Helvetica", 16, "bold"),
            text_color=self.fg_color
        ).pack(pady=(15, 10), padx=15, anchor="w")
        
        btn_frame = ctk.CTkFrame(actions_frame, fg_color="transparent")
        btn_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        ctk.CTkButton(
            btn_frame,
            text="🔍 Search Books",
            font=("Helvetica", 13),
            fg_color=self.primary_color,
            command=lambda: self.switch_screen("search")
        ).pack(side="left", padx=5, fill="x", expand=True)
        
        ctk.CTkButton(
            btn_frame,
            text="📖 View Catalog",
            font=("Helvetica", 13),
            fg_color=self.success_color,
            command=lambda: self.switch_screen("catalog")
        ).pack(side="left", padx=5, fill="x", expand=True)
        
        ctk.CTkButton(
            btn_frame,
            text="📤 My Books",
            font=("Helvetica", 13),
            fg_color="#ffc107",
            command=lambda: self.switch_screen("borrowings")
        ).pack(side="left", padx=5, fill="x", expand=True)
    
    # ======================== SEARCH SCREEN ========================
    
    def show_search_screen(self):
        """Search books"""
        self.nav_buttons["search"].configure(fg_color=self.primary_color)
        
        # Title
        title = ctk.CTkLabel(
            self.content_frame,
            text="🔍 Search Books",
            font=("Helvetica", 32, "bold"),
            text_color=self.primary_color
        )
        title.pack(pady=(0, 25))
        
        # Search bar
        search_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        search_frame.pack(fill="x", pady=18)
        
        ctk.CTkLabel(search_frame, text="Search Type:", font=("Helvetica", 15)).pack(side="left", padx=8)
        
        search_type_var = ctk.StringVar(value="title")
        
        ctk.CTkRadioButton(
            search_frame,
            text="Title",
            variable=search_type_var,
            value="title",
            font=("Helvetica", 12)
        ).pack(side="left", padx=5)
        
        ctk.CTkRadioButton(
            search_frame,
            text="Author",
            variable=search_type_var,
            value="author",
            font=("Helvetica", 12)
        ).pack(side="left", padx=5)
        
        ctk.CTkRadioButton(
            search_frame,
            text="Category",
            variable=search_type_var,
            value="category",
            font=("Helvetica", 12)
        ).pack(side="left", padx=5)
        
        # Input
        input_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        input_frame.pack(fill="x", pady=10)
        
        search_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="Enter book name, author or category...",
            height=45,
            font=("Helvetica", 14)
        )
        search_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        results_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        results_frame.pack(fill="both", expand=True, pady=10)
        
        def perform_search():
            results_frame.pack_forget()
            results_frame.pack(fill="both", expand=True)
            
            for widget in results_frame.winfo_children():
                widget.destroy()
            
            query = search_entry.get().strip()
            if not query:
                empty = ctk.CTkLabel(
                    results_frame,
                    text="Start typing to search",
                    font=("Helvetica", 12),
                    text_color="#cccccc"
                )
                empty.pack(pady=50)
                return
            
            search_type = search_type_var.get()
            results = DataHandler.search_books(query, search_type)
            
            if not results:
                empty = ctk.CTkLabel(
                    results_frame,
                    text="No results found",
                    font=("Helvetica", 12),
                    text_color="#cccccc"
                )
                empty.pack(pady=50)
                return
            
            # Show results
            scroll = ctk.CTkScrollableFrame(results_frame, fg_color="transparent")
            scroll.pack(fill="both", expand=True)
            
            for book in results:
                self.create_book_item(scroll, book)
        
        ctk.CTkButton(
            input_frame,
            text="🔎 Search",
            font=("Helvetica", 12, "bold"),
            width=100,
            fg_color=self.primary_color,
            command=perform_search
        ).pack(side="left", padx=5)
    
    # ======================== CATALOG SCREEN ========================
    
    def show_catalog_screen(self):
        """Browse all books"""
        self.nav_buttons["catalog"].configure(fg_color=self.primary_color)
        
        title = ctk.CTkLabel(
            self.content_frame,
            text="📖 Library Catalog",
            font=("Helvetica", 28, "bold"),
            text_color=self.primary_color
        )
        title.pack(pady=(0, 25))
        
        books = DataHandler.get_all_books()
        
        if not books:
            empty = ctk.CTkLabel(
                self.content_frame,
                text="No books available in library yet",
                font=("Helvetica", 14),
                text_color="#cccccc"
            )
            empty.pack(pady=50)
            return
        
        scroll = ctk.CTkScrollableFrame(self.content_frame, fg_color="transparent")
        scroll.pack(fill="both", expand=True)
        
        for book in books:
            self.create_book_item(scroll, book)
    
    def create_book_item(self, parent, book: dict):
        """Create book item"""
        card = ctk.CTkFrame(parent, fg_color=self.dark_gray, corner_radius=8)
        card.pack(fill="x", pady=8, padx=5)
        
        # Left - Info
        info = ctk.CTkFrame(card, fg_color="transparent")
        info.pack(side="left", fill="both", expand=True, padx=15, pady=12)
        
        title_label = ctk.CTkLabel(
            info,
            text=f"📕 {book['title']}",
            font=("Helvetica", 12, "bold"),
            text_color=self.fg_color
        )
        title_label.pack(anchor="w")
        
        author_label = ctk.CTkLabel(
            info,
            text=f"✍️ {book['author']} | 🏢 {book.get('publisher', 'Unknown')}",
            font=("Helvetica", 10),
            text_color="#cccccc"
        )
        author_label.pack(anchor="w", pady=(3, 0))
        
        category_label = ctk.CTkLabel(
            info,
            text=f"📂 {book.get('category', 'General')} | ISBN: {book['isbn']}",
            font=("Helvetica", 9),
            text_color="#aaaaaa"
        )
        category_label.pack(anchor="w", pady=(2, 0))
        
        # Right - Button
        btn_frame = ctk.CTkFrame(card, fg_color="transparent")
        btn_frame.pack(side="right", padx=15, pady=12)
        
        available = book.get('available_copies', 0) > 0
        status_text = f"✅ Available ({book.get('available_copies', 0)})"
        btn_color = self.success_color if available else self.danger_color
        btn_cmd = lambda: self.request_book(book) if available else None
        
        ctk.CTkLabel(
            btn_frame,
            text=status_text,
            font=("Helvetica", 10),
            text_color=btn_color
        ).pack(side="left", padx=10)
        
        ctk.CTkButton(
            btn_frame,
            text="📦 Borrow" if available else "❌ Unavailable",
            font=("Helvetica", 10, "bold"),
            width=80,
            fg_color=btn_color,
            state="normal" if available else "disabled",
            command=btn_cmd
        ).pack(side="left", padx=5)
    
    def request_book(self, book: dict):
        """Request to borrow book"""
        # Check if already borrowed
        borrowings = DataHandler.get_member_issued_books(self.member_user['id'])
        if any(b['book_id'] == book['id'] for b in borrowings):
            self.show_message("⚠️ You have already borrowed this book", "warning")
            return
        
        # Set due date (14 days from now)
        due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
        
        if DataHandler.issue_book(book['id'], self.member_user['id'], due_date):
            self.show_message(f"✅ Book '{book['title']}' borrowed successfully!\n📅 Return Date: {due_date}", "success")
            # Refresh
            self.after(1000, lambda: self.show_catalog_screen())
        else:
            self.show_message("❌ Error - Could not borrow book", "error")
    
    def show_message(self, message: str, msg_type: str):
        """Message dialog"""
        msg_win = ctk.CTkToplevel(self)
        msg_win.title("Message")
        msg_win.geometry("400x150")
        msg_win.configure(fg_color=self.bg_color)
        
        icon = "✅" if msg_type == "success" else ("⚠️" if msg_type == "warning" else "❌")
        
        ctk.CTkLabel(
            msg_win,
            text=f"{icon}\n{message}",
            font=("Helvetica", 12),
            text_color=self.fg_color
        ).pack(pady=20, padx=20)
        
        ctk.CTkButton(
            msg_win,
            text="OK",
            command=msg_win.destroy
        ).pack(pady=10)
    
    # ======================== BORROWINGS SCREEN ========================
    
    def show_borrowings_screen(self):
        """My current books"""
        self.nav_buttons["borrowings"].configure(fg_color=self.primary_color)
        
        title = ctk.CTkLabel(
            self.content_frame,
            text="📤 My Current Books",
            font=("Helvetica", 28, "bold"),
            text_color=self.primary_color
        )
        title.pack(pady=(0, 25))
        
        borrowings = DataHandler.get_member_issued_books(self.member_user['id'])
        
        if not borrowings:
            empty = ctk.CTkLabel(
                self.content_frame,
                text="You haven't borrowed any books yet",
                font=("Helvetica", 14),
                text_color="#cccccc"
            )
            empty.pack(pady=50)
            return
        
        scroll = ctk.CTkScrollableFrame(self.content_frame, fg_color="transparent")
        scroll.pack(fill="both", expand=True)
        
        for record in borrowings:
            card = ctk.CTkFrame(scroll, fg_color=self.dark_gray, corner_radius=8)
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
                text=f"✍️ {record['author']}",
                font=("Helvetica", 10),
                text_color="#cccccc"
            ).pack(anchor="w", pady=(3, 0))
            
            ctk.CTkLabel(
                info,
                text=f"📅 Borrowed: {record['issue_date']} | Return by: {record['due_date']}",
                font=("Helvetica", 9),
                text_color="#ffc107"
            ).pack(anchor="w", pady=(2, 0))
    
    # ======================== HISTORY SCREEN ========================
    
    def show_history_screen(self):
        """Complete history"""
        self.nav_buttons["history"].configure(fg_color=self.primary_color)
        
        title = ctk.CTkLabel(
            self.content_frame,
            text="📋 My Complete History",
            font=("Helvetica", 28, "bold"),
            text_color=self.primary_color
        )
        title.pack(pady=(0, 25))
        
        history = DataHandler.get_member_history(self.member_user['id'])
        
        if not history:
            empty = ctk.CTkLabel(
                self.content_frame,
                text="No history available",
                font=("Helvetica", 14),
                text_color="#cccccc"
            )
            empty.pack(pady=50)
            return
        
        scroll = ctk.CTkScrollableFrame(self.content_frame, fg_color="transparent")
        scroll.pack(fill="both", expand=True)
        
        for record in history:
            card = ctk.CTkFrame(scroll, fg_color=self.dark_gray, corner_radius=8)
            card.pack(fill="x", pady=8, padx=5)
            
            info = ctk.CTkFrame(card, fg_color="transparent")
            info.pack(fill="both", expand=True, padx=15, pady=12)
            
            ctk.CTkLabel(
                info,
                text=f"📕 {record['book_title']}",
                font=("Helvetica", 12, "bold"),
                text_color=self.fg_color
            ).pack(anchor="w")
            
            status = "✅ Returned" if record['status'] == "returned" else "📤 Active"
            status_color = self.success_color if record['status'] == "returned" else "#ffc107"
            
            ctk.CTkLabel(
                info,
                text=f"Borrowed: {record['issue_date']} | Returned: {record.get('return_date', 'Pending')} | {status}",
                font=("Helvetica", 10),
                text_color=status_color
            ).pack(anchor="w", pady=(3, 0))
    
    # ======================== LOGOUT ========================
    
    def logout(self):
        """Logout"""
        self.destroy()
        from auth import AuthWindow
        app = AuthWindow()
        app.mainloop()


if __name__ == "__main__":
    # Test
    dummy_member = {'id': 1, 'name': 'Test Member', 'email': 'test@member.com'}
    app = MemberDashboard(dummy_member)
    app.mainloop()
