#!/bin/bash

source env/bin/activate
python translator.py -l ar || exec "$0"