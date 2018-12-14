#!/usr/bin/env python3

import math
import os

digits = int(os.getenv('DIGITS', default="10"))

print(round(math.pi, digits))
