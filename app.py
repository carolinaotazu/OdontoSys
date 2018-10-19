from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('login.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
    #traer info ingresada
        usuario= request.form['usuario']
        contra = request.form['contra']
        return render_template('blank.html', usuario=usuario)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template('register.html')

@app.route('/logout',methods=['GET'])
def logout():
    return redirect(url_for('hello_world'))

@app.route('/forgot-password', methods=['GET','POST'])
def forgot():
    if request.method=='GET':
       return render_template('forgot-password.html')
    #if request.method=='POST':
    #traer info ingresada
    #    usuario= request.form['usuario']
    #    contra = request.form['contra']
    #    return render_template('forgot-password.html', usuario=usuario)

if __name__ == '__main__':
    app.run()
