from flask import Blueprint, render_template, request, flash, redirect, url_for
from database import Post, db

views = Blueprint('views', __name__)

@views.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        try:
            db.session.add(Post(data=request.form.to_dict()))
            db.session.commit()
            flash('Record successfully created.', category='success')
        except:
            flash('Oh no, something went wrong.', category='error')

    return render_template('pages/form.html')


@views.route('/data', methods=['GET'])
def data():  
    posts = Post.query.all()
    return render_template('pages/data.html', posts=posts)