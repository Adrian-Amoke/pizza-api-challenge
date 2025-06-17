#!/bin/bash
# Run the Flask app from the parent directory of 'server' package with PYTHONPATH set

export FLASK_APP=server.app
export FLASK_ENV=development
export PYTHONPATH=.

python -m server.app
