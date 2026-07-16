"""
Library Management System - Main Entry Point
"""

from data_handler import DataHandler
from auth import AuthWindow


def main():
    """Initialize and start the system"""
    # Initialize data files
    DataHandler.initialize()
    
    print("=" * 50)
    print("🎓 LIBRARY MANAGEMENT SYSTEM 🎓")
    print("=" * 50)
    print("\n✅ System initialized successfully!")
    print("📁 Data files created in 'data' folder")
    print("🚀 Opening GUI...\n")
    print("=" * 50)
    
    # Launch GUI
    app = AuthWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
