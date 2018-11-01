from flask import Flask, render_template, request, redirect, url_for
from models import *


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True



@app.route('/')
def hello_world():
    return render_template('login.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
    #traer info ingresada
        usuario= str(request.form['usuario'])
        contra = str(request.form['contra'])
        registro = TUsuario.query.filter(TUsuario.username==usuario).first()
        if registro is None:
                return "El usuario no existe"
        else:
            if registro.hash_password != contra:
                return "La contraseña es incorrecta"
            else:
                tipos = TTipoUsuario.query.all()
                return render_template('blank.html', usuario=registro, tipos = tipos)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        tipos = TTipoUsuario.query.all()
        return render_template('register.html', tipos=tipos)
    if request.method == 'POST':
        usuario = TUsuario()
        usuario.username = str(request.form['username'])
        usuario.nombres = str(request.form['nombres'])
        usuario.apellidos = str(request.form['apellidos'])
        usuario.hash_password = str(request.form['contraseña'])

@app.route('/logout',methods=['GET'])
def logout():
    return redirect(url_for('hello_world'))

@app.route('/forgot-password', methods=['GET','POST'])
def forgot():
    if request.method=='GET':
       return render_template('forgot-password.html')
    if request.method=='POST':
    #traer info ingresada
        usuario= request.form['usuario']
        contra = request.form['contra']
        return render_template('forgot-password.html', usuario=usuario)

if __name__ == '__main__':
    app.run()
