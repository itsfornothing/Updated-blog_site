from flask import Flask, render_template, request
import requests
import smtplib
import os


my_gmail = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")
response = requests.get(os.getenv("API_ENDPOINT"))
my_blog = response.json()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', blogs=my_blog)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html', h1="Contact Me")


@app.route("/post/<int:index>")
def post(index):
    for blog in my_blog:
        if blog["id"] == index:
            return render_template('post.html', blog=blog)


@app.route("/contact", methods=["POST"])
def form_entry():
    if request.method == "POST":
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=password)
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["phone"]
            message = request.form["message"]
            connection.sendmail(from_addr=my_gmail,
                                to_addrs="halidmohamed807@gmail.com",
                                msg=f"Subject:New Message:\n\n"
                                    f"Name: {name}\n"
                                    f"Email: {email}\n"
                                    f"Phone: {phone}\n"
                                    f"Message: {message}")
        return render_template('contact.html', h1="Successfully Sent Your Message.")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
