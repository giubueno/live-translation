#!/bin/bash

source env/bin/activate
python translator.py -l es || exec "$0"