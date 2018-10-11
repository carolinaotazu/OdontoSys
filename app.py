from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        usuario = request.form['usuario']
        contra = request.form['contra']
        return 'Hola ' + usuario + ', tu contraseña es: ' + contra

if __name__ == '__main__':
    app.run()
