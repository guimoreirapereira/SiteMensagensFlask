from flask import Flask, render_template, url_for,request, flash, redirect
from markupsafe import escape
from forms import FormCriarConta,FormLogin
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
lista_usuarios = ['Rafaela', 'Guilherme','João Guilherme']
app.config['SECRET_KEY'] = 'c7ab768b15b0c003abdfdf4097eaf0fa'
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///mensagem.db'

database = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template('home.html') 

@app.route('/contato/')
def projects():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login',methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarConta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        #login valido
        flash(f'Login feito com sucesso para o email {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
    if form_criarConta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        flash(f'Conta criada para o email {form_criarConta.email.data}', 'alert-success')
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_criarConta=form_criarConta)

if __name__ == '__main__':
    app.run(debug=True)
   

#@app.route("/<name>")
#def hello(name):
#    return f"Hello, {escape(name)}!"

#@app.route('/user/<username>')
#def show_user_profile(username):
    # show the user profile for that user
#    return f'User {escape(username)}'

#@app.route('/post/<int:post_id>')
#def show_post(post_id):
    # show the post with the given id, the id is an integer
#    return f'Post {post_id}'

#@app.route('/path/<path:subpath>')
#def show_subpath(subpath):
    # show the subpath after /path/
#    return f'Subpath {escape(subpath)}'


