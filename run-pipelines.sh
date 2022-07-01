#!/bin/bash

set -e

jupyter nbconvert --to notebook --execute swell-predictions-feature-pipeline.ipynb
jupyter nbconvert --to notebook --execute surf-report-feature-pipeline.ipynb
jupyter nbconvert --to notebook --execute batch-prediction-pipeline.ipynb

