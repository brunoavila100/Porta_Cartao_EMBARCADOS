Integrantes:
Bruno Avila -
Denys Zandonadi Coco - 8005542
Levi Braquehais - 8549556
Lucas Saraiva Pezolito - 8670545

*****************************

===Bibliotecas===
python:
flask_socketio
flask
random
time
threading
datetime
serial 
csv

arduino:
SPI
MFRC522

*****************************

O projeto consiste de um port�o el�trico residencial que � liberado atrav�s de um cart�o com RFID, e os dados de hor�rio e usu�rio s�o armazenados em planilha de Excel e tambem podem ser visualizados atrav�s do browser, manejados por uma Raspberry.
Foi utilizado um Arduino como escravo, para fazer a interface entre a leitura do sensor RFID MFRC522 e o cart�o, al�m do acionamento dos leds que indicam o estado da abertura do port�o e do rel� que libera a trava do port�o.
Para o sistema embarcado, utilizou-se uma Raspberry pi 3 que l� a informa��o que o arduino envia via porta serial. A raspberry armazena os dados obtidos em um planilha excel e disponibiliza essa informa��o via browser, atrav�s de um IP atribu�do a mesma.