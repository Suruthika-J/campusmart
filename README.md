CampusMart : 
CampusMart is a Django-based marketplace platform designed for students.
It allows users to list items, search & filter products, chat with sellers, and track transactions in a simple and collaborative way.
Tech Stack : 
Backend: Django (Python)
Frontend: Django Templates (HTML, CSS)
Database: SQLite (default) 
Authentication: Django’s built-in User model
Version Control: Git & GitHub (collaborative workflow)

Team Members & Responsibilities

Member 1: Item Listing & Management
Created Item model
Implemented add/edit/delete item functionality
Built item dashboard for sellers

Member 2: Search & Filtering System
Implemented search by name & description
Added filtering by category
Designed search results template

Member 3: Chat & Transaction Tracking
Built chat system between buyers & sellers
Implemented purchase flow (transaction tracking)
Added templates for chat & purchase confirmation


-----------------------------------------------------------------------------
Setup Instructions
1. Clone the Repository
git clone https://github.com/<your-org-or-username>/campusmart.git
cd campusmart

2. Setup Virtual Environment
python -m venv env-site
env-site\Scripts\activate   # On Windows
source env-site/bin/activate   # On Linux/Mac

3. Install Dependencies 
pip install  pillow
pip install channels 


4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Run the Server
python manage.py runserver


Now open http://localhost:8000


Setup Instructions for Admin Dashboard 

1. Create a Superuser
Run the following command to create an admin account:
python manage.py createsuperuser
--
You will be asked for:
Username
Email address
Password
Then visit admin dashboard 
http://127.0.0.1:8000/admin

Admin Views Available
🔹 User Management
Manage registered users.
Reset passwords or deactivate accounts.
Useful for moderating the platform.

🔹 Item Management
Add new items (name, description, category, price, image).
Edit or delete existing items.
Monitor the marketplace inventory.

🔹 Search & Filter Logs (optional if enabled)
Track recent search queries by users.
Useful for analytics (what students are searching for most).
Helps in improving recommendations.

🔹 Chat Management
View chat messages between buyers and sellers.
Useful for moderation and resolving disputes.
Each record includes: sender, receiver, message content, timestamp.

🔹 Transaction Management
Monitor all purchases made on the platform.
Fields include: buyer, item, quantity, total price, timestamp.
Helps maintain accountability in trades.
