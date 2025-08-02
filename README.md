## 🔐 Google OAuth Login App (Flask + SQLAlchemy + OAuthlib)

A simple Flask app with Google Sign-In using OAuth 2.0. User information is stored in a MySQL database using SQLAlchemy ORM.

---

### 🚀 Features

* Google OAuth 2.0 Login
* Stores user profile info in a MySQL DB
* Flask + SQLAlchemy + Flask-Migrate
* Uses `.env` for secure configuration

---

## 📦 Tech Stack

* Python
* Flask
* Flask SQLAlchemy
* Authlib (OAuth)
* Flask-Migrate
* MySQL (via PyMySQL)
* dotenv

---

## 🔧 Setup Instructions

### 1. **Clone the Repository**

```bash
git clone https://github.com/Naveen131114/Google_Signin.git
```

---

### 2. **Create a Virtual Environment & Install Dependencies**

```bash
python -m venv venv
source venv/Scripts/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 3. **Create `.env` File**

```env
# .env
SECRET_KEY=your_secret_key
DATABASE_URL=mysql+pymysql://root:@localhost/google_signin
GOOGLE_OAUTH_CLIENT_ID=your_client_id.apps.googleusercontent.com
GOOGLE_OAUTH_CLIENT_SECRET=your_client_secret

FRONTEND_URL=your_frontend_url_for_after_login
```

---

### 4. **Set Up MySQL Database**

```sql
CREATE DATABASE google_signin;
```

---

### 5. **Configure Google OAuth Credentials**

#### 📌 Steps:

1. Go to: [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use an existing one)
3. Go to **APIs & Services > Credentials**
4. Click **+ Create Credentials > OAuth client ID**
5. Select **Web Application**
6. Add the following to **Authorized redirect URIs**:

```
http://localhost:5000/callback/google
```

7. Copy the generated **Client ID** and **Client Secret** to your `.env` file.

---

### 6. **Initialize the Database**

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

---

### 7. **Run the App**

```bash
python app.py  (or) flask run
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Example Output

* If **logged in**, you'll see:

  * Welcome message
  * Profile picture
  * Email
  * Logout button

* If **not logged in**, a "Login with Google" link will appear.

---

## 📁 File Structure

```
.
├── app.py
├── config.py
├── .env
├── requirements.txt
├── migrations/
└── README.md
```

---
