#!/bin/bash

set -e

echo "Running surf report feature pipeline"
cd notebooks

jupyter nbconvert --to notebook --execute notebooks/surf-report-feature-pipeline.ipynb

