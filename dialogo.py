from distro import *

class Distribution(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        # Contruye la maqueta básica del diálogo con base en el archivo de qt
        self.setupUi(self)

        self.parameters = [self.param_1.value(), self.param_2.value(), self.param_3.value(), self.param_4.value()]

        # callback para la gráfica de la distribución seleccionada
        self.callback_plot = None

        # Conexión de eventos para los botones
        #self.reset.clicked.connect(self.default_values)
        self.submit.clicked.connect(self.pick_params)

        for param in self.params:
            param.valueChanged.connect(self.plot_preview)

    # Sobre-escritura del método closeEvent para el cierre del cuadro de diálogo
    def closeEvent(self, event):
        self.reject()
        event.accept()

    # Recogida de parámetros de la distribución correspondiente
    def pick_params(self, counter):
        self.parameters = [self.param_1.value(), self.param_2.value(), self.param_3.value(), self.param_4.value()]
        self.accept()

    # Reinicio de valores en los parámetros
    def default_values(self, values):
        self.param_1.setValue(self.param_1.minimum())
        self.param_2.setValue(self.param_2.minimum())
        self.param_3.setValue(self.param_3.minimum())
        self.param_4.setValue(self.param_4.minimum())

    # Actualiza los componentes que se deberían mostrar en el modal
    def update_view(self, f1, f2, f3, f4, n):
        # Limpieza del canvas
        self.canvas_lienzo.clean()

        # Visualización de las etiquetas según la distribución
        self.label_1.setVisible(f1)
        self.label_2.setVisible(f2)
        self.label_3.setVisible(f3)
        self.label_4.setVisible(f4)

        # Visualización de los spinbox según la distribución
        self.param_1.setVisible(f1)
        self.param_2.setVisible(f2)
        self.param_3.setVisible(f3)
        self.param_4.setVisible(f4)

    # Actualiza el plot según los parámetros recogidos en el modal
    def plot_preview(self):
        spin_values = [self.param_1.value(), self.param_2.value(), self.param_3.value(), self.param_4.value()]
        self.callback_plot(spin_values)

    # Recolección de parámetros para una distribución de bernoulli
    def bernoulli(self):
        self.callback_plot = self.canvas_lienzo.plot_bernoulli

        # Manejo de la interfaz del modal
        self.description.setPixmap(QtGui.QPixmap("./icons/bern.png"))
        self.update_view(True, False, False, False, 1)
        self.label_1.setText("Succes_prob:")
        self.param_1.setMinimum(0)
        self.param_1.setMaximum(1)
        self.param_1.setValue(0.5)
        
        return "bernoulli"

    # Recolección de parámetros para una distribución beta
    def beta(self):
        self.callback_plot = self.canvas_lienzo.plot_beta

        # Manejo de la interfaz del modal
        
        self.description.setPixmap(QtGui.QPixmap("./icons/beta.png"))
        self.update_view(True, True, True, True, 4)
        self.label_1.setText("Alpha_shape:")
        self.label_2.setText("Beta_shape:")
        self.label_3.setText("Min:")
        self.label_4.setText("Max:")
        self.param_1.setMinimum(0.00000001)
        self.param_1.setMaximum(100000)
        self.param_2.setMinimum(0.00000001)
        self.param_2.setMaximum(100000)
        self.param_3.setMinimum(-1000000)
        self.param_3.setMaximum(100000)
        self.param_4.setMinimum(0.00000001)
        self.param_4.setMaximum(100)
        self.param_1.setValue(3.9285)
        self.param_2.setValue(4.5943)
        self.param_3.setValue(0.04399)
        self.param_4.setValue(0.75)

        return "beta"

    # Recolección de parámetros para una distribución gamma
    def gamma(self):
        # Esto está relacionado con lo que no me acuerdo jajajaja
        self.callback_plot = self.canvas_lienzo.plot_gamma

        # Manejo de la interfaz del modal
        self.description.setPixmap(QtGui.QPixmap("./icons/gamma.png"))
        self.update_view(True, True, False, False, 2)
        self.label_1.setText("Alpha_shape:")
        self.label_2.setText("Lambda_scale:")
        self.param_1.setMinimum(0.00000001)
        self.param_1.setMaximum(100)
        self.param_2.setMinimum(0.00000001)
        self.param_1.setValue(64.423)
        self.param_2.setValue(0.00988)

        return "gamma"

    # Recolección de parámetros para una distribución gumbel
    def gumbel(self):
        # Esto está relacionado con lo que no me acuerdo jajajaja
        self.callback_plot = self.canvas_lienzo.plot_gumbel

        # Manejo de la interfaz del modal
        self.description.setPixmap(QtGui.QPixmap("./icons/gumbel.png"))
        self.update_view(True, True, False, False, 2)
        self.label_1.setText("Mean:")
        self.label_2.setText("Scale:")
        self.param_1.setMinimum(0.00000001)
        self.param_1.setMaximum(10)
        self.param_2.setMinimum(0.00000001)
        self.param_1.setValue(0.59583)
        self.param_2.setValue(0.04929)

        return "gumbel"

    # Recolección de parámetros para una distribución de laplace
    def laplace(self):
        # Esto está relacionado con lo que no me acuerdo jajajaja
        self.callback_plot = self.canvas_lienzo.plot_laplace

        # Manejo de la interfaz del modal
        self.description.setPixmap(QtGui.QPixmap("./icons/laplace.png"))
        self.update_view(True, True, False, False, 2)
        self.label_1.setText("Mean:")
        self.label_2.setText("S_deviation:")
        self.param_1.setMinimum(-0.5)
        self.param_1.setMaximum(100)
        self.param_2.setMinimum(0.00000001)
        self.param_1.setValue(0.60998)
        self.param_2.setValue(1/22.912)

        return "laplace"

    # Recolección de parámetros para una distribución lognormal
    def lognorm(self):
        # Esto está relacionado con lo que no me acuerdo jajajaja
        self.callback_plot = self.canvas_lienzo.plot_lognormal

        # Manejo de la interfaz del modal
        self.description.setPixmap(QtGui.QPixmap("./icons/lognorm.png"))
        self.update_view(True, True, False, False, 2)
        self.label_1.setText("Mean:")
        self.label_2.setText("S_deviation:")
        self.param_1.setMinimum(-10)
        self.param_1.setMaximum(100)
        self.param_2.setMinimum(0.00000001)
        self.param_1.setValue(-0.53468)
        self.param_2.setValue(0.18814)

        return "lognormal"

    # Recolección de parámetros para una distribución lognormal 3p
    def lognorm3p(self):
        # Esto está relacionado con lo eque no me acuerdo jajajaja
        self.callback_plot = self.canvas_lienzo.plot_lognormal_3p

        # Manejo de la interfaz del modal
        self.description.setPixmap(QtGui.QPixmap("./icons/lognorm_3.png"))
        self.update_view(True, True, True, False, 3)
        self.label_1.setText("Mean:")
        self.label_2.setText("S_deviation:")
        self.label_3.setText("Threshold:")
        self.param_1.setMinimum(-5)
        self.param_1.setMaximum(100)
        self.param_2.setMinimum(0.00000001)
        self.param_3.setMinimum(-10)
        self.param_1.setValue(-1.4383)
        self.param_2.setValue(0.50186)
        self.param_3.setValue(-0.00345)

        return "lognormal_3p"

    # Recolección de parámetros para una distribución normal
    def normal(self):
        # Esto está relacionado con lo que no me acuerdo jajajaja
        self.callback_plot = self.canvas_lienzo.plot_normal

        # Manejo de la interfaz del modal
        self.description.setPixmap(QtGui.QPixmap("./icons/normal.png"))
        self.update_view(True, True, False, False, 2)
        self.label_1.setText("Mean:")
        self.label_2.setText("S_deviation:")
        self.param_1.setMinimum(-1)
        self.param_1.setMaximum(100)
        self.param_2.setMinimum(0.00000001)
        self.param_1.setValue(0.18119)
        self.param_2.setValue(0.09331)

        return "normal"

    # Recolección de parámetros para una distribución de rayleigh
    def rayleigh(self):
        # Esto está relacionado con lo que no me acuerdo jajajaja
        self.callback_plot = self.canvas_lienzo.plot_rayleigh

        # Manejo de la interfaz del modal
        self.description.setPixmap(QtGui.QPixmap("./icons/rayleigh.png"))
        self.update_view(True, False, False, False, 1)
        self.label_1.setText("S_deviation:")
        self.param_1.setMinimum(0.00000001)
        self.param_1.setMaximum(100)
        self.param_1.setValue(0.15109)

        return "rayleigh"

    # Recolección de parámetros para una distribución de rayleigh
    def rayleigh2p(self):
        # Esto está relacionado con lo que no me acuerdo jajajaja
        self.callback_plot = self.canvas_lienzo.plot_rayleigh_2p

        # Manejo de la interfaz del modal
        self.description.setPixmap(QtGui.QPixmap("./icons/rayleigh_2.png"))
        self.update_view(True, True, False, False, 2)
        self.label_1.setText("S_deviation:")
        self.label_2.setText("Threshold:")
        self.param_1.setMinimum(0.00000001)
        self.param_1.setMaximum(100)
        self.param_2.setMinimum(-0.5)
        self.param_1.setValue(0.11641)
        self.param_2.setValue(0.05)

        return "rayleigh_2p"

    # Recolección de parámetros para una distribución uniforme
    def uniforme(self):
        # Esto está relacionado con lo que no me acuerdo jajajaja
        self.callback_plot = self.canvas_lienzo.plot_uniforme

        # Manejo de la interfaz del modal
        self.description.setPixmap(QtGui.QPixmap("./icons/uniform.png"))
        self.update_view(True, True, False, False, 2)
        self.label_1.setText("Lower bound:")
        self.label_2.setText("Upper bound:")
        self.param_1.setMinimum(0.00000001)
        self.param_2.setMinimum(0.00000001)
        self.param_1.setValue(0.2)
        self.param_2.setValue(0.5)

        return "uniform"

    # Recolección de parámetros para una distribución de weibull
    def weibull(self):
        # Esto está relacionado con lo que no me acuerdo jajajaja
        self.callback_plot = self.canvas_lienzo.plot_weibull

        # Manejo de la interfaz del modal
        self.description.setPixmap(QtGui.QPixmap("./icons/weibull.png"))
        self.update_view(True, True, True, False, 3)
        self.label_1.setText("K_shape:")
        self.label_2.setText("Lambda_scale:")
        self.label_3.setText("Threshold:")
        self.param_1.setMinimum(0.00000001)
        self.param_1.setMaximum(100000000)
        self.param_2.setMinimum(0.00000001)
        self.param_2.setMaximum(100000000)
        self.param_3.setMinimum(-100000000)
        self.param_3.setMaximum(100000000)
        self.param_1.setValue(4.2694)
        self.param_2.setValue(0.38947)
        self.param_3.setValue(-0.12532)

        return "weibull"
