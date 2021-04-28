from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChartView


# ---- Dialog attributes ----
MINIMUM_WIDTH = 800
MINIMUM_HEIGHT = 400
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 400
SIZE_POLICY_EXPANDING = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
SIZE_POLICY_PREFERRED = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

# ---- Labels ----
DEFAULT_PARAMETER_LABELS = (
    'Parámetro 1:',
    'Parámetro 2:',
    'Parámetro 3:',
    'Parámetro 4:'
)

# ---- Fonts ----
BOX_LABEL_FONT = QtGui.QFont()
BOX_LABEL_FONT.setPointSizeF(12)
MAIN_LABEL_FONT = QtGui.QFont()
MAIN_LABEL_FONT.setPointSizeF(10)
RADIO_LABEL_FONT = QtGui.QFont()
RADIO_LABEL_FONT.setPointSizeF(10)

# ---- Fonts ----
DEFAULT_SINGLE_STEP = 0.5


class DialogTemplate(object):
    def setup(self, dialog, **kwargs):
        dialog.setObjectName("dialog")
        dialog.resize(kwargs.get('width', DEFAULT_WIDTH), kwargs.get('height', DEFAULT_HEIGHT))
        dialog_size_policy = SIZE_POLICY_PREFERRED
        dialog_size_policy.setHorizontalStretch(0)
        dialog_size_policy.setVerticalStretch(0)
        dialog_size_policy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())
        dialog.setSizePolicy(dialog_size_policy)
        dialog.setMinimumSize(QtCore.QSize(MINIMUM_WIDTH, MINIMUM_HEIGHT))
        dialog.setMaximumSize(QtCore.QSize(MINIMUM_WIDTH, MINIMUM_HEIGHT))
        dialog_icon = QtGui.QIcon()
        dialog_icon.addPixmap(
            QtGui.QPixmap("../icons/simulator.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )
        dialog.setWindowIcon(dialog_icon)

        dialog.setStyleSheet("* {\n"
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
        dialog.setModal(True)

        self.dialog_layout = QtWidgets.QHBoxLayout(dialog)
        self.dialog_layout.setContentsMargins(10, 10, 10, 10)
        self.dialog_layout.setSpacing(5)

        self.control_layout = QtWidgets.QVBoxLayout()
        self.control_layout.setContentsMargins(10, 40, 10, 20)
        self.control_layout.setSpacing(30)

        # Preview components
        self.chart_preview_box = QtWidgets.QGroupBox(dialog)
        self.chart_preview = QChartView()
        self._build_preview_box()

        # Parameter components
        self.parameter_box = QtWidgets.QGroupBox(dialog)
        self.parameter_labels = [QtWidgets.QLabel(self.parameter_box) for _ in range(len(DEFAULT_PARAMETER_LABELS))]
        self.parameter_spinners = [QtWidgets.QDoubleSpinBox(self.parameter_box) for _ in range(len(DEFAULT_PARAMETER_LABELS))]
        self._build_parameter_box()

        # Button section
        self.btn_submit = QtWidgets.QPushButton(dialog)
        self.btn_reject = QtWidgets.QPushButton(dialog)
        self._build_button_box()

        self.dialog_layout.addLayout(self.control_layout)
        self.dialog_layout.setStretch(0, 60)
        self.dialog_layout.setStretch(1, 40)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def _build_button_box(self):
        """

        """

        # Size policies
        btn_submit_size_policy = SIZE_POLICY_PREFERRED
        btn_submit_size_policy.setHorizontalStretch(0)
        btn_submit_size_policy.setVerticalStretch(0)
        btn_submit_size_policy.setHeightForWidth(self.btn_submit.sizePolicy().hasHeightForWidth())
        self.btn_submit.setSizePolicy(btn_submit_size_policy)
        btn_reject_size_policy = SIZE_POLICY_PREFERRED
        btn_reject_size_policy.setHorizontalStretch(0)
        btn_reject_size_policy.setVerticalStretch(0)
        btn_reject_size_policy.setHeightForWidth(self.btn_reject.sizePolicy().hasHeightForWidth())
        self.btn_reject.setSizePolicy(btn_reject_size_policy)

        # Layout
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.setContentsMargins(40, 5, 40, 5)
        btn_layout.setSpacing(0)

        # Buttons
        self.btn_submit.setFont(MAIN_LABEL_FONT)
        self.btn_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_submit_icon = QtGui.QIcon()
        btn_submit_icon.addPixmap(QtGui.QPixmap("../icons/accept.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_submit.setIcon(btn_submit_icon)
        self.btn_submit.setIconSize(QtCore.QSize(60, 60))
        self.btn_submit.setFlat(True)
        self.btn_reject.setFont(MAIN_LABEL_FONT)
        self.btn_reject.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_reject_icon = QtGui.QIcon()
        btn_reject_icon.addPixmap(QtGui.QPixmap("../icons/reject.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reject.setIcon(btn_reject_icon)
        self.btn_reject.setIconSize(QtCore.QSize(60, 60))
        self.btn_reject.setFlat(True)

        btn_layout.addWidget(self.btn_submit)
        btn_layout.addWidget(self.btn_reject)
        btn_layout.setStretch(0, 50)
        btn_layout.setStretch(1, 50)
        self.control_layout.addLayout(btn_layout)
        self.control_layout.setStretch(0, 75)
        self.control_layout.setStretch(1, 25)

    def _build_parameter_box(self):
        """

        """

        # Size policies
        parameter_box_size_policy = SIZE_POLICY_EXPANDING
        parameter_box_size_policy.setHorizontalStretch(0)
        parameter_box_size_policy.setVerticalStretch(0)
        parameter_box_size_policy.setHeightForWidth(self.parameter_box.sizePolicy().hasHeightForWidth())
        self.parameter_box.setSizePolicy(parameter_box_size_policy)
        self.parameter_box.setFont(BOX_LABEL_FONT)

        # Layouts
        parameter_box_layout = QtWidgets.QVBoxLayout(self.parameter_box)
        parameter_box_layout.setSpacing(5)
        parameter_box_layout.setContentsMargins(10,20,10,10)
        row_layouts = [QtWidgets.QHBoxLayout() for _ in range(len(DEFAULT_PARAMETER_LABELS))]

        # Labels
        for label, text in zip(self.parameter_labels, DEFAULT_PARAMETER_LABELS):
            label.setFont(MAIN_LABEL_FONT)
            label.setText(text)

        # Spinners
        for spin in self.parameter_spinners:
            spin.setFont(MAIN_LABEL_FONT)
            spin.setDecimals(10)
            spin.setSingleStep(DEFAULT_SINGLE_STEP)

        for index, row_layout in enumerate(row_layouts):
            row_layout.addWidget(self.parameter_labels[index])
            row_layout.addWidget(self.parameter_spinners[index])
            row_layout.setStretch(0, 40)
            row_layout.setStretch(1, 60)
            parameter_box_layout.addLayout(row_layout)

        self.control_layout.addWidget(self.parameter_box)

    def _build_preview_box(self):
        """

        """

        # Size policies
        preview_box_size_policy = SIZE_POLICY_EXPANDING
        preview_box_size_policy.setHorizontalStretch(0)
        preview_box_size_policy.setVerticalStretch(0)
        preview_box_size_policy.setHeightForWidth(self.chart_preview_box.sizePolicy().hasHeightForWidth())
        self.chart_preview_box.setSizePolicy(preview_box_size_policy)
        self.chart_preview_box.setFont(BOX_LABEL_FONT)

        # Layouts
        preview_box_layout = QtWidgets.QHBoxLayout(self.chart_preview_box)
        preview_box_layout.setContentsMargins(10, 15, 10, 10)
        preview_box_layout.setSpacing(5)

        self.chart_preview.setRenderHint(QtGui.QPainter.Antialiasing)

        preview_box_layout.addWidget(self.chart_preview)
        self.dialog_layout.addWidget(self.chart_preview_box)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Parametrization"))
        self.chart_preview_box.setTitle(_translate("dialog", "PDF chart preview"))
        self.parameter_box.setTitle(_translate("dialog", "Distribution parameters"))
