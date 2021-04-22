from src.charts import base

X_CATEGORIES = ['Success', 'Failure']
DEFAULT_BAR_COLORS = [base.LIGHT_GREEN, base.INDIAN_RED]
DEFAULT_SUCCESS_VALUE = 0.5


class BernoulliPMF(base.BaseBarChart):
    """

    """

    def __init__(self, **kwargs):
        self.__success = kwargs.get('success', DEFAULT_SUCCESS_VALUE)
        super(BernoulliPMF, self).__init__(
            title=kwargs.get('title'),
            x_categories=X_CATEGORIES,
            bars=[self.__success, 1 - self.__success]
        )

    def plot(self):
        """

        """

        values = [self.__success, 1 - self.__success]
        self.update_bar_series(values)
