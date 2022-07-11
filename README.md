[![cjsurf-surf-report](https://github.com/jimdowling/cjsurf/actions/workflows/surf-report.yml/badge.svg)](https://github.com/jimdowling/cjsurf/actions/workflows/surf-report.yml)

[![cjsurf-swell-batch-predict](https://github.com/jimdowling/cjsurf/actions/workflows/swell-predictions.yml/badge.svg)](https://github.com/jimdowling/cjsurf/actions/workflows/swell-predictions.yml)

# PyData London Talk

![PyData London talk](https://www.youtube.com/watch?v=AIof4woJSkY)

# Cjsurf
A serverless analytical ML system tha predicts surf (wave) heights at Lahinch Beach, Ireland:

https://jimdowling-cjsurf-streamlit-image-un2its.streamlitapp.com/


![Lahinch](https://github.com/jimdowling/cjsurf/blob/main/lahinch.png)

## Operated using only Free Serverless Services 

1. **Hopsworks**: Features, models, and assets are stored on https://app.hopsworks.ai
2. **Github Actions**: Two feature pipelines and a batch prediction pipeline are executed in total five times per day using GitHubActions.
3. **Streamlit Cloud**: The user interface is a Streamlit application written in Python  

The model training notebook was run manually in [Colab](https://colab.research.google.com/github/jimdowling/cjsurf/blob/main/training-pipeline.ipynb), and can be run again at any time, using the new training data that has been collected since the last training run.

## Architecture

CJSurf is written entirely in Python. 

![CJSurf Architecture](https://github.com/jimdowling/cjsurf/blob/main/cjsurf-architecture.png)

## References

 * This work is based on a [paper we published on predicting wave heights at ICML 2005](https://icml.cc/Conferences/2005/proceedings/papers/015_Predicting_CarneyEtAl.pdf).
