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

O projeto consiste de um portão elétrico residencial que é liberado através de um cartão com RFID, e os dados de horário e usuário são armazenados em planilha de Excel e tambem podem ser visualizados através do browser, manejados por uma Raspberry.
Foi utilizado um Arduino como escravo, para fazer a interface entre a leitura do sensor RFID MFRC522 e o cartão, além do acionamento dos leds que indicam o estado da abertura do portão e do relé que libera a trava do portão.
Para o sistema embarcado, utilizou-se uma Raspberry pi 3 que lê a informação que o arduino envia via porta serial. A raspberry armazena os dados obtidos em um planilha excel e disponibiliza essa informação via browser, através de um IP atribuído a mesma.