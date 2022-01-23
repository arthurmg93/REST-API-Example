# REST-API-Example

(PT-BR)
# Propósito
Aplicação criada para desafio técnico. Espero que, além disso, servir de orientação para quem desejar aprender a criar uma API REST utilizando o Mini Framework Flask.


# Descrição
Este projeto faz requisições em um endpoint que contém uma lista de itens para retornar os 5 primeiros itens da mesma. São feitos alguns tratamentos para caso o retorno não seja a lista em si ou o usuário utilize outro endpoit. As tecnologias utilizadas foram: o Flask por sua simplicidade, rapidez no desenvolvimento e velocidade; e biblioteca 'requests' para fazer requisições nos endpoints desejados.


# Processo de Instalação
Na página inicial do projeto haverá um arquivo chamado 'requeriments.txt', nele estarão contidas todas as bibliotecas necessárias para que tudo funcione de acordo. Baixe e coloque-o no diretório que desejar.
Para instalar os pacotes recomendo, inicialmente, que crie um ambiente virtual para rodar o projeto. Caso não saiba como criar um ambiente virtual, segue um guia explicando o processo: https://docs.python.org/pt-br/3/library/venv.html.
É necessário também que sua máquina tenha instalado o Python3 e o gerenciador de dependências pip (https://python.org.br/instalacao-windows/).

Feito isso, basta abrir o Prompt de Comando (Aperte Windows + X e em seguida C) e insira o comando: 'pip install -r /caminho/até/requirements.txt (onde o trecho '/caminho/até' é o endereço onde está localizado arquivo).

Por fim, basta baixar/clonar a pasta Library deste repositório e colocá-la junto com o ambiente virtual criado.


# Rodando e testando o projeto
Para rodar o projeto basta abrir o Prompt de Comando e ir até a pasta Library e executar o seguinte comando: python main.py ('python3 main.py' para usuários linux/mac).
Isto criará uma instância de servidor localizado no endereço 'http://127.0.0.1:5000'. E pronto, agora já podemos prosseguir com os testes.
Existem 3 formas de se testar o projeto:
 - 1ª: E mais fácil. Basta baixar/clonar o arquivo 'REST API - Challange.postman_collection.json' que é a coleção do Postman com requisições prontas. Basta importar esse arquivo no seu postman e fazer os testes. (https://kb.datamotion.com/?ht_kb=postman-instructions-for-exporting-and-importing)
 - 2ª: Existe um arquivo junto ao 'main.py' que se chama 'test.py'. Execute-o através do prompt de comando (python teste.py) ou de uma IDE de preferência para ver o resultado das suas requisições. Para mudar os parâmetros do teste basta alterar de Usuário e/ou Senha e Extensão.
 - 3ª: Em seu navegador acesse o endereço 'http://127.0.0.1:5000/lista', informe o usuário e senha (Frame / Work) e veja os itens retornados.

Após cada requisição será gerado um arquivo de log, que funciona como histórico, que ficará dentro da pasta 'logs'. Lá dentro estarão todas as requisições feitas com seus respectivos sucessos ou erros.

Observação: Lembre-se sempre de testar enquanto o servidor estiver rodando! Caso contrário não será obtida resposta alguma.


# Créditos
Inspirações e noçoes gerais com Tim (Tech With Tim: https://www.youtube.com/watch?v=GMppyAPbLYk&t=1703s)
Como utilizar Basic Auth com Michael Aboagye (https://geekflare.com/securing-flask-api-with-jwt/)


# Licença
Este projeto pode ser utilizado e copiado por qualquer um DESDE QUE, caso utilize para fins outros além do educacional, sejam dados os devidos crétidos.

/-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------/

(US-EN)
#  Purpose
Basic application using REST API. Might be useful for those who are starting and curious about Flask, Python and APIs in general.


# Description
This project basically returns the first 5 items of a list from an endpoint. Furthermore, some response treatments were done to ensure the endpoint is correct and the user used the right verification. Tecnologies used were: Flask itself because of its simplicity, speed and quick development; 'requests' library to help on creating and sending requests to desired endpoints.

# Instalation Process
@TODO
