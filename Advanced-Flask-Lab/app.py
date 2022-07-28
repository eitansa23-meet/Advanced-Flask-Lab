from flask import Flask, jsonify, request, render_template, url_for
import random
import requests, json

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Variables for tasks
image_link = "https://upload.wikimedia.org/wikipedia/commons/e/ee/Frank_Sinatra_in_1957.jpg"

user_bio = "Middle East Entrepreneurs of Tomorrow. Enabling the next generation of Israeli and Palestinian leaders."



#####


@app.route('/')  # '/' for the default pageima
def home():
    return render_template('index.html', image=image_link,user_bio=user_bio, 
posts = {
    "https://images.maariv.co.il/image/upload/f_auto,fl_lossy/c_fill,g_faces:center,h_750/569046": "2021 cohort's Y3 Accelerator!",
    "https://upload.wikimedia.org/wikipedia/he/thumb/0/08/%D7%9C%D7%99%D7%91%D7%99%D7%A0%D7%92_%D7%93%D7%94_%D7%93%D7%A8%D7%99%D7%9D_-_%D7%A0%D7%95%D7%A0%D7%95.webp/250px-%D7%9C%D7%99%D7%91%D7%99%D7%A0%D7%92_%D7%93%D7%94_%D7%93%D7%A8%D7%99%D7%9D_-_%D7%A0%D7%95%D7%A0%D7%95.webp.png": "MEET graduation!",
    "https://i.ytimg.com/vi/KEIlou1gTV4/maxresdefault.jpg": "#Throwback to one of our favorite #MEETsummer events: #BowlingNight!",
    "https://pbs.twimg.com/media/FI_UkcnVIAAUvWN?format=jpg&name=medium": "2020 cohort in their Y1 summer!"})


@app.route('/about')  # '/' for the default page
def about():
    return render_template('about.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
