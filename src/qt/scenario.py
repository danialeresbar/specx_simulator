from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChartView


CHARTVIEWS = 10


# ---- GUI fonts ----
MAIN_LABEL_FONT = QtGui.QFont()
MAIN_LABEL_FONT.setPointSizeF(8)
BUTTON_LABEL_FONT = QtGui.QFont()
BUTTON_LABEL_FONT.setPointSizeF(10)


class UiSimWindow(object):
    def setupUi(self, sim_window):
        sim_window.setObjectName("sim_window")
        sim_window.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sim_window.sizePolicy().hasHeightForWidth())
        sim_window.setSizePolicy(sizePolicy)
        sim_window.setMinimumSize(QtCore.QSize(1280, 720))
        sim_window.setMaximumSize(QtCore.QSize(1280, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sim_window.setWindowIcon(icon)

        sim_window.setStyleSheet("* {\n"
                                 "    background: #26282b;\n"
                                 "    color: #DDDDDD;\n"
                                 "    border: 1px solid #5A5A5A;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget::item:selected {\n"
                                 "    background: #3D7848;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton{\n"
                                 "    border: none;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox, QRadioButton {\n"
                                 "    border: none;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator, QCheckBox::indicator {\n"
                                 "    width: 13px;\n"
                                 "    height: 13px;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator::unchecked, QCheckBox::indicator::unchecked {\n"
                                 "    border: 1px solid #5A5A5A;\n"
                                 "    background: none;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:unchecked:hover, QCheckBox::indicator:unchecked:hover {\n"
                                 "    border: 1px solid #DDDDDD;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator::checked, QCheckBox::indicator::checked {\n"
                                 "    border: 1px solid #5A5A5A;\n"
                                 "    background: #5A5A5A;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:checked:hover, QCheckBox::indicator:checked:hover {\n"
                                 "    border: 1px solid #DDDDDD;\n"
                                 "    background: #DDDDDD;\n"
                                 "}\n"
                                 "\n"
                                 "QGroupBox {\n"
                                 "    margin-top: 6px;\n"
                                 "}\n"
                                 "\n"
                                 "QGroupBox::title {\n"
                                 "    subcontrol-origin: margin;\n"
                                 "    padding-left: 5px;\n"
                                 "    padding-right: 5px;\n"
                                 "    padding-top: 4px;\n"
                                 "    top: -7px;\n"
                                 "    left: 7px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar {\n"
                                 "    border: 1px solid #5A5A5A;\n"
                                 "    background: #191919;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:horizontal {\n"
                                 "    height: 15px;\n"
                                 "    margin: 0px 0px 0px 32px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:vertical {\n"
                                 "    width: 15px;\n"
                                 "    margin: 32px 0px 0px 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle {\n"
                                 "    background: #353535;\n"
                                 "    border: 1px solid #5A5A5A;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:horizontal {\n"
                                 "    border-width: 0px 1px 0px 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:vertical {\n"
                                 "    border-width: 1px 0px 1px 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:horizontal {\n"
                                 "    min-width: 20px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:vertical {\n"
                                 "    min-height: 20px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line, QScrollBar::sub-line {\n"
                                 "    background:#353535;\n"
                                 "    border: 1px solid #5A5A5A;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line {\n"
                                 "    position: absolute;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line:horizontal {\n"
                                 "    width: 15px;\n"
                                 "    subcontrol-position: left;\n"
                                 "    left: 15px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line:vertical {\n"
                                 "    height: 15px;\n"
                                 "    subcontrol-position: top;\n"
                                 "    top: 15px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-line:horizontal {\n"
                                 "    width: 15px;\n"
                                 "    subcontrol-position: top left;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-line:vertical {\n"
                                 "    height: 15px;\n"
                                 "    subcontrol-position: top;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:left-arrow, QScrollBar::right-arrow, QScrollBar::up-arrow, QScrollBar::down-arrow {\n"
                                 "    border: 1px solid #5A5A5A;\n"
                                 "    width: 3px;\n"
                                 "    height: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-page, QScrollBar::sub-page {\n"
                                 "    background: none;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractButton:disabled {\n"
                                 "	color: #787878;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractButton:hover {\n"
                                 "    background: #353535;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractButton:pressed {\n"
                                 "    background: #5A5A5A;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractItemView {\n"
                                 "    show-decoration-selected: 1;\n"
                                 "    selection-background-color: #3D7848;\n"
                                 "    selection-color: #DDDDDD;\n"
                                 "    alternate-background-color: #353535;\n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView {\n"
                                 "    border: 1px solid #5A5A5A;\n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView::section {\n"
                                 "    background: #191919;\n"
                                 "    border: 1px solid #5A5A5A;\n"
                                 "    padding: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView::section:selected, QHeaderView::section::checked {\n"
                                 "    background: #353535;\n"
                                 "}\n"
                                 "\n"
                                 "QTableView {\n"
                                 "    gridline-color: #5A5A5A;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar {\n"
                                 "    margin-left: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab {\n"
                                 "    border-radius: 0px;\n"
                                 "    padding: 4px;\n"
                                 "    margin: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:selected {\n"
                                 "    background: #353535;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::down-arrow {\n"
                                 "    border: 1px solid #5A5A5A;\n"
                                 "    background: #353535;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::drop-down {\n"
                                 "    border: 1px solid #5A5A5A;\n"
                                 "    background: #353535;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::down-arrow {\n"
                                 "    width: 3px;\n"
                                 "    height: 3px;\n"
                                 "    border: 1px solid #5A5A5A;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractSpinBox {\n"
                                 "    padding-right: 15px;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractSpinBox::up-button, QAbstractSpinBox::down-button {\n"
                                 "    border: 1px solid #5A5A5A;\n"
                                 "    background: #353535;\n"
                                 "    subcontrol-origin: border;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractSpinBox::up-arrow, QAbstractSpinBox::down-arrow {\n"
                                 "    width: 3px;\n"
                                 "    height: 3px;\n"
                                 "    border: 1px solid #5A5A5A;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider {\n"
                                 "    border: none;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::groove:horizontal {\n"
                                 "    height: 5px;\n"
                                 "    margin: 4px 0px 4px 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::groove:vertical {\n"
                                 "    width: 5px;\n"
                                 "    margin: 0px 4px 0px 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::handle {\n"
                                 "    border: 1px solid #5A5A5A;\n"
                                 "    background: #353535;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::handle:horizontal {\n"
                                 "    width: 15px;\n"
                                 "    margin: -4px 0px -4px 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::handle:vertical {\n"
                                 "    height: 15px;\n"
                                 "    margin: 0px -4px 0px -4px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::add-page:vertical, QSlider::sub-page:horizontal {\n"
                                 "    background: #3D7848;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::sub-page:vertical, QSlider::add-page:horizontal {\n"
                                 "    background: #353535;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel {\n"
                                 "    border: none;\n"
                                 "}\n"
                                 "\n"
                                 "QProgressBar {\n"
                                 "    text-align: center;\n"
                                 "}\n"
                                 "\n"
                                 "QProgressBar::chunk {\n"
                                 "    width: 1px;\n"
                                 "    background-color: #3D7848;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::separator {\n"
                                 "    background: #353535;\n"
                                 "}")

        self.container = QtWidgets.QWidget(sim_window)
        self.container.setObjectName("container")
        self.container_layout = QtWidgets.QVBoxLayout(self.container)
        self.container_layout.setContentsMargins(10, 10, 10, 10)
        self.container_layout.setSpacing(5)

        self.tools_layout = QtWidgets.QHBoxLayout()
        self.tools_layout.setSpacing(5)

        self.start_button_widget = QtWidgets.QWidget(self.container)
        self.start_button_widget_layout = QtWidgets.QHBoxLayout(self.start_button_widget)
        self.start_button_widget_layout.setSpacing(5)

        self.btn_start = QtWidgets.QPushButton(self.start_button_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setFont(BUTTON_LABEL_FONT)
        self.btn_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_start.setText("START")
        self.btn_start.setObjectName("btn_start")

        self.start_button_widget_layout.addWidget(self.btn_start)
        self.tools_layout.addWidget(self.start_button_widget)
        self.tools_layout.setStretch(0, 10)
        self.manager_widget = QtWidgets.QWidget(self.container)
        self.manager_widget_layout = QtWidgets.QHBoxLayout(self.manager_widget)
        self.manager_widget_layout.setSpacing(5)

        self.btn_play = QtWidgets.QPushButton(self.manager_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_play.sizePolicy().hasHeightForWidth())
        self.btn_play.setSizePolicy(sizePolicy)
        self.btn_play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        play_icon = QtGui.QIcon()
        play_icon.addPixmap(QtGui.QPixmap("../icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(play_icon)
        self.btn_play.setIconSize(QtCore.QSize(16, 16))
        self.btn_play.setFlat(True)
        self.btn_play.setObjectName("btn_play")
        self.manager_widget_layout.addWidget(self.btn_play)

        self.btn_pause = QtWidgets.QPushButton(self.manager_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pause.sizePolicy().hasHeightForWidth())
        self.btn_pause.setSizePolicy(sizePolicy)
        self.btn_pause.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pause_icon = QtGui.QIcon()
        pause_icon.addPixmap(QtGui.QPixmap("../icons/pause.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pause.setIcon(pause_icon)
        self.btn_pause.setIconSize(QtCore.QSize(16, 16))
        self.btn_pause.setObjectName("btn_pause")
        self.manager_widget_layout.addWidget(self.btn_pause)

        self.btn_stop = QtWidgets.QPushButton(self.manager_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_stop.sizePolicy().hasHeightForWidth())
        self.btn_stop.setSizePolicy(sizePolicy)
        self.btn_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        stop_icon = QtGui.QIcon()
        stop_icon.addPixmap(QtGui.QPixmap("../icons/stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(stop_icon)
        self.btn_stop.setIconSize(QtCore.QSize(16, 16))
        self.btn_stop.setObjectName("btn_stop")
        self.manager_widget_layout.addWidget(self.btn_stop)
        self.tools_layout.addWidget(self.manager_widget)

        self.time_widget = QtWidgets.QWidget(self.container)
        self.time_widget_layout = QtWidgets.QHBoxLayout(self.time_widget)
        self.time_widget_layout.setSpacing(5)

        self.btn_reset_speed = QtWidgets.QPushButton(self.time_widget)
        self.btn_reset_speed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        reset_speed_icon = QtGui.QIcon()
        reset_speed_icon.addPixmap(QtGui.QPixmap("../icons/reset.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reset_speed.setIcon(reset_speed_icon)
        self.btn_reset_speed.setIconSize(QtCore.QSize(16, 16))
        self.btn_reset_speed.setObjectName("btn_reset_speed")
        self.time_widget_layout.addWidget(self.btn_reset_speed)

        self.btn_decrease_speed = QtWidgets.QPushButton(self.time_widget)
        self.btn_decrease_speed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        decrease_speed_icon = QtGui.QIcon()
        decrease_speed_icon.addPixmap(QtGui.QPixmap("../icons/decrease.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_decrease_speed.setIcon(decrease_speed_icon)
        self.btn_decrease_speed.setIconSize(QtCore.QSize(16, 16))
        self.btn_decrease_speed.setObjectName("btn_decrease_speed")
        self.time_widget_layout.addWidget(self.btn_decrease_speed)

        self.speed_label = QtWidgets.QLabel(self.time_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_label.sizePolicy().hasHeightForWidth())
        self.speed_label.setSizePolicy(sizePolicy)
        self.speed_label.setFont(MAIN_LABEL_FONT)
        self.speed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_widget_layout.addWidget(self.speed_label)

        self.btn_increase_speed = QtWidgets.QPushButton(self.time_widget)
        self.btn_increase_speed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        increase_speed_icon = QtGui.QIcon()
        increase_speed_icon.addPixmap(QtGui.QPixmap("../icons/increase.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_increase_speed.setIcon(increase_speed_icon)
        self.btn_increase_speed.setIconSize(QtCore.QSize(16, 16))
        self.btn_increase_speed.setObjectName("btn_increase_speed")
        self.time_widget_layout.addWidget(self.btn_increase_speed)

        self.btn_max_speed = QtWidgets.QPushButton(self.time_widget)
        self.btn_max_speed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        max_speed_icon = QtGui.QIcon()
        max_speed_icon.addPixmap(QtGui.QPixmap("../icons/max.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_max_speed.setIcon(max_speed_icon)
        self.btn_max_speed.setIconSize(QtCore.QSize(16, 16))
        self.btn_max_speed.setObjectName("btn_max_speed")
        self.time_widget_layout.addWidget(self.btn_max_speed)

        spacer_item = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        self.time_widget_layout.setStretch(0, 20)
        self.time_widget_layout.setStretch(1, 20)
        self.time_widget_layout.setStretch(2, 20)
        self.time_widget_layout.setStretch(3, 20)
        self.time_widget_layout.setStretch(4, 20)

        self.tools_layout.addWidget(self.time_widget)
        self.tools_layout.addItem(spacer_item)

        self.file_manager_widget = QtWidgets.QWidget(self.container)
        self.file_manager_widget_layout = QtWidgets.QHBoxLayout(self.file_manager_widget)
        self.file_manager_widget_layout.setSpacing(5)

        self.btn_save_chart = QtWidgets.QPushButton(self.file_manager_widget)
        self.btn_save_chart.setFont(BUTTON_LABEL_FONT)
        self.btn_save_chart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        save_chart_icon = QtGui.QIcon()
        save_chart_icon.addPixmap(QtGui.QPixmap("../icons/chart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save_chart.setIcon(save_chart_icon)
        self.btn_save_chart.setIconSize(QtCore.QSize(16, 16))
        self.btn_save_chart.setFlat(True)
        self.btn_save_chart.setObjectName("btn_save_chart")
        self.file_manager_widget_layout.addWidget(self.btn_save_chart)

        self.btn_show_csvfile = QtWidgets.QPushButton(self.file_manager_widget)
        self.btn_show_csvfile.setFont(BUTTON_LABEL_FONT)
        self.btn_show_csvfile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_show_csvfile_icon = QtGui.QIcon()
        btn_show_csvfile_icon.addPixmap(QtGui.QPixmap("../icons/filepath.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_show_csvfile.setIcon(btn_show_csvfile_icon)
        self.btn_show_csvfile.setIconSize(QtCore.QSize(16, 16))
        self.btn_show_csvfile.setFlat(True)
        self.btn_show_csvfile.setObjectName("btn_show_csvfile")
        self.btn_show_csvfile.setEnabled(False)
        self.file_manager_widget_layout.addWidget(self.btn_show_csvfile)

        self.tools_layout.addWidget(self.file_manager_widget)
        self.tools_layout.setStretch(3, 70)
        self.container_layout.addLayout(self.tools_layout)

        self.channel_layout = QtWidgets.QHBoxLayout()
        self.channel_layout.setSpacing(5)

        self.chart_area_1 = QtWidgets.QVBoxLayout()
        self.chart_area_1.setSpacing(5)
        self.chart_area_2 = QtWidgets.QVBoxLayout()
        self.chart_area_2.setSpacing(5)
        self.chart_area_3 = QtWidgets.QVBoxLayout()
        self.chart_area_3.setSpacing(5)

        self.chartviews = list()
        self.add_chartviews()

        self.channel_layout.addLayout(self.chart_area_1)
        self.channel_layout.addLayout(self.chart_area_2)
        self.channel_layout.addLayout(self.chart_area_3)

        self.container_layout.addLayout(self.channel_layout)

        self.barchart_layout = QtWidgets.QHBoxLayout()
        self.barchart_layout.setContentsMargins(0, 0, 0, 0)
        self.barchart_layout.setSpacing(5)
        self.barchart_layout.addWidget(self.chartviews[9])

        self.container_layout.addLayout(self.barchart_layout)
        self.container_layout.setStretch(0, 5)
        self.container_layout.setStretch(1, 60)
        self.container_layout.setStretch(2, 35)

        sim_window.setCentralWidget(self.container)

        """self.statusbar = QtWidgets.QStatusBar(sim_window)
        self.statusbar.setObjectName("statusbar")
        sim_window.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(sim_window)
        self.toolBar.setObjectName("toolBar")
        sim_window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)"""

        self.retranslateUi(sim_window)
        QtCore.QMetaObject.connectSlotsByName(sim_window)

    def add_chartviews(self):
        for _ in range(CHARTVIEWS):
            chartview = QChartView()
            chartview.setRenderHint(QtGui.QPainter.Antialiasing)
            self.chartviews.append(chartview)

        self.chart_area_1.addWidget(self.chartviews[0])
        self.chart_area_1.addWidget(self.chartviews[1])
        self.chart_area_1.addWidget(self.chartviews[2])
        self.chart_area_2.addWidget(self.chartviews[3])
        self.chart_area_2.addWidget(self.chartviews[4])
        self.chart_area_2.addWidget(self.chartviews[5])
        self.chart_area_3.addWidget(self.chartviews[6])
        self.chart_area_3.addWidget(self.chartviews[7])
        self.chart_area_3.addWidget(self.chartviews[8])

    def retranslateUi(self, sim_window):
        _translate = QtCore.QCoreApplication.translate
        sim_window.setWindowTitle(_translate("sim_window", "Simulation"))
        self.speed_label.setText(_translate("sim_window", "X1"))
        # self.toolBar.setWindowTitle(_translate("sim_window", "toolBar"))
