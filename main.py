from flask import Flask, render_template, request
import requests
import smtplib
import os
app = Flask(__name__)
OWN_EMAIL = "misslynnemunini@gmail.com"
OWN_PASSWORD = "@26041978"

posts = requests.get("https://api.npoint.io/9260e848de41c3dd6999").json()
blog_allposts = ["What we commonly refer to as thorns in the cactus are actually spines: real organs of the plant, namely leaves. At least that’s how it used to be.In the course of evolution, spines have developed from this, which ensure the cacti survival even under the most extreme living conditions. At least their spines. The largest specimens were previously used as gramophone needles. In their barren habitats, cacti would literally be found food for animals. Their spines prevent this. But they can do a lot more: They reflect sunlight and thus protect the plant from sunburn. On the other hand, they keep out the cold on icy nights. Clouds of mist condense on the spines to form water, which the cactus can then absorb. They also get caught in the fur of animals that pass by. Elsewhere they fall out, and a new cactus can grow. So they also help with the propagation.",
"Start watching a new reality series. Watch a classic movie you’ve never seen. Search “happy birthday + [your name]” on YouTube. Make a playlist of your favorite songs from high school.  Read some humor writing. Put together a puzzle. Give yourself a manicure and pedicure. Lie down, close your eyes, and listen to a podcast. Make a fancy cocktail or mocktail. Write a song. Soak some dry beans. There are no doubt tons of files clogging up your computer that you downloaded a long time ago and have absolutely no use for. Delete them and free up some space for more stuff you don’t need later. Are you thinking about getting a tattoo? Why not one that you’ve designed? Draw some stuff, play around, imagine where it could be inked permanently into your flesh. As a kid, there was absolutely nothing more exciting than the idea of getting a letter in the mail from a pen pal. Why do we let time change us? Why do we let age rob us of our youthful sense of wonder? Send a letter to a friend. Maybe they’ll write back! Write a poem. No one ever has to read it.  Apply a soothing face mask. Your skin deserves it.",
"Intermittent fasting (IF) is an eating pattern that cycles between periods of fasting and eating. It’s currently very popular in the health and fitness community. There are several different ways of doing intermittent fasting — all of which involve splitting the day or week into eating and fasting periods. During the fasting periods, you eat either very little or nothing at all. When you fast, human growth hormone levels go up and insulin levels go down. Your body’s cells also change the expression of genes and initiate important cellular repair processes."]
post_objects = []
for post in posts:
    post_objects.append(post)

value = 0

for data in post_objects:
    data["body"] = blog_allposts[value] 
    value += 1
     
@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:Message from Blog\n\nName: {name}\n\nEmail: {email}\n\nPhone: {phone}\n\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, "muninilynne65@gmail.com", email_message)


if __name__ == "__main__":
    app.run(debug=True)
