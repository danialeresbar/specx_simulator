from PySide6.QtCharts import QChart, QChartView
from PySide6.QtGui import QFont, QPainter
from PySide6.QtWidgets import (
    QButtonGroup,
    QDoubleSpinBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget
)

from constants.simulation import DECIMAL_PLACES
from constants.ui import (
    PARAMETER_LABEL_DEFAULT,
    SPINBOX_MINIMUM_DEFAULT,
    SPINBOX_MAXIMUM_DEFAULT,
    SPINBOX_STEP_DEFAULT
)
from models.distribution import ParameterInterval


class ChannelGroupWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        main_layout = QGridLayout(self)
        main_layout.setSpacing(5)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_group = QButtonGroup(self)

    def initialize_buttons(self, button_labels: list[str]) -> None:
        """
        Initialize the buttons of the group. The buttons are added to the button
        group and the button group is added to the layout.

        :param button_labels: The labels for the buttons.

        :return: None
        """
        # TODO: Check how to handle the layout distribution
        for index, label in enumerate(button_labels):
            button: QPushButton = QPushButton(self)
            button.setText(label)
            button.setCheckable(True)
            self.btn_group.addButton(button, index + 1)
            row, col = divmod(index, 4)
            self.layout().addWidget(button, row, col, 1, 1)


class ChannelConfigStack(QStackedWidget):
    """
    This class is responsible for displaying the channel config components. The
    channel stack is a widget that allows the user to config the channels of
    the simulation.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFrameShape(QFrame.NoFrame)
        self.setFrameShadow(QFrame.Raised)

    def clear(self) -> None:
        """
        Remove all the widgets from the stack.

        :return: None
        """
        while self.count():
            widget: QWidget = self.widget(0)
            self.removeWidget(widget)
            widget.deleteLater()


class ChartPreviewFrame(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFrameShape(QFrame.NoFrame)
        self.setFrameShadow(QFrame.Raised)
        self.content_layout = QVBoxLayout(self)
        self.chart_view = QChartView(self)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.content_layout.addWidget(self.chart_view, 0)
        self.content_layout.setContentsMargins(0, 0, 0, 0)

    def get_current_chart(self) -> QChart | None:
        current_chart = self.chart_view.chart()
        if len(current_chart.series()) == 0:
            return None

        return current_chart

    def set_chart(self, chart: QChart):
        self.chart_view.setChart(chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.show()

    def set_default_content(self):
        self.chart_view.setChart(QChart())


class ParameterConfigWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        main_layout = QHBoxLayout(self)
        main_layout.setObjectName(u'horizontal_Layout')
        main_layout.setSpacing(2)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self)
        self.label.setObjectName(u'label')
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText(PARAMETER_LABEL_DEFAULT)
        main_layout.addWidget(self.label)

        self.value_field = QDoubleSpinBox(self)
        self.value_field.setObjectName(u'value_field')
        self.value_field.setFont(font)
        self.value_field.setMinimum(SPINBOX_MINIMUM_DEFAULT)
        self.value_field.setMaximum(SPINBOX_MAXIMUM_DEFAULT)
        self.value_field.setDecimals(DECIMAL_PLACES)
        self.value_field.setSingleStep(SPINBOX_STEP_DEFAULT)
        main_layout.addWidget(self.value_field)

    def set_value_field_interval(self, interval: ParameterInterval) -> None:
        minimum, maximum = interval
        if minimum is not None:
            if minimum == 0:
                self.value_field.setMinimum(1e-3)
            else:
                self.value_field.setMinimum(minimum)
        else:
            self.value_field.setMinimum(-1e5)

        if maximum:
            self.value_field.setMaximum(maximum)
        else:
            self.value_field.setMaximum(1e5)
