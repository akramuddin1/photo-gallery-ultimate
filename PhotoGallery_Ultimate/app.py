import os, sqlite3
from flask import Flask, render_template, request, redirect, session, flash, send_from_directory, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
ALLOWED = {"png","jpg","jpeg"}

app = Flask(__name__)
app.secret_key = "change-this-secret"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH, check_same_thread=False)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db:
        if exception:
            db.rollback()
        else:
            db.commit()
        db.close()

def init_db():
    db = sqlite3.connect(DB_PATH)
    db.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password_hash TEXT,
        created_at TEXT
    )""")
    db.execute("""CREATE TABLE IF NOT EXISTS photos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        filename TEXT,
        uploaded_at TEXT
    )""")
    db.commit()
    db.close()

def allowed(name):
    return "." in name and name.rsplit(".",1)[1].lower() in ALLOWED

@app.route("/", methods=["GET","POST"])
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        user = get_db().execute("SELECT * FROM users WHERE username=?",(request.form["username"],)).fetchone()
        if user and check_password_hash(user["password_hash"], request.form["password"]):
            session["user_id"]=user["id"]
            session["username"]=user["username"]
            return redirect("/gallery")
        flash("Invalid credentials")
    return render_template("login.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method=="POST":
        try:
            get_db().execute(
                "INSERT INTO users(username,password_hash,created_at) VALUES(?,?,?)",
                (request.form["username"], generate_password_hash(request.form["password"]), datetime.utcnow().isoformat())
            )
            flash("Account created. Login now.")
            return redirect("/login")
        except sqlite3.IntegrityError:
            flash("Username already exists")
    return render_template("signup.html")

@app.route("/gallery")
def gallery():
    if "user_id" not in session:
        return redirect("/login")
    photos = get_db().execute(
        "SELECT * FROM photos WHERE user_id=? ORDER BY uploaded_at DESC",
        (session["user_id"],)
    ).fetchall()
    return render_template("gallery.html", photos=photos)

@app.route("/upload", methods=["POST"])
def upload():
    if "user_id" not in session:
        return redirect("/login")
    files = request.files.getlist("photos")
    for f in files:
        if f and allowed(f.filename):
            name = f"{session['user_id']}_{int(datetime.utcnow().timestamp())}_{secure_filename(f.filename)}"
            f.save(os.path.join(UPLOAD_FOLDER,name))
            get_db().execute(
                "INSERT INTO photos(user_id,filename,uploaded_at) VALUES(?,?,?)",
                (session["user_id"], name, datetime.utcnow().isoformat())
            )
    return redirect("/gallery")

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    p = get_db().execute("SELECT * FROM photos WHERE id=? AND user_id=?",(id,session.get("user_id"))).fetchone()
    if p:
        path = os.path.join(UPLOAD_FOLDER,p["filename"])
        if os.path.exists(path): os.remove(path)
        get_db().execute("DELETE FROM photos WHERE id=?",(id,))
    return redirect("/gallery")

@app.route("/uploads/<name>")
def uploads(name):
    return send_from_directory(UPLOAD_FOLDER,name)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__=="__main__":
    init_db()
    app.run(debug=True)