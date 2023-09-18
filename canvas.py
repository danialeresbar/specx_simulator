import math as mt
from scipy import stats
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Canvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        self.ax = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.figure.subplots_adjust(bottom=0.15, top=0.94)
        
    # Limpia el canvas
    def clean(self):
        self.ax.cla()
        self.figure.set_facecolor('#D5F5E3')

    def plot_bernoulli(self, params):
        self.clean()
        self.ax.axis([-1, 2, 0, 100])
        self.ax.set_xticks(np.arange(0, 1.5, 1))
        randoms_b = stats.bernoulli.rvs(p=params[0], size=100)
        self.ax.hist(randoms_b, 20, color='#F98400', label='random_bern')
        self.ax.legend(loc='best', frameon=True)
        self.draw()

    def plot_beta(self, params):
        self.clean()
        x = np.linspace(stats.beta.ppf(0.01, params[0], params[1], params[2], params[3]), stats.beta.ppf(0.99, params[0], params[1], params[2], params[3]), 100)
        self.ax.plot(x, stats.beta.pdf(x, params[0], params[1], params[2], params[3]), color='#F98400', ls='-', lw=1, alpha=0.9, label='beta pdf')
        self.ax.legend(loc='best', frameon=True)
        self.draw()

    def plot_gamma(self, params):
        self.clean()
        x = np.linspace(stats.gamma.ppf(0.01, params[0], loc=0, scale=params[1]), stats.gamma.ppf(0.99, params[0], loc=0, scale=params[1]), 100)
        self.ax.plot(x, stats.gamma.pdf(x, params[0], loc=0, scale=params[1]), color='#F98400', ls='-', lw=1, alpha=0.9, label='gamma pdf')
        self.ax.legend(loc='best', frameon=True)
        self.draw()

    def plot_gumbel(self, params):
        s = np.random.gumbel(params[0], params[1], 1000)
        count, bins, ignored = self.ax.hist(s, 150, density=True)
        self.clean()
        self.ax.plot(bins, (1/params[1])*np.exp(-(bins - params[0])/params[1]) * np.exp( -np.exp( -(bins - params[0]) /params[1]) ), color='#F98400', ls='-', lw=1, alpha=0.9, label='gumbel pdf')
        self.ax.legend(loc='best', frameon=True)
        self.draw()

    def plot_laplace(self, params):
        self.clean()
        x = np.arange(0, 0.8, .005)
        pdf = np.exp(-abs(x-params[0])/params[1])/(2.*params[1])
        self.ax.plot(x, pdf, color='#F98400', ls='-', lw=1, alpha=0.9, label='laplace pdf')
        self.ax.legend(loc='best', frameon=True)
        self.draw()        

    def plot_lognormal(self, params):
        s = np.random.lognormal(params[0], params[1], 1000)
        count, bins, ignored = self.ax.hist(s, 100, density=True, align='mid')
        x = np.linspace(min(bins), max(bins), 10000)
        pdf = (np.exp(-(np.log(x) - params[0])**2 / (2 * params[1]**2)) / (x * params[1] * np.sqrt(2 * np.pi)))
        self.clean()
        self.ax.plot(x, pdf, color='#F98400', ls='-', lw=1, alpha=0.9, label='log-n pdf')
        self.ax.legend(loc='best', frameon=True)
        self.draw() 

    def plot_lognormal_3p(self, params):
        self.clean()
        s = np.random.lognormal(params[0], params[1], 1000)
        x = np.linspace(stats.lognorm.ppf(0.01, s=params[1], loc=params[2], scale=mt.exp(params[0])), stats.lognorm.ppf(0.99, s=params[1], loc=params[2], scale=mt.exp(params[0])), 100)
        self.ax.plot(x, stats.lognorm.pdf(x, s=params[1], loc=params[2], scale=mt.exp(params[0])), color='#F98400', ls='-', lw=1, alpha=0.9, label='log-n pdf')
        self.ax.legend(loc='best', frameon=True)
        self.draw()

    def plot_normal(self, params):
        s = np.random.normal(params[0], params[1], 1000)
        count, bins, ignored = self.ax.hist(s, 200, density=True, align='mid')
        self.clean()
        self.ax.plot(bins,  1/(params[1] * np.sqrt(2 * np.pi)) * np.exp( - (bins - params[0])**2 / (2 * params[1]**2) ), color='#F98400', ls='-', lw=1, alpha=0.9, label='normal pdf')
        self.ax.legend(loc='best', frameon=True)
        self.draw()

    def plot_uniforme(self, params):
        self.clean()
        x = np.linspace(stats.uniform.ppf(0.01, loc=params[0], scale=params[1] - params [0]), stats.uniform.ppf(0.99, loc=params[0], scale=params[1] - params [0]), 100)
        pdf = stats.uniform.pdf(x, loc=params[0], scale=params[1] - params [0])
        self.ax.plot(x, pdf, color='#F98400', ls='-', lw=1, alpha=0.9, label='uniform pdf')
        self.ax.legend(loc='best', frameon=True)
        self.draw()

    def plot_weibull(self, params):
        self.clean()
        x = np.linspace(stats.weibull_min.ppf(0.01, c=params[0], loc=params[2], scale=params[1]), stats.weibull_min.ppf(0.99, c=params[0], loc=params[2], scale=params[1]), 100)
        self.ax.plot(x, stats.weibull_min.pdf(x, c=params[0], loc=params[2], scale=params[1]), color='#F98400', ls='-', lw=1, alpha=0.9, label='weibull pdf')
        self.ax.legend(loc='best', frameon=True)
        self.draw()

    def plot_rayleigh(self, params):
        self.clean()
        x = np.linspace(stats.rayleigh.ppf(0.01, scale=params[0]), stats.rayleigh.ppf(0.99, scale=params[0]), 100)
        self.ax.plot(x, stats.rayleigh.pdf(x, scale=params[0]), color='#F98400', ls='-', lw=1, alpha=0.9, label='rayleigh pdf')
        self.ax.legend(loc='best', frameon=True)
        self.draw()

    def plot_rayleigh_2p(self, params):
        self.clean()
        x = np.linspace(stats.rayleigh.ppf(0.01, loc=params[1], scale=params[0]), stats.rayleigh.ppf(0.99, loc=params[1], scale=params[0]), 100)
        self.ax.plot(x, stats.rayleigh.pdf(x, loc=params[1], scale=params[0]), color='#F98400', ls='-', lw=1, alpha=0.9, label='rayleigh pdf')
        self.ax.legend(loc='best', frameon=True)
        self.draw()

    def plot_hist(self, values):
        ticks = ["473 MHz", "479 MHz", "485 MHz", "491 MHz", "497 MHz", "503 MHz", "509 MHz", "551 MHz", "557 MHz"]
        freq_labels = range(len(ticks))
        self.clean()
        self.figure.set_facecolor('#FFFFFF')
        self.figure.subplots_adjust(top=0.93, bottom=0.03, left=0.3, right= 0.9)
        self.ax.invert_yaxis()
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
        self.ax.tick_params(axis='y', which='major', pad=5)
        self.ax.set_xlim(0, 120)
        self.ax.xaxis.set_ticks_position('top')
        self.ax.set_yticks(freq_labels)
        self.ax.set_yticklabels(ticks, rotation = 40, va='center')
        #self.ax.set_xticks(np.arange(0, 120, 20))
        self.ax.barh(freq_labels, values, height=0.9, align='center', color='#C0C0C0', alpha=0.8, label='% Use')
        self.ax.legend(loc='best', frameon=True)
        self.ax.grid()
        self.percent(values)
        self.draw()

    def percent(self, y_values):
        for i, v in enumerate(y_values):
            self.ax.text(1, i, "{0:.2f}%".format(v), va='center')
    
    def saveplot(self, fname):
        self.figure.savefig(fname)
                    