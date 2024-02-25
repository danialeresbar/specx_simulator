from collections.abc import Iterable

from PySide6.QtWidgets import QDoubleSpinBox, QLayout

from charts.abc import PlotFunctionChart
from constants.charts import DECIMAL_PLACES
from charts.visualization import PDFChart, PMFChart
from models.distribution import DistributionParameter, ProbabilityDistribution
from stats.abc import PDF, PMF
from stats import AVAILABLE_PROBABILITY_DISTRIBUTIONS
from views.components.custom import ParameterConfigWidget
from views.simulation_channel_config_view import ChannelConfigView


class ChannelConfigController(ChannelConfigView):
    """
    This class is responsible for controlling the channel config components.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.function_selector_box.currentIndexChanged.connect(self.update_config_components)
        self.selected_function = None
        for widget in self.function_available_parameters:
            widget.value_field.valueChanged.connect(self._update_selected_function_attributes)

    @property
    def is_ready(self) -> bool:
        return self.selected_function is not None

    def _build_chart_legend(self) -> str:
        return ', '.join([
            f'{widget.label.text()[:-1]}={widget.value_field.value():.{DECIMAL_PLACES}f}'
            for widget in filter(lambda widget: not widget.isHidden(), self.function_available_parameters)
        ])

    def _update_selected_function_attributes(self) -> None:
        """
        Update the attributes of the selected probability distribution. This
        method is called when the user changes the value of a parameter.
        """
        sender: QDoubleSpinBox = self.sender()
        parent_widget: ParameterConfigWidget = sender.parent()
        parameter_name: str = parent_widget.label.text().strip().split(':')[0]
        setattr(self.selected_function, parameter_name, sender.value())
        self.refresh_chart_preview()

    @staticmethod
    def clean_parameters_layout(layout: QLayout) -> None:
        """
        Clean the layout of the parameters frame. This method is called when
        the user selects a new probability distribution. It removes all the
        widgets from the layout.

        :param layout: The layout to be cleaned.
        """
        while layout.count():
            child = layout.takeAt(0)
            layout.removeWidget(child.widget())
            child.widget().setVisible(False)

    def get_available_function_parameter_values(self) -> list[float]:
        """
        Get the available values for the parameters of the selected probability
        distribution.

        :return: The available values for the parameters.
        """
        return [widget.value_field.value() for widget in self.function_available_parameters if widget.isVisible()]

    def update_config_components(self, index: int) -> None:
        """
        Refresh the configuration components for the selected probability
        distribution. This method is called when the user selects an item
        from the available options.

        :param index: Index of the selected item.
        """
        if self.function_selector_box.currentData() is None:
            return

        selected: ProbabilityDistribution = self.function_selector_box.currentData()
        distribution_parameters: list[DistributionParameter] = selected.parameters
        if (function_class := AVAILABLE_PROBABILITY_DISTRIBUTIONS.get(selected.name)) is not None:
            self.selected_function: PDF | PMF = function_class(
                *[parameter.value for parameter in distribution_parameters]
            )

        self.function_description_area.setPlainText(selected.description)
        if (layout := self.function_parameters_frame.layout()) is not None:
            self.clean_parameters_layout(layout=layout)
            widgets: list[ParameterConfigWidget] = self.function_available_parameters[:len(distribution_parameters)]
            for widget, parameter in zip(widgets, distribution_parameters):
                widget.setVisible(True)
                widget.label.setText(f'{parameter.name}:')
                widget.value_field.setValue(parameter.value)
                widget.set_value_field_interval(parameter.interval)
                layout.addWidget(widget)

        self.refresh_chart_preview()

    def refresh_chart_preview(self) -> None:
        """
        Refresh the chart preview with the selected probability distribution. This
        method is called when the user selects a new probability distribution or
        changes the parameters of the current one.
        """
        is_pdf: bool = isinstance(self.selected_function, PDF)
        current_chart: PlotFunctionChart | None = self.function_chart_frame.get_current_chart()
        if current_chart is None:
            current_chart = PDFChart() if is_pdf else PMFChart()
            self.function_chart_frame.set_chart(chart=current_chart)

        if is_pdf:
            x, y = self.selected_function.get_vector_points()
        else:
            x, y = self.selected_function.get_value_set()

        current_chart.plot(x, y, self._build_chart_legend())

    def refresh_selector_options(self, options: Iterable[ProbabilityDistribution]) -> None:
        """
        Configures the options available for the probability distribution
        selector that will be associated to a channel.

        :param options: The available probability distributions.
        """
        self.function_selector_box.clear()
        self.function_description_area.clear()
        for distribution in options:
            self.function_selector_box.addItem(
                self.continuous_function_icon if distribution.is_continuous else self.discrete_function_icon,
                distribution.name,
                distribution  # TODO: Check this approach
            )
