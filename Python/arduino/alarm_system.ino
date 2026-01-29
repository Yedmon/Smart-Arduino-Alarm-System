int greenLED = 8;
int redLED = 9;
int buzzer = 10;

bool alarmActive = false;

void setup() {
  Serial.begin(9600);
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();

    if (command == 'D') {  // DISARM
      alarmActive = false;
      digitalWrite(greenLED, HIGH);
      digitalWrite(redLED, LOW);
      noTone(buzzer);
    }

    if (command == 'A') {  // ARM
      alarmActive = false;
      digitalWrite(greenLED, LOW);
      digitalWrite(redLED, HIGH);
      noTone(buzzer);
    }

    if (command == 'L') {  // ALARM
      alarmActive = true;
    }
  }

  // Alarm mode blinking + sound
  if (alarmActive) {
    digitalWrite(redLED, HIGH);
    tone(buzzer, 1000);
    delay(200);

    digitalWrite(redLED, LOW);
    noTone(buzzer);
    delay(200);
  }
}
