from flask import Blueprint, render_template
from .models import User, Post



blueprint = Blueprint('routes', __name__)



@blueprint.route('/')
def index():
  return render_template('index.html')

@blueprint.route('/contact')
def contact():
  return render_template('contact/contact.html')

@blueprint.route('/posts')
def posts():
  return render_template('posts/posts.html')