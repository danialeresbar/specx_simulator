from enum import Enum
from pydantic import BaseModel, Field, field_validator, model_validator
from typing import List, Optional, Self, Tuple

from constants.distributions import (
    DISTRIBUTION_DESCRIPTION_DEFAULT,
    DISTRIBUTION_PARAMETER_NAME_MAX_LENGTH,
    DISTRIBUTION_PARAMETER_NAME_MIN_LENGTH,
)
from constants.field_names import CONTINUOUS_STR, DISCRETE_STR

############## #
# CUSTOM TYPES #
############## #
ParameterInterval = Tuple[Optional[float], Optional[float]]


class ProbabilityDistributionCategory(Enum):
    DISCRETE = DISCRETE_STR
    CONTINUOUS = CONTINUOUS_STR


class DistributionParameter(BaseModel):
    """
    A distribution parameter is a parameter of a probability distribution. It
    is a value that describes a feature of the distribution, such as location,
    scale, or shape. The value of the parameter is usually not known and is
    estimated from the data.
    """
    name: str = Field(
        ...,
        allow_mutation=False,
        min_length=DISTRIBUTION_PARAMETER_NAME_MIN_LENGTH,
        max_length=DISTRIBUTION_PARAMETER_NAME_MAX_LENGTH
    )
    interval: ParameterInterval
    value: float
    alias: str = None

    class Config:
        validate_assignment = True

    @field_validator('interval')
    @classmethod
    def check_interval(cls, interval: ParameterInterval) -> ParameterInterval:
        lower, upper = interval
        non_infinite = lower is not None and upper is not None
        if non_infinite and lower >= upper:
            raise ValueError('The lower bound of the interval must be less than the upper bound.')

        return interval

    @model_validator(mode='after')
    def check_value_in_interval(self) -> Self:
        if self.is_boundless:
            return self

        lower, upper = self.interval
        if lower is not None and upper is None:
            if self.value < lower:
                raise ValueError('The value of the parameter must be greater than the lower bound.')

        if lower is None and upper is not None:
            if self.value > upper:
                raise ValueError('The value of the parameter must be less than the upper bound.')

        if lower is not None and upper is not None:
            if not lower <= self.value <= upper:
                raise ValueError('The value of the parameter must be within the interval.')

        return self

    @property
    def is_boundless(self) -> bool:
        lower, upper = self.interval
        return lower is None and upper is None


class ProbabilityDistribution(BaseModel):
    name: str
    category: ProbabilityDistributionCategory
    parameters: List[DistributionParameter] = Field(default_factory=list)
    description: str = DISTRIBUTION_DESCRIPTION_DEFAULT

    class Config:
        frozen = True
        use_enum_values = True

    @property
    def is_continuous(self) -> bool:
        return self.category == ProbabilityDistributionCategory.CONTINUOUS.value
