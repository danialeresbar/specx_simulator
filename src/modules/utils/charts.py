import math as mt
import numpy as np
import scipy.stats as stats

from PyQt5.QtChart import (
    QChart,
    QBarCategoryAxis,
    QBarSeries,
    QBarSet,
    QAbstractBarSeries,
    QLegend,
    QLineSeries,
    QSplineSeries,
    QValueAxis
)
from PyQt5.QtCore import Qt, QMargins
from PyQt5.QtGui import QColor, QColorConstants, QFont


# ---- Bar attributes ----
Y_TICKCOUNT = 5


# ---- Colors ----
SERIES_COLOR = QColor("#5f85db")
LIGHT_GREEN = QColorConstants.Svg.lightgreen
INDIAN_RED = QColorConstants.Svg.indianred


# ---- Chart fonts ----
CHART_DEFAULT_TITLE = 'Chart default title'


# ---- Chart fonts ----
CHART_LABEL_FONT = QFont()
CHART_LABEL_FONT.setPointSizeF(8)
CHART_TITLE_FONT = QFont()
CHART_TITLE_FONT.setPointSizeF(12)


# ---- Distribution Labels ----
X_AXIS_LABELS_BERNOULLI = ['Success', 'Fail']
LEGENDS_BERNOULLI = ['Success \nprobability', 'Fail \nprobability']


# ---- Greg letters ----
ALPHA_LETTER = 'α'
BETA_LETTER = 'β'
GAMMA_LETTER = 'γ'
LAMBDA_LETTER = 'λ'
MU_LETTER = 'μ'
SIGMA_LETTER = 'σ'


# ---- Series attributes ----
SERIES_WIDTH = 3
SAMPLES = 100


class PDFChart(QChart):
    """
    Class to manage the graphs of the PDF (Probability density function)
    and the percent bars for the simulations carried out
    """

    def __init__(self, **kwargs):
        super(PDFChart, self).__init__()
        self.title = kwargs.get('title', CHART_DEFAULT_TITLE)
        self.parameters = kwargs.get('parameters', list())

        self.layout().setContentsMargins(0, 0, 0, 0)
        self.setAnimationOptions(QChart.SeriesAnimations)
        self.setBackgroundRoundness(0)
        self.setMargins(QMargins(20, 20, 20, 20))
        self.setTheme(self.ChartThemeLight)
        self.setTitle(self.title)

    def plot_bernoulli(self):
        """
        Generates a graph of a Bernoulli PDF (Probability density function) with the respective parameters
        """
        bars = [parameter.value for parameter in self.parameters]
        legends = LEGENDS_BERNOULLI
        x_axis = X_AXIS_LABELS_BERNOULLI
        bar_colors = [LIGHT_GREEN, INDIAN_RED]
        self.add_bars(x=x_axis, bars=bars + [1-bars[0]], bar_colors=bar_colors, bar_label_format="@value",
                      y_label_format="", y_max=1, y_tickcount=6, legends=legends, legend_alignment=Qt.AlignBottom)

    def plot_beta(self):
        """
        Generates a graph of a Bernoulli PDF (Probability density function) with the respective parameters
        """
        alpha = self.parameters[0].value
        beta = self.parameters[1].value
        a = self.parameters[2].value
        b = self.parameters[3].value
        x = np.linspace(
            stats.beta.ppf(0.01, alpha, beta, loc=a, scale=b),
            stats.beta.ppf(0.99, alpha, beta, loc=a, scale=b),
            SAMPLES
        )
        y = stats.beta.pdf(x, alpha, beta, loc=a, scale=b)
        series = QSplineSeries()
        series.setName(f'{ALPHA_LETTER}={alpha:.4f}, {BETA_LETTER}={beta:.4f}, a={a:.4f}, b={b:.4f}')
        self.add_spline_series(series, x, y)

    def plot_gamma(self):
        alpha = self.parameters[0].value
        gamma = self.parameters[1].value
        lmbda = self.parameters[2].value
        x = np.linspace(
            stats.gamma.ppf(0.01, alpha, loc=gamma, scale=lmbda),
            stats.gamma.ppf(0.99, alpha, loc=gamma, scale=lmbda),
            SAMPLES
        )
        y = stats.gamma.pdf(x, alpha, loc=gamma, scale=lmbda)
        series = QSplineSeries()
        series.setName(
            f'{ALPHA_LETTER}={alpha:.4f}, {LAMBDA_LETTER}={lmbda:.4f}, {GAMMA_LETTER}={gamma:.4f}')
        self.add_spline_series(series, x, y)

    def plot_gumbel(self):
        mu = self.parameters[0].value
        sigma = self.parameters[1].value
        x = np.linspace(
            stats.gumbel_r.ppf(0.01, loc=mu, scale=sigma),
            stats.gumbel_r.ppf(0.99, loc=mu, scale=sigma),
            SAMPLES
        )
        y = stats.gumbel_r.pdf(x, loc=mu, scale=sigma)
        series = QSplineSeries()
        series.setName(f'{MU_LETTER}={mu:.4f}, {SIGMA_LETTER}={sigma:.4f}')
        self.add_spline_series(series, x, y)

    def plot_laplace(self):
        mu = self.parameters[0].value
        b = self.parameters[1].value
        x = np.linspace(
            stats.laplace.ppf(0.01, loc=mu, scale=b),
            stats.laplace.ppf(0.99, loc=mu, scale=b),
            SAMPLES
        )
        y = stats.laplace.pdf(x, loc=mu, scale=b)
        series = QSplineSeries()
        series.setName(f'{MU_LETTER}={mu:.4f}, b={b:.4f}')
        self.add_spline_series(series, x, y)

    def plot_lognorm(self):
        mu = self.parameters[0].value
        sigma = self.parameters[1].value
        gamma = self.parameters[2].value
        x = np.linspace(
            stats.lognorm.ppf(0.01, sigma, loc=gamma, scale=mt.exp(mu)),
            stats.lognorm.ppf(0.99, sigma, loc=gamma, scale=mt.exp(mu)),
            SAMPLES
        )
        y = stats.lognorm.pdf(x, sigma, loc=gamma, scale=mt.exp(mu))
        series = QSplineSeries()
        series.setName(f'{MU_LETTER}={mu:.4f}, {SIGMA_LETTER}={sigma:.4f}, {GAMMA_LETTER}={gamma:.4f}')
        self.add_spline_series(series, x, y)

    def plot_norm(self):
        mu = self.parameters[0].value
        sigma = self.parameters[1].value
        x = np.linspace(
            stats.norm.ppf(0.01, loc=mu, scale=sigma),
            stats.norm.ppf(0.99, loc=mu, scale=sigma),
            SAMPLES
        )
        y = stats.norm.pdf(x, loc=mu, scale=sigma)
        series = QSplineSeries()
        series.setName(f'{MU_LETTER}={mu:.4f}, {SIGMA_LETTER}={sigma:.4f}')
        self.add_spline_series(series, x, y)

    def plot_rayleigh(self):
        sigma = self.parameters[0].value
        lmbda = self.parameters[1].value
        x = np.linspace(
            stats.rayleigh.ppf(0.01, loc=lmbda, scale=sigma),
            stats.rayleigh.ppf(0.99, loc=lmbda, scale=sigma),
            SAMPLES
        )
        y = stats.rayleigh.pdf(x, loc=lmbda, scale=sigma)
        series = QSplineSeries()
        series.setName(f'{SIGMA_LETTER}={sigma:.4f}, {LAMBDA_LETTER}={lmbda:.4f}')
        self.add_spline_series(series, x, y)

    def plot_uniform(self):
        a = self.parameters[0].value
        b = self.parameters[1].value
        x = list()
        y = list()
        try:
            x = np.linspace(
                stats.uniform.ppf(0.01, loc=a, scale=b-a),
                stats.uniform.ppf(0.99, loc=a, scale=b-a),
                SAMPLES
            )
            y = stats.uniform.pdf(x, loc=a, scale=b-a)
        except Exception as e:
            print(e)
        series = QSplineSeries()
        series.setName(f'a={a:.4f}, b={b:.4f}')
        self.add_spline_series(series, x, y)

    def plot_weibull(self):
        alpha = self.parameters[0].value
        beta = self.parameters[1].value
        gamma = self.parameters[2].value
        x = np.linspace(
            stats.weibull_min.ppf(0.01, alpha, loc=gamma, scale=beta),
            stats.weibull_min.ppf(0.99, alpha, loc=gamma, scale=beta),
            SAMPLES
        )
        y = stats.weibull_min.pdf(x, alpha, loc=gamma, scale=beta)
        series = QSplineSeries()
        series.setName(f'{ALPHA_LETTER}={alpha:.4f}, {BETA_LETTER}={beta:.4f}, {GAMMA_LETTER}={gamma:.4f}')
        self.add_spline_series(series, x, y)

    def add_spline_series(self, series, x, y):
        for index in range(len(y)):
            series.append(x[index], y[index])

        pen = series.pen()
        pen.setColor(SERIES_COLOR)
        pen.setWidth(SERIES_WIDTH)
        series.setPen(pen)
        self.addSeries(series)
        self.createDefaultAxes()
        self.axes(Qt.Vertical, series)[0].setRange(0, max(y)+0.1)
        self.legend().setVisible(True)
        self.legend().setMarkerShape(QLegend.MarkerShapeFromSeries)
        self.legend().setAlignment(Qt.AlignTop)
        self.setTitleFont(CHART_TITLE_FONT)

    def add_bars(self, x, bars, bar_colors, bar_label_format, y_label_format, y_max, y_tickcount, legends, legend_alignment):
        for index in range(len(bars)):
            series = QBarSeries()

            bar_set = QBarSet(legends[index])
            if bar_colors:
                bar_set.setColor(bar_colors[index])

            bar_set.setLabelColor(Qt.black)
            bar_set.setLabelFont(CHART_LABEL_FONT)
            bar_set.append(bars[index])

            series.append(bar_set)
            series.setLabelsVisible(True)
            series.setLabelsFormat(bar_label_format)
            if bars[index] < y_max*0.2:
                series.setLabelsPosition(QAbstractBarSeries.LabelsOutsideEnd)

            else:
                series.setLabelsPosition(QAbstractBarSeries.LabelsCenter)
            self.addSeries(series)

        self.createDefaultAxes()
        axis_x = self.axes(Qt.Horizontal)[0]
        self.removeAxis(axis_x)
        axis_x = QBarCategoryAxis()
        axis_x.append(x)
        self.addAxis(axis_x, Qt.AlignBottom)
        axis_x.setLabelsFont(CHART_LABEL_FONT)
        axis_y = self.axes(Qt.Vertical, series)[0]
        axis_y.setRange(0, y_max)
        axis_y.setTickCount(y_tickcount)
        axis_y.setLabelFormat(y_label_format)
        axis_y.setLabelsFont(CHART_LABEL_FONT)
        self.legend().setAlignment(legend_alignment)
        self.legend().setVisible(False)
        self.setTitleFont(CHART_TITLE_FONT)


class SimulationChart(QChart):
    """

    """

    def __init__(self, **kwargs):
        super(SimulationChart, self).__init__()
        self.title = kwargs.get('title')

        # You can customize the chart settings in this section
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.legend().setAlignment(Qt.AlignBottom)
        self.legend().setVisible(False)
        self.setAnimationOptions(QChart.NoAnimation)
        self.setBackgroundRoundness(0)
        self.setMargins(QMargins(5, 5, 5, 5))
        self.setTheme(self.ChartThemeLight)
        self.setTitle(self.title)
        self.setTitleFont(CHART_TITLE_FONT)

    def setup_axes(self):
        """
        Create the default axes. After, these will ve updated with the suitable values
        :return:
        """
        self.createDefaultAxes()


class SplineChart(SimulationChart):
    """

    """

    def __init__(self, **kwargs):
        super(SplineChart, self).__init__(
            title=kwargs.get('title', CHART_DEFAULT_TITLE)
        )

        self.spseries = QSplineSeries()
        self.spseries.setPointsVisible(True)
        self._set_customize_pen()

        self.addSeries(self.spseries)
        self.setup_axes()

        self.x_axis = self.axes(Qt.Horizontal, self.series()[0])[0]
        self.x_axis.setRange(0, 10)
        self.x_axis.setTickCount(5)

        self.y_axis = self.axes(Qt.Vertical, self.series()[0])[0]
        self.y_axis.setRange(0, 0.8)
        self.y_axis.setTickCount(3)

    def _set_customize_pen(self):
        pen = self.spseries.pen()
        pen.setColor(SERIES_COLOR)
        pen.setWidth(3)
        self.spseries.setPen(pen)


class LineChart(SimulationChart):
    """

    """

    def __init__(self, **kwargs):
        super(LineChart, self).__init__(
            title=kwargs.get('title', CHART_DEFAULT_TITLE)
        )

        self.lnseries = QLineSeries()
        self.lnseries.setPointsVisible(True)
        self._set_customize_pen()

        self.addSeries(self.lnseries)
        self.setup_axes()

        self.x_axis = self.axes(Qt.Horizontal, self.series()[0])[0]
        self.x_axis.setRange(0, 10)
        self.x_axis.setTickCount(5)

        self.y_axis = self.axes(Qt.Vertical, self.series()[0])[0]
        self.y_axis.setRange(0, 0.8)
        self.y_axis.setTickCount(3)

    def _set_customize_pen(self):
        pen = self.lnseries.pen()
        pen.setColor(SERIES_COLOR)
        pen.setWidth(3)
        self.lnseries.setPen(pen)


class BarChart(QChart):
    """

    """

    def __init__(self, **kwargs):
        super(BarChart, self).__init__()
        self.title = kwargs.get('title', CHART_DEFAULT_TITLE)
        self.x_categories = kwargs.get('categories', list())

        self.bars = list()
        self._init_bars()
        self._setup_axes()

        self.x_axis = QBarCategoryAxis()
        self.x_axis.setCategories(self.x_categories)
        self.x_axis.setLabelsFont(CHART_LABEL_FONT)
        self.addAxis(self.x_axis, Qt.AlignBottom)

        self.y_axis = self.axes(Qt.Vertical, self.series()[0])[0]
        self.y_axis.setLabelsFont(CHART_LABEL_FONT)
        self.y_axis.setRange(0, 100)
        self.y_axis.setTickCount(Y_TICKCOUNT)

        # You can customize the bar chart settings in this section
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.legend().setAlignment(Qt.AlignBottom)
        self.legend().setVisible(True)
        self.setAnimationOptions(QChart.SeriesAnimations)
        self.setBackgroundRoundness(0)
        self.setMargins(QMargins(10, 10, 10, 10))
        self.setTheme(self.ChartThemeLight)
        self.setTitle(self.title)
        self.setTitleFont(CHART_TITLE_FONT)

    def _init_bars(self):
        """
        Init the chart bars with default values. For this case, 50 is the default percentage
        :return:
        """
        for x_category in self.x_categories:
            series = QBarSeries()
            bar = QBarSet(x_category)
            bar.setLabelColor(Qt.black)
            bar.setLabelFont(CHART_LABEL_FONT)
            bar.append(50)
            series.append(bar)
            series.setLabelsFormat("@value %")
            series.setLabelsVisible(True)
            self.bars.append(bar)
            series.setLabelsPosition(2)
            self.addSeries(series)

    def _setup_axes(self):
        """
        Create the default axes. After, these will ve updated with the suitable values
        :return:
        """
        self.createDefaultAxes()
        self.removeAxis(self.axes(Qt.Horizontal)[0])

    def update_bars(self, values):
        """
        Update the bar values according to the usage percentage calculated in the running simulation
        :return:
        """
        for index, value in enumerate(values):
            self.bars[index].replace(0, value)
