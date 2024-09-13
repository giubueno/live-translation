#!/bin/bash

source env/bin/activate
python translator.py -l zh || exec "$0"