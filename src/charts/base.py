from PyQt5.QtChart import QAbstractBarSeries, QChart, QBarCategoryAxis, QBarSeries, QBarSet, QLineSeries, QValueAxis
from PyQt5.QtCore import Qt, QMargins, QPointF
from PyQt5.QtGui import QColor, QColorConstants, QFont


# ---- BaseBarChart ----
BARCHART_DEFAULT_TILE = 'THIS IS A BAR CHART'
BARCHART_DEFAULT_LABEL_FONT = QFont()
BARCHART_DEFAULT_LABEL_FONT.setPointSizeF(8)
BARCHART_DEFAULT_TITLE_FONT = QFont()
BARCHART_DEFAULT_TITLE_FONT.setPointSizeF(12)
BARCHART_LABEL_FORMAT = "@value %"
BARCHART_DEFAULT_TICKCOUNT = 5

# ---- BaseChart ----
CHART_DEFAULT_TITLE = 'THIS IS A CHART'
CHART_DEFAULT_LABEL_FONT = QFont()
CHART_DEFAULT_LABEL_FONT.setPointSizeF(8)
CHART_DEFAULT_TITLE_FONT = QFont()
CHART_DEFAULT_TITLE_FONT.setPointSizeF(12)
CHART_DEFAULT_SERIES_WIDTH = 3

# ---- Colors ----
SERIES_COLOR = QColor("#5f85db")
BLACK = QColorConstants.Svg.black
LIGHT_GREEN = QColorConstants.Svg.lightgreen
INDIAN_RED = QColorConstants.Svg.indianred


class BaseChart(QChart):
    """
    Class used for the base representation of a chart
    """

    def __init__(self, **kwargs):
        self.__title = kwargs.get('title', CHART_DEFAULT_TITLE)
        super(BaseChart, self).__init__()

        # Base properties
        self.base_series = QLineSeries()
        self.x_axis = QValueAxis()
        self.y_axis = QValueAxis()

        # Customize the base appearance of the chart in this section
        self.layout().setContentsMargins(0, 0, 0, 0)    # Layout margins
        self.legend().setAlignment(Qt.AlignTop)         # Legends position
        self.legend().setVisible(False)                 # Legends visibility
        self.setAnimationOptions(QChart.NoAnimation)    # Chart Animations
        self.setBackgroundRoundness(0)                  # Chart roundness
        self.setMargins(QMargins(5, 5, 5, 5))           # Chart margins
        self.setTheme(self.ChartThemeLight)             # Chart theme
        self.setTitle(self.__title)                     # Chart title
        self.setTitleFont(CHART_DEFAULT_TITLE_FONT)     # Chart title font

    def plot_series(self, x, y):
        self.x_axis.setRange(min(x) - 0.01, max(x) + 0.01)
        self.y_axis.setRange(0, max(y) + 0.1)
        new_points = list()
        for x, y in zip(x, y):
            new_points.append(QPointF(x, y))
        self.base_series.replace(new_points)

    def update_series(self, x, y):
        self.base_series.append(x, y)
        if x >= 12:
            dx = self.plotArea().width() / self.x_axis.tickCount()
            self.scroll(dx, 0)


class BaseBarChart(QChart):
    """
    Class used for the base representation of a bar chart
    """

    def __init__(self, **kwargs):
        self.__title = kwargs.get('title', BARCHART_DEFAULT_TILE)
        self.__x_categories = kwargs.get('x_categories', list())
        self.__default_bars = kwargs.get('bars', list())
        super(BaseBarChart, self).__init__()

        self.bars = list()
        self._build_default_bars()
        self.createDefaultAxes()
        self.removeAxis(self.axes(Qt.Horizontal)[0])

        # X axis customization
        self.x_axis = QBarCategoryAxis()
        self.x_axis.setCategories(self.x_categories)
        self.x_axis.setLabelsFont(CHART_DEFAULT_LABEL_FONT)
        self.addAxis(self.x_axis, Qt.AlignBottom)

        # Y axis customization
        self.y_axis = self.axes(Qt.Vertical, self.series()[0])[0]
        self.y_axis.setLabelsFont(BARCHART_DEFAULT_LABEL_FONT)
        self.y_axis.setRange(0, 100)
        self.y_axis.setTickCount(BARCHART_DEFAULT_TICKCOUNT)

        # Customize the base appearance of the chart in this section
        self.layout().setContentsMargins(0, 0, 0, 0)        # Layout margins
        self.legend().setAlignment(Qt.AlignBottom)          # Legends position
        self.legend().setVisible(True)                      # Legends visibility
        self.setAnimationOptions(QChart.SeriesAnimations)   # Chart Animations
        self.setBackgroundRoundness(0)                      # Chart roundness
        self.setMargins(QMargins(10, 10, 10, 10))           # Chart margins
        self.setTheme(self.ChartThemeLight)                 # Chart theme
        self.setTitle(self.__title)                         # Chart title
        self.setTitleFont(CHART_DEFAULT_TITLE_FONT)         # Chart title font

    def _build_default_bars(self):
        """
        Build a bar series with a default height
        """

        for category, height in zip(self.__x_categories, self.__default_bars):
            bar_series = QBarSeries()

            # Bar customization
            bar = QBarSet(category)
            bar.setLabelColor(BLACK)
            bar.setLabelFont(BARCHART_DEFAULT_LABEL_FONT)
            bar.append(height)

            # Insertion of the bar in the series of bars
            bar_series.append(bar)
            bar_series.setLabelsFormat(BARCHART_LABEL_FORMAT)
            bar_series.setLabelsVisible(True)

            # Bar chart series update
            self.bars.append(bar)
            bar_series.setLabelsPosition(QAbstractBarSeries.LabelsCenter)
            self.addSeries(bar_series)

    def update_bar_series(self, values):
        """
        Update the bar heights
        """

        for index, height in enumerate(values):
            self.bars[index].replace(0, height)
