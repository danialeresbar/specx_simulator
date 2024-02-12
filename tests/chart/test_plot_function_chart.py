from faker import Faker

from src.charts.abc import PlotFunctionChart
from src.charts.exceptions import AbstractQChartInstantiationError
from src.charts.visualization import PDFChart, PMFChart, SingleSeriesChart
from src.constants.charts import CHART_PDF_TITLE, CHART_PMF_TITLE
from src.stats.probability_distributions import BernoulliPMF, NormalPDF
from tests.base import QtApplicationTest

fake = Faker()


class TestPlotFunctionChart(QtApplicationTest):

    def setUp(self):
        self.probability_density_function = NormalPDF(mean=fake.pyfloat(), std=fake.pyfloat(positive=True))
        self.probability_mass_function = BernoulliPMF(p=fake.pyfloat(min_value=0, max_value=1))

    def tearDown(self):
        ...

    def test_create_plot_function_chart(self):
        """
        Test that the PlotFunctionChart can not be instantiated. This is
        because it is an abstract class and should not be instantiated.
        """
        self.assertRaises(AbstractQChartInstantiationError, PlotFunctionChart)

    def test_create_pdf_chart(self):
        """
        Test that a PDFChart can be created with the default values.
        """
        chart = PDFChart()
        self.assertIsInstance(chart, SingleSeriesChart)
        self.assertEqual(chart.title(), CHART_PDF_TITLE)
        self.assertIsNotNone(chart.current_series)
        self.assertGreater(len(chart.axes()), 0)

    def test_create_pmf_chart(self):
        """
        Test that a PMFChart can be created with the default values.
        """
        chart = PMFChart()
        self.assertIsInstance(chart, SingleSeriesChart)
        self.assertEqual(chart.title(), CHART_PMF_TITLE)
        self.assertIsNotNone(chart.current_series)
        self.assertEqual(len(chart.axes()), 0)

    def test_pdf_chart_plot_function(self):
        """
        Test that a PDFChart can plot a probability density function.
        """
        chart = PDFChart()
        x, y = self.probability_density_function.get_vector_points()
        chart.plot(x=x, y=y, series_legend=fake.word())
        self.assertEqual(len(chart.current_series.points()), len(x))

    def test_pmf_chart_plot_function(self):
        """
        Test that a PMFChart can plot a probability mass function.
        """
        chart = PMFChart()
        x, y = self.probability_mass_function.get_value_set()
        chart.plot(x=x, y=y, series_legend=fake.word())
        self.assertEqual(chart.current_series.count(), 1)
        self.assertGreater(len(chart.axes()), 0)
