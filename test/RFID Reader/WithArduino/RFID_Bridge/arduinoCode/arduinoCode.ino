/*
 *  Created by TheCircuit
*/

#define SS_PIN 4  //D2
#define RST_PIN 5 //D1

#include <SPI.h>
#include <MFRC522.h>

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.
int statuss = 0;
int out = 0;
void setup() 
{
    Serial.begin(9600);
    Serial.setTimeout(1);
    SPI.begin();
    mfrc522.PCD_Init();
}
void loop() {
    if ( ! mfrc522.PICC_IsNewCardPresent()) 
    {
        return;
    }
    if ( ! mfrc522.PICC_ReadCardSerial()) 
    {
        return;
    }
    String content= "";
    for (byte i = 0; i < mfrc522.uid.size; i++) 
    {
        content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
        content.concat(String(mfrc522.uid.uidByte[i]));
    }
    content.toUpperCase();
    Serial.println(content);
} 
