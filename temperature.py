from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    converted_t = None
    temp = None
    dest = None
    curr = request.form.get("rd")
    if request.method=="POST":
        temp = int(request.form["temp"])
        converted_t, curr, dest = conversion(temp, curr)
    return render_template("index.html", converted_t=converted_t, temp=temp, curr=curr, dest=dest)

@app.route('/')
def conversion(temp, curr):
    if curr == "F":
        converted_t = (temp-32)*0.5556
        dest = "C"
    else:
        converted_t = temp/0.5556 + 32
        curr = "C"
        dest = "F"
    return converted_t, curr, dest