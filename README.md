# Autonomous-Seed-Dispensing-Quadcopter
## Description
With the increasing number of Forest Fires and Deforestation, the green cover of our planet is depleting at an alarming rate. This project aims to address this issue by providing a device which is able to plant seeds far more effectively than humans by covering larger areas in shorter span of time. This device will also be able to go to hard to reach spots in jungles and requires minimal human interaction to operate. Apart from this it can also be used commercially in agriculture.

![Quadcopter Final Photo](https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/drone-final.jpeg)

## Developing the Quadcopter 
### The Quadcopter has been developed by using the following items :
1. [KK 2.1.5 Flight Controller](https://roboindia.com/store/kk-multi-rotor-flight-control-board)
2. [Electronic Speed Controller ](https://roboindia.com/store/bldc-1400kv-esc-30a-combo?search=esc%20)
3. [4 x Stepper Motor --> 13T/1000kV ](https://roboindia.com/store/bldc-1400kv-esc-30a-combo?search=esc%20)
4. [F450 Frame](https://www.electronicscomp.com/f450-quadcopter-frame-integrated-pcb-wiring-india?gclid=CjwKCAiAkfucBhBBEiwAFjbkr0IBl1zw1hJz7HhGEELttQWdjF2M_oVzJAD0mrw-AD-QbiJElRqZIRoC7mwQAvD_BwE)
5. [Landing Gear](https://robu.in/product/f450-f550-frame-landing-gear-landing-skid/?gclid=CjwKCAiAkfucBhBBEiwAFjbkrwpUympzEwxo4g5hgAdxWcbqXQ7vipw4Qa4F2ztCJAEtSBrjtb6lXhoCSOcQAvD_BwE)
6. [4 x Propeller --> 10x4.5 inch](https://www.electronicscomp.com/1045-propeller-pair-for-quadcopter-black?gclid=CjwKCAiAkfucBhBBEiwAFjbkr9ZYTnbt8evE2fzoc9xayHZ1YdiWRc_qi0__0AXZu5xd1R8LPR1fTBoC8QMQAvD_BwE)
7. [Lithium Polymer 3S 2300 mAh battery](https://www.bhphotovideo.com/c/product/1468031-REG/swellpro_cdc01_0009_2300mah_remote_controller_lipo.html)
8. [Flysky FSCT-6B Transmitter and Reciever](https://www.electronicscomp.com/flysky-fs-t6-6-channel-transmitter-with-fs-r6b-receiver?search=flysky%20transmitter)
9. [Raspberry Pi 3B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/)

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

<img src="https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/funnel2_side-view.jpeg" height="600" width="380">

#### The 3D printed Funnel 
<img src="https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/Funnel-developed.jpeg" height="600" width="380">


## Final Product
### The demo video of the project can be found on [youtube](www.youtube.com)
![Quadcopter Final Photo](https://github.com/aryamanchoudhary123/Autonomous-Seed-Dispensing-Quadcopter/blob/main/Images/drone-final.jpeg)

## Contributors 

### This project was developed by [Aryaman Choudhary](https://github.com/aryamanchoudhary123) and [Harmandeep Singh](https://www.linkedin.com/in/harmandeep-singh-b9740a1b2/)and [Yuvraj Brar](https://www.linkedin.com/in/yuvraj-brar-3508941ab/) and [Lekha Revankar](https://www.linkedin.com/in/lekha-revankar/)  for their final year project for [Computer Science and Engineering Department at Thapar University, India](https://csed.thapar.edu)
