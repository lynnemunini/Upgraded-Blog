from flask import Flask, render_template, request
import requests
import smtplib
app = Flask(__name__)
my_email = "misslynnemunini@gmail.com"
password = "@26041978"

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="muninilynne65@gmail.com",
                                msg=f"Subject:Message from Blog\n\n{name}\n\n{email}\n\n{phone}\n\n{message}")
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)


