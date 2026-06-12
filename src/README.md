# Source Code (src)

## Purpose
This folder contains the main Python script that implements the weather data pipeline.

## Contents
- weather_pipeline.py → Main script responsible for:
  - Fetching weather data from API
  - Processing and validating JSON responses
  - Transforming raw data into structured format
  - Handling errors and retries
  - Passing processed data to storage layer

## Role in Project
This is the core logic layer of the project where all data extraction and transformation happens.
