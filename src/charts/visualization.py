from numpy import ndarray
from PySide6.QtCharts import (
    QAbstractSeries,
    QAbstractBarSeries,
    QBarCategoryAxis,
    QBarSeries,
    QBarSet,
    QChart,
    QLegend,
    QLineSeries,
    QValueAxis,
    QXYSeries,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

from charts.abc import PlotFunctionChart
from src.charts.exceptions import SeriesAdditionError
from constants.charts import (
    CHART_SERIES_COLOR_HEX,
    CHART_SERIES_LINE_WIDTH,
    CHART_PDF_TITLE,
    CHART_PMF_TITLE,
    CHART_TITLE_DEFAULT,
    CHART_X_AXIS_LABEL_DEFAULT,
    CHART_Y_AXIS_LABEL_DEFAULT,
)

SERIES_COLOR = QColor(CHART_SERIES_COLOR_HEX)

__all__ = ['PDFChart', 'PMFChart', 'SingleSeriesChart']


class SingleSeriesChart(QChart):
    """
    QChart subclass that only allows one series to be added to the chart.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setTitle(CHART_TITLE_DEFAULT)
        self.legend().setVisible(True)
        self.legend().setMarkerShape(QLegend.MarkerShapeFromSeries)
        self.setAnimationOptions(QChart.SeriesAnimations)
        self.setContentsMargins(0, 0, 0, 0)

    def addSeries(self, series: QAbstractSeries) -> None:
        """
        Add a series to the chart. This overrides the default method to ensure
        that only one series is added to the chart. If a series is already
        present in the chart, a SeriesAdditionError is raised.

        :param series: The series to add to the chart.
        """
        if self.current_series is not None:
            raise SeriesAdditionError()

        super().addSeries(series)

    def clean_series(self):
        self.removeAllSeries()

    def clean_axes(self):
        """
        Remove all the axes from the chart.
        """
        for axis in self.axes():
            self.removeAxis(axis)

    @property
    def current_series(self) -> QAbstractSeries | QAbstractBarSeries | QXYSeries | None:
        """
        Return the current series of the chart. If there is no series in the
        chart, None is returned.

        :return: The current series of the chart or None if there is no series.
        """
        if self.series():
            return self.series()[0]

        return None


class PDFChart(SingleSeriesChart, PlotFunctionChart):
    """
    QChart subclass for plotting a probability density function for a given
    continuous probability distribution. This chart has default axes attached.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setTitle(CHART_PDF_TITLE)
        self.addSeries(QLineSeries())
        self.createDefaultAxes()
        self.x_axis = self.axes(Qt.Horizontal, self.series()[0])[0]
        self.x_axis.setTitleText(CHART_X_AXIS_LABEL_DEFAULT)
        self.y_axis = self.axes(Qt.Vertical, self.series()[0])[0]
        self.y_axis.setTitleText(CHART_Y_AXIS_LABEL_DEFAULT)

        # Series customization
        self.series_pen = self.current_series.pen()
        self.series_pen.setColor(SERIES_COLOR)
        self.series_pen.setWidth(CHART_SERIES_LINE_WIDTH)
        self.current_series.setPen(self.series_pen)

    def plot(self, x: ndarray, y: ndarray, series_legend: str) -> None:
        """
        Plot the values of x and y arrays provided. This implementation uses
        the replaceNp() method to alter all points in the current series
        instead of removing the points and adding them again.

        :param x: The x values to plot.
        :param y: The y values to plot.
        :param series_legend: The legend of the series.
        """
        self.x_axis.setRange(min(x) - 0.02, max(x) + 0.02)
        self.y_axis.setRange(0, max(y) + 0.05)
        self.current_series.replaceNp(x, y)
        self.current_series.setName(series_legend)


class PMFChart(SingleSeriesChart, PlotFunctionChart):
    """
    QChart subclass for plotting a probability mass function for a given
    discrete probability distribution. This chart does not have default axes
    attached.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setTitle(CHART_PMF_TITLE)
        self.addSeries(QBarSeries())
        self.x_axis = QBarCategoryAxis()
        self.y_axis = QValueAxis()

    def plot(self, x: ndarray, y: ndarray, series_legend: str) -> None:
        """
        Plot the values of x and y arrays provided. This implementation uses
        the << operator to add the values to the current series. This usage of
        the << operator is specific to the QBarSet class in the PySide6.QtCharts
        module. It’s not a standard Python operator, but is a common operator
        in C++ and is used in some Python libraries that have interfaces to C++
        libraries, like PySide6.
        """
        self.clean_series()
        self.clean_axes()
        bar_set = QBarSet(series_legend)
        for y_value in y:
            bar_set << y_value

        bar_set.setColor(SERIES_COLOR)
        series = QBarSeries()
        series.append(bar_set)
        self.addSeries(series)
        self.x_axis.setCategories(x)
        self.y_axis = QValueAxis()
        self.addAxis(self.x_axis, Qt.AlignBottom)
        self.addAxis(self.y_axis, Qt.AlignLeft)
        series.attachAxis(self.x_axis)
        series.attachAxis(self.y_axis)
