#!/bin/bash

source env/bin/activate
python translator.py -l en || exec "$0"