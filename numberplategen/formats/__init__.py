"""This module contains the different formats for number plates.

Supported formats include NL, UK, US, and others.
"""

from .nl import nl_plate_format
from .tr import tr_plate_format
from .uk import uk_plate_format
from .us import us_plate_format

supported_formats = {
    'nl': nl_plate_format,
    'tr': tr_plate_format,
    'uk': uk_plate_format,
    'us': us_plate_format,
}
