#!/bin/bash

set -e

echo "Running surf report feature pipeline"
cd notebooks

jupyter nbconvert --to notebook --execute surf-report-feature-pipeline.ipynb

