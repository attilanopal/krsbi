//deklarasi variable pin driver motor Mxy
//x = motor ke berapa, y = 1 atau 2 (bisa berarti maju atau mundur, tergantung motor)
int M11  = 8;
int M12  = 9;
int M21  = 6;
int M22  = 7;
int M1EN = 10;
int M2EN = 11;
//int M1EN = 20;
//int M2EN = 21;
int M31 = 4;
int M32 = 5;
int M3EN = 12;
//int M3EN = 22;
int M41 = 2;
int M42 = 3;
int M4EN = 13;
//int M4EN = 23;
int relayT = 7;

void setup() {
  Serial.begin(2000000); //mengatur baudrate serial menjadi 2000000
  // membuat semua pin motor menjadi output
  pinMode(M11,OUTPUT);
  pinMode(M12,OUTPUT);
  pinMode(M21,OUTPUT);
  pinMode(M22,OUTPUT);
  pinMode(M1EN,OUTPUT);
  pinMode(M2EN,OUTPUT);
  pinMode(M31,OUTPUT);
  pinMode(M32,OUTPUT);
  pinMode(M41,OUTPUT);
  pinMode(M42,OUTPUT);
  pinMode(M3EN,OUTPUT);
  pinMode(M4EN,OUTPUT);
  pinMode(relayT,OUTPUT);
  digitalWrite(relayT,HIGH);
}

void loop() {
  if(Serial.available()>0){ // memeriksa apakah serial tersedia
    char cmd = 'z'; //supaya char-nya tidak kosong
    unsigned char spd = 'o'; //supaya char-nya tidak kosong
    cmd = Serial.read();//menerima perintah dari python
    if(cmd == 'l'){// menggerakan roda kiri
      digitalWrite(M3EN,HIGH); //menyalakan roda
      spd = Serial.read(); //menerima kecepatan roda
      Serial.println(cmd); //mencetak perintah ke serial
      Serial.println(spd); //mencetak kecepatan ke serial
      analogWrite(M32,spd); //mengatur kecepatan roda
    }
    else{
      digitalWrite(M3EN,LOW);//jika sudah selesai menjalankan perintah maka motor dimatikan
    }
  }
}
