#!/bin/bash

source env/bin/activate
python translator.py -l uk || exec "$0"