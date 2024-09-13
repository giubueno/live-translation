#!/bin/bash

source env/bin/activate
python translator.py -l pl || exec "$0"