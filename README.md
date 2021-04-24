# Specx simulator

Python3 + Qt

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

### Directory Tree ###

## Autores ✒️

El equipo de trabajo que llevó a cabo el estudio de simulación y el desarrollo de *webspecx* está formado 
por las siguientes personas:

* **Héctor Iván Reyes Moncayo** - *Formulación del problema y consideraciones al modelo* - [Director]()
* **Ángel Alfonso Cruz Roa** - *Modelo del sistema* - [Codirector]()
* **Daniel Alejandro Restrepo Barbosa** - *Proceso de muestreo y determinación de distribuciones de probabilidad, 
  diseño y construcción de interfaces gráficas de usuario.* - [Analista]()
* **Siervo Francisco Rodríguez Castellanos** - *Codificación de algoritmos de simulación y optimización 
  de rutinas* - [Desarrollador]()
  
## Expresiones de Gratitud 🎁

- A los directores de este proyecto. El doctor Ángel Cruz por sus aportes tan valiosos al modelo del 
  sistema, sin el cual Specx no podría operar correctamente; además de la dedicación a la revisión de 
  cada funcionalidad del software. El doctor Héctor Reyes por sus conocimientos en el área de 
  telecomunicaciones y radiotransmisiones, ya que su idea de un radio tvws fue la que llevó al desarrollo 
  de *webspecx*.

- A Francisco Rodríguez por sus habilidades en el desarrollo, que permitieron la construcción de varios 
  generadores de variables aleaotorias, así como la optimización en el uso de recursos por parte de la 
  aplicación.

- A la universidad de los llanos por brindar sus espacios y material bibliográfico para el estudio de 
  simulación realizado.
