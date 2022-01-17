
from flask import Flask, render_template
import requests
from post import Post

response = requests.get('https://api.npoint.io/0d32b200afaa3248c208').json()
all_posts = []
for post in response:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    all_posts.append(post_obj)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)


@app.route('/post/<int:post_id>')
def blog_post(post_id):
    requested_post = None
    for post in all_posts:
        if post.id == post_id:
            requested_post = post
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
