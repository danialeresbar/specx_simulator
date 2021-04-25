from PyQt5 import QtWidgets

from src.qt.dialog import DialogTemplate
# from src.charts import stats


class ParametrizationDialog(QtWidgets.QDialog, DialogTemplate):
    """
    Class used for the construction of a dialog box that allows
    the parameterization of a probability distribution
    """

    def __init__(self, *args, **kwargs):
        self.distribution = kwargs.get('distribution', None)
        super(ParametrizationDialog, self).__init__(*args)
        self.setup(self)                                        # Build the GUI designed with Qt designer assistant

        # Signals
        self._connect_button_signals()
        self._connect_spinner_signals()

        # Components
        self._setup_parameters()
        self._update_chart_preview()

    def _connect_button_signals(self):
        """
        Button signal connection
        """

        self.btn_submit.clicked.connect(self.accept)
        self.btn_reject.clicked.connect(self.close)
        # self.radiobtn_1.toggled.connect(self.__radiobtn_checked)
        # self.radiobtn_2.toggled.connect(self.__radiobtn_checked)
        # self.radiobtn_3.toggled.connect(self.__radiobtn_checked)

    def _connect_spinner_signals(self):
        """
        Spinner signal connection
        """

        # Spin signals connection
        for spinner in self.parameter_spinners:
            spinner.valueChanged.connect(self._update_chart_preview)

    def _setup_parameters(self):
        """

        """

        for index, parameter in enumerate(self.distribution.parameters):
            self.parameter_labels[index].setText(f'{parameter.name} \nparameter:')
            self.parameter_labels[index].setVisible(True)
            # self.parameter_spinners[index].setMinimum(parameter.range[0])
            # self.parameter_spinners[index].setMaximum(parameter.range[1])
            self.parameter_spinners[index].setValue(parameter.value)
            self.parameter_spinners[index].setVisible(True)

    def _update_chart_preview(self):
        """

        """

        self._update_parameter_values()
        chart = self.distribution.pdf_chart(

        )
        self.chart_preview.setChart(chart)

    def _update_parameter_values(self):
        for spinner, parameter in zip(self.parameter_spinners, self.distribution.parameters):
            parameter.set_value(spinner.value())

    def closeEvent(self, event):
        """
        Override of the closeEvent method to close the window
        """

        self.reject()
        event.accept()


class CloseWindowDialog(QtWidgets.QDialog):
    """
    Class used for the construction of a dialog box that allows
    confirmation of the closing of a window
    """

    def __init__(self, *args, **kwargs):
        super(CloseWindowDialog, self).__init__(*args)
