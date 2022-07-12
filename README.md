[![cjsurf-surf-report](https://github.com/jimdowling/cjsurf/actions/workflows/surf-report.yml/badge.svg)](https://github.com/jimdowling/cjsurf/actions/workflows/surf-report.yml)

[![cjsurf-swell-batch-predict](https://github.com/jimdowling/cjsurf/actions/workflows/swell-predictions.yml/badge.svg)](https://github.com/jimdowling/cjsurf/actions/workflows/swell-predictions.yml)



# Cjsurf
A serverless analytical ML system tha predicts surf (wave) heights at Lahinch Beach, Ireland:

 * [Live Predictions of Surf Height at Lahinch](https://jimdowling-cjsurf-streamlit-image-un2its.streamlitapp.com/)
 * [PyData London talk on CJSurf as a Serverless ML Platform](https://www.youtube.com/watch?v=AIof4woJSkY)
 * [Predicting surf wave heights (ICML 2005)](https://icml.cc/Conferences/2005/proceedings/papers/015_Predicting_CarneyEtAl.pdf)

![Lahinch](https://github.com/jimdowling/cjsurf/blob/main/lahinch.png)

## Operated using only Free Serverless Services 

1. **Hopsworks**: Features, models, and assets are stored on https://app.hopsworks.ai
2. **Github Actions**: Two feature pipelines and a batch prediction pipeline are executed in total five times per day using GitHubActions.
3. **Streamlit Cloud**: The user interface is a Streamlit application written in Python  

The model training notebook was run manually in [Colab](https://colab.research.google.com/github/jimdowling/cjsurf/blob/main/training-pipeline.ipynb), and can be run again at any time, using the new training data that has been collected since the last training run.

## Architecture

CJSurf is written entirely in Python. 

![CJSurf Architecture](https://github.com/jimdowling/cjsurf/blob/main/cjsurf-architecture.png)

## Details

**Requirements:** Create accounts on app.hopsworks.ai, github.com, streamlit.io.

**Files:**

1. Github Actions files: .github/workflows/*.yml - they run the notebooks below on 6 hr and 24 hr schedules using bash scripts.
2. Streamlit UI: `streamlit-image.py` - this Python program downloads the prediction image from Hopsworks and displays it. You need to set the HOPSWORKS_API_KEY environment variable in your Streamlit application.
3. Notebooks: 
  
 * `surf-report-feature-pipeline.ipynb`: Downloads the latest surf report for today and writes it to the `lahinch` feature group.  Set 'BACKFILL=True' to fill with some surf reports from 2004 from a csv file.
 * `swell-predictions-feature-pipeline.ipynb`: Downloads the latest swell predictions and writes them to `swells_exploded`. Set 'BACKFILL=True' to fill with some swell predictions from 2004 from a csv file.
 * `training-pipeline.ipynb`: Trains a k-nearest neighbor model using scikit-learn. Creates training data using a feature view `lahinch_surf` that is created by performing a point-in-time correct join of features from `lahinch` and `swells_exploded`.
 * `batch-prediction-pipeline.ipynb`: Writes predictions to  feature group `wave_predictions` and generates a PNG image with the predictions that is uploaded to Hopsworks.

4. Scripts: these are run by the Github Actions workflows. They use nbconvert to convert the notebooks to Python programs that are then run.
