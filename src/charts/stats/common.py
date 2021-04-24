from PyQt5.QtChart import QLegend
from src.charts import base

# ---- Greg letters ----
ALPHA = 'α'
BETA = 'β'
GAMMA = 'γ'
LAMBDA = 'λ'
MU = 'μ'
SIGMA = 'σ'

# ---- Statistic ----
SAMPLES = 100


class PDFChart(base.BaseChart):
    """

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Chart attributes
        self.legend().setVisible(True)
        self.legend().setMarkerShape(QLegend.MarkerShapeFromSeries)
        self.setAnimationOptions(base.QChart.SeriesAnimations)

        # Axis settings
        self.addSeries(self.base_series)
        self.createDefaultAxes()
        self.x_axis = self.axes(base.Qt.Horizontal, self.series()[0])[0]
        self.y_axis = self.axes(base.Qt.Vertical, self.series()[0])[0]

        # Series style customization
        pen = self.base_series.pen()
        pen.setColor(base.SERIES_COLOR)
        pen.setWidth(base.CHART_DEFAULT_SERIES_WIDTH)
