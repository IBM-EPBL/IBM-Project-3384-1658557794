from flask import *
import sys

app=Flask(__name__)
app.secret_key="123"

class User:
    def __init__(self,username,password):
        
        self.username=username
        self.password=password


users=[]
users.append(User(username="anusudha",password="anu160@"))
users.append(User(username="jeeva",password="jeeva21@"))
users.append(User(username="sopitha",password="sobi@14"))
users.append(User(username="kaviya",password="kaviya03@"))

@app.route("/dashboard",methods=['GET','POST'])
def dashboard():
    if request.method =='POST':
        uname=request.form.get['uname']
        upass = request.form.get['upass']
        if users.username==uname and users.password==upass:
            return redirect(url_for('user'))
        else:
            flash("Username or Password Mismatch...!!!",'danger')
            return redirect(url_for('login'))
    return render_template("dashboard.html")
@app.route("/",methods=['GET','POST'])
def login():
    if request.method =='POST':
        uname=request.form['uname']
        upass = request.form['upass']
        for data in users:
            if data.username==uname and data.password==upass:
                return redirect("/dashboard")
        else:
            flash("Username or Password Mismatch...!!!",'danger')
            return redirect("/")
        
           
            
    return render_template("index1.html")

@app.route("/donate-plasma",methods=['GET','POST'])
def donateplasma():
    if request.method=='POST':
        iname = request.form.get("inputName")
        # umail = request.form.get("inputEmail")
        # ucontact = request.form.get("inputcontact")
        # udob = request.form.get("inputDoB")
        # ugender = request.form.get("gender")
        # ucity = request.form.get("inputCity")
        # ustate = request.form.get("inputState")
        # upin = request.form.get("inputZip")
        print(iname,file=sys.stdout)
    return render_template("donor_details.html")
@app.route("/plasma-req",methods=['GET','POST'])
def plasmarequest():
    if request.method=='POST':
        uname=request.form['uname']
        upass = request.form['upass']

        for data in users:
            if data.username==uname and data.password==upass:
                session['userid']=data.id
                g.record=1
                return redirect(url_for('/'))
            else:
                g.record=0
        if g.record!=1:
            flash("Username or Password Mismatch...!!!",'danger')
            return redirect(url_for('login'))
    return render_template("plasma_request.html")

@app.route("/home",methods=['GET','POST'])
def home():
    if request.method=='POST':
        uname=request.form['uname']
        upass = request.form['upass']

        for data in users:
            if data.username==uname and data.password==upass:
                session['userid']=data.id
                g.record=1
                return redirect(url_for('/'))
            else:
                g.record=0
        if g.record!=1:
            flash("Username or Password Mismatch...!!!",'danger')
            return redirect(url_for('login'))
    return render_template("home.html")
@app.route("/about",methods=['GET','POST'])
def about():
    if request.method=='POST':
        uname=request.form['uname']
        upass = request.form['upass']

        for data in users:
            if data.username==uname and data.password==upass:
                session['userid']=data.id
                g.record=1
                return redirect(url_for('/'))
            else:
                g.record=0
        if g.record!=1:
            flash("Username or Password Mismatch...!!!",'danger')
            return redirect(url_for('login'))
    return render_template("about.html")
@app.route("/register",methods=['GET','POST'])
def register():
    if request.method=='POST':
        uname=request.form['uname']
        upass = request.form['upass']

        for data in users:
            if data.username==uname and data.password==upass:
                session['userid']=data.id
                g.record=1
                return redirect(url_for('/'))
            else:
                g.record=0
        if g.record!=1:
            flash("Username or Password Mismatch...!!!",'danger')
            return redirect(url_for('login'))
    return render_template("Registration.html")

@app.before_request
def before_request():
    if 'userid' in session:
        for data in users:
            if data.id==session['userid']:
                g.user=data

@app.route('/user')
def user():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('index1.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)
