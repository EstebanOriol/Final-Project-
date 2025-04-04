# Proposal

## What will (likely) be the title of your project?
Max Camera Device

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")
A max for live device that can controll my camera to capture live performence with automated positioning

TODO

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

I will use Max for live to send serial messages via bluetooth (HC-05) to an RasberryPi that is connected to a motor and also to my camera. The RasberryPi will send messages to the camera to record and provided it can access zoom and focus settings I can control those too. The raberry Pi will comunicate to the camera with a python code. Messages will also be sent from the RasberryPi too the motor to send it information on which direction it should move in and at what speed. The motor will control the movement of two wheels that will either move on a rail system or a cable. By having the abilitiy to control this device through live I will be able to record live performances from high angles in my apartment without needing to hold the camera and automate the movement of the camera based on the position of the song. I will also be able to use a pedal to send signals if I automate this in abelton. 

This part is more complex but it better fits the actual goal of what I want to do with my device:
I would like to be able to save positions and angles for the camera on the rail so I can automate movement from one preset position to another. The difficulty in this is I dont know how to keep the movement across the rail constant so it always goes to the same exact position.

T

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?
I think a good outcome would be to have the ability to control the camera recording with max (just sending the signal to record) and to send signal to the RasberryPi and the motor that can move it forward and backwards


### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

I would like to be able to save positions and angles for the camera on the rail so I can automate movement from one preset position to another. The difficulty in this is I dont know how to keep the movement across the rail constant so it always goes to the same exact position.


### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

Controling camera zoom and other settings
Link the camera movement to the tempo
Automate the movement to occur gradually between fixed positions in the song

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

I will need to do more research on controling mechanincal devices with code and how to link it with an RasberryPi. I will also need to strengthen my skills in Max and learn more about using it to send recieve external signals. I will also need construct the rail and wheels. I also need to 