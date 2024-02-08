"""
Dear developer,

Currently, it is not possible to create an abstract class in a conventional way
if classes from the PySide6 library are used in the hierarchy. If we try this
we will get an error like this:

TypeError: metaclass conflict: the metaclass of a derived class must be a
           (non-strict) subclass of the metaclasses of all its bases

This error occurs when we try to create a class that inherits from multiple
base classes, and those base classes have incompatible metaclasses. In Python,
all classes are instances of a metaclass, which defaults to type. When you
create a class that inherits from multiple base classes, Python tries to make
sure that the metaclass of the new class is a subclass of the metaclasses of
all the base classes.

In this case, we are trying to create a class that inherits from QChart
(which is a Qt class, and therefore has a custom metaclass) and ABC
(which has ABCMeta as its metaclass). These two metaclasses are not compatible,
which is causing the error.
"""
from numpy import ndarray
from PySide6.QtCharts import QChart

from exceptions.charts import AbstractQChartInstantiationError, AbstractQChartMethodNotImplemented

__all__ = ['AbstractQChart', 'DownloadableChart', 'PlotFunctionChart']


class AbstractQChart(QChart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if type(self) is AbstractQChart:
            raise AbstractQChartInstantiationError(class_name=self.__class__.__name__)


class DownloadableChart(AbstractQChart):
    """
    Pseudo-abstract class for a chart that can be saved to a file.
    """
    def save(self, filename: str) -> None:
        """
        Save the chart to a file with the given filename. The file type is
        inferred from the filename extension.

        :param filename: The name of the file to save the chart to.
        """
        raise AbstractQChartMethodNotImplemented(method_name='save')


class PlotFunctionChart(AbstractQChart):
    """
    Abstract class for a chart that can plot a function.
    """
    def plot(self, x: ndarray, y: ndarray, series_legend: str) -> None:
        """
        Plot the values of x and y arrays provided. The legend is the name of
        the series that will be shown in the chart legend.

        :param x: The x values to plot.
        :param y: The y values to plot.
        :param series_legend: The legend of the series.
        """
        raise AbstractQChartMethodNotImplemented(method_name='plot')
