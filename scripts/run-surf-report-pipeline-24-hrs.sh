#!/bin/bash

set -e

echo "Running surf report feature pipeline"
cd notebooks
export CJSURF_BACKFILL="False"
jupyter nbconvert --to notebook --execute surf-report-feature-pipeline.ipynb

