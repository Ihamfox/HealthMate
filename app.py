from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

# Configure application
app = Flask(__name__)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")

# the @login_required :
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# Here is Where The Good Stuff Starts :)
@app.route("/")
@login_required
def home():
    username = db.execute("SELECT username FROM users WHERE id = ?", session['user_id'])[0]['username']
    data1 = db.execute("SELECT * FROM user_bmi WHERE user_id = ?", session['user_id'])
    data2 = db.execute("SELECT * FROM user_bmr WHERE user_id = ?", session['user_id'])
    data3 = db.execute("SELECT * FROM user_weight WHERE user_id = ?", session['user_id'])
    return render_template("home.html",username=username,data1=data1,data2=data2,data3=data3)

@app.route("/bmisub",methods = ["GET","POST"])
@login_required
def bmisub():
    bmi = request.form.get("bmi")
    date = request.form.get("date")
    db.execute("INSERT INTO user_bmi (user_id , bmi , date) VALUES (? , ? , ?)", session['user_id'], bmi , date)
    return redirect("/")

@app.route("/bmrsub",methods = ["POST"])
@login_required
def bmrsub():
    bmr = request.form.get("bmr")
    date = request.form.get("date")
    db.execute("INSERT INTO user_bmr (user_id , bmr , date) VALUES (? , ? , ?)", session['user_id'], bmr , date)
    return redirect("/")

@app.route("/weightsub",methods = ["POST"])
@login_required
def weightsub():
    weight = request.form.get("weight")
    date = request.form.get("date")
    db.execute("INSERT INTO user_weight (user_id , weight , date) VALUES (? , ? , ?)", session['user_id'], weight , date)
    return redirect("/")
  

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    username = request.form.get("username")
    if not username :
         return render_template("register.html",error="Please provide a Username !")

    if db.execute("SELECT * FROM users WHERE username = ?",username):
        return render_template("register.html",error="Username already exists !")
    
    password = request.form.get("password")
    if not password :
        return render_template("register.html",error="Please provide a password !")
    
    confirmation = request.form.get("confirmation")
    if password != confirmation or not confirmation :
        return render_template("register.html",error="Invalid Password Confirmation !")
    
    passwordhash = generate_password_hash(password)
    db.execute("INSERT INTO users (username, hash) VALUES (?,?)",username,passwordhash)
    return redirect('/login')

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    username = request.form.get("username")
    rows = db.execute("SELECT * FROM users WHERE username = ?",username)
    if not username or not rows:
        return render_template("login.html",error="Invalid Username !")

    password = request.form.get("password")
    if not password or not check_password_hash(rows[0]['hash'],password):
        return render_template("login.html",error="Invalid Password !")
    
    session["user_id"] = rows[0]["id"]
    return redirect('/')
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/changepass",methods=["GET","POST"])
def changepass():
    if request.method == "GET" :
        return render_template("changepass.html")
    newpass = request.form.get("newpass")
    if not newpass :
        return render_template("changepass.html",error="Please provide a new password !")
    confirmation = request.form.get("confirmation")
    if not confirmation or confirmation != newpass :
        return render_template("changepass.html",error="Invalid Password Confirmation !")
    
    newpasshash = generate_password_hash(newpass)
    if (newpasshash == db.execute("SELECT * FROM users WHERE id= ?",session['user_id'])[0]['hash']):
        return render_template("changepass.html",error="Cannot use the same password as the one currently set to the account !")
    db.execute("UPDATE users SET hash = ? WHERE id = ?", newpasshash, session['user_id'])
    session.clear()
    return redirect("/login")

@app.route("/bmi", methods= ["GET","POST"])
@login_required
def bmi():
    if request.method == "GET" :
        return render_template("bmi.html")
    
    height = float(request.form.get("height"))
    weight = float(request.form.get("weight"))
    bmi = round((weight / (height * height)),2)
    if (bmi < 16):
        st = "Severely thin"
    elif (bmi >= 16 and bmi < 17):
        st = "Moderately thin"
    elif (bmi >= 17 and bmi < 18.5):
        st = "Mildly thin"
    elif (bmi >= 18.5 and bmi < 25):
        st = "Normal"
    elif (bmi >= 25 and bmi < 30):
        st = "Overweight"
    else :
        st = "Obese"
    tt = "Your BMI is : "
    status = "You are considered to be " + st + " as shown in the table below : "
    return render_template("bmi.html",tt=tt,urBMI=bmi,status=status)

@app.route("/bmr", methods = ["GET","POST"])
@login_required
def bmr():
    if request.method == "GET" :
        return render_template("bmr.html")
    
    age = int(request.form.get("age"))
    gender = request.form.get("gender")
    height = float(request.form.get("height"))
    weight = float(request.form.get("weight"))
    if (gender == "male"):
        bmr=round(88.362+(13.397 * weight)+(4.799 * height * 100) - (5.677 * age))
    else :
        bmr=round(447.593+(9.247 * weight)+(3.098 * height * 100) - (4.330 * age))
    
    tt = "Your BMR is : "
    status = str(bmr) + " Calories"
    nex = round(bmr * 1.2)
    oex = round(bmr * 1.375)
    fex = round(bmr * 1.55)
    dex = round(bmr * 1.725)
    return render_template("bmr.html",tt=tt,status=status,nex=nex,oex=oex,fex=fex,dex=dex)

@app.route("/macro",methods=["GET","POST"])
@login_required
def macro():
    if request.method == "GET":
        return render_template("macro.html")
    age = int(request.form.get("age"))
    gender = request.form.get("gender")
    height = float(request.form.get("height"))
    weight = float(request.form.get("weight"))
    if (gender == "male"):
        bmr=round(88.362+(13.397 * weight)+(4.799 * height * 100) - (5.677 * age))
    else :
        bmr=round(447.593+(9.247 * weight)+(3.098 * height * 100) - (4.330 * age))
    
    activity = request.form.get("activity")
    if activity == "nex":
        tdee = round(bmr*1.2)
    elif activity == "oex" :
        tdee = round(bmr*1.375)
    elif activity == "fex" :
        tdee = round(bmr*1.55)
    else:
        tdee = round(bmr*1.725)
    
    protein = round((tdee * 0.225)/4)
    carbs = round((tdee * 0.5)/4)
    fats = round((tdee * 0.275)/9)
    
    return render_template("macro.html",protein=protein,carbs=carbs,fats=fats)
