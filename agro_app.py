from flask import Flask, render_template, redirect, url_for, request, session, flash
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key'  # Change this to a strong secret key

# MySQL connection details
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='KphiL2022*',
        database='digiagro'
    )
    return conn

# Root route (redirects to login or home depending on the session)
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('home'))

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)  # Hash the password

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_password))
            conn.commit()
            flash("Registration successful! Please log in.", "success")  # Flash success message
        except mysql.connector.Error as err:
            flash(f"Error: {err}", "danger")  # Flash error message if registration fails
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('login'))  # Redirect to login page
    
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['user_id']
            session['email'] = user['email']
            session['role'] = user.get('role', 'user')
            flash("Login successful!", "success")  # Flash success message
            return redirect(url_for('home'))
        else:
            flash("Invalid credentials, please try again.", "danger")  # Flash error message
            return redirect(url_for('login'))  # Reload login page with message

    return render_template('login.html')

# Home route
@app.route('/home')
def home():
    if 'user_id' not in session:
        flash("Please log in to access this page.", "warning")
        return redirect(url_for('login'))
    
    return render_template('home.html')

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")  # Flash logout message
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

