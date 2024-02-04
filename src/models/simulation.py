import uuid

from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, model_validator
from typing import List, Self

from constants.simulation import (
    CH_14_FREQUENCY,
    CH_15_FREQUENCY,
    CH_16_FREQUENCY,
    CH_17_FREQUENCY,
    CH_18_FREQUENCY,
    CH_19_FREQUENCY,
    CH_20_FREQUENCY,
    CH_27_FREQUENCY,
    CH_28_FREQUENCY,
    SAMPLE_INTERVAL_MINUTES_MIN,
    SAMPLE_INTERVAL_MINUTES_MAX
)


class ChannelFrequency(Enum):
    CH_14 = CH_14_FREQUENCY
    CH_15 = CH_15_FREQUENCY
    CH_16 = CH_16_FREQUENCY
    CH_17 = CH_17_FREQUENCY
    CH_18 = CH_18_FREQUENCY
    CH_19 = CH_19_FREQUENCY
    CH_20 = CH_20_FREQUENCY
    CH_27 = CH_27_FREQUENCY
    CH_28 = CH_28_FREQUENCY


class TVChannel(BaseModel):
    number: int
    frequency: ChannelFrequency
    # TODO: Add PDF reference


class SimulationSettings(BaseModel):
    sample_interval_minutes: int = Field(..., ge=SAMPLE_INTERVAL_MINUTES_MIN, le=SAMPLE_INTERVAL_MINUTES_MAX)
    energy_threshold: float = Field(..., ge=0.0)
    energy_measurement: bool
    occupancy_measurement: bool

    class Config:
        validate_assignment = True

    @model_validator(mode='after')
    def check_measurement_select(self) -> Self:
        if not self.occupancy_measurement and not self.energy_measurement:
            raise ValueError('At least one measurement must be enabled.')

        if self.occupancy_measurement and self.energy_measurement:
            raise ValueError('Only one measurement can be enabled.')

        return self


class SimulationEnvironment(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    timestamp: datetime = Field(default_factory=datetime.now)
    settings: SimulationSettings = None
    channels: List[TVChannel] = []
