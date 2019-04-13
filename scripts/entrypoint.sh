#!/bin/sh
pip install -r requirements.txt
pip install -e .
app run --host=0.0.0.0 --port=5000