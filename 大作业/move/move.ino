int motorA1pin = 9;
int motorB1pin = 10;

int motorA2pin = 11;
int motorB2pin = 12;

void setup() {
  // put your setup code here, to run once:
  pinMode(motorA1pin, OUTPUT);
  pinMode(motorB1pin, OUTPUT);
  pinMode(motorA2pin, OUTPUT);
  pinMode(motorB2pin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 0; i < 255; i++)
  {
    digitalWrite(motorB1pin, LOW);
    digitalWrite(motorB2pin, LOW);
    analogWrite(motorA1pin, i);
    analogWrite(motorA2pin, i);
    delay(50);

  }
  for (int i = 0; i > -255; i--)
  {
    digitalWrite(motorB1pin, LOW);
    digitalWrite(motorB2pin, LOW);
    analogWrite(motorA1pin, i);
    analogWrite(motorA2pin, i);
    delay(50);

  }
}
