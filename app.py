import os
from flask import Flask, request, render_template, redirect, url_for, flash, session
from lib.database_connection import get_flask_database_connection
from lib.listing_repository import ListingRepository 
from lib.listing import Listing
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from lib.email_validator import email_is_valid
from lib.validator import password_is_valid
from lib.user_repository import UserRepository
from lib.user import User
import bcrypt

# Create a new Flask app
app = Flask(__name__, static_folder='static')
app.secret_key = 'your_secret_key'
# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/home')
def get_home():
    return render_template('home.html')

@app.route('/login')
def get_login():
    return render_template('login.html')

@app.route('/signup')
def get_signup():
    return render_template('signup.html')

@app.route('/listings', methods=['GET'])
def get_all_listings():
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)
    listings = repository.all_listings()
    return render_template('listings.html', listings=listings)

@app.route('/find/<int:listing_id>', methods=['GET'])
def find_listing_by_id(listing_id):
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)
    listing = repository.find_by_id(listing_id) 
    return render_template('listing.html', listing=listing)

@app.route('/new-listing')
def get_to_new_listing():
        return render_template('newlisting.html')

@app.route('/create-listing', methods=['POST'])
def create_listing():
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        image = request.files['image']
        user_id = session['user_id']
        if image:
            filename = secure_filename(image.filename)
            upload_path = os.path.join(app.static_folder, 'uploads', filename)
            image.save(upload_path)
        else:
            filename = None
        connection = get_flask_database_connection(app)
        repository = ListingRepository(connection)
        listing = Listing(id=None, name=name, description=description, price=price, image=filename, user_id=user_id)
        repository.create_listing(listing)
        return redirect(url_for('get_all_listings'))

@app.route('/requests', methods=['GET'])
def get_requests():
    return render_template('requests.html')


@app.route('/listing/<int:listing_id>', methods=['GET'])
def show_listing_with_calendar(listing_id):
    connection = get_flask_database_connection(app)
    repo = ListingRepository(connection)
    listing = repo.find_by_id(listing_id)
    if not listing:
        flash("Listing not found.")
        return redirect('/listings')
    # Convert the disabled dates to strings for proper serialization
    disabled_dates = repo.get_booked_dates(listing_id)
    return render_template('listing.html', listing=listing, disabled_dates=disabled_dates)

@app.route('/book', methods=['POST'])
def book_listing():
    user_id = session['user_id']
    listing_id = int(request.form['listing_id'])
    date_range = request.form['date_range']
    try:
        start_str, end_str = date_range.split(" to ")
        start_date = datetime.strptime(start_str, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_str, "%Y-%m-%d").date()
    except ValueError:
        flash("Invalid date format.")
        return redirect(f"/listing/{listing_id}")
    repo = ListingRepository(get_flask_database_connection(app))
    if not repo.create_booking(listing_id, start_date, end_date, user_id):
        flash("Those dates are already booked.")
    else:
        flash("Booking successful!")
    return redirect(f"/listing/{listing_id}")


@app.route('/signup', methods=['POST'])
def signup():
    # Retrieve form data
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    if password != confirm_password:
        flash("Passwords do not match", "error")
        return redirect('/signup')
    if not email_is_valid(email):
        flash("Invalid email address", "error")
        return redirect('/signup')
    if not password_is_valid(password):
        flash("Password does not meet the required criteria", "error")
        return redirect('/signup')
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    user = User(id=None, name=name, email=email, password_hash=password, phone_number=phone)

    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    repo.create(user)
    flash("Account created successfully! Please log in.", "success")
    return redirect('/login')  # Redirect to login page after successful registration
    
    

def get_user_repository():
    connection = get_flask_database_connection(app)
    return UserRepository(connection)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Get the repository and try to find the user by email
        user_repository = get_user_repository()
        user = user_repository.find_by_email(email)

        if user is None:
            flash("User not found", "danger")
            return redirect(url_for('login'))

        # Check if the password matches the stored hash
        if bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
            # Password is correct, log the user in
            session['user_id'] = user.id
            session['username'] = user.name
            return redirect(url_for('get_all_listings'))  # Redirect to the listings page

        else:
            flash("Incorrect password", "danger")
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()  # Clear the session
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

@app.route('/my-listings')
def my_listings():
    if 'user_id' not in session:
        return redirect('/login')  # ensure the user is logged in

    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)

    # Only fetch listings created by the logged-in user
    user_id = session['user_id']
    listings = repository.find_by_user_id(user_id)

    return render_template('view_user_listings.html', listings=listings)

@app.route('/delete-listing/<int:id>', methods=['POST'])
def delete_listing(id):
    if 'user_id' not in session:
        return redirect('/login')  # Ensure the user is logged in

    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)

    listing = repository.find_by_id(id)

    if listing and listing.user_id == session['user_id']:
        repository.delete_listing(id)  # Only delete if the listing belongs to the logged-in user

    return redirect('/my-listings')  # Redirect back to the user's listings page





# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
