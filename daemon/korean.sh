#!/bin/bash

source env/bin/activate
python translator.py -l ko || exec "$0"