from flask import Flask, render_template, request, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import redirect, url_for
from flask import session



app = Flask(__name__)
app.secret_key = 'my-secret_key'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:@localhost/madicare-network'

db = SQLAlchemy(app)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    message = db.Column(db.String(180), nullable=False)
    date = db.Column(db.String(14), nullable=True)

class Booking(db.Model):
      #  name drname number email address problem
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    doctor = db.Column(db.String(80), nullable=False)
    number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(180), nullable=False)
    problem = db.Column(db.String(180), nullable=False)
    date = db.Column(db.String(14), nullable=True)



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/department")
def department():
    return render_template('department.html')

@app.route("/blogs")
def blogs():
    return render_template('blogs/blogs.html')


@app.route("/review")
def review():
    return render_template('/index.html#review')








@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('name')
        password = request.form.get('password')
        user = Signup.query.filter_by(name=username, password=password).first()
        if user:
            session['user_id'] = user.name  # Store user's name in the session
            return redirect(url_for('home'))
        else:
            error_message = "Invalid username or password"
            return render_template('signup/login.html', error=error_message)
    return render_template('signup/login.html')



class Signup(db.Model):
    # sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),primary_key=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    number = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    date = db.Column(db.String(14), nullable=True)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
     if request.method == 'POST':
        try:
            name = request.form.get('name')
            password = request.form.get('password')
            number = request.form.get('number')
            email = request.form.get('email')
            entry = Signup(name=name, password=password, number=number, email=email, date=datetime.now())
            db.session.add(entry)
            db.session.commit()
        except Exception as e:
            # Handle the exception, print or log the error for debugging
            return f"An error occurred: {str(e)}"
        return redirect(url_for('home'))

     return render_template('signup/signup.html')


@app.route("/logout")
def logout():
    session.pop('user_id', None)  # Remove 'user_id' from the session
    return redirect(url_for('home'))  # Redirect to the desired page




@app.route("/booking", methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            doctor = request.form.get('doctor')
            number = request.form.get('number')
            email = request.form.get('email')
            address = request.form.get('address')
            problem = request.form.get('problem')
            entry = Booking(name=name, doctor=doctor, number=number, email=email, address=address, problem=problem, date=datetime.now())
            db.session.add(entry)
            db.session.commit()
        except Exception as e:
            # Handle the exception, print or log the error for debugging
            return f"An error occurred: {str(e)}"

        return render_template('booking.html')

    return render_template('booking.html')





@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')
            entry = Contact(name=name, email=email, message=message, date= datetime.now())
            db.session.add(entry)
            db.session.commit()
        except Exception as e:
            # Handle the exception, print or log the error for debugging
            return f"An error occurred: {str(e)}"
    return render_template('contact.html')





# @app.route("/profile")
# def profile():
#     if 'user_id' in session:
#         user = Signup.query.filter_by(name=session['user_id']).first()
#         return render_template('profile.html', user=user)
#     return redirect(url_for('login'))


# @app.route("/upload", methods=['POST'])
# def upload():
#     if 'user_id' in session:
#         user = Signup.query.filter_by(name=session['user_id']).first()
#         if 'profile_image' in request.files:
#             profile_image = request.files['profile_image']
#             # Save the image and update user's profile
#             if profile_image:
#                 image_path = save_image(profile_image)  # Implement a function to save the image
#                 user.profile_image_path = image_path
#                 db.session.commit()
#         return redirect(url_for('profile'))
#     return redirect(url_for('login'))



# @app.route("/edit_profile", methods=['GET', 'POST'])
# def edit_profile():
#     if 'user_id' in session:
#         user = Signup.query.filter_by(name=session['user_id']).first()
#         if request.method == 'POST':
#             new_name = request.form.get('new_name')
#             new_email = request.form.get('new_email')
#             # Update the user's profile data
#             user.name = new_name
#             user.email = new_email
#             db.session.commit()
#             return redirect(url_for('profile'))
#         return render_template('edit_profile.html', user=user)
#     return redirect(url_for('login'))




if __name__ == "__main__":
    # Create the database tables if they don't exist
    # db.create_all()
    app.run(debug=True)
