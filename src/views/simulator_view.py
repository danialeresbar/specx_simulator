# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import qtawesome as qta

from PySide6.QtCharts import QChart, QChartView
from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QPainter, QPixmap
from PySide6.QtWidgets import (
    QAbstractSpinBox, QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget
)

from constants.ui import COPYRIGHT_CAPTION, CURRENT_VERSION
from views.components.custom import ChannelGroupWidget, ChannelConfigStack


class SimulatorView:
    def setup_ui(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")

        main_window.resize(1366, 768)
        main_window.setMinimumSize(QSize(1366, 768))
        main_window.setStyleSheet(u"QFrame {\n""	border: none;\n""}")
        self.central_container = QWidget(main_window)
        self.central_container.setObjectName(u"central_container")
        self.verticalLayout = QVBoxLayout(self.central_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.central_container)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.theme_btn = QPushButton(self.header_left_frame)
        self.theme_btn.setCheckable(True)
        self.theme_btn.setObjectName(u"theme_btn")
        self.theme_btn.setIcon(qta.icon('mdi6.theme-light-dark'))

        self.horizontalLayout_3.addWidget(self.theme_btn, 0, Qt.AlignLeft)
        self.specx_icon = QLabel(self.header_left_frame)
        self.specx_icon.setObjectName(u"specx_icon")
        self.specx_icon.setPixmap(QPixmap(u":/feather/icons/activity.svg"))

        self.horizontalLayout_3.addWidget(self.specx_icon, 0, Qt.AlignRight)

        self.specx_label = QLabel(self.header_left_frame)
        self.specx_label.setObjectName(u"specx_label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.specx_label.setFont(font)

        self.horizontalLayout_3.addWidget(self.specx_label)

        self.horizontalLayout.addWidget(self.header_left_frame)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.minimize_btn = QPushButton(self.header_right_frame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setIcon(qta.icon('mdi6.window-minimize'))

        self.horizontalLayout_2.addWidget(self.minimize_btn)

        self.resize_btn = QPushButton(self.header_right_frame)
        self.resize_btn.setObjectName(u"resize_btn")
        self.resize_btn.setIcon(qta.icon('mdi6.window-maximize'))

        self.horizontalLayout_2.addWidget(self.resize_btn)

        self.close_btn = QPushButton(self.header_right_frame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setIcon(qta.icon('mdi6.close-box'))
        self.close_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.close_btn)
        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight)
        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.central_container)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.left_simulation_frame = QFrame(self.main_body_frame)
        self.left_simulation_frame.setObjectName(u"left_simulation_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_simulation_frame.sizePolicy().hasHeightForWidth())
        self.left_simulation_frame.setSizePolicy(sizePolicy1)
        self.left_simulation_frame.setFrameShape(QFrame.StyledPanel)
        self.left_simulation_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_simulation_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.charts_frame = QFrame(self.left_simulation_frame)
        self.charts_frame.setObjectName(u"charts_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.charts_frame.sizePolicy().hasHeightForWidth())
        self.charts_frame.setSizePolicy(sizePolicy2)
        self.charts_frame.setFrameShape(QFrame.StyledPanel)
        self.charts_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.charts_frame)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        # ChartView list
        self.charts = [QChart() for _ in range(9)]  # TODO: Use the available channels length
        self.chart_views = []
        for index, chart in enumerate(self.charts):
            chart.layout().setContentsMargins(3, 3, 3, 3)
            chart_view = QChartView(chart)
            chart_view.setRenderHint(QPainter.Antialiasing)
            row, col = divmod(index, 3)
            self.gridLayout_4.addWidget(chart_view, row, col, 1, 1)
            self.chart_views.append(chart_view)

        self.verticalLayout_2.addWidget(self.charts_frame)

        self.simulation_player_frame = QFrame(self.left_simulation_frame)
        self.simulation_player_frame.setObjectName(u"simulation_player_frame")
        self.simulation_player_frame.setFrameShape(QFrame.StyledPanel)
        self.simulation_player_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.simulation_player_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.simulation_player_control_frame = QFrame(self.simulation_player_frame)
        self.simulation_player_control_frame.setObjectName(u"simulation_player_control_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.simulation_player_control_frame.sizePolicy().hasHeightForWidth())
        self.simulation_player_control_frame.setSizePolicy(sizePolicy3)
        self.simulation_player_control_frame.setFrameShape(QFrame.StyledPanel)
        self.simulation_player_control_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.simulation_player_control_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.play_btn = QPushButton(self.simulation_player_control_frame)
        self.play_btn.setObjectName(u"play_btn")
        self.play_btn.setIcon(qta.icon('fa5s.play-circle'))
        self.play_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.play_btn)

        self.stop_btn = QPushButton(self.simulation_player_control_frame)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setIcon(qta.icon('fa5s.stop-circle'))
        self.stop_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.stop_btn)

        self.reset_speed_btn = QPushButton(self.simulation_player_control_frame)
        self.reset_speed_btn.setObjectName(u"reset_speed_btn")
        self.reset_speed_btn.setIcon(qta.icon('fa5s.fast-backward'))
        self.reset_speed_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.reset_speed_btn)

        self.decrease_speed_btn = QPushButton(self.simulation_player_control_frame)
        self.decrease_speed_btn.setObjectName(u"decrease_speed_btn")
        self.decrease_speed_btn.setIcon(qta.icon('fa5s.backward'))
        self.decrease_speed_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.decrease_speed_btn)

        self.speed_label = QLabel(self.simulation_player_control_frame)
        self.speed_label.setObjectName(u"speed_label")
        font1 = QFont()
        font1.setPointSize(16)
        self.speed_label.setFont(font1)

        self.horizontalLayout_10.addWidget(self.speed_label)

        self.increase_speed_btn = QPushButton(self.simulation_player_control_frame)
        self.increase_speed_btn.setObjectName(u"increase_speed_btn")
        self.increase_speed_btn.setIcon(qta.icon('fa5s.forward'))
        self.increase_speed_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.increase_speed_btn)

        self.max_speed_btn = QPushButton(self.simulation_player_control_frame)
        self.max_speed_btn.setObjectName(u"max_speed_btn")
        self.max_speed_btn.setIcon(qta.icon('fa5s.fast-forward'))
        self.max_speed_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.max_speed_btn)
        self.horizontalLayout_8.addWidget(self.simulation_player_control_frame, 0, Qt.AlignBottom)

        self.simulation_player_info_frame = QFrame(self.simulation_player_frame)
        self.simulation_player_info_frame.setObjectName(u"simulation_player_info_frame")
        self.simulation_player_info_frame.setFrameShape(QFrame.StyledPanel)
        self.simulation_player_info_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.simulation_player_info_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.simulation_status_label = QLabel(self.simulation_player_info_frame)
        self.simulation_status_label.setObjectName(u"simulation_status_label")
        font2 = QFont()
        font2.setPointSize(14)
        self.simulation_status_label.setFont(font2)

        self.horizontalLayout_9.addWidget(self.simulation_status_label)
        self.horizontalLayout_8.addWidget(self.simulation_player_info_frame, 0, Qt.AlignRight | Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.simulation_player_frame, 0, Qt.AlignBottom)
        self.horizontalLayout_7.addWidget(self.left_simulation_frame)

        self.right_simulation_frame = QFrame(self.main_body_frame)
        self.right_simulation_frame.setObjectName(u"right_simulation_frame")
        self.right_simulation_frame.setFrameShape(QFrame.StyledPanel)
        self.right_simulation_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.right_simulation_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.simulation_header_frame = QFrame(self.right_simulation_frame)
        self.simulation_header_frame.setObjectName(u"simulation_header_frame")
        self.simulation_header_frame.setFrameShape(QFrame.StyledPanel)
        self.simulation_header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.simulation_header_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.simulation_header_icon = QLabel(self.simulation_header_frame)
        self.simulation_header_icon.setObjectName(u"simulation_header_icon")
        self.simulation_header_icon.setPixmap(QPixmap(u":/feather/icons/settings.svg"))

        self.horizontalLayout_11.addWidget(self.simulation_header_icon, 0, Qt.AlignLeft)

        self.simulation_header_label = QLabel(self.simulation_header_frame)
        self.simulation_header_label.setObjectName(u"simulation_header_label")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.simulation_header_label.setFont(font4)

        self.horizontalLayout_11.addWidget(self.simulation_header_label, 0, Qt.AlignLeft)

        self.verticalLayout_3.addWidget(self.simulation_header_frame, 0, Qt.AlignLeft | Qt.AlignTop)

        self.simulation_settings_frame = QFrame(self.right_simulation_frame)
        self.simulation_settings_frame.setObjectName(u"simulation_settings_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.simulation_settings_frame.sizePolicy().hasHeightForWidth())
        self.simulation_settings_frame.setSizePolicy(sizePolicy4)
        self.simulation_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.simulation_settings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.simulation_settings_frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 12, 0)
        self.simulation_settings_parameters_frame = QFrame(self.simulation_settings_frame)
        self.simulation_settings_parameters_frame.setObjectName(u"simulation_settings_parameters_frame")
        self.simulation_settings_parameters_frame.setFrameShape(QFrame.StyledPanel)
        self.simulation_settings_parameters_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.simulation_settings_parameters_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 0)
        self.simulation_kind_frame = QFrame(self.simulation_settings_parameters_frame)
        self.simulation_kind_frame.setObjectName(u"simulation_kind_frame")
        self.simulation_kind_frame.setFrameShape(QFrame.StyledPanel)
        self.simulation_kind_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.simulation_kind_frame)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, -1, -1, 0)
        self.simulation_energy_selector_btn = QRadioButton(self.simulation_kind_frame)
        self.simulation_energy_selector_btn.setObjectName(u"simulation_energy_selector_btn")
        font5 = QFont()
        font5.setBold(True)
        self.simulation_energy_selector_btn.setFont(font5)

        self.horizontalLayout_13.addWidget(self.simulation_energy_selector_btn)

        self.simulation_occupancy_selector_btn = QRadioButton(self.simulation_kind_frame)
        self.simulation_occupancy_selector_btn.setObjectName(u"simulation_occupancy_selector_btn")
        self.simulation_occupancy_selector_btn.setFont(font5)

        self.horizontalLayout_13.addWidget(self.simulation_occupancy_selector_btn)

        self.verticalLayout_4.addWidget(self.simulation_kind_frame)

        self.simulation_parameters_frame = QFrame(self.simulation_settings_parameters_frame)
        self.simulation_parameters_frame.setObjectName(u"simulation_parameters_frame")
        self.simulation_parameters_frame.setFrameShape(QFrame.StyledPanel)
        self.simulation_parameters_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.simulation_parameters_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.simulation_sampling_label = QLabel(self.simulation_parameters_frame)
        self.simulation_sampling_label.setObjectName(u"simulation_sampling_label")
        self.simulation_sampling_label.setFont(font5)

        self.gridLayout.addWidget(self.simulation_sampling_label, 0, 0, 1, 1)

        self.simulation_sampling_box = QSpinBox(self.simulation_parameters_frame)
        self.simulation_sampling_box.setObjectName(u"simulation_sampling_box")
        self.simulation_sampling_box.setFont(font5)
        self.simulation_sampling_box.setAutoFillBackground(False)
        self.simulation_sampling_box.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.simulation_sampling_box.setSuffix(" min")
        self.simulation_sampling_box.setRange(1, 5)

        self.gridLayout.addWidget(self.simulation_sampling_box, 0, 1, 1, 1)

        self.simulation_threshold_label = QLabel(self.simulation_parameters_frame)
        self.simulation_threshold_label.setObjectName(u"simulation_threshold_label")
        self.simulation_threshold_label.setFont(font5)

        self.gridLayout.addWidget(self.simulation_threshold_label, 1, 0, 1, 1)

        self.simulation_threshold_box = QDoubleSpinBox(self.simulation_parameters_frame)
        self.simulation_threshold_box.setObjectName(u"simulation_threshold_box")
        self.simulation_threshold_box.setFont(font5)
        self.simulation_threshold_box.setRange(0.01, 0.99)
        self.simulation_threshold_box.setSingleStep(0.01)
        self.simulation_threshold_box.setValue(0.50)

        self.gridLayout.addWidget(self.simulation_threshold_box, 1, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.simulation_parameters_frame)
        self.horizontalLayout_12.addWidget(self.simulation_settings_parameters_frame)

        self.simulation_settings_buttons_frame = QFrame(self.simulation_settings_frame)
        self.simulation_settings_buttons_frame.setObjectName(u"simulation_settings_buttons_frame")
        self.simulation_settings_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.simulation_settings_buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.simulation_settings_buttons_frame)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.save_simulation_settings_btn = QPushButton(self.simulation_settings_buttons_frame)
        self.save_simulation_settings_btn.setObjectName(u"save_simulation_settings_btn")
        self.save_simulation_settings_btn.setIcon(qta.icon('mdi6.content-save-settings'))
        self.save_simulation_settings_btn.setIconSize(QSize(32, 32))
        self.save_simulation_settings_btn.setEnabled(False)

        self.horizontalLayout_14.addWidget(self.save_simulation_settings_btn)

        self.load_simulation_settings_btn = QPushButton(self.simulation_settings_buttons_frame)
        self.load_simulation_settings_btn.setObjectName(u"load_simulation_settings_btn")
        self.load_simulation_settings_btn.setIcon(qta.icon('mdi6.file-upload'))
        self.load_simulation_settings_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_14.addWidget(self.load_simulation_settings_btn)
        self.horizontalLayout_12.addWidget(self.simulation_settings_buttons_frame, 0, Qt.AlignBottom)
        self.verticalLayout_3.addWidget(self.simulation_settings_frame)

        self.simulation_environment_frame = QFrame(self.right_simulation_frame)
        self.simulation_environment_frame.setObjectName(u"simulation_environment_frame")
        self.simulation_environment_frame.setFrameShape(QFrame.StyledPanel)
        self.simulation_environment_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.simulation_environment_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.channel_config_stack_area = ChannelConfigStack(self.simulation_environment_frame)
        self.channel_config_stack_area.setObjectName(u"channel_config_stack_area")

        self.verticalLayout_5.addWidget(self.channel_config_stack_area)

        self.simulation_channel_frame = QFrame(self.simulation_environment_frame)
        self.simulation_channel_frame.setObjectName(u"simulation_channel_frame")
        self.simulation_channel_frame.setFrameShape(QFrame.StyledPanel)
        self.simulation_channel_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.simulation_channel_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.channel_button_group_widget = ChannelGroupWidget(self.simulation_channel_frame)
        self.verticalLayout_6.addWidget(self.channel_button_group_widget)

        self.verticalLayout_5.addWidget(self.simulation_channel_frame)

        self.verticalLayout_3.addWidget(self.simulation_environment_frame)

        self.horizontalLayout_7.addWidget(self.right_simulation_frame)
        self.horizontalLayout_7.setStretch(0, 75)
        self.horizontalLayout_7.setStretch(1, 25)

        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.central_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.copyright_label = QLabel(self.footer_left_frame)
        self.copyright_label.setObjectName(u"copyright_label")

        self.horizontalLayout_5.addWidget(self.copyright_label, 0, Qt.AlignLeft)
        self.horizontalLayout_4.addWidget(self.footer_left_frame)

        self.footer_rigth_frame = QFrame(self.footer_frame)
        self.footer_rigth_frame.setObjectName(u"footer_rigth_frame")
        self.footer_rigth_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_rigth_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_rigth_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.about_button = QPushButton(self.footer_rigth_frame)
        self.about_button.setObjectName(u"about_button")

        self.horizontalLayout_6.addWidget(self.about_button, 0, Qt.AlignRight)
        self.horizontalLayout_4.addWidget(self.footer_rigth_frame)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.size_grip, 0, Qt.AlignBottom)
        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        main_window.setCentralWidget(self.central_container)
        self.retranslate_ui(main_window)
        QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.specx_icon.setText("")
        self.specx_label.setText(QCoreApplication.translate("MainWindow", u"SPECX SIMULATOR", None))
        self.minimize_btn.setText("")
        self.resize_btn.setText("")
        self.close_btn.setText("")
        self.play_btn.setText("")
        self.stop_btn.setText("")
        self.reset_speed_btn.setText("")
        self.decrease_speed_btn.setText("")
        self.speed_label.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.increase_speed_btn.setText("")
        self.max_speed_btn.setText("")
        self.simulation_status_label.setText(QCoreApplication.translate("MainWindow", u"Running", None))
        self.simulation_header_icon.setText("")
        self.simulation_header_label.setText(QCoreApplication.translate("MainWindow", u"Simulation environment", None))
        self.simulation_energy_selector_btn.setText(QCoreApplication.translate("MainWindow", u"Energy", None))
        self.simulation_occupancy_selector_btn.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.simulation_sampling_label.setText(QCoreApplication.translate("MainWindow", u"Sampling:", None))
        self.simulation_threshold_label.setText(QCoreApplication.translate("MainWindow", u"Threshold:", None))
        self.save_simulation_settings_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.load_simulation_settings_btn.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.copyright_label.setText(QCoreApplication.translate(
            "MainWindow", f"Version {CURRENT_VERSION} | {COPYRIGHT_CAPTION}", None)
        )
        self.about_button.setText(QCoreApplication.translate("MainWindow", u"?", None))
