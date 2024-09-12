#!/bin/bash

source env/bin/activate
python translator.py -l tr || exec "$0"