# Force Sensor
A basic programme that varies the colour of a square (red to green) based on how hard the user presses on a DIY force sensor.

I did this project purely to learn how to make Python work with serial communication. I learnt a bit of pygame along the way, which was fun. 

Here's a video of it working: https://youtube.com/shorts/wUYqlScKClk?feature=share

# Working Principle

This programme uses Python to request and read (through a serial port on your computer (USB)) the value of a DIY force sensor connected to an Ardunio. The programme then displays a square (using the pygame libary) and varies the colour of the square between red and green based on how hard the user presses the sensor.

## DIY Force Sensor
Block diagram of system: 
![20240121_130814535_iOS](https://github.com/aleighwood/forceSensor/assets/86426050/edc798c1-7b67-4c08-ab15-e2a67c23ac0a)

Detail on the sensor construction:
![22659](https://github.com/aleighwood/forceSensor/assets/86426050/94362030-9228-418d-8c11-99b90ba5ed78)


The sensor is of simple but effective design. [Velostat](https://en.wikipedia.org/wiki/Velostat) is a piezoresistive material (resistance changes with pressure) making it ideal for use in a force sensor. 

Placing a piece of copper tape on either side and putting it into a potential divider completes the design. 

Choose **R** based on the properties of your sensor or use trial and error to see which value of R gives you the biggest range in voltage at the analog input. 

I found using $`R = 500 \Omega `$ gave a range of 1000 (Ardunio ADC gives a range from 0 to 1023)

I followed this KontinuumLAB [tutorial](https://www.youtube.com/watch?v=gCBbIeI4xTE) on how to make the force sensor.

# Circuit Diagram 
![circuit(1)](https://github.com/aleighwood/forceSensor/assets/86426050/4dbc1afb-7636-434c-937f-a5a05fc02f31)


# Requirements

You will need the pygame, serial, sys and time libaries.

You will also need to upload the Ardunio code to the Ardunio. 
