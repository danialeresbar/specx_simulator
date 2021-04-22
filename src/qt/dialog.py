from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChartView


# ---- Distribution parameters ----
FIRST_PARAMETER = 'Parámetro 1:'
SECOND_PARAMETER = 'Parámetro 2:'
THIRD_PARAMETER = 'Parámetro 3:'
FOURTH_PARAMETER = 'Parámetro 4:'
ONE_PARAMETER = '1P'
TWO_PARAMETERS = '2P'
THREE_PARAMETERS = '3P'


# ---- GUI fonts ----
BOX_LABEL_FONT = QtGui.QFont()
BOX_LABEL_FONT.setPointSizeF(12)
MAIN_LABEL_FONT = QtGui.QFont()
MAIN_LABEL_FONT.setPointSizeF(10)
RADIO_LABEL_FONT = QtGui.QFont()
RADIO_LABEL_FONT.setPointSizeF(10)


class UiConfigDialog(object):
    def setupUi(self, config_dialog):
        config_dialog.setObjectName("config_dialog")
        config_dialog.resize(800, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(config_dialog.sizePolicy().hasHeightForWidth())
        config_dialog.setSizePolicy(sizePolicy)
        config_dialog.setMinimumSize(QtCore.QSize(800, 400))
        config_dialog.setMaximumSize(QtCore.QSize(800, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("../icons/icon.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )
        config_dialog.setWindowIcon(icon)

        config_dialog.setStyleSheet("* {\n"
"    background: #26282b;\n"
"    color: #DDDDDD;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: none;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QCheckBox, QRadioButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QCheckBox::disabled, QRadioButton:disabled {\n"
"    color: #787878;\n"
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
"    background: #353535;\n"
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
"QLabel {\n"
"    border: none;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    background: #7971ea;\n"
"}")
        config_dialog.setModal(True)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(config_dialog)
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3.setSpacing(5)

        self.chart_preview_box = QtWidgets.QGroupBox(config_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart_preview_box.sizePolicy().hasHeightForWidth())
        self.chart_preview_box.setSizePolicy(sizePolicy)
        self.chart_preview_box.setFont(BOX_LABEL_FONT)
        self.pdf_chartview = QChartView()
        self.pdf_chartview.setRenderHint(QtGui.QPainter.Antialiasing)
        self.view_layout = QtWidgets.QHBoxLayout(self.chart_preview_box)
        self.view_layout.setContentsMargins(10, 15, 10, 10)
        self.view_layout.setSpacing(5)
        self.view_layout.addWidget(self.pdf_chartview)
        self.horizontalLayout_3.addWidget(self.chart_preview_box)

        self.control_layout = QtWidgets.QVBoxLayout()
        self.control_layout.setContentsMargins(10, 40, 10, 20)
        self.control_layout.setSpacing(30)

        self.parameters_box = QtWidgets.QGroupBox(config_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameters_box.sizePolicy().hasHeightForWidth())
        self.parameters_box.setSizePolicy(sizePolicy)
        self.parameters_box.setFont(BOX_LABEL_FONT)
        self.parameters_box.setObjectName("parameters_box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.parameters_box)
        self.verticalLayout.setContentsMargins(10, 20, 10, 10)
        self.verticalLayout.setSpacing(5)

        self.row_1 = QtWidgets.QHBoxLayout()
        self.row_1.setContentsMargins(40, -1, 10, -1)
        self.row_1.setSpacing(5)

        self.radiobtn_1 = QtWidgets.QRadioButton(self.parameters_box)
        self.radiobtn_1.setEnabled(True)
        self.radiobtn_1.setFont(RADIO_LABEL_FONT)
        self.row_1.addWidget(self.radiobtn_1)

        self.radiobtn_2 = QtWidgets.QRadioButton(self.parameters_box)
        self.radiobtn_2.setEnabled(True)
        self.radiobtn_2.setFont(RADIO_LABEL_FONT)
        self.row_1.addWidget(self.radiobtn_2)

        self.radiobtn_3 = QtWidgets.QRadioButton(self.parameters_box)
        self.radiobtn_3.setFont(RADIO_LABEL_FONT)
        self.row_1.addWidget(self.radiobtn_3)

        self.row_2 = QtWidgets.QHBoxLayout()
        self.row_2.setContentsMargins(5, 5, 5, 5)
        self.row_2.setSpacing(5)

        self.parameter_label_1 = QtWidgets.QLabel(self.parameters_box)
        self.parameter_label_1.setFont(MAIN_LABEL_FONT)
        self.parameter_spbox_1 = QtWidgets.QDoubleSpinBox(self.parameters_box)
        self.parameter_spbox_1.setEnabled(True)
        self.parameter_spbox_1.setFont(MAIN_LABEL_FONT)
        self.parameter_spbox_1.setDecimals(10)
        self.parameter_spbox_1.setSingleStep(0.1)
        self.parameter_spbox_1.setValue(0.5)

        self.row_2.addWidget(self.parameter_label_1)
        self.row_2.addWidget(self.parameter_spbox_1)
        self.row_2.setStretch(0, 40)
        self.row_2.setStretch(1, 60)

        self.row_3 = QtWidgets.QHBoxLayout()
        self.row_3.setContentsMargins(5, 5, 5, 5)
        self.row_3.setSpacing(5)

        self.parameter_label_2 = QtWidgets.QLabel(self.parameters_box)
        self.parameter_label_2.setFont(MAIN_LABEL_FONT)
        self.parameter_spbox_2 = QtWidgets.QDoubleSpinBox(self.parameters_box)
        self.parameter_spbox_2.setFont(MAIN_LABEL_FONT)
        self.parameter_spbox_2.setDecimals(10)
        self.parameter_spbox_2.setSingleStep(0.1)
        self.parameter_spbox_2.setObjectName("parameter_spbox_2")
        self.parameter_spbox_2.setValue(0.2)

        self.row_3.addWidget(self.parameter_label_2)
        self.row_3.addWidget(self.parameter_spbox_2)
        self.row_3.setStretch(0, 40)
        self.row_3.setStretch(1, 60)

        self.row_4 = QtWidgets.QHBoxLayout()
        self.row_4.setContentsMargins(5, 5, 5, 5)
        self.row_4.setSpacing(5)

        self.parameter_label_3 = QtWidgets.QLabel(self.parameters_box)
        self.parameter_label_3.setFont(MAIN_LABEL_FONT)
        self.parameter_label_3.setObjectName("parameter_label_3")
        self.row_4.addWidget(self.parameter_label_3)
        self.parameter_spbox_3 = QtWidgets.QDoubleSpinBox(self.parameters_box)
        self.parameter_spbox_3.setFont(MAIN_LABEL_FONT)
        self.parameter_spbox_3.setDecimals(10)
        self.parameter_spbox_3.setSingleStep(0.1)
        self.parameter_spbox_3.setObjectName("parameter_spbox_3")
        self.parameter_spbox_3.setValue(0.2)

        self.row_4.addWidget(self.parameter_spbox_3)
        self.row_4.setStretch(0, 40)
        self.row_4.setStretch(1, 60)

        self.row_5 = QtWidgets.QHBoxLayout()
        self.row_5.setContentsMargins(5, 5, 5, 5)
        self.row_5.setSpacing(5)

        self.parameter_label_4 = QtWidgets.QLabel(self.parameters_box)
        self.parameter_label_4.setFont(MAIN_LABEL_FONT)
        self.parameter_label_4.setObjectName("parameter_label_4")
        self.row_5.addWidget(self.parameter_label_4)
        self.parameter_spbox_4 = QtWidgets.QDoubleSpinBox(self.parameters_box)
        self.parameter_spbox_4.setFont(MAIN_LABEL_FONT)
        self.parameter_spbox_4.setSingleStep(0.1)
        self.parameter_spbox_4.setDecimals(10)
        self.parameter_spbox_4.setValue(0.5)

        self.row_5.addWidget(self.parameter_spbox_4)
        self.row_5.setStretch(0, 40)
        self.row_5.setStretch(1, 60)

        self.verticalLayout.addLayout(self.row_1)
        self.verticalLayout.addLayout(self.row_2)
        self.verticalLayout.addLayout(self.row_3)
        self.verticalLayout.addLayout(self.row_4)
        self.verticalLayout.addLayout(self.row_5)

        self.control_layout.addWidget(self.parameters_box)

        self.radios = [self.radiobtn_1, self.radiobtn_2, self.radiobtn_3]

        self.parameter_labels = [self.parameter_label_1, self.parameter_label_2,
                                 self.parameter_label_3, self.parameter_label_4]

        self.spboxes = [self.parameter_spbox_1, self.parameter_spbox_2,
                                  self.parameter_spbox_3, self.parameter_spbox_4]

        self.btn_layout_outer = QtWidgets.QVBoxLayout()
        self.btn_layout_outer.setContentsMargins(0, 0, 0, 0)
        self.btn_layout_outer.setSpacing(10)

        self.btn_layout_inner = QtWidgets.QHBoxLayout()
        self.btn_layout_inner.setContentsMargins(40, 5, 40, 5)
        self.btn_layout_inner.setSpacing(0)

        self.btn_submit = QtWidgets.QPushButton(config_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_submit.sizePolicy().hasHeightForWidth())
        self.btn_submit.setSizePolicy(sizePolicy)
        self.btn_submit.setFont(MAIN_LABEL_FONT)
        self.btn_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/accept.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_submit.setIcon(icon1)
        self.btn_submit.setIconSize(QtCore.QSize(60, 60))
        self.btn_submit.setFlat(True)
        self.btn_submit.setObjectName("btn_submit")
        self.btn_layout_inner.addWidget(self.btn_submit)

        self.btn_reject = QtWidgets.QPushButton(config_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_reject.sizePolicy().hasHeightForWidth())
        self.btn_reject.setSizePolicy(sizePolicy)
        self.btn_reject.setFont(MAIN_LABEL_FONT)
        self.btn_reject.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/reject.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reject.setIcon(icon2)
        self.btn_reject.setIconSize(QtCore.QSize(60, 60))
        self.btn_reject.setFlat(True)
        self.btn_reject.setObjectName("btn_reject")
        self.btn_layout_inner.addWidget(self.btn_reject)
        self.btn_layout_inner.setStretch(0, 50)
        self.btn_layout_inner.setStretch(1, 50)
        self.btn_layout_outer.addLayout(self.btn_layout_inner)
        self.btn_layout_outer.setStretch(0, 40)

        self.control_layout.addLayout(self.btn_layout_outer)
        self.control_layout.setStretch(0, 75)
        self.control_layout.setStretch(1, 25)
        self.horizontalLayout_3.addLayout(self.control_layout)
        self.horizontalLayout_3.setStretch(0, 60)
        self.horizontalLayout_3.setStretch(1, 40)

        self.retranslateUi(config_dialog)
        QtCore.QMetaObject.connectSlotsByName(config_dialog)

    def retranslateUi(self, config_dialog):
        _translate = QtCore.QCoreApplication.translate
        config_dialog.setWindowTitle(_translate("config_dialog", "Parametrization"))
        self.chart_preview_box.setTitle(_translate("config_dialog", "PDF chart preview"))
        self.parameters_box.setTitle(_translate("config_dialog", "Distribution parameters"))
        self.radiobtn_1.setText(_translate("config_dialog", ONE_PARAMETER))
        self.radiobtn_2.setText(_translate("config_dialog", TWO_PARAMETERS))
        self.radiobtn_3.setText(_translate("config_dialog", THREE_PARAMETERS))
        self.parameter_label_1.setText(_translate("config_dialog", FIRST_PARAMETER))
        self.parameter_label_2.setText(_translate("config_dialog", SECOND_PARAMETER))
        self.parameter_label_3.setText(_translate("config_dialog", THIRD_PARAMETER))
        self.parameter_label_4.setText(_translate("config_dialog", FOURTH_PARAMETER))
