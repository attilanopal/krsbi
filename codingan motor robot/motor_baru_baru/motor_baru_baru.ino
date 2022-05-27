//deklarasi variable pin driver motor Mxy
//x = motor ke berapa, y = 1 atau 2 (bisa berarti maju atau mundur, tergantung motor)
int M11  = 9;
int M12  = 10;
int M21  = 6;
int M22  = 7;
int M1EN = 7;
int M2EN = 8;
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
  Serial.begin(38400);
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
  if(Serial.available()>=8){ 
    unsigned char leftmove = 0;
    unsigned char left = 0;
    unsigned char rightmove = 0;
    unsigned char right = 0;
    unsigned char frontmove = 0;
    unsigned char front = 0;
    unsigned char behindmove = 0;
    unsigned char behind = 0;
    leftmove = Serial.read();
    left = Serial.read();
    if(left==0){
      digitalWrite(M1EN,LOW);
    }
    else{
      digitalWrite(M1EN,HIGH);
    }
    if(leftmove=='f'){
      analogWrite(M11,left); 
      analogWrite(M12,0);  
    }
    else if(leftmove=='r'){
      analogWrite(M11,0); 
      analogWrite(M12,left);  
    }
    rightmove = Serial.read();
    right = Serial.read();
    if(right==0){
      digitalWrite(M2EN,LOW);
    }
    else{
      digitalWrite(M2EN,HIGH);
    }
    if(rightmove=='f'){
      analogWrite(M21,right);
      analogWrite(M22,0);  
    }
    else if(rightmove=='r'){
      analogWrite(M21,0);  
      analogWrite(M22,right);  
    }
    frontmove = Serial.read();
    front = Serial.read();
    if(front==0){
      digitalWrite(M3EN,LOW);
    }
    else{
      digitalWrite(M3EN,HIGH);
    }
    if(frontmove=='f'){
      analogWrite(M31,front);  
      analogWrite(M32,0);  
    }
    else if(frontmove=='r'){
      analogWrite(M31,0);  
      analogWrite(M32,front);  
    }
    behindmove = Serial.read();
    behind = Serial.read();
    if(behind==0){
      digitalWrite(M4EN,LOW);
    }
    else{
      digitalWrite(M4EN,HIGH);
    }
    if(behindmove=='f'){
      analogWrite(M41,behind);
      analogWrite(M42,0);  
    }
    else if(behindmove=='r'){
      analogWrite(M41,0);
      analogWrite(M42,behind);  
    }
  }
}
