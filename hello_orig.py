from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired 

#Create a Flask Instance
# app = Flask(__name__)
# app.config["SECRET_KEY"] = "my super secret key that nobody knows "

# Create a Form Class
# class NamerForm(FlaskForm):
# 	name = StringField ("Enter your name", validators=[DataRequired()])
# 	submit = SubmitField("Submit")

#Create a route decorator, the initial landing page
# @app.route("/")
 
#def index():
#	return "<h1>Hello World!<h1>"

def index():
	first_name = "Eamonn"
	stuff = "This is bold text"

	favourite_pizza = ["Peperoni", "Cheese", "Mushrooms", 41 ]
	return render_template("index.html", 
		first_name = first_name,
		stuff = stuff,
		favourite_pizza = favourite_pizza)

# localhost:5000/user/john
# @app.route("/user/<name>")

#def user (name):
#	return "<h1>Hello {}! </h1>".format(name)

# def user(name):
# 	return render_template("user.html", user_name = name)

# Create Custom Error Pages

# Invalid URL
# @app.errorhandler(404)
# def page_not_found(e):
# 	return render_template("404.html"), 404

	# Internal Server Error
# @app.errorhandler(500)
# def page_not_found(e):
# 	return render_template("500.html"), 500

# Createname page
# @app.route("/name", methods=["GET", "POST"])
# def name():
# 	name = None
# 	form = NamerForm()
	#Validate Form 
	#if form.validate_on_submit():
	#	name = form.name.data
	#	form.name.data = ""
	#return render_template("name.html", name = name, form = form)

