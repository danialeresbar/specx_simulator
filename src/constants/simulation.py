from typing import Final

SAMPLE_INTERVAL_MIN: Final[int] = 1
SAMPLE_INTERVAL_MAX: Final[int] = 10
THRESHOLD_MIN: Final[float] = 0.01
CHANNEL_COUNT_DEFAULT: Final[int] = 9  # TODO: Do it from UI
ENERGY_THRESHOLD_DEFAULT: Final[float] = 0.33
SAMPLE_INTERVAL_DEFAULT: Final[int] = 1

##################### #
# CHANNEL FREQUENCIES #
##################### #
CH_14_FREQUENCY: Final[str] = "473 MHz"
CH_15_FREQUENCY: Final[str] = "479 MHz"
CH_16_FREQUENCY: Final[str] = "485 MHz"
CH_17_FREQUENCY: Final[str] = "491 MHz"
CH_18_FREQUENCY: Final[str] = "497 MHz"
CH_19_FREQUENCY: Final[str] = "503 MHz"
CH_20_FREQUENCY: Final[str] = "509 MHz"
CH_27_FREQUENCY: Final[str] = "551 MHz"
CH_28_FREQUENCY: Final[str] = "557 MHz"

########## #
# CHANNELS #
########## #
FIRST_CHANNEL: Final[int] = 14
LAST_CHANNEL: Final[int] = 28

#################### #
# MODULES & PACKAGES #
#################### #
PROBABILITY_DISTRIBUTIONS_MODULE: Final[str] = "probability_distributions"
STATISTICS_PACKAGE: Final[str] = "statistics"
