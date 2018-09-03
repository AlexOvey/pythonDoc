import os 
import secrets 
from PiL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db, bcrypt, mail
from flaskblog.forms import (registrationForm, LoginForm, 
							UpdateAccountForm,PostForm, requestResetForm, ResetPassword Form)
from flaskblog.models import User, PostForm
from flask_login import Login_user, logout_user, login_reques
from flask_mail import message

@app.route("/")
@ap.route("/home")
def home():
	page = request.args.get("page", 1, type =int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page)
	return render_template('home.html', posts=posts)

	@app.route("/about")
