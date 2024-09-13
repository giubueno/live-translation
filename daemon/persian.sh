#!/bin/bash

source env/bin/activate
python translator.py -l fa || exec "$0"