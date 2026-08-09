from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_textbox", methods=["GET","POST"])
def add_one_textbox():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into textbox (forme,ombre,user_id) values (:forme,:ombre,:user_id)",hey)
        user = query_db('select * from textbox')

        return render_template("textboxform.html", textboxs=user, one_user=one_user, the_title="add new textbox", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from textbox')
    one_user = query_db("select * from textbox limit 1", one=True)
    return render_template("textboxform.html", textboxs=user, one_user=one_user, the_title="add new textbox", touslesuser=touslesuser)

@app.route("/add_one_image", methods=["GET","POST"])
def add_one_image():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into image (forme,user_id) values (:forme,:user_id)",hey)
        user = query_db('select * from image')

        return render_template("imageform.html", images=user, one_user=one_user, the_title="add new image", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from image')
    one_user = query_db("select * from image limit 1", one=True)
    return render_template("imageform.html", images=user, one_user=one_user, the_title="add new image", touslesuser=touslesuser)

@app.route("/add_one_words", methods=["GET","POST"])
def add_one_words():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into words (content,user_id) values (:content,:user_id)",hey)
        user = query_db('select * from words')

        return render_template("wordsform.html", wordss=user, one_user=one_user, the_title="add new words", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from words')
    one_user = query_db("select * from words limit 1", one=True)
    return render_template("wordsform.html", wordss=user, one_user=one_user, the_title="add new words", touslesuser=touslesuser)

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,country_id,email,password,phone) values (:username,:country_id,:email,:password,:phone)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','country_id','email','password','phone']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','country_id','email','password','phone']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','country_id','email','password','phone']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_stuff", methods=["GET","POST"])
def add_one_stuff():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into stuff (name,color,form,size,user_id) values (:name,:color,:form,:size,:user_id)",hey)
        user = query_db('select * from stuff')

        return render_template("stuffform.html", stuffs=user, one_user=one_user, the_title="add new stuff", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from stuff')
    one_user = query_db("select * from stuff limit 1", one=True)
    return render_template("stuffform.html", stuffs=user, one_user=one_user, the_title="add new stuff", touslesuser=touslesuser)

@app.route("/add_one_picturetotext", methods=["GET","POST"])
def add_one_picturetotext():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into picturetotext (pic,description,user_id) values (:pic,:description,:user_id)",hey)
        user = query_db('select * from picturetotext')

        return render_template("picturetotextform.html", picturetotexts=user, one_user=one_user, the_title="add new picturetotext", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from picturetotext')
    one_user = query_db("select * from picturetotext limit 1", one=True)
    return render_template("picturetotextform.html", picturetotexts=user, one_user=one_user, the_title="add new picturetotext", touslesuser=touslesuser)

@app.route("/add_one_texttospeech", methods=["GET","POST"])
def add_one_texttospeech():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into texttospeech (text,speech) values (:text,:speech)",hey)
        user = query_db('select * from texttospeech')

        return render_template("texttospeechform.html", texttospeechs=user, one_user=one_user, the_title="add new texttospeech")


    user = query_db('select * from texttospeech')
    one_user = query_db("select * from texttospeech limit 1", one=True)
    return render_template("texttospeechform.html", texttospeechs=user, one_user=one_user, the_title="add new texttospeech")

