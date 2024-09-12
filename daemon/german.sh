#!/bin/bash

source env/bin/activate
python translator.py -l de || exec "$0"