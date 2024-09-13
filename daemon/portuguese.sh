#!/bin/bash

source env/bin/activate
python translator.py -l pt || exec "$0"