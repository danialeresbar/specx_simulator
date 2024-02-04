from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, model_validator
from typing import List, Optional, Self
from uuid import uuid4

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
    FIRST_CHANNEL,
    LAST_CHANNEL,
    SAMPLE_INTERVAL_MIN,
    SAMPLE_INTERVAL_MAX
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
    number: int = Field(..., ge=FIRST_CHANNEL, le=LAST_CHANNEL)
    frequency: ChannelFrequency


class SimulationSettings(BaseModel):
    sample_interval: int = Field(..., ge=SAMPLE_INTERVAL_MIN, le=SAMPLE_INTERVAL_MAX)
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
    id: str = Field(default_factory=lambda: uuid4().hex)
    timestamp: datetime = Field(default_factory=datetime.now)
    settings: SimulationSettings
    channels: Optional[List[TVChannel]] = None
