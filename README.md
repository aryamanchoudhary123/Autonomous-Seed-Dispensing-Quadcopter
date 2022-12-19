# Autonomous-Seed-Dispensing-Quadcopter
## Description
With the increasing number of Forest Fires and Deforestation, the green cover of our planet is depleting at an alarming rate. This project aims to address this issue by providing a device which is able to plant seeds far more effectively than humans by covering larger areas in shorter span of time. This device will also be able to go to hard to reach spots in jungles and requires minimal human interaction to operate. Apart from this it can also be used commercially in agriculture.

![Quadcopter Final Photo](https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/Densenet-accuracy.png)

## Developing the Quadcopter 
### The Quadcopter has been developed by using the following items :
1. [KK 2.1.5 Flight Controller](www.link.com)
2. [Electronic Speed Controller ](www.link.com)
3. [4 x Stepper Motor --> 13T/1000kV ](www.link.com)
4. [F450 Frame](www.link.com)
5. [Landing Gear](www.link.com)
6. [4 x Propeller --> 10x4.5 inch](www.link.com)
7. [Lithium Polymer 3S 2300 mAh battery](www.link.com)
8. [Flysky FSCT-6B Transmitter and Reciever](www.link.com)
9. [Raspberry Pi 3B+](www.link.com)

### Assembled the parts via soldering and developed a steady flight quadcopter
<img src="https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/drone-initial.jpeg" height="600" width="380">


## Developing the Suitable Land Detection Algorithm 

### For The development of Suitable Land Detection Algorithm, first a dataset was created which can be found at [kaggle link](https://www.kaggle.com/datasets/aryamanchoudhary/quadcopter-captured-different-land-types?datasetId=2703305)

### Various Deep Learning Methods were compared
![Comparison Photo](https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/comparison.png)

### Based on this Resnet 50 model was selected 

#### Accuracy Graph 

![Resnet Accuracy Graph](https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/resnet-accuracy.png)

#### Loss Graph 

![Resnet Loss Graph](https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/resnet-loss.png)

## Designing the Seed Dispensing Mechanism 

### For the Seed Dispensing Mechanism we designed a funnel onto which we will attach a servo motor that acts like a movable lid. This will allow for a required amount of seeds to fall out of the drone and onto the ground which under suitable conditions will lead to its germination to a plant.

#### The Design of the Funnel 

<img src="https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/funnel2_side-view.jpeg" height="600" width="380">

#### The 3D printed Funnel 
<img src="https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/Funnel-developed.jpeg" height="600" width="380">


## Final Product
### The demo video of the project can be found on [youtube](www.youtube.com)
![Quadcopter Final Photo](https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/Densenet-accuracy.png)

## Contributors 

### This project was developed by [Aryaman Choudhary](https://github.com/aryamanchoudhary123) and [Harmandeep Singh](https://www.linkedin.com/in/harmandeep-singh-b9740a1b2/) for their final year project for [Computer Science and Engineering Department at Thapar University, India](https://csed.thapar.edu)
