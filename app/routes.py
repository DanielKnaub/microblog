from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Daniil'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body':'The Avengers mvie was so cool!'
        },
        {
            'author': {'username': 'Ippolit'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

