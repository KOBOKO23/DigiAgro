from flask import Flask, render_template, redirect, url_for, request, session
import mysql.connector
from werkzeug.security import check_password_hash

app = Flask(__name__)

# Secret key for session management (required for sessions)
app.secret_key = 'your_secret_key'  # You should change this to a strong secret key

# MySQL connection details
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',         # Host for the database (localhost in your case)
        port=3306,                # Default MySQL port
        user='root',              # Your MySQL username
        password='KphiL2022*',    # Your MySQL password
        database='digiagro'       # Your MySQL database name
    )
    return conn

# Root route (redirects to login or home depending on the session)
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect to login if the user is not logged in
    return redirect(url_for('home'))  # Redirect to home if the user is logged in

# Login route (renders the login template and handles login logic)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Connect to the MySQL database and check credentials
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()  # Get the first result
        
        # If user exists and password matches
        if user and check_password_hash(user['password'], password):
            # Create a session for the logged-in user
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            session['role'] = user['role']
            return redirect(url_for('home'))  # Redirect to home page after successful login
        else:
            return "Invalid credentials, please try again."
        
    return render_template('login.html')  # Render the login template if it's a GET request

# Home route (forms page, only accessible if the user is logged in)
@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect to login if the user is not logged in
    
    return render_template('home.html')  # Render the home template if the user is logged in

# Logout route (to clear the session and redirect to login)
@app.route('/logout')
def logout():
    session.clear()  # Clear session data
    return redirect(url_for('login'))  # Redirect to login page after logging out


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Running the app on port 5000
