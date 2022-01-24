from flask import json
from werkzeug.exceptions import HTTPException
from src.server.instance import server
from src.controllers.logs import createLog

app = server.app

#Criar objeto log para manipular as informações do log
logging = createLog()


@app.errorhandler(HTTPException)
def handleException(e):
    #Preenchendo o log
    logging.error(e.description)

    #Returna JSON ao invés de HTML para erros HTTP
    response = e.get_response()

    response = json.dumps({
        "error": {
            "reason": e.description,
        }
    })

    return response


def handleResponse(r):
    #Caso a resposta do servidor não seja 200 (OK) a razão do erro é retornada aqui.
    error = {
        "error": {
            "reason": r.reason
        }
    }
    return error
