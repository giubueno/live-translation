#!/bin/bash

source env/bin/activate
python translator.py -l fr || exec "$0"