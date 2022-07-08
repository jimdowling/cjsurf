[![cjsurf-surf-report](https://github.com/jimdowling/cjsurf/actions/workflows/surf-report.yml/badge.svg)](https://github.com/jimdowling/cjsurf/actions/workflows/surf-report.yml)

[![cjsurf-swell-batch-predict](https://github.com/jimdowling/cjsurf/actions/workflows/swell-predictions.yml/badge.svg)](https://github.com/jimdowling/cjsurf/actions/workflows/swell-predictions.yml)

# Cjsurf
A serverless analytical ML system tha predicts surf (wave) heights at Lahinch Beach, Ireland:

https://jimdowling-cjsurf-streamlit-image-un2its.streamlitapp.com/

## Operated using only Free Serverless Services 

1. **Hopsworks**: Features, models, and assets are stored on https://app.hopsworks.ai
2. **Github Actions**: Two feature pipelines and a batch prediction pipeline are executed in total five times per day using GitHubActions.
3. **Streamlit Cloud**: The user interface is a Streamlit application written in Python  

## Architecture
![CJSurf Architecture](https://github.com/jimdowling/cjsurf/blob/main/cjsurf-architecture.png)

