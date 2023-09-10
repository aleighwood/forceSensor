# Force Sensor
A basic programme that varies the colour of a square (red to green) based on how hard the user presses on a DIY force sensor.

I did this project purely to learn how to make Python work with serial communication. I learnt a bit of pyGame along the way, which was fun. 

# Working Principle

This programme uses Python to request and read (through a serial port on your computer (USB)) the value of a DIY force sensor connected to an Ardunio. The programme then displays a square (using the pyGame libary) and varies the colour of the square between red and green based on how hard the user presses the sensor.

## DIY Force Sensor
![22659](https://github.com/aleighwood/forceSensor/assets/86426050/838c3ff1-3f5a-4e75-8581-7b76968a3938)

The sensor is of simple but effective design. [Velostat](https://en.wikipedia.org/wiki/Velostat) is a piezoesistive material (resistance changes with pressure) making it useful for use in a force sensor. 

Placing a piece of copper tape on either side and putting it into a potential divider completes the design. 

Choose **R** based on the properties of your sensor or use trial and error to see which value of R gives you the biggest range in voltage at the analog input. 

I found an using R $/approx 500 /Omega$ gave a range of 1000 (Ardunio ADC gives a range from 0 to 1023)

I followed this KontinuumLAB [tutorial](https://www.youtube.com/watch?v=gCBbIeI4xTE) on how to make a force sensor.

# Circuit Diagram 
![circuit](https://github.com/aleighwood/forceSensor/assets/86426050/ec08e0c1-1aac-4e43-9928-5429485bfc54)

# Requirements
