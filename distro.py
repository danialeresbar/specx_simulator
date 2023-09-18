from PyQt5 import QtCore, QtGui, QtWidgets
import canvas

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(700, 450))
        Dialog.setMaximumSize(QtCore.QSize(700, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/prob.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QDialog#Dialog{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(59, 59, 59, 255));    \n"
"}")
        Dialog.setModal(True)

        self.container = QtWidgets.QWidget(Dialog)
        self.container.setGeometry(QtCore.QRect(0, 0, 700, 450))
        sizePolicy_widget = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy_widget.setHorizontalStretch(0)
        sizePolicy_widget.setVerticalStretch(0)
        sizePolicy_widget.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
        self.container.setSizePolicy(sizePolicy_widget)
        self.container.setMinimumSize(QtCore.QSize(700, 450))

        self.layout_central = QtWidgets.QGridLayout(self.container)
        self.layout_central.setContentsMargins(10, 10, 10, 10)
        self.layout_central.setHorizontalSpacing(0)
        self.layout_central.setVerticalSpacing(10)
        
        self.div_1 = QtWidgets.QWidget(self.container)
        sizePolicy_widget.setHeightForWidth(self.div_1.sizePolicy().hasHeightForWidth())
        self.div_1.setSizePolicy(sizePolicy_widget)
        self.div_1.setMinimumSize(QtCore.QSize(680, 200))

        self.layout_dynamic = QtWidgets.QGridLayout(self.div_1)
        self.layout_dynamic.setContentsMargins(0, 0, 0, 0)
        self.layout_dynamic.setHorizontalSpacing(5)
        self.layout_dynamic.setVerticalSpacing(0)
        self.layout_dynamic.setObjectName("layout_dynamic")

        self.params_box = QtWidgets.QGroupBox(self.div_1)
        sizePolicy_widget.setHeightForWidth(self.params_box.sizePolicy().hasHeightForWidth())
        self.params_box.setSizePolicy(sizePolicy_widget)
        self.params_box.setMinimumSize(QtCore.QSize(320, 200))
        font_box = QtGui.QFont()
        font_box.setFamily("Garamond")
        font_box.setPointSize(22)
        self.params_box.setFont(font_box)
        self.params_box.setStyleSheet("QGroupBox {\n"
"    margin-top:25px;\n"
"    border:1px solid rgba(25,25,25,127);\n"
"    border-radius:8px;\n"
"    background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(106,106,106,255),stop:1 rgba(106,106,106,75));\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(59, 59, 59, 255));\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 5px;\n"
"    subcontrol-origin: margin;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    subcontrol-position: top left;\n"
"    left: 20px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"\n"
"}\n"
"")

        self.layout_params = QtWidgets.QGridLayout(self.params_box)
        self.layout_params.setContentsMargins(10, 10, 10, 10)
        self.layout_params.setSpacing(5)
        
        self.params_area = QtWidgets.QWidget(self.params_box)
        sizePolicy_widget.setHeightForWidth(self.params_area.sizePolicy().hasHeightForWidth())
        self.params_area.setSizePolicy(sizePolicy_widget)
        self.params_area.setStyleSheet("QLabel{\n"
"    color: #ffffff;\n"
"}")
    
        self.layout_name = QtWidgets.QGridLayout(self.params_area)
        self.layout_name.setContentsMargins(0, 0, 0, 0)
        self.layout_name.setSpacing(5)

        self.label_1 = QtWidgets.QLabel(self.params_area)
        self.label_2 = QtWidgets.QLabel(self.params_area)
        self.label_3 = QtWidgets.QLabel(self.params_area)
        self.label_4 = QtWidgets.QLabel(self.params_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        font_label = QtGui.QFont()
        font_label.setFamily("Garamond")
        font_label.setPointSize(18)
        font_label.setBold(True)
        font_label.setWeight(75)
        self.labels = [self.label_1, self.label_2, self.label_3, self.label_4]
        row = 0
        for label in self.labels:
            label.setMinimumSize(QtCore.QSize(176, 33))
            sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
            label.setSizePolicy(sizePolicy)
            label.setFont(font_label)
            label.setAlignment(QtCore.Qt.AlignCenter)
            self.layout_name.addWidget(label, row, 0, 1, 1)
            row = row + 1

        self.layout_params.addWidget(self.params_area, 0, 0, 1, 1)

        self.value_area = QtWidgets.QWidget(self.params_box)
        sizePolicy_widget.setHeightForWidth(self.value_area.sizePolicy().hasHeightForWidth())
        self.value_area.setSizePolicy(sizePolicy_widget)
        
        self.layout_spin = QtWidgets.QGridLayout(self.value_area)
        self.layout_spin.setContentsMargins(0, 0, 0, 0)
        self.layout_spin.setHorizontalSpacing(0)
        self.layout_spin.setVerticalSpacing(5)
        
        self.param_1 = QtWidgets.QDoubleSpinBox(self.value_area)
        self.param_2 = QtWidgets.QDoubleSpinBox(self.value_area)
        self.param_3 = QtWidgets.QDoubleSpinBox(self.value_area)
        self.param_4 = QtWidgets.QDoubleSpinBox(self.value_area)        
        font_spin = QtGui.QFont()
        font_spin.setPointSize(10)
        self.params = [self.param_1, self.param_2, self.param_3, self.param_4]
        row = 0
        for param in self.params:
            param.setMinimumSize(QtCore.QSize(117, 33))
            sizePolicy.setHeightForWidth(param.sizePolicy().hasHeightForWidth())
            param.setFont(font_spin)
            param.setSizePolicy(sizePolicy)
            param.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            param.setAlignment(QtCore.Qt.AlignCenter)
            param.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
            param.setDecimals(8)
            param.setMaximum(100)
            param.setValue(1)
            param.setSingleStep(0.1)
            self.layout_spin.addWidget(param, row, 0, 1, 1)
            row = row + 1

        self.layout_params.addWidget(self.value_area, 0, 1, 1, 1)
        self.layout_params.setColumnStretch(0, 60)
        self.layout_params.setColumnStretch(1, 40)
        self.layout_dynamic.addWidget(self.params_box, 0, 0, 1, 1)

        self.description = QtWidgets.QLabel(self.div_1)
        sizePolicy_widget.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy_widget)
        self.description.setMinimumSize(QtCore.QSize(330, 200))
        self.description.setPixmap(QtGui.QPixmap("../clon/ui/icons/bern.png"))
        self.description.setScaledContents(True)
        self.description.setAlignment(QtCore.Qt.AlignCenter)
        self.layout_dynamic.addWidget(self.description, 0, 1, 1, 1)
        self.layout_dynamic.setColumnStretch(0, 40)
        self.layout_dynamic.setColumnStretch(1, 60)
        self.layout_central.addWidget(self.div_1, 0, 0, 1, 1)

        self.div_2 = QtWidgets.QWidget(self.container)
        sizePolicy_widget.setHeightForWidth(self.div_2.sizePolicy().hasHeightForWidth())
        self.div_2.setSizePolicy(sizePolicy_widget)
        self.layout_static = QtWidgets.QGridLayout(self.div_2)
        self.layout_static.setContentsMargins(0, 0, 0, 0)
        self.layout_static.setHorizontalSpacing(5)
        self.layout_static.setVerticalSpacing(0)

        self.view_area = QtWidgets.QGroupBox(self.div_2)
        sizePolicy_widget.setHeightForWidth(self.view_area.sizePolicy().hasHeightForWidth())
        self.view_area.setSizePolicy(sizePolicy_widget)
        self.view_area.setMinimumSize(QtCore.QSize(420, 220))
        self.view_area.setFont(font_box)
        self.view_area.setStyleSheet("QGroupBox {\n"
"    margin-top:25px;\n"
"    border:1px solid rgba(25,25,25,127);\n"
"    border-radius:8px;\n"
"    background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(106,106,106,255),stop:1 rgba(106,106,106,75));\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(59, 59, 59, 255));\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 5px;\n"
"    subcontrol-origin: margin;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    subcontrol-position: top left;\n"
"    left: 20px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"\n"
"}\n"
"")
        
        self.layout_view = QtWidgets.QGridLayout(self.view_area)
        self.layout_view.setContentsMargins(10, 10, 10, 10)
        self.layout_view.setSpacing(5)
        self.layout_view.setObjectName("layout_view")

        self.plot_area = QtWidgets.QWidget(self.view_area)
        sizePolicy_widget.setHeightForWidth(self.plot_area.sizePolicy().hasHeightForWidth())
        self.plot_area.setSizePolicy(sizePolicy_widget)
        self.canvas_lienzo = canvas.Canvas()
        layout_canvas = QtWidgets.QGridLayout(self.plot_area)
        layout_canvas.setContentsMargins(0, 0, 0, 0)
        layout_canvas.addWidget(self.canvas_lienzo, 0, 0, 1, 1)
        
        self.layout_view.addWidget(self.plot_area, 0, 0, 1, 1)
        self.layout_static.addWidget(self.view_area, 0, 0, 1, 1)

        self.control_area = QtWidgets.QWidget(self.div_2)
        sizePolicy_widget.setHeightForWidth(self.control_area.sizePolicy().hasHeightForWidth())
        self.control_area.setSizePolicy(sizePolicy_widget)
        self.layout_buttons = QtWidgets.QGridLayout(self.control_area)
        self.layout_buttons.setContentsMargins(0, 0, 0, 0)
        self.layout_buttons.setHorizontalSpacing(0)
        self.layout_buttons.setVerticalSpacing(5)
        self.layout_buttons.setObjectName("layout_buttons")

        self.control_box = QtWidgets.QGroupBox(self.control_area)
        sizePolicy_widget.setHeightForWidth(self.control_box.sizePolicy().hasHeightForWidth())
        self.control_box.setSizePolicy(sizePolicy_widget)
        self.control_box.setMinimumSize(QtCore.QSize(250, 100))
        self.control_box.setFont(font_box)
        self.control_box.setStyleSheet("QGroupBox {\n"
"    margin-top:25px;\n"
"    border:1px solid rgba(25,25,25,127);\n"
"    border-radius:8px;\n"
"    background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(106,106,106,255),stop:1 rgba(106,106,106,75));\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(59, 59, 59, 255));\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 5px;\n"
"    subcontrol-origin: margin;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    subcontrol-position: top left;\n"
"    left: 20px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"\n"
"}\n"
"")
        
        self.layout_control = QtWidgets.QGridLayout(self.control_box)
        self.layout_control.setContentsMargins(10, 10, 10, 10)
        self.layout_control.setSpacing(5)
        self.layout_control.setObjectName("layout_control")

        self.reset = QtWidgets.QPushButton(self.control_box)
        self.reset.setEnabled(True)
        sizePolicy_buttons = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy_buttons.setHorizontalStretch(0)
        sizePolicy_buttons.setVerticalStretch(0)
        sizePolicy_buttons.setHeightForWidth(self.reset.sizePolicy().hasHeightForWidth())
        self.reset.setSizePolicy(sizePolicy_buttons)
        self.reset.setMinimumSize(QtCore.QSize(110, 40))
        font_buttons = QtGui.QFont()
        font_buttons.setFamily("Garamond")
        font_buttons.setPointSize(14)
        font_buttons.setBold(False)
        font_buttons.setWeight(50)
        self.reset.setFont(font_buttons)
        self.reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset.setStyleSheet("QPushButton {\n"
"    color: qlineargradient(spread:pad, x1:0.471, y1:1, x2:0.455045, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(39, 39, 39, 255));\n"
"    border: 1px solid qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(106,106,106,255),stop:1 rgba(106,106,106,75));;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2487C8;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        icon_reset = QtGui.QIcon()
        icon_reset.addPixmap(QtGui.QPixmap("../clon/ui/icons/default.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset.setIcon(icon_reset)
        self.reset.setIconSize(QtCore.QSize(32, 32))
        self.layout_control.addWidget(self.reset, 0, 0, 1, 1)

        self.submit = QtWidgets.QPushButton(self.control_box)
        self.submit.setEnabled(True)
        sizePolicy_buttons.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy_buttons)
        self.submit.setMinimumSize(QtCore.QSize(110, 40))
        self.submit.setFont(font_buttons)
        icon_submit = QtGui.QIcon()
        icon_submit.addPixmap(QtGui.QPixmap("icons/submit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submit.setIcon(icon_submit)
        self.submit.setIconSize(QtCore.QSize(32, 32))
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit.setStyleSheet("QPushButton {\n"
"    color: qlineargradient(spread:pad, x1:0.471, y1:1, x2:0.455045, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(39, 39, 39, 255));\n"
"    border: 1px solid qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(106,106,106,255),stop:1 rgba(106,106,106,75));;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2487C8;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        
        self.layout_control.addWidget(self.submit, 0, 1, 1, 1)
        self.layout_buttons.addWidget(self.control_box, 1, 0, 1, 1)

        self.icon_area = QtWidgets.QWidget(self.control_area)
        sizePolicy_widget.setHeightForWidth(self.icon_area.sizePolicy().hasHeightForWidth())
        self.icon_area.setSizePolicy(sizePolicy_widget)
        self.icon_area.setObjectName("icon_area")
        self.layout_icon = QtWidgets.QGridLayout(self.icon_area)
        self.layout_icon.setContentsMargins(0, 0, 0, 0)
        self.layout_icon.setHorizontalSpacing(5)
        self.layout_icon.setVerticalSpacing(0)

        self.icon_prob = QtWidgets.QLabel(self.icon_area)
        sizePolicy_widget.setHeightForWidth(self.icon_prob.sizePolicy().hasHeightForWidth())
        self.icon_prob.setSizePolicy(sizePolicy_widget)
        self.icon_prob.setMinimumSize(QtCore.QSize(122, 115))
        self.icon_prob.setPixmap(QtGui.QPixmap("icons/verify.png"))
        self.icon_prob.setScaledContents(True)
        self.layout_icon.addWidget(self.icon_prob, 0, 0, 1, 1)
        self.icon_look = QtWidgets.QLabel(self.icon_area)
        sizePolicy_widget.setHeightForWidth(self.icon_look.sizePolicy().hasHeightForWidth())
        self.icon_look.setSizePolicy(sizePolicy_widget)
        self.icon_look.setMinimumSize(QtCore.QSize(122, 115))
        self.icon_look.setPixmap(QtGui.QPixmap("icons/view.png"))
        self.icon_look.setScaledContents(True)
        self.layout_icon.addWidget(self.icon_look, 0, 1, 1, 1)
        self.layout_buttons.addWidget(self.icon_area, 0, 0, 1, 1)
        self.layout_static.addWidget(self.control_area, 0, 1, 1, 1)
        self.layout_central.addWidget(self.div_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Distribution"))
        self.params_box.setTitle(_translate("Dialog", "Parameters"))
        self.label_1.setText(_translate("Dialog", "Lambda_scale"))
        self.label_2.setText(_translate("Dialog", "Lambda_scale"))
        self.label_3.setText(_translate("Dialog", "Lambda_scale"))
        self.label_4.setText(_translate("Dialog", "Lambda_scale"))
        self.view_area.setTitle(_translate("Dialog", "Preview"))
        self.control_box.setTitle(_translate("Dialog", "Control"))
        self.reset.setText(_translate("Dialog", "Reset"))
        self.submit.setText(_translate("Dialog", "Submit"))
