from PyQt5 import QtCore, QtGui, QtWidgets
import dialogo
from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Dialogo de parametrización de las distribuciones
        self.modal = dialogo.Distribution()

        MainWindow.setEnabled(True)
        MainWindow.resize(1150, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1150, 700))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setWindowTitle("Specx")
        icon_mainwindow = QtGui.QIcon()
        icon_mainwindow.addPixmap(QtGui.QPixmap("icons/spectre.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon_mainwindow)
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color:qlineargradient(spread:pad, x1:0.471, y1:1, x2:0.455045, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(39, 39, 39, 255));\n"
"}\n"
"\n"
"QWidget#centralwidget{    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(59, 59, 59, 255));    \n"
"}")
        
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.layout_main = QtWidgets.QGridLayout(self.centralwidget)

        self.display_area = QtWidgets.QWidget(self.centralwidget)
        sizePolicy_area = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy_area.setHorizontalStretch(0)
        sizePolicy_area.setVerticalStretch(0)
        sizePolicy_area.setHeightForWidth(self.display_area.sizePolicy().hasHeightForWidth())
        self.display_area.setSizePolicy(sizePolicy_area)
        self.display_area.setMinimumSize(QtCore.QSize(1130, 500))
        self.display_area.setStyleSheet("")
        self.display_area.setObjectName("display_area")
        self.layout_display = QtWidgets.QGridLayout(self.display_area)
        self.layout_display.setContentsMargins(0, 0, 0, 0)
        self.layout_display.setSpacing(10)
        
        self.graphics_area = QtWidgets.QWidget(self.display_area)
        sizePolicy_area.setHeightForWidth(self.graphics_area.sizePolicy().hasHeightForWidth())
        self.graphics_area.setSizePolicy(sizePolicy_area)
        self.graphics_area.setMinimumSize(QtCore.QSize(750, 500))
        self.graphics_area.setStyleSheet("")
        self.graphics_area.setObjectName("graphics_area")
        self.layout_view = QtWidgets.QGridLayout(self.graphics_area)
        self.layout_view.setContentsMargins(0, 0, 0, 0)
        self.layout_view.setSpacing(5)

        self.hist_area = QtWidgets.QWidget(self.graphics_area)
        sizePolicy_area.setHeightForWidth(self.hist_area.sizePolicy().hasHeightForWidth())
        self.hist_area.setSizePolicy(sizePolicy_area)
        self.hist_area.setMinimumSize(QtCore.QSize(0, 0))
        self.layout_hist = QtWidgets.QGridLayout(self.hist_area)
        self.layout_hist.setContentsMargins(0, 0, 0, 0)

        self.bar_summary = dialogo.canvas.Canvas()
        
        self.layout_hist.addWidget(self.bar_summary, 0, 0, 1, 1)
        self.layout_view.addWidget(self.hist_area, 0, 1, 1, 1)

        self.plot_area = QtWidgets.QWidget(self.graphics_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_area.sizePolicy().hasHeightForWidth())
        self.plot_area.setSizePolicy(sizePolicy)
        self.plot_area.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_area.setStyleSheet("")
        self.plot_area.setObjectName("plot_area")
        self.layout_plot = QtWidgets.QGridLayout(self.plot_area)
        self.layout_plot.setContentsMargins(0, 0, 0, 0)
        self.layout_plot.setSpacing(5)

        self.canvas_1 = QtWidgets.QWidget(self.plot_area)
        self.canvas_2 = QtWidgets.QWidget(self.plot_area)
        self.canvas_3 = QtWidgets.QWidget(self.plot_area)
        self.canvas_4 = QtWidgets.QWidget(self.plot_area)
        self.canvas_5 = QtWidgets.QWidget(self.plot_area)
        self.canvas_6 = QtWidgets.QWidget(self.plot_area)
        self.canvas_7 = QtWidgets.QWidget(self.plot_area)
        self.canvas_8 = QtWidgets.QWidget(self.plot_area)
        self.canvas_9 = QtWidgets.QWidget(self.plot_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        canvas_list = [self.canvas_1, self.canvas_2, self.canvas_3, self.canvas_4, self.canvas_5, self.canvas_6, self.canvas_7, self.canvas_8, self.canvas_9]
        for canvas in canvas_list:            
            sizePolicy.setHeightForWidth(canvas.sizePolicy().hasHeightForWidth())
            canvas.setSizePolicy(sizePolicy)
            canvas.setStyleSheet("QWidget {\n"
"    border: 1px solid #c8c8c8;\n"
"    border-radius: 6px;\n"
"}")

        self.plot_1 = PlotWidget()
        self.plot_2 = PlotWidget()
        self.plot_3 = PlotWidget()
        self.plot_4 = PlotWidget()
        self.plot_5 = PlotWidget()
        self.plot_6 = PlotWidget()
        self.plot_7 = PlotWidget()
        self.plot_8 = PlotWidget()
        self.plot_9 = PlotWidget()
        layout_c1 = QtWidgets.QGridLayout(self.canvas_1)
        layout_c2 = QtWidgets.QGridLayout(self.canvas_2)
        layout_c3 = QtWidgets.QGridLayout(self.canvas_3)
        layout_c4 = QtWidgets.QGridLayout(self.canvas_4)
        layout_c5 = QtWidgets.QGridLayout(self.canvas_5)
        layout_c6 = QtWidgets.QGridLayout(self.canvas_6)
        layout_c7 = QtWidgets.QGridLayout(self.canvas_7)
        layout_c8 = QtWidgets.QGridLayout(self.canvas_8)
        layout_c9 = QtWidgets.QGridLayout(self.canvas_9)

        plot_list = [self.plot_1, self.plot_2, self.plot_3, self.plot_4, self.plot_5, self.plot_6, self.plot_7, self.plot_8, self.plot_9]
        layout_list = [layout_c1, layout_c2, layout_c3, layout_c4, layout_c5, layout_c6, layout_c7, layout_c8, layout_c9]
        index_plot = 0
        for layout in layout_list:
            plot = plot_list[index_plot]
            plot.showAxis('bottom', show=False)
            #plot.setTitle("Samples", size='12pt')
            #plot.setLabel('bottom', 'Time', units='s')
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(plot, 0, 0, 1, 1)
            self.layout_plot.addWidget(canvas_list[index_plot], index_plot, 0, 1, 1)            
            index_plot = index_plot + 1

        self.layout_view.addWidget(self.plot_area, 0, 0, 1, 1)
        self.layout_view.setColumnStretch(0, 70)
        self.layout_view.setColumnStretch(1, 30)
        self.layout_display.addWidget(self.graphics_area, 0, 1, 1, 1)

        self.statistics_box = QtWidgets.QGroupBox(self.display_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.statistics_box.sizePolicy().hasHeightForWidth())
        self.statistics_box.setSizePolicy(sizePolicy)
        self.statistics_box.setMinimumSize(QtCore.QSize(350, 500))
        self.statistics_box.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(20)
        self.statistics_box.setFont(font)
        self.statistics_box.setAutoFillBackground(False)
        self.statistics_box.setStyleSheet("QGroupBox#statistics_box {\n"
"    background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(106,106,106,255),stop:1 rgba(106,106,106,75));\n"
"      margin-top:27px;\n"
"      border:1px solid rgba(25,25,25,127);\n"
"      border-radius:8px;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QGroupBox#statistics_box::title {\n"
"    color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(59, 59, 59, 255));\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 5px;\n"
"    subcontrol-origin: margin;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    subcontrol-position: top left;\n"
"    left: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    padding-top: 2px;\n"
"}")

        self.statistics_box.setObjectName("statistics_box")
        self.layout_dist = QtWidgets.QGridLayout(self.statistics_box)
        self.layout_dist.setContentsMargins(10, 10, 10, 5)
        self.layout_dist.setHorizontalSpacing(10)
        self.layout_dist.setVerticalSpacing(5)
        self.layout_dist.setObjectName("layout_dist")

        #Propiedades de los labels para las frecuencias
        font_label = QtGui.QFont()
        font_label.setFamily("Garamond")
        font_label.setPointSize(16)
        font_label.setBold(True)
        font_label.setWeight(75)

        self.freq_1 = QtWidgets.QLabel("473 MHz", self.statistics_box)
        self.freq_2 = QtWidgets.QLabel("479 MHz", self.statistics_box)
        self.freq_3 = QtWidgets.QLabel("485 MHz", self.statistics_box)
        self.freq_4 = QtWidgets.QLabel("491 MHz", self.statistics_box)
        self.freq_5 = QtWidgets.QLabel("497 MHz", self.statistics_box)
        self.freq_6 = QtWidgets.QLabel("503 MHz", self.statistics_box)
        self.freq_7 = QtWidgets.QLabel("509 MHz", self.statistics_box)
        self.freq_8 = QtWidgets.QLabel("551 MHz", self.statistics_box)
        self.freq_9 = QtWidgets.QLabel("557 MHz", self.statistics_box)

        self.labels = [self.freq_1, self.freq_2, self.freq_3, self.freq_4, self.freq_5, self.freq_6, self.freq_7, self.freq_8, self.freq_9]
        row = 0
        for label in self.labels:
            label.setMinimumSize(QtCore.QSize(80, 20))
            label.setFont(font_label)
            self.layout_dist.addWidget(label, row, 0, 1, 1)
            row = row + 1

        # Propiedades de los boxes
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font_box = QtGui.QFont()
        font_box.setFamily("Garamond")
        font_box.setPointSize(14)
        icon_choose = QtGui.QIcon()
        icon_choose.addPixmap(QtGui.QPixmap("icons/select.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_dist = QtGui.QIcon()
        icon_dist.addPixmap(QtGui.QPixmap("icons/dist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.box_1 = QtWidgets.QComboBox(self.statistics_box)
        self.box_2 = QtWidgets.QComboBox(self.statistics_box)
        self.box_3 = QtWidgets.QComboBox(self.statistics_box)
        self.box_4 = QtWidgets.QComboBox(self.statistics_box)
        self.box_5 = QtWidgets.QComboBox(self.statistics_box)
        self.box_6 = QtWidgets.QComboBox(self.statistics_box)
        self.box_7 = QtWidgets.QComboBox(self.statistics_box)
        self.box_8 = QtWidgets.QComboBox(self.statistics_box)
        self.box_9 = QtWidgets.QComboBox(self.statistics_box)

        self.boxes = [self.box_1, self.box_2, self.box_3, self.box_4, self.box_5, self.box_6, self.box_7, self.box_8, self.box_9]
        row = 0
        for box in self.boxes:
            sizePolicy.setHeightForWidth(box.sizePolicy().hasHeightForWidth())
            box.setSizePolicy(sizePolicy)
            box.setMinimumSize(QtCore.QSize(100, 30))
            box.setFont(font_box)
            box.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            box.setMaxVisibleItems(5)
            box.setIconSize(QtCore.QSize(16, 16))
            box.addItem(icon_choose, "Choose")
            box.addItem(icon_dist, "Bernoulli", self.modal.bernoulli)
            box.addItem(icon_dist, "Beta", self.modal.beta)
            box.addItem(icon_dist, "Gamma", self.modal.gamma)
            box.addItem(icon_dist, "Gumbel Max", self.modal.gumbel)
            box.addItem(icon_dist, "Laplace", self.modal.laplace)
            box.addItem(icon_dist, "Lognormal", self.modal.lognorm)
            box.addItem(icon_dist, "Lognormal(3p)", self.modal.lognorm3p)
            box.addItem(icon_dist, "Normal", self.modal.normal)
            box.addItem(icon_dist, "Rayleigh", self.modal.rayleigh)
            box.addItem(icon_dist, "Rayleigh(2p)", self.modal.rayleigh2p)
            box.addItem(icon_dist, "Uniform", self.modal.uniforme)
            box.addItem(icon_dist, "Weibull(3p)", self.modal.weibull)
            box.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}")
            self.layout_dist.addWidget(box, row, 1, 1, 1)
            box.setCurrentIndex(0)
            row = row + 1
            
        self.layout_dist.setColumnStretch(0, 30)
        self.layout_dist.setColumnStretch(1, 70)
        self.layout_display.addWidget(self.statistics_box, 0, 0, 1, 1)
        self.layout_display.setColumnStretch(0, 25)
        self.layout_main.addWidget(self.display_area, 0, 0, 1, 1)

        # Widget contenedor de los boxes y el logo de la Universidad
        self.box_area = QtWidgets.QWidget(self.centralwidget)
        sizePolicy_box = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy_box.setHorizontalStretch(0)
        sizePolicy_box.setVerticalStretch(0)
        self.layout_boxes = QtWidgets.QGridLayout(self.box_area)
        self.layout_boxes.setContentsMargins(0, 0, 0, 0)
        self.layout_boxes.setSpacing(10)
        self.layout_boxes.setObjectName("layout_boxes")

        # Box contenedor de los items de control de la simulación
        self.control_box = QtWidgets.QGroupBox(self.box_area)
        sizePolicy_box.setHeightForWidth(self.control_box.sizePolicy().hasHeightForWidth())
        self.control_box.setSizePolicy(sizePolicy_box)
        font_box = QtGui.QFont()
        font_box.setFamily("Garamond")
        font_box.setPointSize(20)
        self.control_box.setFont(font_box)
        self.control_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.control_box.setObjectName("control_box")
        self.control_box.setStyleSheet("QGroupBox#control_box {\n"
"    background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(106,106,106,255),stop:1 rgba(106,106,106,75));\n"
"      margin-top:27px;\n"
"      border:1px solid rgba(25,25,25,127);\n"
"      border-radius:8px;\n"
"}\n"
"\n"
"QGroupBox#control_box::title {\n"
"    color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(59, 59, 59, 255));\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 5px;\n"
"    subcontrol-origin: margin;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    subcontrol-position: top left;\n"
"    left: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    padding-top: 2px;\n"
"}")
        
        self.layout_control = QtWidgets.QGridLayout(self.control_box)
        self.layout_control.setContentsMargins(10, 10, 10, 10)
        self.layout_control.setHorizontalSpacing(10)
        self.layout_control.setVerticalSpacing(5)

        # Propiedades de los botones
        font_buttons = QtGui.QFont()
        font_buttons.setFamily("Garamond")
        font_buttons.setPointSize(12)
        font_buttons.setBold(False)
        font_buttons.setWeight(50)

        self.pause = QtWidgets.QPushButton(self.control_box)
        self.pause.setEnabled(False)
        icon_pause = QtGui.QIcon()
        icon_pause.addPixmap(QtGui.QPixmap("icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause.setIcon(icon_pause)
        sizePolicy_box.setHeightForWidth(self.pause.sizePolicy().hasHeightForWidth())
        self.pause.setSizePolicy(sizePolicy_box)
        self.pause.setFont(font_buttons)
        self.pause.setObjectName("pause")
        self.pause.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pause.setStyleSheet("QPushButton#pause {\n"
"    color: qlineargradient(spread:pad, x1:0.471, y1:1, x2:0.455045, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(39, 39, 39, 255));\n"
"    border: 1px solid whitesmoke;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QPushButton#pause:hover {\n"
"    background-color: rgb(171, 171, 171);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        
        self.layout_control.addWidget(self.pause, 1, 0, 1, 1)

        self.start = QtWidgets.QPushButton(self.control_box)
        self.start.setEnabled(False)
        icon_start = QtGui.QIcon()
        icon_start.addPixmap(QtGui.QPixmap("icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start.setIcon(icon_start)
        sizePolicy_box.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy_box)
        self.start.setFont(font_buttons)
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start.setObjectName("start")
        self.start.setStyleSheet("QPushButton#start {\n"
"    color: qlineargradient(spread:pad, x1:0.471, y1:1, x2:0.455045, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(39, 39, 39, 255));\n"
"    border: 1px solid whitesmoke;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#start:hover {\n"
"    background-color: #32CD32;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        
        self.layout_control.addWidget(self.start, 0, 0, 1, 1)

        self.label_scale = QtWidgets.QLabel(self.control_box)
        sizePolicy_box.setHeightForWidth(self.label_scale.sizePolicy().hasHeightForWidth())
        self.label_scale.setSizePolicy(sizePolicy_box)
        font_label.setPointSize(16)
        self.label_scale.setFont(font_label)
        self.label_scale.setAlignment(QtCore.Qt.AlignCenter)
        self.label_scale.setStyleSheet("QLabel {\n"
"color: rgb(255, 255, 255);\n"
"}")

        self.layout_control.addWidget(self.label_scale, 1, 1, 1, 1)

        self.slider_area = QtWidgets.QWidget(self.control_box)
        self.layout_slider = QtWidgets.QGridLayout(self.slider_area)
        self.layout_slider.setContentsMargins(0, 0, 0, 0)
        self.layout_slider.setSpacing(5)

        self.icon_timer = QtWidgets.QLabel(self.slider_area)
        sizePolicy_box.setHeightForWidth(self.icon_timer.sizePolicy().hasHeightForWidth())
        self.icon_timer.setSizePolicy(sizePolicy_box)
        self.icon_timer.setMinimumSize(QtCore.QSize(40, 30))
        self.icon_timer.setPixmap(QtGui.QPixmap("icons/timer.ico"))
        self.icon_timer.setScaledContents(True)
        self.icon_timer.setAlignment(QtCore.Qt.AlignCenter)
        self.layout_slider.addWidget(self.icon_timer, 0, 0, 1, 1)

        self.scale_time = QtWidgets.QSlider(self.slider_area)
        sizePolicy_box.setHeightForWidth(self.scale_time.sizePolicy().hasHeightForWidth())
        self.scale_time.setSizePolicy(sizePolicy_box)
        self.scale_time.setMinimumSize(QtCore.QSize(120, 20))
        self.scale_time.setMinimum(1)
        self.scale_time.setMaximum(50)
        self.scale_time.setSingleStep(20)
        self.scale_time.setValue(1)
        self.scale_time.setOrientation(QtCore.Qt.Horizontal)
        self.scale_time.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.scale_time.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 15px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        
        self.layout_slider.addWidget(self.scale_time, 0, 1, 1, 1)
        self.layout_slider.setColumnStretch(0, 15)
        self.layout_slider.setColumnStretch(1, 85)
        self.layout_control.addWidget(self.slider_area, 0, 1, 1, 1)
        self.layout_control.setColumnStretch(0, 25)
        self.layout_control.setColumnStretch(1, 75)
        self.layout_control.setRowStretch(0, 50)
        self.layout_control.setRowStretch(1, 50)
        self.layout_boxes.addWidget(self.control_box, 0, 1, 1, 1)

        # Box contenedor de items de archivos de finalización
        self.results_box = QtWidgets.QGroupBox(self.box_area)
        sizePolicy_box.setHeightForWidth(self.results_box.sizePolicy().hasHeightForWidth())
        self.results_box.setSizePolicy(sizePolicy_box)
        self.results_box.setFont(font_box)
        self.results_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.results_box.setObjectName("results_box")
        self.results_box.setStyleSheet("QGroupBox#results_box {\n"
"    background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(106,106,106,255),stop:1 rgba(106,106,106,75));\n"
"      margin-top:27px;\n"
"      border:1px solid rgba(25,25,25,127);\n"
"      border-radius:8px;\n"
"}\n"
"\n"
"QGroupBox#results_box::title {\n"
"    color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(59, 59, 59, 255));\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 5px;\n"
"    subcontrol-origin: margin;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    subcontrol-position: top left;\n"
"    left: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    padding-top: 2px;\n"
"}")
        
        self.layout_results = QtWidgets.QGridLayout(self.results_box)
        self.layout_results.setContentsMargins(10, 10, 10, 10)
        self.layout_results.setHorizontalSpacing(10)
        self.layout_results.setVerticalSpacing(5)

        self.save_graph = QtWidgets.QPushButton(self.results_box)
        self.save_graph.setEnabled(True)
        sizePolicy_box.setHeightForWidth(self.save_graph.sizePolicy().hasHeightForWidth())
        self.save_graph.setSizePolicy(sizePolicy_box)
        self.save_graph.setFont(font_buttons)
        icon_graph = QtGui.QIcon()
        icon_graph.addPixmap(QtGui.QPixmap("icons/graphs.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_graph.setIcon(icon_graph)
        self.save_graph.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_graph.setObjectName("save_graph")
        self.save_graph.setStyleSheet("QPushButton#save_graph {\n"
"    color: qlineargradient(spread:pad, x1:0.471, y1:1, x2:0.455045, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(39, 39, 39, 255));\n"
"    border: 1px solid whitesmoke;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#save_graph:hover {\n"
"    background-color: #2487C8;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        
        self.layout_results.addWidget(self.save_graph, 1, 0, 1, 1)

        self.output = QtWidgets.QPushButton(self.results_box)
        self.output.setEnabled(False)
        sizePolicy_box.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy_box)
        self.output.setMinimumSize(QtCore.QSize(0, 0))
        self.output.setFont(font_buttons)
        icon_file = QtGui.QIcon()
        icon_file.addPixmap(QtGui.QPixmap("icons/outcome.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.output.setIcon(icon_file)
        self.output.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.output.setObjectName("output")
        self.output.setStyleSheet("QPushButton#output {\n"
"    color: qlineargradient(spread:pad, x1:0.471, y1:1, x2:0.455045, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(39, 39, 39, 255));\n"
"    border: 1px solid whitesmoke;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#output:hover {\n"
"    background-color: #2487C8;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        
        self.layout_results.addWidget(self.output, 0, 0, 1, 1)

        self.icon_results = QtWidgets.QLabel(self.results_box)
        sizePolicy_box.setHeightForWidth(self.icon_results.sizePolicy().hasHeightForWidth())
        self.icon_results.setSizePolicy(sizePolicy_box)
        self.icon_results.setMinimumSize(QtCore.QSize(100, 70))
        self.icon_results.setPixmap(QtGui.QPixmap("icons/report.png"))
        self.icon_results.setScaledContents(True)
        self.icon_results.setAlignment(QtCore.Qt.AlignCenter)
        self.layout_results.addWidget(self.icon_results, 0, 1, 2, 1)

        self.layout_results.setColumnStretch(0, 45)
        self.layout_results.setColumnStretch(1, 55)
        self.layout_results.setRowStretch(0, 50)
        self.layout_results.setRowStretch(1, 50)
        self.layout_boxes.addWidget(self.results_box, 0, 2, 1, 1)

        # Box contenedor de los items con los parámetros de la simulación
        self.config_box = QtWidgets.QGroupBox(self.box_area)
        sizePolicy_box.setHeightForWidth(self.config_box.sizePolicy().hasHeightForWidth())
        self.config_box.setSizePolicy(sizePolicy_box)
        self.config_box.setFont(font_box)
        self.config_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.config_box.setObjectName("config_box")
        self.config_box.setStyleSheet("QGroupBox#config_box {\n"
"    background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(106,106,106,255),stop:1 rgba(106,106,106,75));\n"
"      margin-top:27px;\n"
"      border:1px solid rgba(25,25,25,127);\n"
"      border-radius:8px;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QGroupBox#config_box::title {\n"
"    color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(59, 59, 59, 255));\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 5px;\n"
"    subcontrol-origin: margin;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    subcontrol-position: top left;\n"
"    left: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    padding-top: 2px;\n"
"}")
        
        self.layout_params = QtWidgets.QGridLayout(self.config_box)
        self.layout_params.setContentsMargins(10, 10, 10, 10)
        self.layout_params.setHorizontalSpacing(5)
        self.layout_params.setVerticalSpacing(0)

        self.settings_area = QtWidgets.QWidget(self.config_box)
        sizePolicy_box.setHeightForWidth(self.settings_area.sizePolicy().hasHeightForWidth())
        self.settings_area.setSizePolicy(sizePolicy_box)
        self.layout_settings = QtWidgets.QGridLayout(self.settings_area)
        self.layout_settings.setContentsMargins(0, 0, 0, 0)
        self.layout_settings.setHorizontalSpacing(10)
        self.layout_settings.setVerticalSpacing(0)
        
        self.read_area = QtWidgets.QWidget(self.settings_area)
        sizePolicy_box.setHeightForWidth(self.read_area.sizePolicy().hasHeightForWidth())
        self.read_area.setSizePolicy(sizePolicy_box)
        self.layout_read = QtWidgets.QGridLayout(self.read_area)
        self.layout_read.setContentsMargins(0, 0, 0, 0)
        self.layout_read.setSpacing(5)

        self.icon_step = QtWidgets.QLabel(self.read_area)
        sizePolicy_box.setHeightForWidth(self.icon_step.sizePolicy().hasHeightForWidth())
        self.icon_step.setSizePolicy(sizePolicy_box)
        self.icon_step.setMinimumSize(QtCore.QSize(110, 70))
        self.icon_step.setPixmap(QtGui.QPixmap("icons/step.png"))
        self.icon_step.setScaledContents(True)
        self.icon_step.setAlignment(QtCore.Qt.AlignCenter)
        self.layout_read.addWidget(self.icon_step, 0, 0, 1, 1)
        self.layout_read.setRowStretch(0, 60)
        self.layout_settings.addWidget(self.read_area, 0, 0, 1, 1)

        self.config_area = QtWidgets.QWidget(self.settings_area)
        sizePolicy_box.setHeightForWidth(self.config_area.sizePolicy().hasHeightForWidth())
        self.config_area.setSizePolicy(sizePolicy_box)
        self.layout_config = QtWidgets.QGridLayout(self.config_area)
        self.layout_config.setContentsMargins(5, 5, 5, 5)
        self.layout_config.setHorizontalSpacing(0)
        self.layout_config.setVerticalSpacing(5)
    
        self.label_sp = QtWidgets.QLabel(self.config_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.label_sp.sizePolicy().hasHeightForWidth())
        self.label_sp.setSizePolicy(sizePolicy)
        font_label.setPointSize(14)
        font_label.setBold(True)
        font_label.setWeight(75)
        self.label_sp.setFont(font_label)
        self.label_sp.setAlignment(QtCore.Qt.AlignCenter)
        self.layout_config.addWidget(self.label_sp, 0, 0, 1, 1)

        self.sp_value = QtWidgets.QSpinBox(self.config_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy_box.setHeightForWidth(self.sp_value.sizePolicy().hasHeightForWidth())
        self.sp_value.setSizePolicy(sizePolicy_box)
        font_label.setPointSize(12)
        font_label.setBold(True)
        font_label.setWeight(50)
        self.sp_value.setFont(font_label)
        self.sp_value.setFrame(True)
        self.sp_value.setAlignment(QtCore.Qt.AlignCenter)
        self.sp_value.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sp_value.setMinimum(1)
        self.sp_value.setMaximum(15)
        self.sp_value.setMinimumSize(QtCore.QSize(80, 25))
        self.layout_config.addWidget(self.sp_value, 0, 1, 1, 1)

        self.label_th = QtWidgets.QLabel(self.config_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.label_th.sizePolicy().hasHeightForWidth())
        self.label_th.setSizePolicy(sizePolicy)
        font_label.setPointSize(14)
        font_label.setBold(True)
        font_label.setWeight(75)
        self.label_th.setFont(font_label)
        self.label_th.setAlignment(QtCore.Qt.AlignCenter)
        self.layout_config.addWidget(self.label_th, 1, 0, 1, 1)

        self.th_value = QtWidgets.QDoubleSpinBox(self.config_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.th_value.sizePolicy().hasHeightForWidth())
        self.th_value.setSizePolicy(sizePolicy)
        font_label.setPointSize(12)
        font_label.setBold(False)
        font_label.setWeight(50)
        self.th_value.setFont(font_label)
        self.th_value.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.th_value.setAlignment(QtCore.Qt.AlignCenter)
        self.th_value.setMinimum(0.01)
        self.th_value.setMaximum(0.75)
        self.th_value.setSingleStep(0.1)
        self.th_value.setProperty("value", 0.33)
        self.layout_config.addWidget(self.th_value, 1, 1, 1, 1)

        self.layout_config.setColumnStretch(0, 60)
        self.layout_config.setColumnStretch(1, 40)
        self.layout_config.setRowStretch(0, 50)
        self.layout_config.setRowStretch(1, 50) 

        self.layout_settings.addWidget(self.config_area, 0, 1, 1, 1)
        self.layout_settings.setColumnStretch(0, 40)
        self.layout_settings.setColumnStretch(1, 60)

        self.layout_params.addWidget(self.settings_area, 0, 0, 1, 1)
        self.layout_boxes.addWidget(self.config_box, 0, 0, 1, 1)

        self.icon_box = QtWidgets.QWidget(self.box_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_box.sizePolicy().hasHeightForWidth())
        self.icon_box.setSizePolicy(sizePolicy)
        self.icon_layout = QtWidgets.QGridLayout(self.icon_box)
        self.icon_layout.setContentsMargins(10, 10, 10, 10)
        self.icon_layout.setSpacing(5)

        self.icon_unillanos = QtWidgets.QLabel(self.icon_box)
        sizePolicy_box.setHeightForWidth(self.icon_unillanos.sizePolicy().hasHeightForWidth())
        self.icon_unillanos.setSizePolicy(sizePolicy_box)
        self.icon_unillanos.setMinimumSize(QtCore.QSize(130, 100))
        self.icon_unillanos.setPixmap(QtGui.QPixmap("icons/unillanos.png"))
        self.icon_unillanos.setScaledContents(True)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.icon_layout.addItem(spacerItem, 0, 0, 1, 1)
        self.icon_layout.addWidget(self.icon_unillanos, 0, 1, 1, 1)
        self.icon_layout.setColumnStretch(0, 80)
        self.icon_layout.setColumnStretch(1, 20)
        self.layout_boxes.addWidget(self.icon_box, 0, 3, 1, 1)

        self.layout_boxes.setColumnStretch(0, 30)
        self.layout_boxes.setColumnStretch(1, 15)
        self.layout_boxes.setColumnStretch(2, 15)
        self.layout_boxes.setColumnStretch(3, 40)
        
        self.layout_main.addWidget(self.box_area, 1, 0, 1, 1)
        self.layout_main.setRowStretch(0, 90)
        self.layout_main.setRowStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)

        # Barra de menú
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1148, 27))
        font_menubar = QtGui.QFont()
        font_menubar.setPointSize(12)
        self.menubar.setFont(font_menubar)
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("QMenuBar#menubar {\n"
"    background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(25,25,25,127),stop:1 rgba(53,53,53,75));\n"
"    border-bottom:2px solid rgba(25,25,25,75);\n"
"}\n"
"\n"
"QMenuBar#menubar::item {\n"
"    color:rgb(255, 255, 255);\n"
"    spacing:2px;\n"
"    padding:3px 4px;\n"
"    background:transparent;\n"
"}\n"
"\n"
"QMenuBar#menubar::item:selected {\n"
"    background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(106,106,106,255),stop:1 rgba(106,106,106,75));\n"
"    border-left:1px solid rgba(106,106,106,127);\n"
"    border-right:1px solid rgba(106,106,106,127);\n"
"}\n"
"\n"
"QMenuBar#menubar::item:pressed {\n"
"\n"
"    border-left:1px solid rgba(25,25,25,127);\n"
"    border-right:1px solid rgba(25,25,25,127);\n"
"}\n"
"")
        
        font_menu = QtGui.QFont()
        font_menu.setPointSize(11)

        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setFont(font_menu)
        self.file_menu.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.file_menu.setObjectName("file_menu")
        self.file_menu.setStyleSheet("QMenu#file_menu::item:disabled{\n"
"    background-color:rgba(35,35,35,127);\n"
"    color:palette(disabled);\n"
"}\n"
"\n"
"QMenu#file_menu {\n"
"    background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(25,25,25,127),stop:1 rgba(53,53,53,75));\n"
"    color: rgb(255, 255, 255);\n"
"    border:1px solid palette(shadow);\n"
"}\n"
"\n"
"QMenu#file_menu::item {\n"
"    padding: 3px 25px 3px 20px;\n"
"    border: 1px solid transparent;\n"
"}\n"
"\n"
"QMenu#file_menu::item:selected {\n"
"    border-color:rgba(147,191,236,127);\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    color:    rgb(0, 0, 0);\n"
"}\n"
"\n"
"QMenu#file_menu::separator{\n"
"      height:1px;\n"
"      background:palette(alternate-base);\n"
"      margin-left:5px;\n"
"    margin-right:5px;\n"
"}\n"
"\n"
"QMenu#file_menu::indicator{\n"
"     width:18px;\n"
"    height:18px;\n"
"}")
        
        self.config_menu = QtWidgets.QMenu(self.menubar)
        self.config_menu.setFont(font_menu)
        self.config_menu.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.config_menu.setObjectName("config_menu")
        self.config_menu.setStyleSheet("QMenu#config_menu::item:disabled{\n"
"    background-color:rgba(35,35,35,127);\n"
"    color:palette(disabled);\n"
"}\n"
"\n"
"QMenu#config_menu {\n"
"    background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(25,25,25,127),stop:1 rgba(53,53,53,75));\n"
"    color: rgb(255, 255, 255);\n"
"    border:1px solid palette(shadow);\n"
"}\n"
"\n"
"QMenu#config_menu::item {\n"
"    padding: 3px 25px 3px 20px;\n"
"    border: 1px solid transparent;\n"
"}\n"
"\n"
"QMenu#config_menu::item:selected {\n"
"    border-color:rgba(147,191,236,127);\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    color:    rgb(0, 0, 0);\n"
"}\n"
"\n"
"QMenu#config_menu::separator{\n"
"      height:1px;\n"
"      background:palette(alternate-base);\n"
"      margin-left:5px;\n"
"    margin-right:5px;\n"
"}\n"
"\n"
"QMenu#config_menu::indicator{\n"
"     width:18px;\n"
"    height:18px;\n"
"}")
        
        self.help_menu = QtWidgets.QMenu(self.menubar)
        self.help_menu.setFont(font_menu)
        self.help_menu.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.help_menu.setObjectName("help_menu")
        self.help_menu.setStyleSheet("QMenu#help_menu::item:disabled{\n"
"    background-color:rgba(35,35,35,127);\n"
"    color:palette(disabled);\n"
"}\n"
"\n"
"QMenu#help_menu {\n"
"    background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(25,25,25,127),stop:1 rgba(53,53,53,75));\n"
"    color: rgb(255, 255, 255);\n"
"    border:1px solid palette(shadow);\n"
"}\n"
"\n"
"QMenu#help_menu::item {\n"
"    padding: 3px 25px 3px 20px;\n"
"    border: 1px solid transparent;\n"
"}\n"
"\n"
"QMenu#help_menu::item:selected {\n"
"    border-color:rgba(147,191,236,127);\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    color:    rgb(0, 0, 0);\n"
"}\n"
"\n"
"QMenu#help_menu::separator{\n"
"      height:1px;\n"
"      background:palette(alternate-base);\n"
"      margin-left:5px;\n"
"    margin-right:5px;\n"
"}\n"
"\n"
"QMenu#help_menu::indicator{\n"
"     width:18px;\n"
"    height:18px;\n"
"}")
        
        MainWindow.setMenuBar(self.menubar)
        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        self.status_bar.showMessage("Welcome to PAWS Simulation")
        self.status_bar.setStyleSheet("QStatusBar{\n"
                            "   color: #FFFFFF;\n"
                            "}")
        MainWindow.setStatusBar(self.status_bar)

        self.new_action = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/new.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_action.setIcon(icon7)
        self.new_action.setObjectName("new_action")
        self.close_action = QtWidgets.QAction(MainWindow)
        self.close_action.setObjectName("close_action")
        self.about_action = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/info.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_action.setIcon(icon8)
        self.about_action.setObjectName("about_action")
        self.save_action = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_action.setIcon(icon9)
        self.save_action.setObjectName("save_action")
        self.load_action = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/load.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.load_action.setIcon(icon10)
        self.load_action.setObjectName("load_action")
        self.file_menu.addAction(self.new_action)
        self.file_menu.addAction(self.close_action)
        self.config_menu.addAction(self.save_action)
        self.config_menu.addAction(self.load_action)
        self.help_menu.addAction(self.about_action)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.config_menu.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.statistics_box.setTitle(_translate("MainWindow", "Distributions"))
        self.freq_1.setText(_translate("MainWindow", "473 MHz"))
        self.freq_2.setText(_translate("MainWindow", "479 MHz"))
        self.freq_3.setText(_translate("MainWindow", "485 MHz"))
        self.freq_4.setText(_translate("MainWindow", "491 MHz"))
        self.freq_5.setText(_translate("MainWindow", "497 MHz"))
        self.freq_6.setText(_translate("MainWindow", "503 MHz"))
        self.freq_7.setText(_translate("MainWindow", "509 MHz"))
        self.freq_8.setText(_translate("MainWindow", "551 MHz"))
        self.freq_9.setText(_translate("MainWindow", "557 MHz"))
        self.control_box.setTitle(_translate("MainWindow", "Control"))
        self.config_box.setTitle(_translate("MainWindow", "Simulation-Parameters"))
        self.results_box.setTitle(_translate("MainWindow", "Results"))
        self.pause.setText(_translate("MainWindow", "Pause"))
        self.start.setText(_translate("MainWindow", "Run"))
        self.label_scale.setText(_translate("MainWindow", "Speed X 1"))
        self.save_graph.setText(_translate("MainWindow", "Save_graph"))
        self.output.setText(_translate("MainWindow", "Output file"))
        self.label_sp.setText(_translate("MainWindow", "Sampling:"))
        self.label_th.setText(_translate("MainWindow", "Threshold:"))
        self.sp_value.setSuffix(_translate("MainWindow", "min"))
        self.file_menu.setTitle(_translate("MainWindow", "File"))
        self.config_menu.setTitle(_translate("MainWindow", "Configuration"))
        self.help_menu.setTitle(_translate("MainWindow", "Help"))
        self.new_action.setText(_translate("MainWindow", "New Simulation"))
        self.close_action.setText(_translate("MainWindow", "Exit"))
        self.save_action.setText(_translate("MainWindow", "Save config-file"))
        self.load_action.setText(_translate("MainWindow", "Load config-file"))
        self.about_action.setText(_translate("MainWindow", "About Specx"))
