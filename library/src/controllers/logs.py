import logging
import datetime
import os



def createLog():
    #Verifica se a pasta 'logs' existe. Se não, cria uma nova.
    if not os.path.exists("logs/"):
        os.makedirs("logs/")
    d_inicio = str(datetime.datetime.now().date())
    log_name = f"logs/api_{d_inicio}.log"
    #Cria o objeto logging com o nome relacionado a uma data. Neste caso os logs serão acompanhados diariamente.
    #filemode a+ é usado para criar um arquivo log caso ele não exista. Caso contrário ele apenas abre e preenche a nova informação na última linha do mesmo.
    logging.basicConfig(filename=log_name, filemode='a+', level=logging.INFO)

    return logging

