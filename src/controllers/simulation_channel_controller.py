from PySide6.QtWidgets import QLayout
from typing import Iterable

from constants.field_names import PDF_STR, PMF_STR
from constants.simulation import (
    PROBABILITY_DISTRIBUTIONS_MODULE,
    STATISTICS_PACKAGE
)
from models.distribution import DistributionParameter, ProbabilityDistribution
from stats.abc import PDF, PMF
from views.simulation_channel_config_view import ChannelConfigView
from views.simulation_channel_config_view import ParameterConfigWidget
from tools.imports import import_class_from_module


class ChannelConfigController(ChannelConfigView):

    def __init__(self, *args, **kwargs):
        super(ChannelConfigController, self).__init__(*args, **kwargs)
        self.function_selector_box.currentIndexChanged.connect(self.update_config_components)
        self.selected_function = None
        # TODO: Connect the spin box signals

    @staticmethod
    def clean_parameters_layout(layout: QLayout) -> None:
        """
        Clean the layout of the parameters frame. This method is called when
        the user selects a new probability distribution. It removes all the
        widgets from the layout.
        """
        while layout.count():
            child = layout.takeAt(0)
            layout.removeWidget(child.widget())
            child.widget().setVisible(False)

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
        desired_class: str = '{distribution}{suffix}'.format(
            distribution=selected.name,
            suffix=PDF_STR if selected.is_continuous else PMF_STR
        )
        imported_class: type = import_class_from_module(
            module_name=PROBABILITY_DISTRIBUTIONS_MODULE,
            package_name=STATISTICS_PACKAGE,
            class_name=desired_class
        )
        function: PDF | PMF = imported_class(*[parameter.value for parameter in distribution_parameters])
        self.function_description_area.setPlainText(selected.description)
        # TODO: Draw the Function chart

        if (layout := self.function_parameters_frame.layout()) is not None:
            self.clean_parameters_layout(layout=layout)
            widgets: list[ParameterConfigWidget] = self.function_available_parameters[:len(distribution_parameters)]
            for widget, parameter in zip(widgets, distribution_parameters):
                widget.label.setText(f'{parameter.name}:')
                widget.value_field.setValue(parameter.value)
                widget.set_value_field_interval(parameter.interval)
                if widget.isHidden():
                    widget.setVisible(True)

                layout.addWidget(widget)

    def refresh_selector_options(self, options: Iterable[ProbabilityDistribution]) -> None:
        """
        Configures the options available for the probability distribution
        selector (ComboBox) that will be associated to a channel.

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
