from faker import Faker
from PySide6.QtCharts import QChart, QLineSeries, QSplineSeries

from src.charts.exceptions import SeriesAdditionError
from src.charts.visualization import SingleSeriesChart
from src.constants.charts import CHART_TITLE_DEFAULT
from tests.base import QtApplicationTest

fake = Faker()


class TestSingleSeriesChart(QtApplicationTest):
    """
    Test the SingleSeriesChart class.
    """
    def test_create_single_series_chart(self):
        """
        Test that a SingleSeriesChart can be created with the default values.
        """
        chart = SingleSeriesChart()
        self.assertIsInstance(chart, QChart)
        self.assertEqual(chart.title(), CHART_TITLE_DEFAULT)
        self.assertTrue(chart.legend().isVisible())
        self.assertIsNone(chart.current_series)

    def test_add_series_to_single_series_chart(self):
        """
        Test that an error is raised when a series is already present in the
        chart.
        """
        chart = SingleSeriesChart()
        self.assertIsNone(chart.current_series)
        series = QLineSeries()
        chart.addSeries(series=series)
        self.assertEqual(chart.current_series, series)
        with self.assertRaises(SeriesAdditionError):
            chart.addSeries(series=QSplineSeries())

    def test_clean_series(self):
        """
        Test that the current series is removed from the chart. A new series
        can be added after the current series is removed.
        """
        chart = SingleSeriesChart()
        series = QLineSeries()
        chart.addSeries(series=series)
        self.assertEqual(chart.current_series, series)
        chart.clean_series()
        self.assertIsNone(chart.current_series)
        new_series = QSplineSeries()
        chart.addSeries(series=new_series)
        self.assertEqual(chart.current_series, new_series)
