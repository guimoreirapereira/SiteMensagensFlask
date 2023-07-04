from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo    

class FormCriarConta(FlaskForm):
   username = StringField('Nome do usuário', validators=[DataRequired()])
   email = StringField('e-mail', validators=[DataRequired(), Email()])
   senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
   confirmacao = PasswordField('Confirmação senha', validators=[DataRequired(), EqualTo('senha')]) 
   botao_submit_criarconta = SubmitField('Criar conta')

class FormLogin(FlaskForm):
   email = StringField('e-mail', validators=[DataRequired(), Email()])
   senha = PasswordField('Senha', validators=[DataRequired(),Length(6,20)])
   lembrarDados = BooleanField('Lembrar dados de acesso')
   botao_submit_login = SubmitField('Fazer login')