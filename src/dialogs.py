from modules.qt.dialogs_qt_ui import UiConfigDialog, QtWidgets


# ---- Bernoulli Distribution ----
SUCCESS_PROB_LABEL = 'Probabilidad\nde exito:'


# ---- Beta Distribution ----
BETA_SHAPE_1_LABEL = 'Parámetro de\nforma alpha:'
BETA_SHAPE_2_LABEL = 'Parámetro de\nforma beta:'


# ---- Uniform Distribution ----
UNIFORM_INF_LABEL = 'Parámetro de\ncota inferior:'
UNIFORM_SUP_LABEL = 'Parámetro de\ncota superior:'


class ParametrizationDialog(UiConfigDialog, QtWidgets.QDialog):
    """
    Class with the required components for the parameterization of a probability distribution assigned to a channel
    """

    def __init__(self, *args, **kwargs):
        super(ParametrizationDialog, self).__init__(*args)
        self.setupUi(self)  # Build the GUI designed with Qt designer

        self.distribution = kwargs.get('distribution', None)
        self.setup_dialog_components()
        self.plot_chart_preview()

        # Button signals connection
        # self.btn_submit.clicked.connect(self.pick_spinbox_values)
        self.btn_reject.clicked.connect(self.close)
        self.radiobtn_1.toggled.connect(self.__radiobtn_checked)
        self.radiobtn_2.toggled.connect(self.__radiobtn_checked)
        self.radiobtn_3.toggled.connect(self.__radiobtn_checked)

        # Spin signals connection
        self.parameter_spbox_1.valueChanged.connect(self.plot_chart_preview)
        self.parameter_spbox_2.valueChanged.connect(self.plot_chart_preview)
        self.parameter_spbox_3.valueChanged.connect(self.plot_chart_preview)
        self.parameter_spbox_4.valueChanged.connect(self.plot_chart_preview)

        self.setWindowTitle(f'{self.distribution.name} Distribution')

    def closeEvent(self, event):
        """
        Override of the closeEvent method to close the window
        """
        self.reject()
        event.accept()

    def update_distribution_parameters_value(self):
        for spbox, parameter in zip(self.spboxes, self.distribution.parameters):
            parameter.set_value(spbox.value())

    def __show_radio_buttons(self, f1, f2, f3):
        self.radiobtn_1.setVisible(f1)
        self.radiobtn_2.setVisible(f2)
        self.radiobtn_3.setVisible(f3)

    def __show_params(self, f1, f2, f3, f4):
        """
        Allows you to view the parameters according to the selected distribution
        """
        self.parameter_spbox_1.setVisible(f1)
        self.parameter_label_1.setVisible(f1)
        self.parameter_spbox_2.setVisible(f2)
        self.parameter_label_2.setVisible(f2)
        self.parameter_spbox_3.setVisible(f3)
        self.parameter_label_3.setVisible(f3)
        self.parameter_spbox_4.setVisible(f4)
        self.parameter_label_4.setVisible(f4)

    def __radiobtn_checked(self):
        radiobtn = self.sender()
        if radiobtn.isChecked() and radiobtn.text() == '1P':
            self.__show_params(True, False, False, False)

        elif radiobtn.isChecked() and radiobtn.text() == '2P':
            self.__show_params(True, True, False, False)

        elif radiobtn.isChecked() and radiobtn.text() == '3P':
            self.__show_params(True, True, True, False)

    def plot_chart_preview(self):
        """
        Method
        :return:
        """
        self.update_distribution_parameters_value()
        self.distribution.plot_chart()
        self.pdf_chartview.setChart(self.distribution.chart)

    def setup_dialog_components(self):
        """
        Method
        :return:
        """
        for index, parameter in enumerate(self.distribution.parameters):
            self.parameter_labels[index].setText(f'{parameter.name} \nparameter:')
            self.spboxes[index].setMinimum(parameter.range[0])
            self.spboxes[index].setMaximum(parameter.range[1])
            self.spboxes[index].setValue(parameter.value)
