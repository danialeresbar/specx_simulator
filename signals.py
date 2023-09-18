from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class Worker(QObject):
    
    #Señales personalizadas
    signal_end = pyqtSignal(list, 'PyQt_PyObject')
    signal_plot = pyqtSignal('PyQt_PyObject', float, int)
    signal_hist = pyqtSignal(list, int)
    signal_clear = pyqtSignal(list)
    finished = pyqtSignal()

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)