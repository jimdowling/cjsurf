#!/bin/bash

set -e

echo "Running surf report feature pipeline"
jupyter nbconvert --to notebook --execute surf-report-feature-pipeline.ipynb

