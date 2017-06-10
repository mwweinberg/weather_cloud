#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 6

//holds the keyboard input
//not sure why it has to be a byte but it does
byte keyIn;


// Parameter 1 = number of pixels in strip
// Parameter 2 = Arduino pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_RGBW    Pixels are wired for RGBW bitstream (NeoPixel RGBW products)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(8, PIN, NEO_GRBW + NEO_KHZ800);

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 300 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel.  Avoid connecting
// on a live circuit...if you must, connect GND first.

int counter = 0;
int counter1 = 0;

void setup() {

  strip.begin();
  strip.show(); // Initialize all pixels to 'off'

  Serial.begin(9600); // turns on serial port

  
}

void loop() {

  Serial.println("Enter input");
  //pauses until there is input
  while (Serial.available() == 0)
  { 
    
  }
  //keyIn holds the key input at the prompt
  keyIn = Serial.read();   

  // if the input is 'a'
  if (keyIn == 'a')
  {

    //this just creates a variable that runs from 0-100 to use to manipulate the values
    for(int k = 0; k<100; k++)
      {
        strip.setPixelColor(0,(155+k),(40+k),0,0); //fade up orange
        strip.setPixelColor(1,(155+k),(155+k),0,0); // fade up yellow
        strip.setPixelColor(2,(255-k),(140-k),0,0); //fade down orange
        strip.setPixelColor(3,(255-k),(255-k),0,0); //fade down yellow
        strip.setPixelColor(4,(155+k),(40 + (k*2)),0,0); //fade up orange to yellow
        strip.setPixelColor(5,(155+k),(155+(k/6)),0,0); //fade up yellow to orange
        strip.setPixelColor(6,(255-k),(140+(k/6)),0,0); // fade down orange to yellow
        //strip.setPixelColor(7,(255-k),(255-k),0,0); // fade down yellow to orange
        strip.setPixelColor(7,0,0,0,(k*2)); //fade up white
  
        strip.show();
        delay(50);
      }
    for(int k = 0; k<100; k++)
      {
        strip.setPixelColor(0,(255-k),(140-k),0,0); //fade down orange
        strip.setPixelColor(1,(255-k),(255-k),0,0); // fade down yellow
        strip.setPixelColor(2,(155+k),(40+k),0,0); //fade up orange
        strip.setPixelColor(3,(155+k),(155+k),0,0); //fade up yellow
        strip.setPixelColor(4,(255-k),(255-(2*k)),0,0); //fade down yellow to orange
        strip.setPixelColor(5,(255-k),(140+(k/6)),0,0); //fade down orange to yellow
        strip.setPixelColor(6,(155+k),(155+(k/6)),0,0); // fade up yellow to orange
        //strip.setPixelColor(7,(255-k),(255-k),0,0); // fade down yellow to orange
        strip.setPixelColor(7,0,0,0,(200-(k*2))); //fade down white
  
        strip.show();
        delay(50);
      }
  }

  if (keyIn == 'b')
  {
    //lightning flash 1 up
  
      for(int k = 0; k<100; k++)
      {
        strip.setPixelColor(0,0,0,0,(50+k));
        strip.setPixelColor(1,0,0,0,(100+k));
        strip.setPixelColor(2,0,0,0,(150+k));
        strip.setPixelColor(3,0,0,0,(100+k));
        strip.setPixelColor(4,0,0,0,(50+k));
        strip.setPixelColor(5,0,0,0,0);
        strip.setPixelColor(6,0,0,0,0);
        strip.setPixelColor(7,0,0,0,0); 
  
        strip.show();
        delay(2);
      }
  
     //lightning flash 1 down
  
      for(int k = 0; k<100; k++)
      {
        strip.setPixelColor(0,0,0,0,(150-k));
        strip.setPixelColor(1,0,0,0,(200-k));
        strip.setPixelColor(2,0,0,0,(250-k));
        strip.setPixelColor(3,0,0,0,(200-k));
        strip.setPixelColor(4,0,0,0,(150-k));
        strip.setPixelColor(5,0,0,0,0);
        strip.setPixelColor(6,0,0,0,0);
        strip.setPixelColor(7,0,0,0,0); 
  
        strip.show();
        delay(2);
      }
  }

  if (keyIn == 'c')
  {
    //lightning flash 2 up
  
      for(int k = 0; k<100; k++)
      {
        //I was just too lazy to reorder these
        strip.setPixelColor(3,0,0,0,(50+k));
        strip.setPixelColor(4,0,0,0,(100+k));
        strip.setPixelColor(5,0,0,0,(150+k));
        strip.setPixelColor(6,0,0,0,(100+k));
        strip.setPixelColor(7,0,0,0,(50+k));
        strip.setPixelColor(0,0,0,0,0);
        strip.setPixelColor(1,0,0,0,0);
        strip.setPixelColor(2,0,0,0,0); 
  
        strip.show();
        delay(4);
      }
  
     //lightning flash 2 down
  
      for(int k = 0; k<100; k++)
      {
        strip.setPixelColor(3,0,0,0,(150-k));
        strip.setPixelColor(4,0,0,0,(200-k));
        strip.setPixelColor(5,0,0,0,(250-k));
        strip.setPixelColor(6,0,0,0,(200-k));
        strip.setPixelColor(7,0,0,0,(150-k));
        strip.setPixelColor(0,0,0,0,0);
        strip.setPixelColor(1,0,0,0,0);
        strip.setPixelColor(2,0,0,0,0); 
  
        strip.show();
        delay(4);
      }
  }    
  

}
