from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError    
from mensagens.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
   username = StringField('Nome do usuário', validators=[DataRequired()])
   email = StringField('e-mail', validators=[DataRequired(), Email()])
   senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
   confirmacao = PasswordField('Confirmação senha', validators=[DataRequired(), EqualTo('senha')]) 
   botao_submit_criarconta = SubmitField('Criar conta')

   def validate_email(self, email):
      usuario = Usuario.query.filter_by(email=email.data).first()
      if usuario:
         raise ValidationError('e-mail já cadastrado. Cadastre-se com outro e-mail ou faça login')

class FormLogin(FlaskForm):
   email = StringField('e-mail', validators=[DataRequired(), Email()])
   senha = PasswordField('Senha', validators=[DataRequired(),Length(6,20)])
   lembrarDados = BooleanField('Lembrar dados de acesso')
   botao_submit_login = SubmitField('Fazer login')

class FormEditarPerfil(FlaskForm):
   username = StringField('Nome do usuário', validators=[DataRequired()])
   email = StringField('e-mail', validators=[DataRequired(), Email()])
   foto_perfil = FileField('Atualizar foto perfil', validators=[FileAllowed(['jpg','png'])])
   curso_dotnet = BooleanField('.NET')
   curso_python = BooleanField('python')
   curso_go = BooleanField('Golang')
   botao_submit_editarperfil = SubmitField('Confirmar edição')

   def validate_email(self, email):
      if current_user.email != email.data:
         usuario = Usuario.query.filter_by(email=email.data).first()
         if usuario:
            raise ValidationError('Já existe um usuário com esse email. Cadastre outro email')