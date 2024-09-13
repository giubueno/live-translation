#!/bin/bash

source env/bin/activate
python translator.py -l bg || exec "$0"