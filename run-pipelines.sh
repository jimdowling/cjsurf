#!/bin/bash

set -e

echo "Running swell predictions feature pipeline"
jupyter nbconvert --to notebook --execute swell-predictions-feature-pipeline.ipynb
echo "Running surf report feature pipeline"
jupyter nbconvert --to notebook --execute surf-report-feature-pipeline.ipynb
echo "Running batch prediction pipeline"
jupyter nbconvert --to notebook --execute batch-prediction-pipeline.ipynb

