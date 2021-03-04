import os
from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
from werkzeug.utils import secure_filename
import json
import math

with open('config.json', 'r') as f:
    params = json.load(f)['params']

app = Flask(__name__)
print(app)
app.secret_key = "my-secret-key"

app.config["UPLOAD_FOLDER"] = params["upload_location"]

app.config.update(
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail_user'],
    MAIL_PASSWORD=params['gmail_pass']
)

mail = Mail(app)
is_local_server = params['is_local_server']

if is_local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_url']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_url']

db = SQLAlchemy(app)


@app.route("/", methods=['GET'])
def home():
    # Pagination Logic
    # Getting all posts
    posts = Post.query.order_by(Post.post_id.desc()).all()

    """Calculating no of pages
    len(posts) = 5
    params['no_of_posts'] = 2
    no_of_pages = 3"""
    no_of_pages = math.ceil(len(posts) / int(params['no_of_posts']))

    page = request.args.get('page')
    if not str(page).isnumeric():
        page = 1

    # Converting page into integer
    page = int(page)

    """Showing posts
    If on page 1: [0*2: 0*2+2] = [0:2]
    If on page 2: [1*2: 1*2+2] = [2:4]
    If on page 3: [2*2: 2*2+2] = [4:6] and likewise"""

    posts = posts[(page - 1) * int(params['no_of_posts']):(page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]

    # User can be on First Page
    if page == 1:
        prev = "#"
        next = "/?page=" + str(page + 1)

    # User can be on Last Page
    elif page == no_of_pages:
        prev = "/?page=" + str(page - 1)
        next = "#"

    # User can be on Middle Page
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)

    return render_template("index.html", params=params, posts=posts, prev=prev, next=next)


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if 'user' in session and session['user'] == params['admin_username']:
        posts = Post.query.all()
        return render_template('dashboard.html', params=params, posts=posts)

    if request.method == "POST":
        uname = request.form.get('uname')
        password = request.form.get('pass')

        if uname == params['admin_username'] and password == params['admin_password']:
            session['user'] = params['admin_username']
            posts = Post.query.all()
            return render_template('dashboard.html', params=params, posts=posts)
        else:
            flash("Incorrect username or password!", "danger")

    return render_template("login.html", params=params)


@app.route("/uploader", methods=['GET', 'POST'])
def uploader():
    if 'user' in session and session['user'] == params['admin_username']:
        if request.method == "POST":
            file = request.files['file1']
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(file.filename)))
            return "Uploaded Successfully!"


@app.route("/logout")
def logout():
    if 'user' in session and session['user'] == params['admin_username']:
        session.pop('user')
        flash("Logged Out Successfully!", "primary")
        return redirect('/dashboard')


@app.route("/delete/<string:post_id>", methods=['GET', 'POST'])
def delete(post_id):
    if 'user' in session and session['user'] == params['admin_username']:
        post = Post.query.filter_by(post_id=post_id).first()
        db.session.delete(post)
        db.session.commit()
        flash("Post Deleted Successfully!", "danger")
    return redirect('/dashboard')


@app.route("/edit/<string:post_id>", methods=['GET', 'POST'])
def edit(post_id):
    if 'user' in session and session['user'] == params['admin_username']:
        if request.method == "POST":
            title = request.form.get('title')
            s_title = request.form.get('s_title')
            slug = request.form.get('slug')
            author = request.form.get('author')
            # img = request.form.get('img')
            content = request.form.get('content')
            date = datetime.now()
            img_file = request.files['file1']
            img = img_file.filename
            if img == "":
                img = request.form.get('filename')
            img_file.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(img)))

            if post_id == '0':
                post = Post(post_title=title, post_subtitle=s_title, post_content=content, post_slug=slug,
                            post_author=author, post_img=img, post_date=date)
                db.session.add(post)
                db.session.commit()
                flash("Post Added Successfully!", "success")

            else:
                post = Post.query.filter_by(post_id=post_id).first()
                post.post_title = title
                post.post_subtitle = s_title
                post.post_content = content
                post.post_slug = slug
                post.post_author = author
                post.post_img = img
                post.post_date = date
                db.session.commit()
                flash("Post Updated Successfully!", "success")
                return redirect('/edit/' + post_id)
        post = Post.query.filter_by(post_id=post_id).first()
        return render_template("edit.html", params=params, post=post, post_id=post_id)
    # return render_template("login.html", params=params)


@app.route("/about")
def about():
    return render_template("about.html", params=params)


class Contact(db.Model):
    contact_id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String(50), nullable=True)
    contact_email = db.Column(db.String(100), nullable=True)
    contact_phone = db.Column(db.Integer, nullable=True)
    contact_message = db.Column(db.String(100), nullable=True)
    contact_date = db.Column(db.String(12), nullable=True)


class Post(db.Model):
    # 	post_id	post_title	post_content	post_slug	post_date	post_author	post_img
    post_id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(50), nullable=True)
    post_subtitle = db.Column(db.String(50), nullable=True)
    post_content = db.Column(db.String(1000), nullable=True)
    post_slug = db.Column(db.String(50), nullable=True)
    post_author = db.Column(db.String(50), nullable=True)
    post_img = db.Column(db.String(50), nullable=True)
    post_date = db.Column(db.String(12), nullable=True)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # getting data from the form
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # Passing data to Contact class
        entry = Contact(contact_name=name, contact_email=email, contact_phone=phone, contact_message=message,
                        contact_date=datetime.now())
        db.session.add(entry)
        # Committing changes
        db.session.commit()

        mail.send_message("New Message from " + name,
                          sender=email,
                          recipients=[params['gmail_user']],
                          body=message + "\nContact:" + phone)

        flash("Message Sent Successfully! We'll get back to you soon", "success")
    return render_template("contact.html", params=params)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post(post_slug):
    posts = Post.query.filter_by(post_slug=post_slug).first()
    return render_template("post.html", params=params, post=posts)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
