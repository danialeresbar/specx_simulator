# Specx simulator

![PyQt](https://upload.wikimedia.org/wikipedia/commons/e/e6/Python_and_Qt.svg)

## Description ##

Specx is an application that allows the configuration of suitable scenarios
for the generation of random variables from time to time according to certain
probability distributions identified in a sampling process carried out at
digital television frequencies in the city of Villavicencio. The software
performs a simulation of a synchronous time stochastic process. 
The application has the following functionalities:

1. To assign to each frequency understood as a random variable, one of the probability
   distributions discussed above, and configure the necessary parameters of this.

2. To save and load files with the configurations made for the distributions, in order
   not to repeat processes. The data is stored in JSON-formatted files.

3. To set a sampling time in minutes.

4. The simulation can only be started as soon as each frequency has a probability
   distribution assigned and configured.

5. To pause and resume the simulation at any time.

6. To Manipulate the flow of time, which implies a scaling of the sampling time
   during the simulation process.

7. To Visualize the sequence of values generated for each frequency in an individual
   graph that is updated in real time.

8. To Save the graphs built during the simulation in PNG format.

9. At the end of the simulation, the program generates a plain text file with
   information on the generated values.

The main goal of *Specx* is to reinforce the information on television blanks
contained in databases such as those used by the [PAWS protocol (https://tools.ietf.org/html/rfc7545).
Information that provides great opportunities for efficient use of the spectrum.

## Scope 🚀 ##

Specx is designed to simulate the level of occupation of channels in the
television band (UHF). These are the following frequencies that the simulator
analyzes:

| Frequency | Channel | Operator |
| :--- | :--- | :--- |
| `473 MHz` | 14 | Caracol |
| `479 MHz` | 15 | RCN |
| `485 MHz` | 16| RTVC |
| `491 MHz` | 17| Government, ICT Ministry and Mayor's Office of Bogotá |
| `497 MHz` | -- | -- |
| `503 MHz` | -- | -- |
| `509 MHz` | -- | -- |
| `551 MHz` | 27 | ETCE |
| `557 MHz` | 28 | Government, ICT Ministry and Mayor's Office of Bogotá | 

### Directory Tree ###

## Autores ✒️

The work team that carried out the simulation study and the development of *Specx*
is made up of the following people:

* **Héctor Iván Reyes Moncayo** - *Formulation of the problem and considerations to the model* - [Director]()
* **Ángel Alfonso Cruz Roa** - *System model* - [Co-director]()
* **Daniel Alejandro Restrepo Barbosa** - *Sampling process and determination of probability distributions, 
  design and construction of graphical user interfaces* - [Developer and Analyst]()
* **Siervo Francisco Rodríguez Castellanos** - *Coding of simulation algorithms and routine
  optimization* - [Developer]()
  
## Expresiones de Gratitud 🎁

- To the directors of this project. Dr. Ángel Cruz for his valuable contributions to the model of the
   system, without which Specx could not operate properly; in addition to dedication to reviewing
   each software functionality. Dr. Héctor Reyes for his knowledge in the area of
   telecommunications and radio transmissions, since his idea of a tvws radio was the one that led to the
  *Specx* development

- To Francisco Rodríguez for his development skills, which allowed the construction of several
   generators of random variables, as well as optimization in the use of resources by the
   app.

- To the University of Los Llanos for providing its spaces and bibliographic material for the study of
   simulation performed.
