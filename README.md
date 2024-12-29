# DataOps Pipeline Project

## Description

This project demonstrates a complete DataOps pipeline using Python, integrating data generation, extraction, transformation, validation, and loading processes. It also includes testing and orchestration of the entire pipeline.

## How to run

1. Install dependencies:

pip install -r requirements.txt

2. Generate raw data:

python data_generation/generate_data.py

3. Run the pipeline:

python pipelines/etl_pipeline.py

## Directory Structure

- `data_generation/` - Scripts for generating raw data.
- `data_extraction/` - Scripts for extracting data.
- `data_transformation/` - Scripts for transforming data.
- `data_validation/` - Scripts for validating data.
- `data_loading/` - Scripts for loading data into a database.
- `tests/` - Unit tests for different parts of the pipeline.
- `pipelines/` - Script for orchestrating the complete pipeline.
