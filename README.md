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
2. Streamlit UI: `streamlit-image.py` - this Python program downloads the prediction image from Hopsworks and displays it. You need to set the HOPSWORKS_API_KEY environment variable in your Streamlit application. You create the HOPSWORKS_API_KEY in app.hopsworks.ai.
3. Notebooks: 
 * `surf-report-feature-pipeline.ipynb`: Downloads the latest surf report for today and writes it to the `lahinch` feature group.  Run manually first with 'BACKFILL=True' to fill the feature group with some surf reports from 2004 from a csv file.
 * `swell-predictions-feature-pipeline.ipynb`: Downloads the latest swell predictions and writes them to `swells_exploded`. Run manually first with 'BACKFILL=True' to fill the feature group with some swell predictions from 2004 from a csv file.
 * `training-pipeline.ipynb`: Trains a k-nearest neighbor model using scikit-learn. Creates training data using a feature view `lahinch_surf` that is created by performing a point-in-time correct join of features from the `lahinch` and `swells_exploded` feature groups.
 * `batch-prediction-pipeline.ipynb`: Gets the latest feature values for the `lahinch_surf` feature view and makes predictions of the surf heights for every 2 hours for the next 238 hours. It writes the predictions to a feature group `wave_predictions` and generates a PNG image with the predictions that is uploaded to Hopsworks. Streamlit downloads and shows this PNG as the surf predictions.

4. Scripts: these are run by the Github Actions workflows. They use nbconvert to convert the notebooks to Python programs that are then run.



### Data Sources

**Buoy for Predictions**

* ftp://ftpprd.ncep.noaa.gov/pub/data/nccf/com/gfs/v16.2/gfs.20220710/00/wave/station/bulls.t00z/gfswave.62081.spec
* https://polar.ncep.noaa.gov/waves/WEB/gfswave.latest_run/plots/gfswave.62081.bull
* https://polar.ncep.noaa.gov/waves/product_table.shtml?-latest-gfswave-tp_sw1-NE_atlantic-

**Surf Height Observations at Lahinch Beach**

* https://www.lahinchsurfshop.com/
