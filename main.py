from flask import Flask, render_template
import requests
app = Flask(__name__)


posts = requests.get("https://api.npoint.io/9260e848de41c3dd6999").json()
post_objects = []
for post in posts:
    post_objects.append(post)

    
@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)


