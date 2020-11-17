#!/bin/bash

set -e

source .venv/bin/activate

python aoa_vis.py

deactivate
