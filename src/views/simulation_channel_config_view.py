import qtawesome as qta

from PySide6.QtCharts import QChartView
from PySide6.QtGui import QFont, QPainter, QPixmap, Qt
from PySide6.QtWidgets import (
    QComboBox, QDoubleSpinBox, QFrame, QGraphicsPixmapItem, QHBoxLayout, QLabel, QPlainTextEdit, QSizePolicy,
    QVBoxLayout, QWidget
)

from constants.ui import SPINBOX_DECIMAL_PLACES, SPINBOX_MINIMUM_DEFAULT, SPINBOX_MAXIMUM_DEFAULT, SPINBOX_STEP_DEFAULT
from models.distribution import ParameterInterval
from views.resources import icons_rc


class PDFChartView(QChartView):

    def __init__(self, *args, **kwargs):
        super(PDFChartView, self).__init__(*args, **kwargs)
        self.setRenderHint(QPainter.Antialiasing)


class ParameterConfigWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(ParameterConfigWidget, self).__init__(*args, **kwargs)
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
        self.label.setText('Parameter:')
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


class ChannelConfigView(QWidget):
    """
    This class is responsible for displaying the channel config components.
    """

    def __init__(self, *args, **kwargs):
        super(ChannelConfigView, self).__init__(*args, **kwargs)
        main_layout = QVBoxLayout(self)
        main_layout.setObjectName(u'vertical_Layout')
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # ComboBox icons
        self.continuous_function_icon = qta.icon('mdi6.chart-bell-curve')
        self.discrete_function_icon = qta.icon('mdi6.chart-bar')

        # Channel PDF ChartView
        self.default_chart_pixmap = QGraphicsPixmapItem(QPixmap(u":/assets/images/analytics.svg"))
        self.function_chart_view = PDFChartView(self)
        self.function_chart_view.setObjectName(u'channel_function_chart_view')
        main_layout.addWidget(self.function_chart_view)
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.function_chart_view.sizePolicy().hasHeightForWidth())
        self.function_chart_view.setSizePolicy(size_policy)
        self.function_chart_view.setFrameShape(QFrame.NoFrame)
        self.function_chart_view.setFrameShadow(QFrame.Raised)

        main_layout.addWidget(self.function_chart_view)

        self.function_config_frame = QFrame(self)
        self.function_config_frame.setObjectName(u"function_config_frame")
        self.function_config_frame.setFrameShape(QFrame.NoFrame)
        self.function_config_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.function_config_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 0, 12, 0)
        self.function_descriptor_frame = QFrame(self.function_config_frame)
        self.function_descriptor_frame.setObjectName(u"function_descriptor_frame")
        size_policy.setHeightForWidth(self.function_descriptor_frame.sizePolicy().hasHeightForWidth())
        self.function_descriptor_frame.setSizePolicy(size_policy)
        self.function_descriptor_frame.setFrameShape(QFrame.NoFrame)
        self.function_descriptor_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.function_descriptor_frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.function_descriptor_area_frame = QFrame(self.function_descriptor_frame)
        self.function_descriptor_area_frame.setObjectName(u"function_descriptor_area")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.function_descriptor_area_frame.sizePolicy().hasHeightForWidth())
        self.function_descriptor_area_frame.setSizePolicy(sizePolicy1)
        self.function_descriptor_area_frame.setFrameShape(QFrame.NoFrame)
        self.function_descriptor_area_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.function_descriptor_area_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.function_selector_label = QLabel(self.function_descriptor_area_frame)
        self.function_selector_label.setObjectName(u"function_selector_label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.function_selector_label.setFont(font)
        self.function_selector_label.setText('PDF:')

        self.horizontalLayout_2.addWidget(self.function_selector_label)

        self.function_selector_box = QComboBox(self.function_descriptor_area_frame)
        self.function_selector_box.setObjectName(u"function_selector_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.function_selector_box.sizePolicy().hasHeightForWidth())
        self.function_selector_box.setSizePolicy(sizePolicy2)
        self.function_selector_box.setFont(font)
        self.function_selector_box.setPlaceholderText('Select')

        self.horizontalLayout_2.addWidget(self.function_selector_box)
        self.verticalLayout_2.addWidget(self.function_descriptor_area_frame)

        self.function_description_area = QPlainTextEdit(self.function_descriptor_frame)
        self.function_description_area.setObjectName(u"function_description_area")
        self.function_description_area.setReadOnly(True)
        size_policy.setHeightForWidth(self.function_description_area.sizePolicy().hasHeightForWidth())
        self.function_description_area.setSizePolicy(size_policy)

        self.verticalLayout_2.addWidget(self.function_description_area)

        self.verticalLayout_2.setStretch(0, 50)
        self.verticalLayout_2.setStretch(1, 50)

        self.horizontalLayout.addWidget(self.function_descriptor_frame)

        self.function_parameters_frame = QFrame(self.function_config_frame)
        self.function_parameters_frame.setObjectName(u"function_parameters_frame")
        size_policy.setHeightForWidth(self.function_parameters_frame.sizePolicy().hasHeightForWidth())
        self.function_parameters_frame.setSizePolicy(size_policy)
        self.function_parameters_frame.setFrameShape(QFrame.NoFrame)
        self.function_parameters_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.function_parameters_frame)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        # Hidden PDF parameters
        self.function_available_parameters = []
        for _ in range(3):
            parameter_config = ParameterConfigWidget(self.function_parameters_frame)
            parameter_config.setVisible(False)
            self.verticalLayout_3.addWidget(parameter_config)
            self.function_available_parameters.append(parameter_config)

        self.horizontalLayout.addWidget(self.function_parameters_frame, 0, Qt.AlignVCenter)

        self.horizontalLayout.setStretch(0, 60)
        self.horizontalLayout.setStretch(1, 40)

        main_layout.addWidget(self.function_config_frame, 0, Qt.AlignBottom)

        main_layout.setStretch(0, 75)
        main_layout.setStretch(1, 25)


class DefaultChannelConfigView(QWidget):

    def __init__(self, *args, **kwargs):
        super(DefaultChannelConfigView, self).__init__(*args, **kwargs)
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.background_label = QLabel(self)
        self.background_label.setText('Select a channel to configure')
        self.background_label.setPixmap(QPixmap(u":/assets/images/settings.svg"))
        self.background_label.setScaledContents(True)
        main_layout.addWidget(self.background_label, 0, Qt.AlignCenter | Qt.AlignCenter)
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.background_label.sizePolicy().hasHeightForWidth())
