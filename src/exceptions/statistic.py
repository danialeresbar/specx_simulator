class StatisticError(Exception):
    pass


class RandomVariableGeneratorError(StatisticError):
    pass


class GeneratorNotImplementedError(RandomVariableGeneratorError):
    """
    Raised when a generator is not implemented for a probability distribution.
    """

    def __init__(self, distribution: str):
        super().__init__(f'Generator not implemented for {distribution}.')


class GeneratorWrongParametersError(RandomVariableGeneratorError):
    """
    Raised when a generator when a generator cannot be parameterized correctly.
    """

    def __init__(self, distribution: str, parameter: dict):
        super().__init__(f'Generator parameter error for {distribution} with parameters {parameter}.')


class GeneratorMissingParametersError(RandomVariableGeneratorError):
    """
    Raised when a generator when a generator cannot be parameterized correctly.
    """

    def __init__(self, distribution: str):
        super().__init__(f'Generator missing parameters for {distribution}.')


class PDFVectorGenerationError(StatisticError):
    """
    Raised when a PDF vector cannot be generated.
    """
