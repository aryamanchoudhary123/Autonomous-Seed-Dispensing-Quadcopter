# Autonomous-Seed-Dispensing-Quadcopter
## Description
With the increasing number of Forest Fires and Deforestation, the green cover of our planet is depleting at an alarming rate. This project aims to address this issue by providing a device which is able to plant seeds far more effectively than humans by covering larger areas in shorter span of time. This device will also be able to go to hard to reach spots in jungles and requires minimal human interaction to operate. Apart from this it can also be used commercially in agriculture.

![Quadcopter Final Photo](https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/drone-final.jpeg)

## Developing the Quadcopter 
### The Quadcopter has been developed by using the following items :
1. KK 2.1.5 Flight Controller
2. Electronic Speed Controller 
3. 4 x Stepper Motor --> 13T/1000kV 
4. F450 Frame
5. Landing Gear
6. 4 x Propeller --> 10x4.5 inch
7. Lithium Polymer 3S 2300 mAh battery
9. Raspberry Pi 3B+

### Assembled the parts via soldering and developed a steady flight quadcopter
<img src="https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/drone-initial.jpeg" height="600" width="380">


## Developing the Suitable Land Detection Algorithm 

### For The development of Suitable Land Detection Algorithm, first a dataset was created which can be found at [kaggle link](https://www.kaggle.com/datasets/aryamanchoudhary/quadcopter-captured-different-land-types?datasetId=2703305)

### Various Deep Learning Methods were compared
![Comparison Photo](https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/comparison.png)

### Based on this Resnet 50 model was selected 
#### Resnet Architecture
![Resnet Architecture](https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/Resnet50-architecture.png)

#### Accuracy Graph 

![Resnet Accuracy Graph](https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/resnet-accuracy.png)

#### Loss Graph 

![Resnet Loss Graph](https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/resnet-loss.png)

## Designing the Seed Dispensing Mechanism 

### For the Seed Dispensing Mechanism we designed a funnel onto which we will attach a servo motor that acts like a movable lid. This will allow for a required amount of seeds to fall out of the drone and onto the ground which under suitable conditions will lead to its germination to a plant.

#### The Design of the Funnel 

<img src="https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/funnel2_side-view.jpeg" height="400" width="380">

#### The 3D printed Funnel 
<img src="https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/Funnel-developed.jpeg" height="400" width="380">


## Final Product
### The demo video of the project can be found on [youtube](https://www.youtube.com/watch?v=KUw-NEblgLw)
![Quadcopter Final Photo](https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/drone-final.jpeg)

## Contributors 

### This project was developed by [Aryaman Choudhary](https://github.com/aryamanchoudhary123) and [Harmandeep Singh](https://www.linkedin.com/in/harmandeep-singh-b9740a1b2/) for their Capstone project for [Computer Science and Engineering Department at Thapar University, India](https://csed.thapar.edu)
