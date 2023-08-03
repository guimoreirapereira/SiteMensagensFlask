from mensagens import database,app
from mensagens.models import Usuario, Post


with app.app_context():
    database.drop_all()
    database.create_all()


#usuario = Usuario(username="Guilherme", senha="12456", email="guimoreirapereira@gmail.com")
#usuario2 = Usuario(username="João", senha="12456", email="jjjg@gmail.com")

#with app.app_context():
#    database.session.add(usuario)
#    database.session.add(usuario2)
#    database.session.commit()

#with app.app_context():
#    usuarios = Usuario.query.all()
#    usuario_filtrado = Usuario.query.filter_by(id=2).first()
#    print(usuario_filtrado)

#with app.app_context():
#    meu_post = Post(id_usuario=1,titulo='Post de teste',corpo='Maasssa Demais!!')
#    database.session.add(meu_post)
#    database.session.add(meu_post)
#    database.session.commit()

#with app.app_context():
#    posts = Post.query.all()
#    post = Post.query.first()
#    print(post.autor.email)