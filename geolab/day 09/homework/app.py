from flask import Flask , render_template
app = Flask(__name__)

profiles = [
    {'name':'tungtung',    'surname':'sahur',      'image':'download1.jpg',       'username':'sahuuurr'},
    {'name':'balerina',    'surname':'capuchina',  'image':'download (2).jpg',    'username':'balerina777'},
    {'name':'lirili',      'surname':'larila',     'image':'images.jpg',          'username':'lirili_larilashvili'},
    {'name':'bombordiro',  'surname':'crocodilo',  'image':'download.jpg',        'username':'b0mbord1lo'}
   ]

@app.route("/")
def home():
    return render_template('home.html' ,profiles = profiles)

@app.route('/profile/<username>')
def profile(username):
    if username == 'sahuuurr':
        return render_template('profile.html',profiles = profiles[0])
    elif username == 'balerina777':
        return render_template('profile.html',profiles = profiles[1])
    elif username == 'lirili_larilashvili':
        return render_template('profile.html',profiles = profiles[2])
    elif username == 'b0mbord1lo':
        return render_template('profile.html',profiles = profiles[3])





@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/FAQs")
def FAQ():
    return render_template('FAQs.html')

@app.route("/about")
def About():
    return render_template('about.html')




if __name__ =="__main__":

    app.run(debug=True)