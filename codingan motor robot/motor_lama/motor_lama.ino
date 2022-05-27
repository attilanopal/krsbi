  int M11  = 8;
  int M12  = 9;
  int M21  = 6;
  int M22  = 7;
  int M1EN = 10;
  int M2EN = 11;
//  int M1EN = 20;
//  int M2EN = 21;
  int M31 = 4;
  int M32 = 5;
  int M3EN = 12;
//  int M3EN = 22;
  int M41 = 2;
  int M42 = 3;
  int M4EN = 13;
//  int M4EN = 23;
  int relayT = 7;
  bool majucheck = false;
  bool mundurcheck = false;
  bool kanancheck = false;
  bool kiricheck = false;
  bool spinleftcheck = false;
  bool spinrightcheck = false;
  bool rotateleftcheck = false;
  bool rotaterightcheck = false;
  
void setup() {
  Serial.begin(9600);
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
  if(Serial.available() > 0){
    char cmd='z';
    cmd = Serial.read();
    if(cmd=='F'){
      periksa(mundurcheck,300);
      periksa(kiricheck,300);
      periksa(kanancheck,300);
      periksa(spinrightcheck,300);
      periksa(spinleftcheck,300);
      periksa(rotateleftcheck,300);
      periksa(rotaterightcheck,300);
      majucheck=true;
      maju();
    }
    if(cmd=='B'){
      periksa(majucheck,300);
      periksa(kiricheck,300);
      periksa(kanancheck,300);
      periksa(spinrightcheck,300);
      periksa(spinleftcheck,300);
      periksa(rotateleftcheck,300);
      periksa(rotaterightcheck,300);
      mundurcheck = true;
      mundur();
    }
    if(cmd=='R'){
      periksa(majucheck,300);
      periksa(mundurcheck,300);
      periksa(kiricheck,300);
      periksa(spinrightcheck,300);
      periksa(spinleftcheck,300);
      periksa(rotateleftcheck,300);
      periksa(rotaterightcheck,300);
      kanancheck=true;
      kanan();
    }
    if(cmd=='L'){
      periksa(majucheck,300);
      periksa(mundurcheck,300);
      periksa(kanancheck,300);
      periksa(spinrightcheck,300);
      periksa(spinleftcheck,300);
      periksa(rotateleftcheck,300);
      periksa(rotaterightcheck,300);
      kiricheck=true;
      kiri();
    }
    if(cmd=='T'){
      periksa(majucheck,300);
      periksa(mundurcheck,300);
      periksa(kiricheck,300);
      periksa(kanancheck,300);
      periksa(spinrightcheck,300);
      periksa(spinleftcheck,300);
      periksa(rotateleftcheck,300);
      periksa(rotaterightcheck,300);
      delay(1000);
//      mundur();
//      unsigned long mulai = millis();
//      unsigned long berhenti1  = millis();
//      while(berhenti1 - mulai <= 500){
//        berhenti1 = millis();
//      }
      berhenti();
      delay(1000);
//      maju();
//      delay(1000);
//      majucheck = true;
//      digitalWrite (relayT, LOW);
//      delay(1000);
//      digitalWrite (relayT, HIGH);
//      delay(1000);
    }
    if(cmd=='S'){
      periksa(majucheck,300);
      periksa(mundurcheck,300);
      periksa(kiricheck,300);
      periksa(kanancheck,300);
      periksa(spinrightcheck,300);
      periksa(spinleftcheck,300);
      periksa(rotateleftcheck,300);
      periksa(rotaterightcheck,300);
    }
    if(cmd=='l'){
      periksa(majucheck,300);
      periksa(mundurcheck,300);
      periksa(kiricheck,300);
      periksa(kanancheck,300);
      periksa(spinrightcheck,300);
      periksa(rotateleftcheck,300);
      periksa(rotaterightcheck,300);
      spinleftcheck = true;
      spinleft();
    }
    if(cmd=='r'){
      periksa(majucheck,300);
      periksa(mundurcheck,300);
      periksa(kiricheck,300);
      periksa(kanancheck,300);
      periksa(spinleftcheck,300);
      periksa(rotateleftcheck,300);
      periksa(rotaterightcheck,300);
      spinrightcheck = true;
      spinright();
    }
    if(cmd=='o'){
      periksa(majucheck,300);
      periksa(mundurcheck,300);
      periksa(kiricheck,300);
      periksa(kanancheck,300);
      periksa(spinrightcheck,300);
      periksa(spinleftcheck,300);
      periksa(rotaterightcheck,300);
      rotateleftcheck=true;
      rotateleft();
    }
    if(cmd=='p'){
      periksa(majucheck,300);
      periksa(mundurcheck,300);
      periksa(kiricheck,300);
      periksa(kanancheck,300);
      periksa(spinrightcheck,300);
      periksa(spinleftcheck,300);
      periksa(rotateleftcheck,300);
      rotaterightcheck=true;
      rotateright();
    }
    if(cmd=='M'){
      miringkiri();
      delay(3000);
      berhenti();
    }
  }
}

void periksa(bool &x, int waktu){
  if(x){
    berhenti();
    delay(waktu);
    x=false;
  }
}

void maju(){
  Serial.print("Forward\n");
  digitalWrite(M3EN,HIGH);
  analogWrite(M31,0);
  analogWrite(M32,250);
  digitalWrite(M4EN,HIGH);
  analogWrite(M41,250);
  analogWrite(M42,0);
  digitalWrite(M1EN,LOW);
  analogWrite(M11,0);
  analogWrite(M12,0);
  digitalWrite(M2EN,LOW);
  analogWrite(M21,0);
  analogWrite(M22,0);
}
void mundur(){
  Serial.print("Backward\n");
  digitalWrite(M3EN,HIGH);
  analogWrite(M31,250);
  analogWrite(M32,0);
  digitalWrite(M4EN,HIGH);
  analogWrite(M41,0);
  analogWrite(M42,250);
  digitalWrite(M1EN,LOW);
  analogWrite(M11,0);
  analogWrite(M12,0);
  digitalWrite(M2EN,LOW);
  analogWrite(M21,0);
  analogWrite(M22,0);
}
void berhenti(){
  Serial.print("Stop\n");
  digitalWrite(M3EN,LOW);
  analogWrite(M31,0);
  analogWrite(M32,0);
  digitalWrite(M4EN,LOW);
  analogWrite(M41,0);
  analogWrite(M42,0);
  digitalWrite(M1EN,LOW);
  analogWrite(M11,0);
  analogWrite(M12,0);
  digitalWrite(M2EN,LOW);
  analogWrite(M21,0);
  analogWrite(M22,0);
}
void kiri(){
  Serial.print("Kiri\n");
  digitalWrite(M3EN,LOW);
  analogWrite(M31,0);
  analogWrite(M32,0);
  digitalWrite(M4EN,LOW);
  analogWrite(M41,0);
  analogWrite(M42,0);
  digitalWrite(M1EN,HIGH);
  analogWrite(M11,0);
  analogWrite(M12,250);
  digitalWrite(M2EN,HIGH);
  analogWrite(M21,0);
  analogWrite(M22,250);
}
void kanan(){
  Serial.print("Kanan\n");
  digitalWrite(M3EN,LOW);
  analogWrite(M31,0);
  analogWrite(M32,0);
  digitalWrite(M4EN,LOW);
  analogWrite(M41,0);
  analogWrite(M42,0);
  digitalWrite(M1EN,HIGH);
  analogWrite(M11,250);
  analogWrite(M12,0);
  digitalWrite(M2EN,HIGH);
  analogWrite(M21,250);
  analogWrite(M22,0);
}
void miringkiri(){
  Serial.print("Miring kiri\n");
  digitalWrite(M3EN,HIGH);
  analogWrite(M31,0);
  analogWrite(M32,100);
  digitalWrite(M4EN,HIGH);
  analogWrite(M41,0);
  analogWrite(M42,0);
  digitalWrite(M1EN,HIGH);
  analogWrite(M11,0);
  analogWrite(M12,0);
  digitalWrite(M2EN,HIGH);
  analogWrite(M21,0);
  analogWrite(M22,100);
}
void spinleft(){
  Serial.print("Spinleft\n");
  digitalWrite(M4EN,HIGH);
  analogWrite(M41,0);
  analogWrite(M42,150);
  digitalWrite(M3EN,HIGH);
  analogWrite(M31,0);
  analogWrite(M32,150);
  digitalWrite(M1EN,HIGH);
  analogWrite(M11,0);
  analogWrite(M12,150);
  digitalWrite(M2EN,HIGH);
  analogWrite(M21,150);
  analogWrite(M22,0);
}
void spinright(){
  Serial.print("Spinright\n");
  digitalWrite(M4EN,HIGH);
  analogWrite(M41,150);
  analogWrite(M42,0);
  digitalWrite(M3EN,HIGH);
  analogWrite(M31,150);
  analogWrite(M32,0);
  digitalWrite(M1EN,HIGH);
  analogWrite(M11,150);
  analogWrite(M12,0);
  digitalWrite(M2EN,HIGH);
  analogWrite(M21,0);
  analogWrite(M22,150);
}
void rotateleft(){
  Serial.print("Rotateleft\n");
  digitalWrite(M4EN,HIGH);
  analogWrite(M41,150);
  analogWrite(M42,0);
  digitalWrite(M3EN,HIGH);
  analogWrite(M31,150);
  analogWrite(M32,0);
  digitalWrite(M1EN,HIGH);
  analogWrite(M11,0);
  analogWrite(M12,250);
  digitalWrite(M2EN,HIGH);
  analogWrite(M21,0);
  analogWrite(M22,250);
}
void rotateright(){
  Serial.print("Rotateright\n");
  digitalWrite(M4EN,HIGH);
  analogWrite(M41,0);
  analogWrite(M42,150);
  digitalWrite(M3EN,HIGH);
  analogWrite(M31,0);
  analogWrite(M32,150);
  digitalWrite(M1EN,HIGH);
  analogWrite(M11,250);
  analogWrite(M12,0);
  digitalWrite(M2EN,HIGH);
  analogWrite(M21,250);
  analogWrite(M22,0);
}
