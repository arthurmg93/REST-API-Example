from flask import Flask
from flask_restx import Api

#Função somente de armazenar as informações do nossa aplicação
class Server():
    #Inicialização da aplicação e API
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
                       version='1.0.0',
                       title='Framework Challenge REST API',
                       description='Desafio Técnico Framework',
                       doc='/docs'
                       )
    #Comando para executar a aplicação
    def run(self, ):
        self.app.run(debug=False)


#Instancia um objeto Server
server = Server()
