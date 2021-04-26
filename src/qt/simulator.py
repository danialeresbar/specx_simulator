import math
from PyQt5 import QtCore, QtChart, QtGui, QtWidgets
from src.model import simulation

# ---- Window attributes ----
MINIMUM_WIDTH = 1280
MINIMUM_HEIGHT = 720
DEFAULT_WIDTH = 1280
DEFAULT_HEIGHT = 720
SIZE_POLICY_EXPANDING = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
SIZE_POLICY_FIXED = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
SIZE_POLICY_PREFERRED = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

# ---- Charts ----
CHART_PER_ROWS = 3

# ---- Fonts ----
MAIN_LABEL_FONT = QtGui.QFont()
MAIN_LABEL_FONT.setPointSizeF(8)
BUTTON_LABEL_FONT = QtGui.QFont()
BUTTON_LABEL_FONT.setPointSizeF(10)


class SimulatorTemplate(object):
    def setup(self, simulator):
        simulator.resize(DEFAULT_WIDTH, DEFAULT_HEIGHT)
        simulator_size_policy = SIZE_POLICY_FIXED
        simulator_size_policy.setHorizontalStretch(0)
        simulator_size_policy.setVerticalStretch(0)
        simulator_size_policy.setHeightForWidth(simulator.sizePolicy().hasHeightForWidth())
        simulator.setSizePolicy(simulator_size_policy)
        simulator.setMinimumSize(QtCore.QSize(DEFAULT_WIDTH, DEFAULT_HEIGHT))
        simulator.setMaximumSize(QtCore.QSize(DEFAULT_WIDTH, DEFAULT_HEIGHT))
        simulator_icon = QtGui.QIcon()
        simulator_icon.addPixmap(QtGui.QPixmap("../icons/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        simulator.setWindowIcon(simulator_icon)
        simulator.setStyleSheet("* {\n"
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

        self.container = QtWidgets.QWidget(simulator)
        self.container_layout = QtWidgets.QVBoxLayout(self.container)
        self.container_layout.setContentsMargins(10, 10, 10, 10)
        self.container_layout.setSpacing(5)

        # Tools section
        self.btn_start = QtWidgets.QPushButton(self.container)
        self.btn_play = QtWidgets.QPushButton(self.container)
        self.btn_pause = QtWidgets.QPushButton(self.container)
        self.btn_stop = QtWidgets.QPushButton(self.container)
        self.btn_reset_speed = QtWidgets.QPushButton(self.container)
        self.btn_decrease_speed = QtWidgets.QPushButton(self.container)
        self.btn_increase_speed = QtWidgets.QPushButton(self.container)
        self.btn_save_chart = QtWidgets.QPushButton(self.container)
        self.btn_open_csvfile = QtWidgets.QPushButton(self.container)
        self.speed_label = QtWidgets.QLabel(self.container)
        self._build_tool_box()

        # Chartviews section
        self.simulation_charts = [QtChart.QChart() for _ in range(len(simulation.FREQUENCIES))]
        self.percentage_chart = QtChart.QChart()
        self.simulation_chartviews = [QtChart.QChartView() for _ in range(len(simulation.FREQUENCIES))]
        self.percentage_bars_chartview = QtChart.QChartView()
        self._build_chartview_box()

        self.container_layout.setStretch(0, 5)
        self.container_layout.setStretch(1, 60)
        self.container_layout.setStretch(2, 35)

        simulator.setCentralWidget(self.container)

        self.retranslateUi(simulator)
        QtCore.QMetaObject.connectSlotsByName(simulator)

    def _build_tool_box(self):
        """

        """

        # Size policies
        btn_start_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        btn_start_size_policy.setVerticalStretch(0)
        btn_start_size_policy.setHorizontalStretch(0)
        btn_start_size_policy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        btn_play_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        btn_play_size_policy.setVerticalStretch(0)
        btn_play_size_policy.setHorizontalStretch(0)
        btn_play_size_policy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        btn_pause_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        btn_pause_size_policy.setVerticalStretch(0)
        btn_pause_size_policy.setHorizontalStretch(0)
        btn_pause_size_policy.setHeightForWidth(self.btn_pause.sizePolicy().hasHeightForWidth())
        btn_stop_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        btn_stop_size_policy.setVerticalStretch(0)
        btn_stop_size_policy.setHorizontalStretch(0)
        btn_stop_size_policy.setHeightForWidth(self.btn_stop.sizePolicy().hasHeightForWidth())

        # Widgets (Area)
        control_area = QtWidgets.QWidget(self.container)
        files_area = QtWidgets.QWidget(self.container)
        time_area = QtWidgets.QWidget(self.container)

        # Layouts
        control_area_layout = QtWidgets.QHBoxLayout(control_area)
        control_area_layout.setSpacing(5)
        files_area_layout = QtWidgets.QHBoxLayout(files_area)
        files_area_layout.setSpacing(0)
        time_area_layout = QtWidgets.QHBoxLayout(time_area)
        time_area_layout.setSpacing(5)
        tools_layout = QtWidgets.QHBoxLayout()
        tools_layout.setSpacing(5)

        # Labels
        self.speed_label.setFont(MAIN_LABEL_FONT)
        self.speed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.speed_label.setText('X1')

        # Buttons
        self.btn_start.setSizePolicy(btn_start_size_policy)
        self.btn_start.setFont(BUTTON_LABEL_FONT)
        self.btn_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_start.setText("START")
        self.btn_play.setSizePolicy(btn_play_size_policy)
        self.btn_play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_play_icon = QtGui.QIcon()
        btn_play_icon.addPixmap(QtGui.QPixmap("../icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(btn_play_icon)
        self.btn_play.setIconSize(QtCore.QSize(16, 16))
        self.btn_play.setFlat(True)
        self.btn_pause.setSizePolicy(btn_pause_size_policy)
        self.btn_pause.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_pause_icon = QtGui.QIcon()
        btn_pause_icon.addPixmap(QtGui.QPixmap("../icons/pause.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pause.setIcon(btn_pause_icon)
        self.btn_pause.setIconSize(QtCore.QSize(16, 16))
        self.btn_stop.setSizePolicy(btn_stop_size_policy)
        self.btn_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_stop_icon = QtGui.QIcon()
        btn_stop_icon.addPixmap(QtGui.QPixmap("../icons/stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(btn_stop_icon)
        self.btn_stop.setIconSize(QtCore.QSize(16, 16))
        self.btn_reset_speed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_reset_speed_icon = QtGui.QIcon()
        btn_reset_speed_icon.addPixmap(QtGui.QPixmap("../icons/reset.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reset_speed.setIcon(btn_reset_speed_icon)
        self.btn_reset_speed.setIconSize(QtCore.QSize(16, 16))
        self.btn_decrease_speed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_decrease_speed_icon = QtGui.QIcon()
        btn_decrease_speed_icon.addPixmap(QtGui.QPixmap("../icons/decrease.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_decrease_speed.setIcon(btn_decrease_speed_icon)
        self.btn_decrease_speed.setIconSize(QtCore.QSize(16, 16))
        self.btn_increase_speed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_increase_speed_icon = QtGui.QIcon()
        btn_increase_speed_icon.addPixmap(QtGui.QPixmap("../icons/increase.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_increase_speed.setIcon(btn_increase_speed_icon)
        self.btn_increase_speed.setIconSize(QtCore.QSize(16, 16))
        self.btn_save_chart.setFont(BUTTON_LABEL_FONT)
        self.btn_save_chart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_save_chart_icon = QtGui.QIcon()
        btn_save_chart_icon.addPixmap(QtGui.QPixmap("../icons/chart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save_chart.setIcon(btn_save_chart_icon)
        self.btn_save_chart.setIconSize(QtCore.QSize(16, 16))
        self.btn_save_chart.setFlat(True)
        self.btn_open_csvfile.setFont(BUTTON_LABEL_FONT)
        self.btn_open_csvfile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_open_csvfile_icon = QtGui.QIcon()
        btn_open_csvfile_icon.addPixmap(QtGui.QPixmap("../icons/filepath.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open_csvfile.setIcon(btn_open_csvfile_icon)
        self.btn_open_csvfile.setIconSize(QtCore.QSize(16, 16))
        self.btn_open_csvfile.setFlat(True)
        self.btn_open_csvfile.setEnabled(False)

        # Spaces
        spacer_item = QtWidgets.QSpacerItem(int(DEFAULT_WIDTH/2), 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        control_area_layout.addWidget(self.btn_start)
        control_area_layout.addWidget(self.btn_play)
        control_area_layout.addWidget(self.btn_pause)
        control_area_layout.addWidget(self.btn_stop)
        files_area_layout.addWidget(self.btn_save_chart)
        files_area_layout.addWidget(self.btn_open_csvfile)
        time_area_layout.addWidget(self.btn_decrease_speed)
        time_area_layout.addWidget(self.speed_label)
        time_area_layout.addWidget(self.btn_increase_speed)
        time_area_layout.addWidget(self.btn_reset_speed)

        tools_layout.addWidget(control_area)
        tools_layout.addWidget(time_area)
        tools_layout.addItem(spacer_item)
        tools_layout.addWidget(files_area)
        tools_layout.setStretch(4, 70)
        self.container_layout.addLayout(tools_layout)

    def _build_chartview_box(self):
        """

        """

        # Layouts
        simulation_chartview_layout = QtWidgets.QVBoxLayout()
        simulation_chartview_layout.setSpacing(5)
        results_chartview_layout = QtWidgets.QHBoxLayout()
        results_chartview_layout.setSpacing(5)
        results_chartview_layout.setContentsMargins(0, 0, 0, 0)
        row_layouts = [QtWidgets.QHBoxLayout() for _ in range(math.ceil((len(simulation.FREQUENCIES)/CHART_PER_ROWS)))]
        for row_layout in row_layouts:
            row_layout.setSpacing(5)

        # Chartviews
        aux = 0
        for index, chartview in enumerate(self.simulation_chartviews, 1):
            chartview.setRenderHint(QtGui.QPainter.Antialiasing)
            row_layouts[aux].addWidget(chartview)
            if index % 3 == 0:
                aux += 1

        for row in row_layouts:
            simulation_chartview_layout.addLayout(row)

        for chart, chartview in zip(self.simulation_charts, self.simulation_chartviews):
            chartview.setChart(chart)
        results_chartview_layout.addWidget(self.percentage_bars_chartview)

        self.container_layout.addLayout(simulation_chartview_layout)
        self.container_layout.addLayout(results_chartview_layout)

    def retranslateUi(self, simulator):
        _translate = QtCore.QCoreApplication.translate
        simulator.setWindowTitle(_translate("simulator", "Simulation"))
        # self.toolBar.setWindowTitle(_translate("simulator", "toolBar"))
