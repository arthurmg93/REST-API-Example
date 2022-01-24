
from flask_restx import  Resource
import requests
from src.controllers.logs import createLog
from src.controllers.errors import handleResponse
from src.controllers.basic_auth import verify, auth
from src.server.instance import server

app, api = server.app, server.api

#Criar objeto log para manipular as informações do log
logging = createLog()


class Lista(Resource):
    #Informando que é necessário fazer autenticação para retornar a resposta da requisição.
    @auth.login_required

    #Sobrescrevendo o método GET para que ele faça além do retorno
    def get(self, ):
        #Requisição inicial na lista no endpoint informado
        raw_list = requests.get('https://jsonplaceholder.typicode.com/todos')

        #Preenchendo o log
        logging.info(raw_list.url)

        #Se a resposta da requisição for diferente de 200 (OK) será tratado através da função handleResponse
        if(raw_list.status_code != 200):
            logging.error(raw_list.url)
            return handleResponse(raw_list)
        else:
            #Recebe a lista 'bruta' e converte para json e limita para os 5 primeiros itens.
            raw_list_json = raw_list.json()[0:5]

            #Edita os itens recebidos de acordo com as informações solicitadas
            filtered_list = []
            for r in raw_list_json:
                filtered_list.append(
                    {
                        'id': r['id'],
                        'title': r['title']
                    }
                )

            return(filtered_list)

#Inclui na API a rota da classe Lista
api.add_resource(Lista, '/lista')
