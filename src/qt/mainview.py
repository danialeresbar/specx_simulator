from PyQt5 import QtCore, QtGui, QtWidgets

from src.model import simulation
from src.model.distributions import base

# ---- Window attributes ----
MINIMUM_WIDTH = 600
MINIMUM_HEIGHT = 450
DEFAULT_WIDTH = 600
DEFAULT_HEIGHT = 450
SIZE_POLICY_EXPANDING = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
SIZE_POLICY_PREFERRED = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

# ---- Fonts ----
BOX_LABEL_FONT = QtGui.QFont()
BOX_LABEL_FONT.setPointSizeF(12)
MAIN_LABEL_FONT = QtGui.QFont()
MAIN_LABEL_FONT.setPointSizeF(10)

# ---- Drops ----
DROP_DEFAULT_ITEM_LABEL = 'Choose a distribution'
DROP_VISIBLE_ITEMS = 5

# ---- Spin Boxes ----
SAMPLE_TIME_DEFAULT_VALUE = 5
SAMPLE_TIME_MINIMUM_VALUE = 1
SAMPLE_TIME_MAXIMUM_VALUE = 30
THRESHOLD_DEFAULT_VALUE = 0.33
THRESHOLD_MINIMUM_VALUE = 0.01
THRESHOLD_MAXIMUM_VALUE = 0.45


class MainViewTemplate:
    def setup(self, mainview, **kwargs):
        mainview.resize(kwargs.get('width', DEFAULT_WIDTH), kwargs.get('height', DEFAULT_HEIGHT))
        mainview.setMinimumSize(QtCore.QSize(MINIMUM_WIDTH, MINIMUM_HEIGHT))
        mainview_size_policy = SIZE_POLICY_PREFERRED
        mainview_size_policy.setHorizontalStretch(0)
        mainview_size_policy.setVerticalStretch(0)
        mainview_size_policy.setHeightForWidth(mainview.sizePolicy().hasHeightForWidth())
        mainview.setSizePolicy(mainview_size_policy)
        mainview_icon = QtGui.QIcon()
        mainview_icon.addPixmap(
            QtGui.QPixmap("../icons/icon.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )
        mainview.setWindowIcon(mainview_icon)
        mainview.setStyleSheet("* {\n"
                                  "    background: #26282b;\n"
                                  "    color: #DDDDDD;\n"
                                  "    border: 1px solid #5A5A5A;\n"
                                  "}\n"
                                  "\n"
                                  "QWidget::item:selected {\n"
                                  "    background: #5f85db;\n"
                                  "}\n"
                                  "\n"
                                  "QCheckBox::disabled, QRadioButton:disabled {\n"
                                  "    color: #787878;\n"
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
                                  "    top: -7px;\n"
                                  "    left: 7px;\n"
                                  "}\n"
                                  "\n"
                                  "QScrollBar {\n"
                                  "    border: 1px solid #5A5A5A;\n"
                                  "    background: #353941;\n"
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
                                  "    background:#353941;\n"
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
                                  "    selection-background-color: #5f85db;\n"
                                  "    selection-color: #DDDDDD;\n"
                                  "    alternate-background-color: #26282b;\n"
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
                                  "    background: #393e46;\n"
                                  "}\n"
                                  "\n"
                                  "QComboBox:disabled {\n"
                                  "color: #787878;\n"
                                  "}\n"
                                  "\n"
                                  "QComboBox::down-arrow {\n"
                                  "    border: 1px solid #5A5A5A;\n"
                                  "    background: #393e46;\n"
                                  "}\n"
                                  "\n"
                                  "QComboBox::drop-down {\n"
                                  "    border: 1px solid #5A5A5A;\n"
                                  "    background: #393e46;\n"
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
                                  "QAbstractSpinBox:disabled {\n"
                                  "    color: #787878;\n"
                                  "}\n"
                                  "\n"
                                  "QAbstractSpinBox::up-button, QAbstractSpinBox::down-button {\n"
                                  "    border: 1px solid #5A5A5A;\n"
                                  "    background: #393e46;\n"
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
                                  "QMenu::separator {\n"
                                  "    background: #7971ea;\n"
                                  "}")

        self.container = QtWidgets.QWidget(mainview)
        container_size_policy = SIZE_POLICY_EXPANDING
        container_size_policy.setHorizontalStretch(0)
        container_size_policy.setVerticalStretch(0)
        container_size_policy.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
        self.container.setSizePolicy(container_size_policy)
        self.container.setStyleSheet("QGroupBox::title {\n"
                                     "    subcontrol-origin: margin;\n"
                                     "    padding-left: 5px;\n"
                                     "    padding-right: 5px;\n"
                                     "    padding-top: 4px;\n"
                                     "}")

        # TODO: Check this layout
        self.container_layout = QtWidgets.QGridLayout(self.container)
        self.config_layout = QtWidgets.QVBoxLayout()
        self.config_layout.setContentsMargins(10, 40, 10, 40)
        self.config_layout.setSpacing(60)

        # Settings components
        self.settings_box = QtWidgets.QGroupBox(self.container)
        self.sample_time_label = QtWidgets.QLabel(self.settings_box)
        self.threshold_label = QtWidgets.QLabel(self.settings_box)
        self.sample_time = QtWidgets.QSpinBox(self.settings_box)
        self.threshold = QtWidgets.QDoubleSpinBox(self.settings_box)
        self.energy_flag = QtWidgets.QCheckBox(self.settings_box)
        self.usage_flag = QtWidgets.QCheckBox(self.settings_box)
        self._build_settings_box()

        # Action components
        self.btn_simulator = QtWidgets.QPushButton(self.container)
        self.btn_clean = QtWidgets.QPushButton(self.container)
        self._build_button_box()

        self.config_layout.addWidget(self.settings_box)
        # self.config_layout.addLayout(self.buttons_layout)
        self.config_layout.setStretch(0, 50)
        self.config_layout.setStretch(1, 50)

        self.container_layout.addLayout(self.config_layout, 0, 1, 1, 1)

        # TODO: Check this layout
        self.freq_layout = QtWidgets.QGridLayout()
        self.freq_layout.setContentsMargins(5, 5, 5, 5)
        self.freq_layout.setSpacing(5)

        # Channel section
        self.channel_box = QtWidgets.QGroupBox(self.container)
        self.channel_labels = [QtWidgets.QLabel(self.channel_box) for _ in range(len(simulation.FREQUENCIES))]
        self.channel_drops = [QtWidgets.QComboBox(self.channel_box) for _ in range(len(simulation.FREQUENCIES))]
        self.btn_save_settings = QtWidgets.QPushButton(self.channel_box)
        self.btn_load_settings = QtWidgets.QPushButton(self.channel_box)
        self._build_channel_box()

        self.freq_layout.addWidget(self.channel_box, 0, 0, 1, 1)

        self.container_layout.addLayout(self.freq_layout, 0, 0, 1, 1)
        self.container_layout.setColumnStretch(0, 50)
        self.container_layout.setColumnStretch(1, 50)

        mainview.setCentralWidget(self.container)

        # Menu bar
        self.menubar = QtWidgets.QMenuBar(mainview)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menubar.setFont(MAIN_LABEL_FONT)
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setFont(MAIN_LABEL_FONT)
        self.about_menu = QtWidgets.QMenu(self.menubar)
        self.about_menu.setFont(MAIN_LABEL_FONT)
        mainview.setMenuBar(self.menubar)

        # Menu items
        self.action_menu_new = QtWidgets.QAction(mainview)
        self.action_menu_exit = QtWidgets.QAction(mainview)
        self.action_menu_about = QtWidgets.QAction(mainview)
        self.action_menu_help = QtWidgets.QAction(mainview)

        self.file_menu.addAction(self.action_menu_new)
        self.file_menu.addAction(self.action_menu_exit)
        self.about_menu.addAction(self.action_menu_about)
        self.about_menu.addAction(self.action_menu_help)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.about_menu.menuAction())

        # Status bar
        self.statusBar = QtWidgets.QStatusBar(mainview)
        self.statusBar.setObjectName("statusBar")
        mainview.setStatusBar(self.statusBar)

        # Tool bar
        self.toolBar = QtWidgets.QToolBar(mainview)
        self.toolBar.setObjectName("toolBar")
        mainview.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.translate(mainview)
        QtCore.QMetaObject.connectSlotsByName(mainview)

    def _build_settings_box(self):
        """

        """

        # Size policies
        settings_box_size_policy = SIZE_POLICY_EXPANDING
        settings_box_size_policy.setHorizontalStretch(0)
        settings_box_size_policy.setVerticalStretch(0)
        settings_box_size_policy.setHeightForWidth(self.settings_box.sizePolicy().hasHeightForWidth())
        self.settings_box.setSizePolicy(settings_box_size_policy)
        self.settings_box.setFont(BOX_LABEL_FONT)

        # Layouts
        settings_box_layout = QtWidgets.QVBoxLayout(self.settings_box)
        settings_box_layout.setContentsMargins(10, 10, 10, 10)
        settings_box_layout.setSpacing(5)
        optional_parameter_layout = QtWidgets.QHBoxLayout()
        sample_parameter_layout = QtWidgets.QHBoxLayout()
        sample_parameter_layout.setSpacing(5)
        threshold_parameter_layout = QtWidgets.QHBoxLayout()
        threshold_parameter_layout.setSpacing(5)

        # Labels
        self.energy_flag.setFont(MAIN_LABEL_FONT)
        self.sample_time_label.setFont(MAIN_LABEL_FONT)
        self.threshold_label.setFont(MAIN_LABEL_FONT)
        self.usage_flag.setFont(MAIN_LABEL_FONT)

        # Spins
        self.sample_time.setFont(MAIN_LABEL_FONT)
        self.sample_time.setMinimum(SAMPLE_TIME_MINIMUM_VALUE)
        self.sample_time.setMaximum(SAMPLE_TIME_MAXIMUM_VALUE)
        self.sample_time.setValue(SAMPLE_TIME_DEFAULT_VALUE)
        self.threshold.setFont(MAIN_LABEL_FONT)
        self.threshold.setMinimum(THRESHOLD_MINIMUM_VALUE)
        self.threshold.setMaximum(THRESHOLD_MAXIMUM_VALUE)
        self.threshold.setSingleStep(0.05)
        self.threshold.setValue(THRESHOLD_DEFAULT_VALUE)

        optional_parameter_layout.addWidget(self.energy_flag)
        optional_parameter_layout.addWidget(self.usage_flag)
        sample_parameter_layout.addWidget(self.sample_time_label)
        sample_parameter_layout.addWidget(self.sample_time)
        sample_parameter_layout.setStretch(0, 60)
        sample_parameter_layout.setStretch(1, 40)
        threshold_parameter_layout.addWidget(self.threshold_label)
        threshold_parameter_layout.addWidget(self.threshold)
        threshold_parameter_layout.setStretch(0, 60)
        threshold_parameter_layout.setStretch(1, 40)

        settings_box_layout.addLayout(sample_parameter_layout)
        settings_box_layout.addLayout(threshold_parameter_layout)
        settings_box_layout.addLayout(optional_parameter_layout)

    def _build_channel_box(self):
        """

        """

        # Size policies
        channel_box_size_policy = SIZE_POLICY_EXPANDING
        channel_box_size_policy.setHorizontalStretch(0)
        channel_box_size_policy.setVerticalStretch(0)
        channel_box_size_policy.setHeightForWidth(self.channel_box.sizePolicy().hasHeightForWidth())
        self.channel_box.setSizePolicy(channel_box_size_policy)
        self.channel_box.setFont(BOX_LABEL_FONT)

        # Layouts
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setSpacing(5)
        channel_box_layout = QtWidgets.QVBoxLayout(self.channel_box)
        channel_box_layout.setSpacing(5)
        channel_box_layout.setContentsMargins(10, 10, 10, 5)
        channel_layouts = [QtWidgets.QHBoxLayout() for _ in range(len(simulation.FREQUENCIES))]

        # Labels
        for label, frequency in zip(self.channel_labels, simulation.FREQUENCIES):
            label.setFont(MAIN_LABEL_FONT)
            label.setText(frequency)

        # Buttons
        self.btn_save_settings.setFont(MAIN_LABEL_FONT)
        self.btn_save_settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save_settings.setEnabled(False)
        self.btn_load_settings.setFont(MAIN_LABEL_FONT)
        self.btn_load_settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Drops
        for drop in self.channel_drops:
            drop.setFont(MAIN_LABEL_FONT)
            drop.setMaxVisibleItems(DROP_VISIBLE_ITEMS)
            drop.setPlaceholderText(DROP_DEFAULT_ITEM_LABEL)
            drop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            # Adding items (probability distribution names)
            for item in base.ALLOWED_CONTINUOUS_DISTRIBUTIONS:
                drop.setPlaceholderText('Choose')
                drop.addItem(item[1])  # This position contain the distribution name

        for index, channel_layout in enumerate(channel_layouts):
            channel_layout.setSpacing(5)
            channel_layout.addWidget(self.channel_labels[index])
            channel_layout.addWidget(self.channel_drops[index])
            channel_layout.setStretch(0, 30)
            channel_layout.setStretch(1, 70)
            channel_box_layout.addLayout(channel_layout)

        button_layout.addWidget(self.btn_save_settings)
        button_layout.addWidget(self.btn_load_settings)
        button_layout.setStretch(0, 50)
        button_layout.setStretch(1, 50)
        channel_box_layout.addLayout(button_layout)

    def _build_button_box(self):
        """

        """

        # Size policies
        btn_simulate_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        btn_simulate_size_policy.setHorizontalStretch(0)
        btn_simulate_size_policy.setVerticalStretch(0)
        btn_simulate_size_policy.setHeightForWidth(self.btn_simulator.sizePolicy().hasHeightForWidth())
        self.btn_simulator.setSizePolicy(btn_simulate_size_policy)
        btn_clean_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        btn_clean_size_policy.setHorizontalStretch(0)
        btn_clean_size_policy.setVerticalStretch(0)
        btn_clean_size_policy.setHeightForWidth(self.btn_clean.sizePolicy().hasHeightForWidth())
        self.btn_clean.setSizePolicy(btn_clean_size_policy)

        # Layouts
        button_box_layout = QtWidgets.QHBoxLayout()
        button_box_layout.setSpacing(5)
        button_box_layout.setContentsMargins(20, -1, 20, -1)

        # Buttons
        btn_simulate_icon = QtGui.QIcon()
        btn_simulate_icon.addPixmap(
            QtGui.QPixmap("../icons/run.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )

        self.btn_simulator.setIcon(btn_simulate_icon)
        self.btn_simulator.setIconSize(QtCore.QSize(110, 110))
        self.btn_simulator.setFlat(True)
        self.btn_simulator.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_simulator.setEnabled(False)
        self.btn_simulator.setStyleSheet("QPushButton{\n"
                                         "    border: none;\n"
                                         "}")
        btn_clean_icon = QtGui.QIcon()
        btn_clean_icon.addPixmap(
            QtGui.QPixmap("../icons/clean.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )
        self.btn_clean.setIcon(btn_clean_icon)
        self.btn_clean.setIconSize(QtCore.QSize(110, 110))
        self.btn_clean.setFlat(True)
        self.btn_clean.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clean.setStyleSheet("QPushButton{\n"
                                     "    border: none;\n"
                                     "}")

        button_box_layout.addWidget(self.btn_simulator)
        button_box_layout.addWidget(self.btn_clean)

    def translate(self, mainview):
        _translate = QtCore.QCoreApplication.translate
        mainview.setWindowTitle(_translate("mainview", "Specx"))
        self.settings_box.setTitle(_translate("mainview", "Parámetros"))
        self.sample_time_label.setText(_translate("mainview", "Tiempo de muestreo:"))
        self.sample_time.setSuffix(_translate("mainview", "min"))
        self.threshold_label.setText(_translate("mainview", "Umbral de energía:"))
        self.energy_flag.setText(_translate("mainview", "Energía"))
        self.usage_flag.setText(_translate("mainview", "Ocupación de canal"))
        self.channel_box.setTitle(_translate("mainview", "Frecuencias"))
        self.btn_save_settings.setText(_translate("mainview", "Exportar"))
        self.btn_load_settings.setText(_translate("mainview", "Importar"))
        self.file_menu.setTitle(_translate("mainview", "Archivo"))
        self.about_menu.setTitle(_translate("mainview", "Acerca"))
        self.toolBar.setWindowTitle(_translate("mainview", "toolBar"))
        self.action_menu_new.setText(_translate("mainview", "Nuevo..."))
        self.action_menu_exit.setText(_translate("mainview", "Salir"))
        self.action_menu_about.setText(_translate("mainview", "Acerca de"))
        self.action_menu_help.setText(_translate("mainview", "Ayuda"))
