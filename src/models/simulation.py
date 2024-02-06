from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from uuid import uuid4

from constants.field_names import ENERGY_STR, OCCUPANCY_STR
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
    ENERGY_THRESHOLD_DEFAULT,
    FIRST_CHANNEL,
    LAST_CHANNEL,
    SAMPLE_INTERVAL_MIN,
    SAMPLE_INTERVAL_MAX,
)
from models.distribution import ProbabilityDistribution


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
    associated_distribution: ProbabilityDistribution | None = None

    class Config:
        use_enum_values = True


class SimulationMeasurement(Enum):
    ENERGY = ENERGY_STR
    OCCUPANCY = OCCUPANCY_STR


class SimulationSettings(BaseModel):
    sample_interval: int = Field(..., ge=SAMPLE_INTERVAL_MIN, le=SAMPLE_INTERVAL_MAX)
    energy_threshold: float = Field(..., ge=ENERGY_THRESHOLD_DEFAULT)
    measurement: SimulationMeasurement

    class Config:
        validate_assignment = True
        use_enum_values = True


class SimulationEnvironment(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex)
    timestamp: datetime = Field(default_factory=datetime.now)
    settings: SimulationSettings
    channels: list[TVChannel] | None = None
