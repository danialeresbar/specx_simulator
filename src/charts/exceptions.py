from constants.messages import SERIES_ADDITION_ERROR_MESSAGE


class AbstractQChartError(Exception):
    def __init__(self, message):
        super().__init__(message)


class AbstractQChartInstantiationError(AbstractQChartError):
    def __init__(self, class_name: str):
        super().__init__(f'Abstract class "{class_name}" cannot be instantiated.')


class AbstractQChartMethodNotImplemented(AbstractQChartError, NotImplementedError):
    def __init__(self, method_name: str):
        super().__init__(f'Abstract method "{method_name}" must be implemented.')


class ChartError(Exception):
    def __init__(self, message):
        super().__init__(message)


class SeriesAdditionError(ChartError):
    def __init__(self):
        super().__init__(SERIES_ADDITION_ERROR_MESSAGE)
