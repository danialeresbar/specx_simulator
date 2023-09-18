import threading
import time
from datetime import datetime, timedelta

class My_thread(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name)
        self.target = target
        self.args = args
        self.kwargs = kwargs

        # Bandera para indicar la pausa del hilo
        self.paused = False

        # Bandera para indicar la parada del hilo
        self.stopped = False

        # Explicitly using Lock over RLock since the use of self.paused
        # break reentrancy anyway, and I believe using Lock could allow
        # one thread to pause the worker, while another resumes; haven't
        # checked if Condition imposes additional limitations that would 
        # prevent that. In Python 2, use of Lock instead of RLock also
        # boosts performance.
        self.pause_cond = threading.Condition(threading.Lock())
        # Finish flag
        self.stop_flag = threading.Event()

    def run(self):
        # Recursos de la simulación
        params = self.args[0]
        limit = self.args[1]*30
        graphics = self.args[2]
        pointing = self.args[3]

        index = 0
        file_data = list()
        stamp = datetime.now()
        instant = datetime.now()

        for source in params:
            v_counter = 0
            data = source[3]
            stack = list()
            randoms = list()
                
            while(not self.stop_flag.is_set() and v_counter < limit):
                wait = 2/self.target()   
                var = source[2](data)
                line = instant.strftime("%m-%d-%Y-%H:%M:%S") + ';' + source[0] + ';' + source[1] + ';' + str(var)
                time.sleep(wait)
                instant = instant + timedelta(seconds=2)
                v_counter = v_counter + 1
                stack.append(line)
                randoms.append(var)
                pointing.signal_plot.emit(graphics[index], var, index)
                with self.pause_cond:
                    while self.paused:
                        self.pause_cond.wait()

            if self.stopped == True:
                return

            file_data.append(stack)
            pointing.signal_hist.emit(randoms, index)
            index = index + 1
        
        if self.stopped == True:
            return

        pointing.signal_end.emit(file_data, stamp)
        return
    
    # Pause the thread        
    def pause(self):
        self.paused = True
        # If in sleep, we acquire immediately, otherwise we wait for thread
        # to release condition. In race, worker will still see self.paused
        # and begin waiting until it's set back to False
        self.pause_cond.acquire()

    # Resume the thread
    def resume(self):
        self.paused = False
        # Notify so thread will wake after lock released
        self.pause_cond.notify()
        # Now release the lock
        self.pause_cond.release()

    # Stop the thread
    def stop(self):
        self.stopped = True
        self.stop_flag.set()
