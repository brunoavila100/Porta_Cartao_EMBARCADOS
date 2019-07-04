Integrantes:
Bruno Avila - 9012667
Denys Zandonadi Coco - 8005542
Levi Braquehais - 8549556
Lucas Saraiva Pezolito - 8670545

*****************************

Link do video: https://youtu.be/XSsGQIEnN98

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
Motivação:
Como moramos em uma república, temos muitas visitas de amigos que se reúnem tanto para estudar como para festejar. 
As vezes não há ninguém em casa e algum amigo aparece na república e gostariamos que eles tivessem a liberdade de entrar quando quisessem. Por esse motivo, pensamos na ideia de construir uma trava pro portão que seja liberado pela Carteirinha da USP, pois todos a possuem. Como nós realizariamos o cadastro de cada carteirinha, não correria o risco de um desconhecido entrar em casa.
*****************************

O projeto consiste de um portão elétrico residencial que é liberado através de um cartão com RFID, e os dados de horário e usuário são armazenados em planilha de Excel e tambem podem ser visualizados através do browser, manejados por uma Raspberry.
Foi utilizado um Arduino como escravo, para fazer a interface entre a leitura do sensor RFID MFRC522 e o cartão, além do acionamento dos leds que indicam o estado da abertura do portão e do relé que libera a trava do portão.
Para o sistema embarcado, utilizou-se uma Raspberry pi 3 que lê a informação que o arduino envia via porta serial. A raspberry armazena os dados obtidos em um planilha excel e disponibiliza essa informação via browser, através de um IP atribuído a mesma.

*****************************

Imagens dos componentes utilizados

Arduino UNO
![alt text](https://github.com/brunoavila100/Porta_Cartao_EMBARCADOS/blob/master/fotos/uno_cabo.jpg)

Raspiberry Pi 3
![alt text](https://github.com/brunoavila100/Porta_Cartao_EMBARCADOS/blob/master/fotos/rpi3.jpg)

Trava 12V
![alt text](https://github.com/brunoavila100/Porta_Cartao_EMBARCADOS/blob/master/fotos/trava-12v.jpg)

Relé 5V
![alt text](https://github.com/brunoavila100/Porta_Cartao_EMBARCADOS/blob/master/fotos/LDR-com-rele-5v.jpg)

Leds
![alt text](https://github.com/brunoavila100/Porta_Cartao_EMBARCADOS/blob/master/fotos/led.jpg)
