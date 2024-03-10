from abc import ABC, abstractmethod
from numpy import ndarray

__all__ = ['RandomVariableGenerator', 'PDF', 'PMF', 'PMFValueSet', 'PDFVectorPoints']

############## #
# CUSTOM TYPES #
############## #
PMFValueSet = tuple[ndarray, ndarray]
PDFVectorPoints = tuple[ndarray, ndarray]


class RandomVariableGenerator(ABC):
    """
    Abstract class for random variable generators.
    """

    @abstractmethod
    def rvs(self, size: int) -> ndarray:
        """
        Generates random numbers using the probability distribution associated.

        :param size: The number of random numbers to generate.
        :return: An array of random numbers.
        """
        pass


class PDF(RandomVariableGenerator):
    """
    A probability density function (PDF), density function, or density of an
    absolutely continuous random variable, is a function whose value at any
    given sample (or point) in the sample space (the set of possible values
    taken by the random variable).
    """

    @abstractmethod
    def get_vector_points(self) -> PDFVectorPoints:
        """
        Generates a vector of points for each axis of the Cartesian plane (2D)
        according to the parameters of the probability distribution. Vectors
        allow you to study the probability density function (PDF) associated
        with the distribution.

        :return: A tuple of two arrays.
        """
        pass


class PMF(RandomVariableGenerator):
    """
    The Probability Mass function is defined on all the values of R, where it
    takes all the arguments of any real number. It does not belong to the value
    of X when the argument value equals to zero and when the argument belongs
    to x, the value of PMF should be positive.
    """

    @abstractmethod
    def get_value_set(self) -> PMFValueSet:
        """
        Generates a set of values for the probability mass function (PMF) of
        the distribution. The set is represented by a tuple of two arrays, the
        first array contains the values of the random variable and the second
        array contains the probabilities associated with each value.

        :return: A tuple of two arrays.
        """
        pass
