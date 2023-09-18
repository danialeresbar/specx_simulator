# Software de simulación de espacios en blanco de televisión

_Producto final de un estudio de simulación._

Specx es un software que permite la configuración de escenarios adecuados para la generación de variables aleatorias cada cierto tiempo de acuerdo con ciertas distribuciones de probabilidad identificadas en un proceso de muestreo realizado a las frecuencias de televisión digital en la ciudad de Villavicencio. El software realiza una la simulación de un proceso estocástico de tiempo sincrónico. Cuenta con las siguientes funcionalidades:

-Asignar a cada frecuencia entendida como una variable aleatoria, alguna de las distribuciones de probabilidad tratadas anteriormente, y configurar los parámetros necesarios de esta.

-Guardar y cargar archivos con las configuraciones realizadas para las distribuciones, con el fin de no repetir procesos. Los datos se almacenan en archivos con formato JSON.

-Fijar un tiempo de muestreo en minutos.

-La simulación solo se podrá iniciar en cuanto cada frecuencia tenga asignada y configurada una distribución de probabilidad.

-Pausar y reanudar la simulación en cualquier momento.

-Manipular el flujo del tiempo, lo que implica una escalización al tiempo de muestreo durante el proceso de simulación.

-Visualizar la secuencia de valores generados para cada frecuencia en una gráfica por individual que se actualiza en tiempo real.

-Guardar las gráficas construidas durante la simulación en formato PNG.

-Al final de la simulación, el programa genera un archivo de texto plano con información de los valores generados.

La finalidad con la que fue creado Specx es reforzar la información sobre los espacios en blanco de televisión que contienen las bases de datos como las que usa el protocolo [PAWS](https://tools.ietf.org/html/rfc7545). Información que brinda grandes oportunidades para un uso eficiente del espectro.

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local:_

* Puedes clonar el repositorio [aqui](https://github.com/danialeresbar/Simulation_EPI) o descargar las fuentes en un archivo comprimido.

* Ahora que tienes los fuentes de Specx, antes de ejecutar por primera vez el software debes tener instaladas las siguientes librerías y dependencias en tu máquina.

### Pre-requisitos 📋

_Specx está desarrollado completamente en Python, lenguaje que dispone de una gran variedad de librerías para diferentes áreas._

#### Python

En primer lugar, asegúrese de que Python 3 esté disponible en su sistema. Puede verificar esto fácilmente abriendo la terminal e ingresando el comando python3. Si necesita instalarlo, en caso de usar Windows consulte la [página de inicio](https://www.python.org/downloads/) de Python y descargue la versión 3.7, o instálelo con homebrew (brew install python3) en OS X, o su administrador de paquetes de Linux favorito:

*$ sudo apt install python3.7*

__Las librerías usadas por este software son las siguientes:__

* PyQt5
* Pyqtgraph
* Numpy
* Scipy
* Matplotlib

__Las librerías anteriores no vienen por defecto con la instalación de la versión de Python especificada, librerías que son conocidas como "nativas". Librerías como:__

- Time
- Math
- Os
- Json
- Threading

### Instalación 🔧

_Los siguientes pasos se deben ejecutar para poder ejecutar Specx con todas sus funcionalidades:_

Una vez instalada la versión de Python, lo siguiente es la instalación de las librerías que no so son nativas. En primer lugar deberemos instalar PyQt en su última versión: PyQt5, el binding o ligadura directa de qt para Python, que nos permite uar a los módulos y plugins para el desarrollo de interfaces gráficas de usuario. Tanto la versión GPL como la comercial de PyQt5 pueden construirse a partir de paquetes fuente o instalarse desde wheels. Wheels es el formato de empaquetado estándar de Python para Python puro o módulos de extensión binaria como PyQt5. Solo se admiten Python v3.5 y versiones posteriores. Se proporcionan para Windows de 32 y 64 bits, macOS de 64 bits y Linux de 64 bits, plataformas para las cuales The Qt Company proporciona instaladores binarios. Los wheels se instalan utilizando el programa pip que se incluye con las versiones actuales de Python.

```
pip install PyQt5
```

SIP es una colección de herramientas que hace que sea muy fácil crear enlaces de Python para bibliotecas C y C ++. Fue desarrollado originalmente en 1998 para crear PyQt, los enlaces de Python para el kit de herramientas Qt, pero puede usarse para crear enlaces para cualquier biblioteca C o C ++. Se instala utilizando el programa pip

```
pip install sip
```

El paquete pyqt-tools tiene como objetivo proporcionar herramientas como el Qt designer en un paquete separado que es útil para los desarrolladores, mientras que los wheels oficiales PyQt5 se mantienen enfocadas en cumplir con las dependencias de las aplicaciones PyQt5. Puede isntalarlo con pip:

```
pip install pyqt5-tools
```

PyQtGraph es una librería de visualización de gráficas para Python que proporciona funcionalidades básicas que usualmente requieren las aplicaciones de ingeniería y ciencias. PyQtGraph hace un uso intensivo de la plataforma Qt GUI (a través de PyQt o PySide) por sus gráficos de alto rendimiento y de numpy para la gran cantidad de números. En particular, utiliza el marco GraphicsView de Qt. Hay muchas formas diferentes de instalar pyqtgraph, según sus necesidades:

La forma más común de instalar pyqtgraph es con pip:

```
pip install pyqtgraph
```

Para obtener acceso a las últimas funciones y correcciones de errores, clone pyqtgraph desde github:

```
git clone https://github.com/pyqtgraph/pyqtgraph
python setup.py install
```

NumPy es el paquete fundamental para la computación científica con Python. NumPy también se puede utilizar como un contenedor eficiente multidimensional de datos genéricos. Se pueden definir tipos de datos arbitrarios. Esto permite que NumPy se integre sin problemas y rápidamente con una amplia variedad de bases de datos. Está bajo la [licencia BSD](https://numpy.org/license.html#license) , lo que permite su reutilización con pocas restricciones. Puede isntalarlo con pip:

```
pip install numpy
```

La biblioteca Scipy depende de NumPy. Está diseñada para funcionar con matrices NumPy y proporciona muchas rutinas numéricas eficientes y fáciles de usar, como las rutinas para la integración y optimización numéricas. Juntos, se ejecutan en todos los sistemas operativos populares, se instalan rápidamente y son gratuitos. Puede isntalarlo con pip:

```
pip install scipy
```

Matplotlib es una biblioteca de trazado 2D para Python que produce cifras de calidad de publicación en una variedad de formatos impresos y entornos interactivos en todas las plataformas. Matplotlib se puede usar en scripts de Python, los shells de Python e IPython, el cuaderno Jupyter, los servidores de aplicaciones web y cuatro kits de herramientas de interfaz gráfica de usuario. Puede isntalarlo con pip:

```
pip install matplotlib
```


## Ejecutando las pruebas ⚙️

_Para ejecutar Specx por primera vez mira las siguientes instrucciones:_

* Dirígete por consola al directorio en el que se se encuentran las fuentes de Specx

* Ejecuta el siguiente comando:

```
python mainframe.py
```

Esto debería ser suficiente para iniciar el software, ya que el resto de scripts son importados en el momento en que sean necesarios.


## Construido con 🛠️

_Para el desarrollo de Specx se utilizaron las siguientes herramientas_

* [Qt](https://doc.qt.io/) - El framework para GUI usado


## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.


## Autores ✒️

_El equipo de trabajo que llevó a cabo el estudio de simulación, el cual hizo posible el desarrollo del software Specx está formado por las siguientes personas:_

* **Héctor Iván Reyes Moncayo** - *Formulación del problema y consideraciones al modelo* - [Director]()
* **Ángel Alfonso Cruz Roa** - *Modelo del sistema* - [Codirector]()
* **Daniel Alejandro Restrepo Barbosa** - *Proceso de muestreo y determinación de distribuciones de probabilidad, diseño y construcción de interfaces gráficas de usuario.* - [Analista]()
* **Siervo Francisco Rodríguez Castellanos** - *Codificación de algoritmos de simulación y optimización de rutinas* - [Desarrollador]()


## Licencia 📄

Este proyecto está bajo la Licencia [GPLv3](http://www.gnu.org/licenses/gpl-3.0.html).


## Expresiones de Gratitud 🎁

* A los directores de este proyecto. El doctor Ángel Cruz por sus aportes tan valiosos al modelo del sistema, sin el cual Specx no podría operar correctamente; además de la dedicación a la revisión de cada funcionalidad del software. El doctor Héctor Reyes por sus conocimientos en el área de telecomunicaciones y radiotransmisiones, ya que su idea de un radio tvws fue la que llevó al desarrollo de Specx.

* A Francisco Rodríguez por sus habilidades en el desarrollo, que permitieron la construcción de varios generadores de variables aleaotorias, así como la optimización en el uso de recursos por parte de la aplicación.

* A la universidad de los llanos por brindar sus espacios y material bibliográfico para el estudio de simulación realizado.

