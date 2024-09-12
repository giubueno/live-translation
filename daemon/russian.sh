#!/bin/bash

source env/bin/activate
python translator.py -l ru || exec "$0"