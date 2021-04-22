from qt.dialogs_qt_ui import UiConfigDialog, QtWidgets
from charts.charts import PDFChart


class ParametrizationDialog(UiConfigDialog, QtWidgets.QDialog):
    """
    Class with the required components for the parameterization of a probability distribution assigned to a channel
    """

    def __init__(self, *args, **kwargs):
        super(ParametrizationDialog, self).__init__(*args)
        self.setupUi(self)  # Build the GUI designed with Qt designer

        self.distribution = kwargs.get('distribution', None)
        self.distribution_chart = PDFChart(
            title=f'''
                    Probability Density Function
                    <center><small>{self.distribution.name} Distribution</small></center>
            ''',
            parameters=self.distribution.parameters
        )
        self.setWindowTitle(f'{self.distribution.name} Distribution')
        self.hide_parameter_rows()
        self.setup_dialog_components()
        self.plot_chart_preview()

        # Button signals connection
        self.btn_submit.clicked.connect(self.accept)
        self.btn_reject.clicked.connect(self.close)
        # self.radiobtn_1.toggled.connect(self.__radiobtn_checked)
        # self.radiobtn_2.toggled.connect(self.__radiobtn_checked)
        # self.radiobtn_3.toggled.connect(self.__radiobtn_checked)

        # Spin signals connection
        self.parameter_spbox_1.valueChanged.connect(self.plot_chart_preview)
        self.parameter_spbox_2.valueChanged.connect(self.plot_chart_preview)
        self.parameter_spbox_3.valueChanged.connect(self.plot_chart_preview)
        self.parameter_spbox_4.valueChanged.connect(self.plot_chart_preview)

    def closeEvent(self, event):
        """
        Override of the closeEvent method to close the window
        """
        self.reject()
        event.accept()

    def hide_parameter_rows(self):
        for label, spbox in zip(self.parameter_labels, self.spboxes):
            label.setVisible(False)
            spbox.setVisible(False)

    def hide_radiobtn_rows(self):
        self.radiobtn_1.setVisible(False)
        self.radiobtn_2.setVisible(False)
        self.radiobtn_3.setVisible(False)

    def update_distribution_parameters(self):
        for spbox, parameter in zip(self.spboxes, self.distribution.parameters):
            parameter.set_value(spbox.value())

    def plot_chart_preview(self):
        """
        Method
        :return:
        """
        self.update_distribution_parameters()
        self.distribution.plot_pdfchart(self.distribution_chart)
        self.pdf_chartview.setChart(self.distribution_chart)

    def setup_dialog_components(self):
        """
        Method
        :return:
        """
        for index, parameter in enumerate(self.distribution.parameters):
            self.parameter_labels[index].setText(f'{parameter.name} \nparameter:')
            self.parameter_labels[index].setVisible(True)
            self.spboxes[index].setMinimum(parameter.range[0])
            self.spboxes[index].setMaximum(parameter.range[1])
            self.spboxes[index].setValue(parameter.value)
            self.spboxes[index].setVisible(True)

        if self.distribution.variant:
            pass

        else:
            self.hide_radiobtn_rows()
