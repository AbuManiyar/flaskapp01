## Create a simple flask application

from flask import Flask,render_template,request,redirect,url_for

## create the flask app

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

## Assignemnt Try for loop( Done)

list_emp=[]
@app.route('/entries', methods=["GET", "POST"])
def entries():
    if request.method == "GET":
        return render_template("adder.html")
    else:
        name = request.form['Name']
        phone = request.form['Phone']
        position = request.form['Position']
        
        entry = {"name": name, "phone": phone, "position": position }
        list_emp.append(entry)
        return redirect(url_for('entries'))
    
    
@app.route('/display')
def display():
     l = len(list_emp)
     i = []
     for k in range(l): i.append(k+1)
     return render_template('display.html', emp = list_emp, lengthy= i)
    
if __name__=='__main__':
    app.run(debug=True)


