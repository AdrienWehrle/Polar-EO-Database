#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Adrien Wehrlé, University of Zurich, Switzerland

"""

import json
import yaml
import os

# read JSON file automatically generated
with open("order.json", "r") as json_file:
    data = json.load(json_file)

# extract sensor name
sensor_name = data["sensor-name"]

# rename file with sensor name and convert to YAML
with open(f"./data/{sensor_name}.yaml", "w") as yaml_file:
    outputs = yaml.dump(data, yaml_file, default_flow_style=False)

# remove temporary JSON file
os.remove("order.json")
