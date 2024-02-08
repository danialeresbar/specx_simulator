from PySide6.QtCharts import QChart, QChartView
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap, QPainter
from PySide6.QtWidgets import QDoubleSpinBox, QFrame, QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout, QWidget

from constants.paths import UI_ASSETS_PATH
from constants.ui import (
    PARAMETER_LABEL_DEFAULT,
    SPINBOX_DECIMAL_PLACES,
    SPINBOX_MINIMUM_DEFAULT,
    SPINBOX_MAXIMUM_DEFAULT,
    SPINBOX_STEP_DEFAULT
)
from models.distribution import ParameterInterval


class ChartPreviewFrame(QFrame):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
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


class DefaultChannelConfigView(QWidget):

    def __init__(self, *args, **kwargs):
        super(DefaultChannelConfigView, self).__init__(*args, **kwargs)
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap(f'{UI_ASSETS_PATH}/img/settings.svg'))
        self.background_label.setScaledContents(True)
        main_layout.addWidget(self.background_label, 0, Qt.AlignCenter | Qt.AlignCenter)
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.background_label.sizePolicy().hasHeightForWidth())


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
        self.value_field.setDecimals(SPINBOX_DECIMAL_PLACES)
        self.value_field.setSingleStep(SPINBOX_STEP_DEFAULT)
        main_layout.addWidget(self.value_field)

    def set_value_field_interval(self, interval: ParameterInterval) -> None:
        minimum, maximum = interval
        if minimum is not None:
            self.value_field.setMinimum(minimum)
        else:
            self.value_field.setMinimum(-1e5)

        if maximum:
            self.value_field.setMaximum(maximum)
        else:
            self.value_field.setMaximum(1e5)
