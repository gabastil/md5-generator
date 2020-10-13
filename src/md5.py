#!/usr/bin/env python
#-*- encoding: utf8 -*-
import random

digits = random.getrandbits(128)

# Print the digits to the screen
print(f"MD5: {digits:32x}")
