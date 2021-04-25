from PyQt5 import QtWidgets

from src.qt.dialog import DialogTemplate
# from src.charts import stats


class ParametrizationDialog(QtWidgets.QDialog, DialogTemplate):
    """
    Class used for the construction of a dialog box that allows
    the parameterization of a probability distribution
    """

    def __init__(self, *args, **kwargs):
        super(ParametrizationDialog, self).__init__(*args)
        self.setup(self)                                        # Build the GUI designed with Qt designer assistant
        self.distribution = kwargs.get('distribution', None)
        self.distribution_chart = self.distribution.pdf_chart()
        # self.hide_parameter_rows()
        self.setup_dialog_components()
        self.plot_chart_preview()

        # Button signals connection
        self.btn_submit.clicked.connect(self.accept)
        self.btn_reject.clicked.connect(self.close)
        # self.radiobtn_1.toggled.connect(self.__radiobtn_checked)
        # self.radiobtn_2.toggled.connect(self.__radiobtn_checked)
        # self.radiobtn_3.toggled.connect(self.__radiobtn_checked)

        # Spin signals connection
        # for spinner in self.parameter_spinners:
        #     spinner.valueChanged.connect(self.plot_chart_preview())

    def closeEvent(self, event):
        """
        Override of the closeEvent method to close the window
        """

        self.reject()
        event.accept()

    def hide_parameter_rows(self):
        for label, spinner in zip(self.parameter_labels, self.parameter_spinners):
            label.setVisible(False)
            spinner.setVisible(False)

    # def hide_radiobtn_rows(self):
    #     self.radiobtn_1.setVisible(False)
    #     self.radiobtn_2.setVisible(False)
    #     self.radiobtn_3.setVisible(False)

    def update_distribution_parameters(self):
        for spinner, parameter in zip(self.parameter_spinners, self.distribution.parameters):
            parameter.set_value(spinner.value())

    def plot_chart_preview(self):
        """

        :return:
        """
        self.update_distribution_parameters()
        self.chart_preview.setChart(self.distribution_chart)

    def setup_dialog_components(self):
        """
        Method
        :return:
        """
        for index, parameter in enumerate(self.distribution.parameters):
            self.parameter_labels[index].setText(f'{parameter.name} \nparameter:')
            self.parameter_labels[index].setVisible(True)
            # self.parameter_spinners[index].setMinimum(parameter.range[0])
            # self.parameter_spinners[index].setMaximum(parameter.range[1])
            self.parameter_spinners[index].setValue(parameter.value)
            self.parameter_spinners[index].setVisible(True)


class CloseWindowDialog(QtWidgets.QDialog):
    """
    Class used for the construction of a dialog box that allows
    confirmation of the closing of a window
    """

    def __init__(self, *args, **kwargs):
        super(CloseWindowDialog, self).__init__(*args)
