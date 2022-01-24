from flask_httpauth import HTTPBasicAuth

#Instancia objeto HTTPBasciAuth para controlar as autenticações
auth = HTTPBasicAuth()

#Informações de usuários e senha 'mocados' para teste simples
USER_INFO ={
    'frame': 'work'
}

#Função de verificação dos dados de usuário e senha
@auth.verify_password
def verify(user,pw):
    if not(user and pw):
        return False
    return USER_INFO.get(user) == pw

