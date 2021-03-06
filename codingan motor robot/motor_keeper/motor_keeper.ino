  int M11  = 31;
  int M12  = 30;
  int M21  = 33;
  int M22  = 32;
  int M1EN = 8;
  int M2EN = 9;
  int M31 = 35;
  int M32 = 34;
  int M3EN = 10;
  int M41 = 37;
  int M42 = 36;
  int M4EN = 11;
  int relayT = 7;
  int threshold = 200;
  int posisi = 0;
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
    if(cmd=='R' && posisi<threshold){
      periksa(majucheck,300);
      periksa(mundurcheck,300);
      periksa(kiricheck,300);
      periksa(spinrightcheck,300);
      periksa(spinleftcheck,300);
      periksa(rotateleftcheck,300);
      periksa(rotaterightcheck,300);
      kanancheck=true;
      kanan();
      posisi += 5;
    }
    else{
      periksa(kanancheck,300);
    }
    if(cmd=='L' && posisi>-threshold){
      periksa(majucheck,300);
      periksa(mundurcheck,300);
      periksa(kanancheck,300);
      periksa(spinrightcheck,300);
      periksa(spinleftcheck,300);
      periksa(rotateleftcheck,300);
      periksa(rotaterightcheck,300);
      kiricheck=true;
      kiri();
      posisi -= 5;
    }
    else{
      periksa(kiricheck,300);
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
      digitalWrite (relayT, LOW);
      delay(1000);
      digitalWrite (relayT, HIGH);
      delay(1000);
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
  analogWrite(M1EN,250);
  digitalWrite(M11,HIGH);
  digitalWrite(M12,LOW);
  analogWrite(M2EN,250);
  digitalWrite(M21,LOW);
  digitalWrite(M22,HIGH);
  analogWrite(M3EN,0);
  digitalWrite(M31,LOW);
  digitalWrite(M32,LOW);
  analogWrite(M4EN,0);
  digitalWrite(M41,LOW);
  digitalWrite(M42,LOW);
}
void mundur(){
  Serial.print("Backward\n");
  analogWrite(M1EN,250);
  digitalWrite(M11,LOW);
  digitalWrite(M12,HIGH);
  analogWrite(M2EN,250);
  digitalWrite(M21,HIGH);
  digitalWrite(M22,LOW);
  analogWrite(M3EN,0);
  digitalWrite(M31,LOW);
  digitalWrite(M32,LOW);
  analogWrite(M4EN,0);
  digitalWrite(M41,LOW);
  digitalWrite(M42,LOW); 
}
void berhenti(){
  Serial.print("Stop\n");
  analogWrite(M1EN,0);
  digitalWrite(M11,LOW);
  digitalWrite(M12,LOW);
  analogWrite(M2EN,0);
  digitalWrite(M21,LOW);
  digitalWrite(M22,LOW);
  analogWrite(M3EN,0);
  digitalWrite(M31,LOW);
  digitalWrite(M32,LOW);
  analogWrite(M4EN,0);
  digitalWrite(M41,LOW);
  digitalWrite(M42,LOW); 
}
void kiri(){
  Serial.print("Kiri\n");
  analogWrite(M1EN,0);
  digitalWrite(M11,LOW);
  digitalWrite(M12,LOW);
  analogWrite(M2EN,0);
  digitalWrite(M21,LOW);
  digitalWrite(M22,LOW);
  analogWrite(M3EN,250);
  digitalWrite(M31,LOW);
  digitalWrite(M32,HIGH);
  analogWrite(M4EN,250);
  digitalWrite(M41,HIGH);
  digitalWrite(M42,LOW);
}
void kanan(){
  Serial.print("Kanan\n");
  analogWrite(M1EN,0);
  digitalWrite(M11,LOW);
  digitalWrite(M12,LOW);
  analogWrite(M2EN,0);
  digitalWrite(M21,LOW);
  digitalWrite(M22,LOW);
  analogWrite(M3EN,250);
  digitalWrite(M31,HIGH);
  digitalWrite(M32,LOW);
  analogWrite(M4EN,250);
  digitalWrite(M41,LOW);
  digitalWrite(M42,HIGH);
}
void spinleft(){
  Serial.print("Spinleft\n");
  analogWrite(M1EN,100);
  digitalWrite(M11,LOW);
  digitalWrite(M12,HIGH);
  analogWrite(M2EN,100);
  digitalWrite(M21,LOW);
  digitalWrite(M22,HIGH);
  analogWrite(M3EN,100);
  digitalWrite(M31,LOW);
  digitalWrite(M32,HIGH);
  analogWrite(M4EN,100);
  digitalWrite(M41,LOW);
  digitalWrite(M42,HIGH);
}
void spinright(){
  Serial.print("Spinright\n");
  analogWrite(M1EN,100);
  digitalWrite(M11,HIGH);
  digitalWrite(M12,LOW);
  analogWrite(M2EN,100);
  digitalWrite(M21,HIGH);
  digitalWrite(M22,LOW);
  analogWrite(M3EN,100);
  digitalWrite(M31,HIGH);
  digitalWrite(M32,LOW);
  analogWrite(M4EN,100);
  digitalWrite(M41,HIGH);
  digitalWrite(M42,LOW);
}
void rotateleft(){
  Serial.print("Rotateleft\n");
  analogWrite(M1EN,100);
  digitalWrite(M11,HIGH);
  digitalWrite(M12,LOW);
  analogWrite(M2EN,100);
  digitalWrite(M21,HIGH);
  digitalWrite(M22,LOW);
  analogWrite(M3EN,250);
  digitalWrite(M31,LOW);
  digitalWrite(M32,HIGH);
  analogWrite(M4EN,250);
  digitalWrite(M41,HIGH);
  digitalWrite(M42,LOW);
}
void rotateright(){
  Serial.print("Rotateright\n");
  analogWrite(M1EN,100);
  digitalWrite(M11,LOW);
  digitalWrite(M12,HIGH);
  analogWrite(M2EN,100);
  digitalWrite(M21,LOW);
  digitalWrite(M22,HIGH);
  analogWrite(M3EN,250);
  digitalWrite(M31,HIGH);
  digitalWrite(M32,LOW);
  analogWrite(M4EN,250);
  digitalWrite(M41,LOW);
  digitalWrite(M42,HIGH);
}
