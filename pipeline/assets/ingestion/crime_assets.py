import os
import gc
import requests
import polars as pl
from datetime import datetime

# Replace MaterializeResult with Output
from dagster import asset, Output, MetadataValue

@asset(
    name="crime_nypd_arrests",
    io_manager_key="fastopendata_partitioned_parquet_io_manager",
    group_name="crime",
    tags={"domain": "crime", "type": "ingestion", "source": "fastopendata"},
    metadata={
        "data_url": MetadataValue.url("https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u/about_data")
    }
)
def crime_nypd_arrests():
    """
    Asset that wants data from March 2022 to December 2024, for example.
    Instead of returning a Polars DataFrame, we return a dict with the
    start/end that the IO manager can use to fetch data from R2.
    """
    return {
        "start_year": 2013,
        "start_month": 3,
        "end_year": 2023,
        "end_month": 12
    }

