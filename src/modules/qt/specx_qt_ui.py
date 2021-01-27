from PyQt5 import QtCore, QtGui, QtWidgets

# ---- GUI fonts ----
BOX_LABEL_FONT = QtGui.QFont()
BOX_LABEL_FONT.setPointSizeF(12)
MAIN_LABEL_FONT = QtGui.QFont()
MAIN_LABEL_FONT.setPointSizeF(10)

# ---- Parameters ----
BOX_DEFAULT_LABEL = 'Choose a distribution'
BOX_VISIBLE_ITEMS = 5
DISTRIBUTIONS = 10


class UiMainWindow(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(600, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QtCore.QSize(600, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("../icons/icon.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )
        main_window.setWindowIcon(icon)

        main_window.setStyleSheet("* {\n"
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
        self.container = QtWidgets.QWidget(main_window)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
        self.container.setSizePolicy(sizePolicy)
        self.container.setStyleSheet("QGroupBox::title {\n"
                                     "    subcontrol-origin: margin;\n"
                                     "    padding-left: 5px;\n"
                                     "    padding-right: 5px;\n"
                                     "    padding-top: 4px;\n"
                                     "}")

        self.main_layout = QtWidgets.QGridLayout(self.container)
        self.config_layout = QtWidgets.QVBoxLayout()
        self.config_layout.setContentsMargins(10, 40, 10, 40)
        self.config_layout.setSpacing(60)
        self.box_params = QtWidgets.QGroupBox(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_params.sizePolicy().hasHeightForWidth())
        self.box_params.setSizePolicy(sizePolicy)
        self.box_params.setFont(BOX_LABEL_FONT)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.box_params)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(5)

        self.param_1 = QtWidgets.QHBoxLayout()
        self.param_1.setSpacing(5)

        self.sample_label = QtWidgets.QLabel(self.box_params)
        self.sample_label.setFont(MAIN_LABEL_FONT)

        self.param_1.addWidget(self.sample_label)

        self.sample_time = QtWidgets.QSpinBox(self.box_params)
        self.sample_time.setFont(MAIN_LABEL_FONT)
        self.sample_time.setMinimum(1)
        self.sample_time.setMaximum(15)
        self.sample_time.setProperty("value", 5)

        self.param_1.addWidget(self.sample_time)
        self.param_1.setStretch(0, 60)
        self.param_1.setStretch(1, 40)
        self.verticalLayout_2.addLayout(self.param_1)

        self.param_2 = QtWidgets.QHBoxLayout()
        self.param_2.setSpacing(5)

        self.threshold_label = QtWidgets.QLabel(self.box_params)
        self.threshold_label.setFont(MAIN_LABEL_FONT)

        self.param_2.addWidget(self.threshold_label)

        self.threshold = QtWidgets.QDoubleSpinBox(self.box_params)
        self.threshold.setFont(MAIN_LABEL_FONT)
        self.threshold.setMinimum(0.01)
        self.threshold.setMaximum(0.8)
        self.threshold.setSingleStep(0.05)
        self.threshold.setProperty("value", 0.33)

        self.param_2.addWidget(self.threshold)
        self.param_2.setStretch(0, 60)
        self.param_2.setStretch(1, 40)
        self.verticalLayout_2.addLayout(self.param_2)

        self.options = QtWidgets.QHBoxLayout()

        self.energy_flag = QtWidgets.QCheckBox(self.box_params)
        self.energy_flag.setFont(MAIN_LABEL_FONT)
        self.options.addWidget(self.energy_flag)

        self.usage_flag = QtWidgets.QCheckBox(self.box_params)
        self.usage_flag.setFont(MAIN_LABEL_FONT)

        self.options.addWidget(self.usage_flag)
        self.verticalLayout_2.addLayout(self.options)
        self.config_layout.addWidget(self.box_params)
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setContentsMargins(20, -1, 20, -1)
        self.buttons_layout.setSpacing(5)

        self.btn_simulator = QtWidgets.QPushButton(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_simulator.sizePolicy().hasHeightForWidth())
        self.btn_simulator.setSizePolicy(sizePolicy)
        self.btn_simulator.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_simulator.setStyleSheet("QPushButton{\n"
                                         "    border: none;\n"
                                         "}")
        self.btn_simulator.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/run.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_simulator.setIcon(icon1)
        self.btn_simulator.setIconSize(QtCore.QSize(110, 110))
        self.btn_simulator.setFlat(True)
        self.buttons_layout.addWidget(self.btn_simulator)
        self.btn_simulator.setEnabled(False)

        self.btn_clean = QtWidgets.QPushButton(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clean.sizePolicy().hasHeightForWidth())
        self.btn_clean.setSizePolicy(sizePolicy)
        self.btn_clean.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clean.setStyleSheet("QPushButton{\n"
                                     "    border: none;\n"
                                     "}")
        self.btn_clean.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/clean.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_clean.setIcon(icon2)
        self.btn_clean.setIconSize(QtCore.QSize(110, 110))
        self.btn_clean.setFlat(True)
        self.buttons_layout.addWidget(self.btn_clean)
        self.config_layout.addLayout(self.buttons_layout)
        self.config_layout.setStretch(0, 50)
        self.config_layout.setStretch(1, 50)
        self.main_layout.addLayout(self.config_layout, 0, 1, 1, 1)
        self.freq_layout = QtWidgets.QGridLayout()
        self.freq_layout.setContentsMargins(5, 5, 5, 5)
        self.freq_layout.setSpacing(5)
        self.box_freq = QtWidgets.QGroupBox(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_freq.sizePolicy().hasHeightForWidth())
        self.box_freq.setSizePolicy(sizePolicy)
        self.box_freq.setFont(BOX_LABEL_FONT)
        self.freq_layout_2 = QtWidgets.QVBoxLayout(self.box_freq)
        self.freq_layout_2.setContentsMargins(10, 10, 10, 5)
        self.freq_layout_2.setSpacing(5)

        self.add_labels()
        self.add_boxes()

        self.field_1 = QtWidgets.QHBoxLayout()
        self.field_2 = QtWidgets.QHBoxLayout()
        self.field_3 = QtWidgets.QHBoxLayout()
        self.field_4 = QtWidgets.QHBoxLayout()
        self.field_5 = QtWidgets.QHBoxLayout()
        self.field_6 = QtWidgets.QHBoxLayout()
        self.field_7 = QtWidgets.QHBoxLayout()
        self.field_8 = QtWidgets.QHBoxLayout()
        self.field_9 = QtWidgets.QHBoxLayout()

        self.fields = [self.field_1, self.field_2, self.field_3, self.field_4, self.field_5, self.field_6,
                       self.field_7, self.field_8, self.field_9]

        for index in range(len(self.fields)):
            self.fields[index].setSpacing(5)
            self.fields[index].addWidget(self.labels[index])
            self.fields[index].addWidget(self.boxes[index])
            self.fields[index].setStretch(0, 30)
            self.fields[index].setStretch(1, 70)

        self.freq_layout_2.addLayout(self.field_1)
        self.freq_layout_2.addLayout(self.field_2)
        self.freq_layout_2.addLayout(self.field_3)
        self.freq_layout_2.addLayout(self.field_4)
        self.freq_layout_2.addLayout(self.field_5)
        self.freq_layout_2.addLayout(self.field_6)
        self.freq_layout_2.addLayout(self.field_7)
        self.freq_layout_2.addLayout(self.field_8)
        self.freq_layout_2.addLayout(self.field_9)

        self.foot_layout = QtWidgets.QHBoxLayout()
        self.foot_layout.setSpacing(5)

        self.btn_save_file = QtWidgets.QPushButton(self.box_freq)
        self.btn_save_file.setFont(MAIN_LABEL_FONT)
        self.btn_save_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save_file.setEnabled(False)
        self.foot_layout.addWidget(self.btn_save_file)

        self.btn_load_file = QtWidgets.QPushButton(self.box_freq)
        self.btn_load_file.setFont(MAIN_LABEL_FONT)
        self.btn_load_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.foot_layout.addWidget(self.btn_load_file)
        self.foot_layout.setStretch(0, 50)
        self.foot_layout.setStretch(1, 50)
        self.freq_layout_2.addLayout(self.foot_layout)
        self.freq_layout.addWidget(self.box_freq, 0, 0, 1, 1)
        self.main_layout.addLayout(self.freq_layout, 0, 0, 1, 1)
        self.main_layout.setColumnStretch(0, 50)
        self.main_layout.setColumnStretch(1, 50)

        main_window.setCentralWidget(self.container)

        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menubar.setFont(MAIN_LABEL_FONT)
        self.menubar.setObjectName("menubar")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setFont(MAIN_LABEL_FONT)
        self.file_menu.setObjectName("file_menu")
        self.about_menu = QtWidgets.QMenu(self.menubar)
        self.about_menu.setFont(MAIN_LABEL_FONT)
        self.about_menu.setObjectName("about_menu")
        main_window.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(main_window)
        self.statusBar.setObjectName("statusBar")
        main_window.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(main_window)
        self.toolBar.setObjectName("toolBar")
        main_window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.new_action_menu = QtWidgets.QAction(main_window)
        self.new_action_menu.setObjectName("new_action_menu")
        self.exit_action_menu = QtWidgets.QAction(main_window)
        self.exit_action_menu.setObjectName("exit_action_menu")
        self.about_action_menu = QtWidgets.QAction(main_window)
        self.about_action_menu.setObjectName("about_action_menu")
        self.help_action_menu = QtWidgets.QAction(main_window)
        self.help_action_menu.setObjectName("help_action_menu")
        self.file_menu.addAction(self.new_action_menu)
        self.file_menu.addAction(self.exit_action_menu)
        self.about_menu.addAction(self.about_action_menu)
        self.about_menu.addAction(self.help_action_menu)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.about_menu.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def add_labels(self):
        self.label_channel_1 = QtWidgets.QLabel(self.box_freq)
        self.label_channel_2 = QtWidgets.QLabel(self.box_freq)
        self.label_channel_3 = QtWidgets.QLabel(self.box_freq)
        self.label_channel_4 = QtWidgets.QLabel(self.box_freq)
        self.label_channel_5 = QtWidgets.QLabel(self.box_freq)
        self.label_channel_6 = QtWidgets.QLabel(self.box_freq)
        self.label_channel_7 = QtWidgets.QLabel(self.box_freq)
        self.label_channel_8 = QtWidgets.QLabel(self.box_freq)
        self.label_channel_9 = QtWidgets.QLabel(self.box_freq)

        self.labels = [self.label_channel_1, self.label_channel_2, self.label_channel_3, self.label_channel_4,
                       self.label_channel_5, self.label_channel_6, self.label_channel_7, self.label_channel_8,
                       self.label_channel_9]

        for label in self.labels:
            label.setFont(MAIN_LABEL_FONT)

    def add_boxes(self):
        self.box_1 = QtWidgets.QComboBox(self.box_freq)
        self.box_2 = QtWidgets.QComboBox(self.box_freq)
        self.box_3 = QtWidgets.QComboBox(self.box_freq)
        self.box_4 = QtWidgets.QComboBox(self.box_freq)
        self.box_5 = QtWidgets.QComboBox(self.box_freq)
        self.box_6 = QtWidgets.QComboBox(self.box_freq)
        self.box_7 = QtWidgets.QComboBox(self.box_freq)
        self.box_8 = QtWidgets.QComboBox(self.box_freq)
        self.box_9 = QtWidgets.QComboBox(self.box_freq)

        self.boxes = [self.box_1, self.box_2, self.box_3, self.box_4, self.box_5, self.box_6, self.box_7,
                      self.box_8, self.box_9]

        for box in self.boxes:
            box.setFont(MAIN_LABEL_FONT)
            box.setMaxVisibleItems(BOX_VISIBLE_ITEMS)
            box.setPlaceholderText(BOX_DEFAULT_LABEL)
            for _ in range(DISTRIBUTIONS):
                box.addItem("")

            box.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Specx"))
        self.box_params.setTitle(_translate("main_window", "Parámetros"))
        self.sample_label.setText(_translate("main_window", "Tiempo de muestreo:"))
        self.sample_time.setSuffix(_translate("main_window", "min"))
        self.threshold_label.setText(_translate("main_window", "Umbral de energía:"))
        self.energy_flag.setText(_translate("main_window", "Energía"))
        self.usage_flag.setText(_translate("main_window", "Ocupación de canal"))
        self.box_freq.setTitle(_translate("main_window", "Frecuencias"))
        self.label_channel_1.setText(_translate("main_window", "473 MHz"))
        self.box_1.setItemText(0, _translate("main_window", "Bernoulli"))
        self.box_1.setItemText(1, _translate("main_window", "Beta"))
        self.box_1.setItemText(2, _translate("main_window", "Gamma"))
        self.box_1.setItemText(3, _translate("main_window", "Gumbel max"))
        self.box_1.setItemText(4, _translate("main_window", "Laplace"))
        self.box_1.setItemText(5, _translate("main_window", "Lognormal"))
        self.box_1.setItemText(6, _translate("main_window", "Normal"))
        self.box_1.setItemText(7, _translate("main_window", "Rayleigh"))
        self.box_1.setItemText(8, _translate("main_window", "Uniforme"))
        self.box_1.setItemText(9, _translate("main_window", "Weibull"))
        self.label_channel_2.setText(_translate("main_window", "479 MHz"))
        self.box_2.setItemText(0, _translate("main_window", "Bernoulli"))
        self.box_2.setItemText(1, _translate("main_window", "Beta"))
        self.box_2.setItemText(2, _translate("main_window", "Gamma"))
        self.box_2.setItemText(3, _translate("main_window", "Gumbel max"))
        self.box_2.setItemText(4, _translate("main_window", "Laplace"))
        self.box_2.setItemText(5, _translate("main_window", "Lognormal"))
        self.box_2.setItemText(6, _translate("main_window", "Normal"))
        self.box_2.setItemText(7, _translate("main_window", "Rayleigh"))
        self.box_2.setItemText(8, _translate("main_window", "Uniforme"))
        self.box_2.setItemText(9, _translate("main_window", "Weibull"))
        self.label_channel_3.setText(_translate("main_window", "485 MHz"))
        self.box_3.setItemText(0, _translate("main_window", "Bernoulli"))
        self.box_3.setItemText(1, _translate("main_window", "Beta"))
        self.box_3.setItemText(2, _translate("main_window", "Gamma"))
        self.box_3.setItemText(3, _translate("main_window", "Gumbel max"))
        self.box_3.setItemText(4, _translate("main_window", "Laplace"))
        self.box_3.setItemText(5, _translate("main_window", "Lognormal"))
        self.box_3.setItemText(6, _translate("main_window", "Normal"))
        self.box_3.setItemText(7, _translate("main_window", "Rayleigh"))
        self.box_3.setItemText(8, _translate("main_window", "Uniforme"))
        self.box_3.setItemText(9, _translate("main_window", "Weibull"))
        self.label_channel_4.setText(_translate("main_window", "491 MHz"))
        self.box_4.setItemText(0, _translate("main_window", "Bernoulli"))
        self.box_4.setItemText(1, _translate("main_window", "Beta"))
        self.box_4.setItemText(2, _translate("main_window", "Gamma"))
        self.box_4.setItemText(3, _translate("main_window", "Gumbel max"))
        self.box_4.setItemText(4, _translate("main_window", "Laplace"))
        self.box_4.setItemText(5, _translate("main_window", "Lognormal"))
        self.box_4.setItemText(6, _translate("main_window", "Normal"))
        self.box_4.setItemText(7, _translate("main_window", "Rayleigh"))
        self.box_4.setItemText(8, _translate("main_window", "Uniforme"))
        self.box_4.setItemText(9, _translate("main_window", "Weibull"))
        self.label_channel_5.setText(_translate("main_window", "497 MHz"))
        self.box_5.setItemText(0, _translate("main_window", "Bernoulli"))
        self.box_5.setItemText(1, _translate("main_window", "Beta"))
        self.box_5.setItemText(2, _translate("main_window", "Gamma"))
        self.box_5.setItemText(3, _translate("main_window", "Gumbel max"))
        self.box_5.setItemText(4, _translate("main_window", "Laplace"))
        self.box_5.setItemText(5, _translate("main_window", "Lognormal"))
        self.box_5.setItemText(6, _translate("main_window", "Normal"))
        self.box_5.setItemText(7, _translate("main_window", "Rayleigh"))
        self.box_5.setItemText(8, _translate("main_window", "Uniforme"))
        self.box_5.setItemText(9, _translate("main_window", "Weibull"))
        self.label_channel_6.setText(_translate("main_window", "503 MHz"))
        self.box_6.setItemText(0, _translate("main_window", "Bernoulli"))
        self.box_6.setItemText(1, _translate("main_window", "Beta"))
        self.box_6.setItemText(2, _translate("main_window", "Gamma"))
        self.box_6.setItemText(3, _translate("main_window", "Gumbel max"))
        self.box_6.setItemText(4, _translate("main_window", "Laplace"))
        self.box_6.setItemText(5, _translate("main_window", "Lognormal"))
        self.box_6.setItemText(6, _translate("main_window", "Normal"))
        self.box_6.setItemText(7, _translate("main_window", "Rayleigh"))
        self.box_6.setItemText(8, _translate("main_window", "Uniforme"))
        self.box_6.setItemText(9, _translate("main_window", "Weibull"))
        self.label_channel_7.setText(_translate("main_window", "509 MHz"))
        self.box_7.setItemText(0, _translate("main_window", "Bernoulli"))
        self.box_7.setItemText(1, _translate("main_window", "Beta"))
        self.box_7.setItemText(2, _translate("main_window", "Gamma"))
        self.box_7.setItemText(3, _translate("main_window", "Gumbel max"))
        self.box_7.setItemText(4, _translate("main_window", "Laplace"))
        self.box_7.setItemText(5, _translate("main_window", "Lognormal"))
        self.box_7.setItemText(6, _translate("main_window", "Normal"))
        self.box_7.setItemText(7, _translate("main_window", "Rayleigh"))
        self.box_7.setItemText(8, _translate("main_window", "Uniforme"))
        self.box_7.setItemText(9, _translate("main_window", "Weibull"))
        self.label_channel_8.setText(_translate("main_window", "551 MHz"))
        self.box_8.setItemText(0, _translate("main_window", "Bernoulli"))
        self.box_8.setItemText(1, _translate("main_window", "Beta"))
        self.box_8.setItemText(2, _translate("main_window", "Gamma"))
        self.box_8.setItemText(3, _translate("main_window", "Gumbel max"))
        self.box_8.setItemText(4, _translate("main_window", "Laplace"))
        self.box_8.setItemText(5, _translate("main_window", "Lognormal"))
        self.box_8.setItemText(6, _translate("main_window", "Normal"))
        self.box_8.setItemText(7, _translate("main_window", "Rayleigh"))
        self.box_8.setItemText(8, _translate("main_window", "Uniforme"))
        self.box_8.setItemText(9, _translate("main_window", "Weibull"))
        self.label_channel_9.setText(_translate("main_window", "557 MHz"))
        self.box_9.setItemText(0, _translate("main_window", "Bernoulli"))
        self.box_9.setItemText(1, _translate("main_window", "Beta"))
        self.box_9.setItemText(2, _translate("main_window", "Gamma"))
        self.box_9.setItemText(3, _translate("main_window", "Gumbel max"))
        self.box_9.setItemText(4, _translate("main_window", "Laplace"))
        self.box_9.setItemText(5, _translate("main_window", "Lognormal"))
        self.box_9.setItemText(6, _translate("main_window", "Normal"))
        self.box_9.setItemText(7, _translate("main_window", "Rayleigh"))
        self.box_9.setItemText(8, _translate("main_window", "Uniforme"))
        self.box_9.setItemText(9, _translate("main_window", "Weibull"))
        self.btn_save_file.setText(_translate("main_window", "Exportar"))
        self.btn_load_file.setText(_translate("main_window", "Importar"))
        self.file_menu.setTitle(_translate("main_window", "Archivo"))
        self.about_menu.setTitle(_translate("main_window", "Acerca"))
        self.toolBar.setWindowTitle(_translate("main_window", "toolBar"))
        self.new_action_menu.setText(_translate("main_window", "Nuevo..."))
        self.exit_action_menu.setText(_translate("main_window", "Salir"))
        self.about_action_menu.setText(_translate("main_window", "Acerca de"))
        self.help_action_menu.setText(_translate("main_window", "Ayuda"))
