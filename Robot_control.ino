
#include <ezButton.h>

class Cylinder{
  public:
  Cylinder (int valvePin);
  void extend();
  void retract();

  private:
  int _valvePin;
};

Cylinder::Cylinder(int valvePin){
  pinMode(valvePin, OUTPUT);
  _valvePin=valvePin;
}

void Cylinder::extend(){
  digitalWrite(_valvePin, HIGH);
}

void Cylinder::retract(){
  digitalWrite(_valvePin, LOW);
}
  
//int solenoidPin1=13;
int solenoidPin2=13;
int airPin=12;

//Cylinder Pusher_Cyl(solenoidPin1);
Cylinder Pick_Cyl(solenoidPin2);

//define pin numbers
const int stepPinx=3;
const int dirPinx=2;
const int stepPiny=5;
const int dirPiny=4;
const int stepPinp=7;
const int dirPinp=6;

const int pin_switch_x1=8;
const int pin_switch_y=9;
const int pin_switch_p=10;
const int pin_switch_x2=11;

#define NEXT 10
#define PICK 20
#define PLACE 30
#define COUNT 40
#define PUSH 50

#define PICK_DIS 50 //distance between two pick positions
#define PLACE_DIS 35 //distance between two place positions
#define PUSH_DIS 50 //distance between two push positions
#define STEP_DIS 0.31428571 //one step in mm
#define Y_START_POS 100 //pick position y
#define X_START_POS 100 //pick position X
#define P_START_POS 100 //first push postition 
#define Y_PLACE_POS 300 //place position y
#define X_PLACE_POS 500 //place position X
int DELAY; //delay in micoseconds between steps


int sequence_step=10;
int X; //X current postion
int Y; //Y current position
int P; //P current postion
int xoffset=0; //x index of matrix 
int yoffset=0; //y index of matrix 
int count =0; //count of picks
int r=5; //number of rows 
int c=5; //numeber of colomns of mosaic
int next;

//limit switch
ezButton home_x1 (pin_switch_x1);
ezButton home_x2 (pin_switch_x2);
ezButton home_y (pin_switch_y);
ezButton home_p(pin_switch_p);


int homing(int stepPin, int dirPin, ezButton home_switch, bool flag);
void SingleStep(int stepPin);
int move(int target, int curr, int dirPin, int stepPin, bool f);
int homing2(int stepPin, int dirPin, ezButton home_switch1, ezButton home_switch2, bool flag);

void setup() {
  // put your setup code here, to run once:
  pinMode(stepPinx,OUTPUT); 
  pinMode(dirPinx,OUTPUT);
  pinMode(stepPiny,OUTPUT); 
  pinMode(dirPiny,OUTPUT);
  pinMode(stepPinp,OUTPUT); 
  pinMode(dirPinp,OUTPUT);
  pinMode(airPin, OUTPUT);
  
  
  Serial.begin(9600);
  delay(1000);

  
  //homing
  DELAY=1200;
  Serial.print("-------------Stepper is Homing--------------------");
  Y=homing(stepPiny, dirPiny, home_y, LOW);
  P=homing(stepPinp, dirPinp, home_p, HIGH);
  X=homing2(stepPinx, dirPinx, home_x1, home_x2, LOW);
  DELAY=1200;
  delay(2000);
 


}

void loop() {
  // put your main code here, to run repeatedly:
  switch (sequence_step){

    case NEXT:
    Serial.println("o");
    while (Serial.available()==0){}
    next=Serial.readString().toInt();
    sequence_step=PICK;
    break;
    
    case PICK:
    
    //pick
    //Serial.print("Picking from X: ");
    //move(X_START_POS, Y_START_POS+ (next*DISTANCE));
    //delay(1000);
    X=move(X_START_POS, X, dirPinx, stepPinx, LOW);//changed
    Y=move(Y_START_POS+ (next*PICK_DIS), Y, dirPiny, stepPiny, HIGH);
    //Serial.print("Picking from X: ");
    //Serial.print(X);
    //Serial.print(" Y:");
    //Serial.println(Y);
    //delay(1000);
    Pick_Cyl.extend();
    delay(1000);
    digitalWrite(airPin, HIGH);
    delay(1000);
    Pick_Cyl.retract();
    delay(1000);
    sequence_step=PLACE;
    break;

    case PLACE:
    //Serial.print("Placing at X: ");
    //delay(1000);
    X=move(X_PLACE_POS+(xoffset*PLACE_DIS), X, dirPinx, stepPinx, HIGH);
    Y=move(Y_PLACE_POS+(yoffset*PLACE_DIS), Y, dirPiny, stepPiny, HIGH);
    //Serial.print("Placing at X: ");
    //Serial.print(X);
    //Serial.print(" Y:");
    //Serial.println(Y);
    //delay(1000);
    Pick_Cyl.extend();
    delay(1000);

    digitalWrite(airPin, LOW);
    delay(3000);

    Pick_Cyl.retract();
    delay(1000);
    sequence_step=COUNT;
    break;

    case COUNT:
    count++;
    Serial.print(" Count: ");
    Serial.println(count);
    if (yoffset < c){
      yoffset++;
    }
    else if(yoffset == c){
      yoffset=0;
      if (xoffset<r){
        xoffset++;
      }
    }
    sequence_step=PUSH;
    break;

    case PUSH:
    //delay(1000);
    //P=move(P_START_POS+(next*PUSH_DIS), P, dirPinp, stepPinp, LOW)
    //delay(1000);
    //Pusher_Cyl.extend();
    //delay(1000);
    //Pusher_Cyl.retract();
    delay(1000);
    
    //Y=homing(stepPiny, dirPiny, home_y, HIGH);
    //X=homing2(stepPinx, dirPinx, home_x1, home_x2, HIGH);
    sequence_step= NEXT;
    break;
    
  }
}

int homing(int stepPin, int dirPin, ezButton home_switch, bool flag){
  digitalWrite(dirPin, flag);
  while (!(home_switch.isPressed())){
    home_switch.loop();
    if (home_switch.isPressed()){
    Serial.println("Button is pressed");
    }
    SingleStep(stepPin);
    //delayMicroseconds(500)
  }
  return 0;
}


int move(int target, int curr, int dirPin, int stepPin, bool f){
  int stepsToGo= abs(target-curr);
  if(f){
  if (target>curr){
    digitalWrite(dirPin,LOW);
  }
  else {
    digitalWrite(dirPin,HIGH);
  }
  }
  else{
    if (target>curr){
    digitalWrite(dirPin,HIGH);
  }
  else {
    digitalWrite(dirPin,LOW);
  }
  }

   while (stepsToGo>0){
      SingleStep(stepPin);
      stepsToGo--;
   
  }
  return target;
}

int homing2(int stepPin, int dirPin, ezButton home_switch1, ezButton home_switch2, bool flag){
  digitalWrite(dirPin, flag);
  while (!(home_switch1.isPressed() or home_switch2.isPressed())){
    home_switch1.loop();
    home_switch2.loop();
    if (home_switch1.isPressed() or home_switch2.isPressed()){
    Serial.println("Button is pressed");
    }
    SingleStep(stepPin);
    //delayMicroseconds(500)
  }
  return 0;
}

void SingleStep(int stepPin){
  digitalWrite(stepPin,HIGH); 
  delayMicroseconds(DELAY); 
  digitalWrite(stepPin,LOW); 
  delayMicroseconds(DELAY); 
}
