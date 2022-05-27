char hasil=0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(7, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    hasil = Serial.read();
    Serial.write(hasil);
    if(hasil == 'f'){
      digitalWrite(7,HIGH);
    }
    else if(hasil == 'a'){
      digitalWrite(7,LOW);
    }
  }
}
