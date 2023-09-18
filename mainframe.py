from gui_qt import *
import signals
import generators as gen
import threads as th
import json_manager as jm

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    POINTING = signals.Worker()
    STRAND = QtCore.QThread()
    freq_parameters = [[]] * 9
    start_flag = True
    sim_thread = None
    path_data = ""

    # Constructor de la mainframe
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # Construye la interfaz de la mainframe a partir del archivo qt
        self.setupUi(self)

        # Diálogo de mensajes para avisos
        self.notice = QtWidgets.QMessageBox(self)

        self.generators = [gen.bernoulli, gen.beta, gen.gamma, gen.gumbel, gen.laplace, gen.lognormal, gen.lognormal_3p, gen.normal_scheimen, gen.rayleigh, gen.rayleigh, gen.uniform_inverse_transformation, gen.weibull]
        self.generator = None

        # Inicialización de los plots
        self.var_data = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
        self.graphic_1 = self.plot_1.plot(self.var_data[0], symbol='o', symbolSize=5, symbolBrush=('#FFFF00'))
        self.graphic_2 = self.plot_2.plot(self.var_data[1], symbol='o', symbolSize=5, symbolBrush=('#FFFF00'))
        self.graphic_3 = self.plot_3.plot(self.var_data[2], symbol='o', symbolSize=5, symbolBrush=('#FFFF00'))
        self.graphic_4 = self.plot_4.plot(self.var_data[3], symbol='o', symbolSize=5, symbolBrush=('#FFFF00'))
        self.graphic_5 = self.plot_5.plot(self.var_data[4], symbol='o', symbolSize=5, symbolBrush=('#FFFF00'))
        self.graphic_6 = self.plot_6.plot(self.var_data[5], symbol='o', symbolSize=5, symbolBrush=('#FFFF00'))
        self.graphic_7 = self.plot_7.plot(self.var_data[6], symbol='o', symbolSize=5, symbolBrush=('#FFFF00'))
        self.graphic_8 = self.plot_8.plot(self.var_data[7], symbol='o', symbolSize=5, symbolBrush=('#FFFF00'))
        self.graphic_9 = self.plot_9.plot(self.var_data[8], symbol='o', symbolSize=5, symbolBrush=('#FFFF00'))

        self.bars = [0]*9
        self.bar_summary.plot_hist(self.bars)

        # Inicializacíón del hilo
        self.sim_thread = th.My_thread()

        # Hilo qt usado para emitirb y procesar señales personalizadas
        self.STRAND.start()
        self.STRAND.setTerminationEnabled(True)
        # Mueve las señales al hilo qt
        self.POINTING.moveToThread(self.STRAND)

        # Conexión de las señales personalizadas
        self.POINTING.signal_clear.connect(self.clear_plot)
        self.POINTING.signal_plot.connect(self.update_plot)
        self.POINTING.signal_hist.connect(self.update_hist)
        self.POINTING.signal_end.connect(self.finish_sim)
        self.POINTING.finished.connect(self.STRAND.quit)

        # Conexión de las señales de los botones
        self.start.clicked.connect(self.start_sim)
        self.pause.clicked.connect(self.pause_sim)
        self.output.clicked.connect(self.open_file)
        self.save_graph.clicked.connect(self.save_bars)

        # Conexión la señal activated de los combobox
        for box in self.boxes:
            box.activated.connect(self.box_manager)

        # Conexión de las señales de los menús
        self.new_action.triggered.connect(self.newsim)
        self.close_action.triggered.connect(self.close)
        self.save_action.triggered.connect(self.savecfg)
        self.load_action.triggered.connect(self.loadcfg)
        self.about_action.triggered.connect(self.about)

        # Conexión de la señal del Slider
        self.scale_time.valueChanged.connect(self.change_speed)

    # Inicia o reanuda la simulación según el indicador
    def start_sim(self):
        if self.start_flag:
            #Manejo de GUI
            self.start.setEnabled(False)
            self.pause.setEnabled(True)
            self.spin_activator(False, False)
            self.box_activator(False, False)

            # Configuración de parámetros de simulación
            graphic_list = [self.graphic_1, self.graphic_2, self.graphic_3, self.graphic_4, self.graphic_5, self.graphic_6, self.graphic_7, self.graphic_8, self.graphic_9]
            self.sim_thread = th.My_thread(target=self.change_speed, args=(self.freq_parameters, int(self.sp_value.value()), graphic_list, self.POINTING,), name='thread_sim')
            self.sim_thread.setDaemon(True)
            self.sim_thread.start()
            self.start_flag = False

        else:
            #Reanuda el hilo en caso de que ya haya iniciado la simulación
            self.sim_thread.resume()
            self.pause.setEnabled(True)
            self.start.setEnabled(False)

    # Pausar la simulación
    def pause_sim(self):
        if self.sim_thread.is_alive():
            self.sim_thread.pause()
            self.pause.setEnabled(False)
            self.start.setText("Resume")
            self.start.setEnabled(True)
        else:
            self.shownotice("The simulation has been finished!")
        
    # Ejecuta el archivo de salida con las VA
    def open_file(self):
        thread_file = th.threading.Thread(target=self.daemon_file, name='output')
        thread_file.setDaemon(True)
        thread_file.start()

    # Nueva simulación
    def newsim(self):
        decision = QtWidgets.QMessageBox.question(self, "New simulation", "Do you want making the new simulation?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if decision == QtWidgets.QMessageBox.Yes:
            # En caso de que el hilo aún siga en ejecución se finaliza
            if self.sim_thread.is_alive():
                if self.sim_thread.paused:
                    self.sim_thread.resume()
                    self.sim_thread.stop()

            self.freq_parameters = [[]] * 9
            self.path_data = ""
            self.start_flag = True
            self.generator = None
            graphic_list = [self.graphic_1, self.graphic_2, self.graphic_3, self.graphic_4, self.graphic_5, self.graphic_6, self.graphic_7, self.graphic_8, self.graphic_9]
            self.POINTING.signal_clear.emit(graphic_list)
            self.bars = [0]*9
            self.bar_summary.plot_hist(self.bars)
            
            #Manejo de la GUI
            self.start.setEnabled(False)
            self.start.setText("Start")
            self.pause.setEnabled(False)
            self.output.setEnabled(False)
            #self.save_graph.setEnabled(False)
            self.spin_activator(True, True)
            self.box_activator(True, True)
            self.scale_time.setValue(1)

    # Sobre-escritura del método closeEvent para el cierre de la app (adaptar al css de la mainframe)
    def closeEvent(self, event):
        if self.sim_thread.is_alive() and self.sim_thread.paused == False:
            self.sim_thread.pause()

        decision = QtWidgets.QMessageBox.question(self, 'Exit', "Are you sure?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if decision == QtWidgets.QMessageBox.Yes:
            # Finalizar hilo qt
            self.POINTING.finished.emit()
            event.accept()

        else:
            if self.sim_thread.paused:
                self.sim_thread.resume()
                self.start.setEnabled(False)
                self.pause.setEnabled(True)
            event.ignore()

    # Guarda archivos de configuraición (JSON según lo planeado), posiblemente haya que usar hilos... no se jajaja
    def savecfg(self):
        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save file', './config', 'JSON Files (*.json)')
        if filepath:
            jm.save_config(filepath)

    # Carga archivos de configuraición (JSON según lo planeado), posiblemente haya que usar hilos... no se jajaja
    def loadcfg(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Load file', './config', 'JSON Files (*.json)')
        if filepath:
            self.freq_parameters = [[]] * 9
            jm.load_config(filepath)
            for index in range(len(self.labels)):
                box = self.boxes[index]
                label = self.labels[index].text()
                if label in jm.current_config:
                    dist_id = jm.current_config[label]['distribution']
                    box.setCurrentIndex(dist_id)
                    dist_name = box.currentData()
                    settings = [label, dist_name(), self.generators[dist_id - 1], jm.current_config[label]['values']]
                    self.freq_parameters[index] = settings
            self.start.setEnabled(self.verify_init())
            self.path_data = str(filepath).split('/')[-1]
        else:
            self.shownotice("This file isn´t a configuration file")

    # Guarda el gráfico de barras de la mainframe
    def save_bars(self):
        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save bars', './test', 'PNG Files (*.png)')
        if filepath:
            self.bar_summary.saveplot(filepath)

    # Información del software (debe mejorarse y adaptarse al css de la mainframe creo)
    def about(self):
        self.shownotice("This software is the ostiaaaaaa :V")

    # Comunica el valor del Slider al hilo de simulación
    def change_speed(self):
        self.label_scale.setText("Speed X " + str(self.scale_time.value()))
        return self.scale_time.value()

    # Grafica las VA generadas
    def update_plot(self, graphic, value, index):
        self.var_data[index].append(value)
        graphic.setData(self.var_data[index][1:])

    # Actualiza el histograma según las VA generadas
    def update_hist(self, values, index):
        count = 0
        if len(values) != 0:
            for value in values:
                if (value >= self.th_value.value()):
                    count = count + 1

            self.bars[index] = (count/len(values))*100
            self.bar_summary.plot_hist(self.bars)

    # Borra los datos graficados durante la simulación previa
    def clear_plot(self, graphics):
        self.var_data = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
        for graphic in graphics:
            graphic.setData([0])

    # Notifica la terminación de la simulación
    def finish_sim(self, data, date_sim):
        self.start.setEnabled(False)
        self.pause.setEnabled(False)
        self.output.setEnabled(True)
        self.shownotice("The simulation has been succesfully completed!")
        self.path_file = './test/Simulation-' + self.path_data.split('.')[0] + '-' + date_sim.strftime("%m_%d_%Y_%H_%M_%S") + '.txt'
        out_file = open(self.path_file, 'a')
        
        # Escritura del archivo con las VA generadas
        for line in data:
            index = 0
            while(index < len(line)):
                out_file.write(line[index] + '\n')
                index = index + 1    
            
        out_file.close()    
        
    def box_activator(self, view, default):
        for box in self.boxes:
            box.setEnabled(view)
            if default:
                box.setCurrentIndex(0)

    def spin_activator(self, view, default):
        self.sp_value.setEnabled(view)
        self.th_value.setEnabled(view)
        if default:
            self.sp_value.setValue(1)
            self.th_value.setValue(0.33)

    def verify_init(self):
        for box in self.boxes:
            if box.currentIndex() == 0:
                return False

        return True

    # Ejecución del diálogo de avisos
    def shownotice(self, msg):
        self.notice.setIcon(QtWidgets.QMessageBox.Information)
        self.notice.setText(msg)
        self.notice.setWindowTitle("Aviso")
        self.notice.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.notice.setStyleSheet("QLabel{\n"
                            "   color: #000000;\n"
                            "}"  
                            )
        self.notice.exec_()

    # Invoca el modal para la recolección de parámetros de acuerdo a la distribución seleccionada
    def box_manager(self, index):
        call_b = self.sender().currentData()
        dist_id = self.sender().currentIndex()

        if call_b is None:
            self.shownotice("You must select a distribution")
            self.start.setEnabled(False)
            return

        name = call_b()
        self.modal.exec()

        if self.modal.result() == 1:
            self.generator = self.generators[dist_id - 1]
            for index in range(len(self.boxes)):
                settings = []
                if self.sender() == self.boxes[index]:
                    jm.current_config[self.labels[index].text()] = {
                        'distribution': dist_id,
                        'values': self.modal.parameters[:jm.get_params_count(dist_id)],
                    }
                    settings = [self.labels[index].text(), name, self.generator, self.modal.parameters]
                    self.freq_parameters[index] = settings

        else:
            self.sender().setCurrentIndex(0)

        self.start.setEnabled(self.verify_init())

    # Demonio para la visualización del .txt con las VA
    def daemon_file(self):
        import os
        import subprocess
        path = scriptDir = os.getcwd() + os.path.sep + self.path_data
        subprocess.call(path, shell=True)

# Arranque de la aplicación
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
