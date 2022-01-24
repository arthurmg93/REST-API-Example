import requests

# Url do localhost onde o server ficará rodando
url = 'http://127.0.0.1:5000/'

#Usuário e Senha para fazer a requisição
User = 'frame'
Password = 'work'

#Extensão para a nossa lista
ext = 'lista'

# Comando 'get' na url do nosso servidor com a extensão da lista desejada
response = requests.get(url + ext, auth=(User, Password))

# Imprimir no prompt a lista que retornou
if response.status_code == 200:
    for i in response.json():
        print(i)

else:
    print(response.reason)
