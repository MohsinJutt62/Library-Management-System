"""
Authentication Module - Login/Signup Screen
Admin and Member both
"""

import customtkinter as ctk
from data_handler import DataHandler
from PIL import Image
import hashlib


class AuthWindow(ctk.CTk):
    """Login/Signup Window"""
    
    def __init__(self):
        super().__init__()
        
        self.title("Library Management - Login/Signup")
        self.geometry("600x500")
        self.resizable(False, False)
        
        # Color scheme
        self.bg_color = "#0a0a0a"
        self.fg_color = "#ffffff"
        self.primary_color = "#007bff"
        self.danger_color = "#dc3545"
        
        self.configure(fg_color=self.bg_color)
        
        # Current user data
        self.current_user = None
        self.user_type = None  # 'admin' or 'member'
        
        # Show login screen by default
        self.show_login_screen()
    
    def clear_window(self):
        """Clear all widgets"""
        for widget in self.winfo_children():
            widget.destroy()
    
    def show_login_screen(self):
        """Show login screen"""
        self.clear_window()
        
        # Header
        header = ctk.CTkLabel(
            self,
            text="🎓 LIBRARY MANAGEMENT",
            font=("Helvetica", 32, "bold"),
            text_color=self.primary_color
        )
        header.pack(pady=25)
        
        subtitle = ctk.CTkLabel(
            self,
            text="Login to Your Account",
            font=("Helvetica", 18),
            text_color="#cccccc"
        )
        subtitle.pack(pady=(0, 30))
        
        # User Type Selection
        frame_type = ctk.CTkFrame(self, fg_color="transparent")
        frame_type.pack(pady=10)
        
        ctk.CTkLabel(
            frame_type,
            text="Select Account Type:",
            font=("Helvetica", 16),
            text_color=self.fg_color
        ).pack(side="left", padx=10)
        
        self.login_type_var = ctk.StringVar(value="member")
        
        ctk.CTkRadioButton(
            frame_type,
            text="👨‍💼 Admin",
            variable=self.login_type_var,
            value="admin",
            font=("Helvetica", 14)
        ).pack(side="left", padx=5)
        
        ctk.CTkRadioButton(
            frame_type,
            text="👤 Member",
            variable=self.login_type_var,
            value="member",
            font=("Helvetica", 14)
        ).pack(side="left", padx=5)
        
        # Input Fields
        frame_inputs = ctk.CTkFrame(self, fg_color="transparent")
        frame_inputs.pack(pady=20, padx=40, fill="both", expand=True)
        
        ctk.CTkLabel(
            frame_inputs,
            text="Email/Username:",
            font=("Helvetica", 16),
            text_color=self.fg_color
        ).pack(anchor="w", pady=(0, 8))
        
        self.login_email = ctk.CTkEntry(
            frame_inputs,
            placeholder_text="Enter your email",
            width=300,
            height=55,
            font=("Helvetica", 15),
            border_width=2,
            border_color=self.primary_color
        )
        self.login_email.pack(pady=(0, 20), fill="x")
        
        ctk.CTkLabel(
            frame_inputs,
            text="Password:",
            font=("Helvetica", 16),
            text_color=self.fg_color
        ).pack(anchor="w", pady=(0, 8))
        
        self.login_password = ctk.CTkEntry(
            frame_inputs,
            placeholder_text="Enter your password",
            width=300,
            height=55,
            font=("Helvetica", 15),
            show="●",
            border_width=2,
            border_color=self.primary_color
        )
        self.login_password.pack(pady=(0, 20), fill="x")
        
        # Buttons
        frame_buttons = ctk.CTkFrame(frame_inputs, fg_color="transparent")
        frame_buttons.pack(fill="x", pady=10)
        
        ctk.CTkButton(
            frame_buttons,
            text="Login",
            font=("Helvetica", 14, "bold"),
            height=50,
            command=self.handle_login,
            fg_color=self.primary_color,
            hover_color="#0056b3"
        ).pack(side="left", padx=5, fill="x", expand=True)
        
        ctk.CTkButton(
            frame_buttons,
            text="Sign Up",
            font=("Helvetica", 14, "bold"),
            height=50,
            command=self.show_signup_screen,
            fg_color="#28a745",
            hover_color="#218838"
        ).pack(side="left", padx=5, fill="x", expand=True)
        
        # Status Label
        self.status_label = ctk.CTkLabel(
            self,
            text="",
            font=("Helvetica", 10),
            text_color=self.danger_color
        )
        self.status_label.pack(pady=10)
    
    def show_signup_screen(self):
        """Show signup screen"""
        self.clear_window()
        
        # Header
        header = ctk.CTkLabel(
            self,
            text="🎓 LIBRARY MANAGEMENT",
            font=("Helvetica", 32, "bold"),
            text_color=self.primary_color
        )
        header.pack(pady=25)
        
        subtitle = ctk.CTkLabel(
            self,
            text="Create New Account",
            font=("Helvetica", 18),
            text_color="#cccccc"
        )
        subtitle.pack(pady=(0, 20))
        
        # Account Type Selection
        frame_type = ctk.CTkFrame(self, fg_color="transparent")
        frame_type.pack(pady=10)
        
        ctk.CTkLabel(
            frame_type,
            text="Account Type:",
            font=("Helvetica", 16),
            text_color=self.fg_color
        ).pack(side="left", padx=10)
        
        self.signup_type_var = ctk.StringVar(value="member")
        
        # Input Fields (scrollable)
        frame_scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        frame_scroll.pack(pady=10, padx=40, fill="both", expand=True)
        
        # Name
        ctk.CTkLabel(
            frame_scroll,
            text="Full Name:",
            font=("Helvetica", 16),
            text_color=self.fg_color
        ).pack(anchor="w", pady=(0, 8))
        
        self.signup_name = ctk.CTkEntry(
            frame_scroll,
            placeholder_text="Enter your full name",
            height=50,
            font=("Helvetica", 14),
            border_width=2,
            border_color=self.primary_color
        )
        self.signup_name.pack(pady=(0, 15), fill="x")
        
        # Email
        ctk.CTkLabel(
            frame_scroll,
            text="Email:",
            font=("Helvetica", 16),
            text_color=self.fg_color
        ).pack(anchor="w", pady=(0, 8))
        
        self.signup_email = ctk.CTkEntry(
            frame_scroll,
            placeholder_text="Enter your email",
            height=50,
            font=("Helvetica", 14),
            border_width=2,
            border_color=self.primary_color
        )
        self.signup_email.pack(pady=(0, 15), fill="x")
        
        # Member ID Label (for members only)
        self.member_id_label = ctk.CTkLabel(
            frame_scroll,
            text="Member/Student ID:",
            font=("Helvetica", 16),
            text_color=self.fg_color
        )
        self.member_id_label.pack(anchor="w", pady=(0, 8))
        
        # Member ID Entry
        self.signup_id = ctk.CTkEntry(
            frame_scroll,
            placeholder_text="e.g., STU001",
            height=50,
            font=("Helvetica", 14),
            border_width=2,
            border_color=self.primary_color
        )
        self.signup_id.pack(pady=(0, 15), fill="x")
        
        # Admin Password Label (for admin only)
        self.admin_password_label = ctk.CTkLabel(
            frame_scroll,
            text="Existing Admin Password:",
            font=("Helvetica", 16),
            text_color=self.fg_color
        )
        
        # Admin Password Entry (for admin only)
        self.admin_password_entry = ctk.CTkEntry(
            frame_scroll,
            placeholder_text="Enter existing admin password",
            height=50,
            font=("Helvetica", 14),
            show="●",
            border_width=2,
            border_color=self.primary_color
        )
        
        # Password
        ctk.CTkLabel(
            frame_scroll,
            text="Password:",
            font=("Helvetica", 16),
            text_color=self.fg_color
        ).pack(anchor="w", pady=(0, 8))
        
        self.signup_password = ctk.CTkEntry(
            frame_scroll,
            placeholder_text="Enter password",
            height=50,
            font=("Helvetica", 14),
            show="●",
            border_width=2,
            border_color=self.primary_color
        )
        self.signup_password.pack(pady=(0, 15), fill="x")
        
        # Confirm Password
        ctk.CTkLabel(
            frame_scroll,
            text="Confirm Password:",
            font=("Helvetica", 16),
            text_color=self.fg_color
        ).pack(anchor="w", pady=(0, 8))
        
        self.signup_confirm = ctk.CTkEntry(
            frame_scroll,
            placeholder_text="Confirm password",
            height=50,
            font=("Helvetica", 14),
            show="●",
            border_width=2,
            border_color=self.primary_color
        )
        self.signup_confirm.pack(pady=(0, 15), fill="x")
        
        def on_type_change():
            """Update form when account type changes"""
            account_type = self.signup_type_var.get()
            if account_type == "admin":
                # Hide member ID fields, show admin password field
                self.member_id_label.pack_forget()
                self.signup_id.pack_forget()
                self.admin_password_label.pack(anchor="w", pady=(0, 8))
                self.admin_password_entry.pack(pady=(0, 15), fill="x")
            else:
                # Show member ID fields, hide admin password field
                self.admin_password_label.pack_forget()
                self.admin_password_entry.pack_forget()
                self.member_id_label.pack(anchor="w", pady=(0, 8))
                self.signup_id.pack(pady=(0, 15), fill="x")
        
        ctk.CTkRadioButton(
            frame_type,
            text="👨‍💼 Admin",
            variable=self.signup_type_var,
            value="admin",
            font=("Helvetica", 14),
            command=on_type_change
        ).pack(side="left", padx=5)
        
        ctk.CTkRadioButton(
            frame_type,
            text="👤 Member",
            variable=self.signup_type_var,
            value="member",
            font=("Helvetica", 14),
            command=on_type_change
        ).pack(side="left", padx=5)
        
        # Buttons
        frame_buttons = ctk.CTkFrame(frame_scroll, fg_color="transparent")
        frame_buttons.pack(fill="x", pady=10)
        
        ctk.CTkButton(
            frame_buttons,
            text="Create Account",
            font=("Helvetica", 14, "bold"),
            height=50,
            command=self.handle_signup,
            fg_color="#28a745",
            hover_color="#218838"
        ).pack(fill="x", pady=8)
        
        ctk.CTkButton(
            frame_buttons,
            text="Back to Login",
            font=("Helvetica", 14, "bold"),
            height=50,
            command=self.show_login_screen,
            fg_color="#6c757d",
            hover_color="#5a6268"
        ).pack(side="left", padx=5, fill="x", expand=True)
        
        # Status Label
        self.status_label = ctk.CTkLabel(
            self,
            text="",
            font=("Helvetica", 10),
            text_color=self.danger_color
        )
        self.status_label.pack(pady=10)
    
    def handle_login(self):
        """Login"""
        email = self.login_email.get().strip()
        password = self.login_password.get()
        user_type = self.login_type_var.get()
        
        if not email or not password:
            self.show_status("❌ Fill all fields!", "error")
            return
        
        if user_type == "admin":
            # Admin login
            user = DataHandler.get_admin(email, password)
            if user:
                self.current_user = user
                self.user_type = "admin"
                self.show_status("✅ Admin login successful!", "success")
                self.after(500, self.go_to_admin_dashboard)
            else:
                self.show_status("❌ Invalid email or password!", "error")
        else:
            # Member login
            user = DataHandler.get_member(email, password)
            if user:
                self.current_user = user
                self.user_type = "member"
                self.show_status("✅ Login successful!", "success")
                self.after(500, self.go_to_member_dashboard)
            else:
                self.show_status("❌ Invalid email or password! Please check and try again.", "error")
    
    def handle_signup(self):
        """Sign up"""
        name = self.signup_name.get().strip()
        email = self.signup_email.get().strip()
        member_id = self.signup_id.get().strip()
        password = self.signup_password.get()
        confirm = self.signup_confirm.get()
        account_type = self.signup_type_var.get()
        
        # Validation
        if not all([name, email, password, confirm]):
            self.show_status("❌ Please fill all required fields!", "error")
            return
        
        # Email format validation
        if '@' not in email or '.' not in email:
            self.show_status("❌ Please enter a valid email address!", "error")
            return
        
        if account_type == "member" and not member_id:
            self.show_status("❌ Member ID is required for member accounts!", "error")
            return
        
        if account_type == "admin":
            # Verify existing admin password
            admin_password = self.admin_password_entry.get()
            if not admin_password:
                self.show_status("❌ Enter existing admin password!", "error")
                return
            
            # Check if password is correct by verifying with database
            if not DataHandler.verify_admin_password(admin_password):
                self.show_status("❌ Incorrect admin password! Cannot create new admin.", "error")
                return
        
        if password != confirm:
            self.show_status("❌ Passwords don't match!", "error")
            return
        
        if len(password) < 4:
            self.show_status("❌ Password must be at least 4 characters!", "error")
            return
        
        if account_type == "admin":
            # Admin signup
            if DataHandler.admin_exists(email):
                self.show_status("❌ This email is already registered as admin!", "error")
                return
            
            admin_data = {
                'name': name,
                'email': email,
                'password': password,
                'role': 'admin'
            }
            
            success, message = DataHandler.add_admin(admin_data)
            if success:
                self.show_status(f"✅ {message} Now login", "success")
                self.after(1000, self.show_login_screen)
            else:
                self.show_status(f"❌ {message}", "error")
        else:
            # Member signup
            if DataHandler.member_exists(email):
                self.show_status("❌ This email is already registered. Please use a different email.", "error")
                return
            
            member_data = {
                'name': name,
                'email': email,
                'member_id': member_id,
                'password': password,
                'phone': '',
                'address': '',
                'status': 'active'
            }
            
            success, message = DataHandler.register_member(member_data)
            if success:
                self.show_status(f"✅ {message} Now login", "success")
                self.after(1000, self.show_login_screen)
            else:
                self.show_status(f"❌ {message}", "error")
    
    def show_status(self, message: str, status_type: str = "info"):
        """Show status message"""
        color = "#dc3545" if status_type == "error" else "#28a745"
        if hasattr(self, 'status_label'):
            self.status_label.configure(text=message, text_color=color)
    
    def go_to_admin_dashboard(self):
        """Go to admin dashboard"""
        from admin_dashboard import AdminDashboard
        self.destroy()
        app = AdminDashboard(self.current_user)
        app.mainloop()
    
    def go_to_member_dashboard(self):
        """Go to member dashboard"""
        from member_dashboard import MemberDashboard
        self.destroy()
        app = MemberDashboard(self.current_user)
        app.mainloop()


if __name__ == "__main__":
    app = AuthWindow()
    app.mainloop()
