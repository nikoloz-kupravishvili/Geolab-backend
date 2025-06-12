from flask import Flask ,render_template

app = Flask(__name__)

profiles = [
    {'name':'nickeyyyyyyyyyyyy', 'age':13}
]


@app.route("/")

def home():
    return render_template('index.html')



@app.route("/sign-up")
@app.route("/registeruser")
@app.route("/register")
@app.route("/signup")
def signup():
    return render_template('second.html')


@app.route("/profile/<int:profile_id>")
def profile(profile_id):
    if profile_id == 1:
        return render_template('profile.html' ,profiles_user = profiles)




if __name__ =="__main__":

    app.run(debug=True)




