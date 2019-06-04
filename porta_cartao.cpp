#include <SPI.h>
#include <MFRC522.h>
#include <LiquidCrystal.h>
 
#define SS_PIN 10
#define RST_PIN 9
#define pinoFechadura 3
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Criar MFRC522.
 
char st[20];
 
void setup() 
{
  Serial.begin(9600);   // Inicia a serial
  SPI.begin();      // Inicia  SPI bus
  mfrc522.PCD_Init();   // Inicia MFRC522
  Serial.println("Aproxime o seu cartao do leitor...");
  Serial.println(); 
}
 
void loop() 
{
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  //Mostra UID na serial
  Serial.print("UID da tag :");
  String conteudo= "";
  byte letra;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     Serial.print(mfrc522.uid.uidByte[i], HEX);
     conteudo.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     conteudo.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  Serial.println();
  Serial.print("Mensagem : ");
  conteudo.toUpperCase();
  if (conteudo.substring(1) == "ED 78 03 CA") //UID 1 - Cartao 1 // botar numeros do cartao de cada um
  {
    Serial.println("Ola Cartao 1 !");
    abrirFechadura();
    Serial.println();
    delay(100);
  }
 
  else if (conteudo.substring(1) == "BD 9B 06 7D") //UID 2 - Cartao 2
  {
    Serial.println("Ola Cartao 2 !");
    abrirFechadura();
    Serial.println();
    delay(100);
  }
  else if (conteudo.substring(1) == "BD 9B 06 7D") //UID 3 - Cartao 3
  {
    Serial.println("Ola Cartao 3 !");
    abrirFechadura();
    Serial.println();
    delay(100);
  }
  else if (conteudo.substring(1) == "BD 9B 06 7D") //UID 4 - Cartao 4
  {
    Serial.println("Ola Cartao 4 !");
    abrirFechadura();
    Serial.println();
    delay(100);
  }
  else 
  {
    Serial.println("Entrada nao permitida");
    delay(1000);
  }
} 

void abrirFechadura(){
    digitalWrite(pinoFechadura, HIGH);
    delay(5000);
    digitalWrite(pinoFechadura, LOW);
  }
