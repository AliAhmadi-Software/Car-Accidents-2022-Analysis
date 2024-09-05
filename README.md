# Car Accidents 2022 Analysis

## Introduction
This project presents a comprehensive analysis of the “Car Accidents 2022” dataset obtained from Kaggle. The dataset provides an extensive compilation of data on road accidents reported over the year 2022, encompassing a wide range of attributes related to accidents, vehicles, and casualties. The objective of this analysis is to identify patterns and correlations within the data that could provide valuable insights into the factors contributing to road accidents and their severity.

## Overview
The dataset offers an extensive compilation of data on road accidents reported over 2022. It covers a wide range of attributes pertaining to the status of accidents, references for vehicles and casualties, demographic details, and the severity of injuries.

| Feature | Description |
| --- | --- |
| STATUS | Current state of the accident (e.g., reported, under investigation) |
| ACCIDENT INDEX | Unique identifier assigned to each reported accident |
| ACCIDENT YEAR | The year the accident took place |
| ACCIDENT REFERENCE | Reference number linked to the accident |
| VEHICLE REFERENCE | Reference number assigned to the vehicle involved in the accident |
| CASUALTY REFERENCE | Reference number assigned to the casualty in the accident |
| CASUALTY CLASS | Class of the casualty (e.g., driver, passenger, pedestrian) |
| SEX OF CASUALTY | Gender of the casualty (male or female) |
| AGE OF CASUALTY | Age of the casualty |
| AGE BAND OF CASUALTY | Age group of the casualty (e.g., 0-5, 6-10, 11-15) |
| CASUALTY SEVERITY | Severity of the casualty’s injuries (e.g., fatal, serious, slight) |
| PEDESTRIAN LOCATION | Location of the pedestrian when the accident occurred |
| PEDESTRIAN MOVEMENT | Movement of the pedestrian at the time of the accident |
| CAR PASSENGER | Indicates if the casualty was a car passenger during the accident (yes or no) |
| BUS OR COACH PASSENGER | Indicates if the casualty was a bus or coach passenger (yes or no) |
| PEDESTRIAN ROAD MAINTENANCE WORKER | Indicates if the casualty was a road maintenance worker (yes or no) |
| CASUALTY TYPE | Type of casualty (e.g., driver/rider, passenger, pedestrian) |
| CASUALTY HOME AREA TYPE | Type of area where the casualty resides (e.g., urban, rural) |
| CASUALTY IMD DECILE | IMD decile of the casualty’s residential area (a measure of deprivation) |
| LSOA OF CASUALTY | The Lower Layer Super Output Area (LSOA) linked to the casualty’s location |


## Requirements

The following Python packages are required to run the application:

- **contourpy** version 1.2.0: A Python library for contouring and gridding of 2D data.
- **cycler** version 0.12.1: Composable style cycles.
- **fonttools** version 4.49.0: Library to manipulate font files from Python.
- **joblib** version 1.3.2: Lightweight pipelining in Python.
- **kiwisolver** version 1.4.5: A fast implementation of the Cassowary constraint solver.
- **matplotlib** version 3.8.3: A Python 2D plotting library.
- **numpy** version 1.26.4: The fundamental package for scientific computing with Python.
- **packaging** version 23.2: Core utilities for Python packages.
- **pandas** version 2.2.1: Powerful data structures for data analysis, time series, and statistics.
- **pillow** version 10.2.0: Python Imaging Library (Fork).
- **pyparsing** version 3.1.1: Python parsing module.
- **python-dateutil** version 2.8.2: Extensions to the standard Python datetime module.
- **pytz** version 2024.1: World timezone definitions, modern and historical.
- **scikit-learn** version 1.4.1.post1: A set of python modules for machine learning and data mining.
- **scipy** version 1.12.0: Scientific Library for Python.
- **seaborn** version 0.13.2: Statistical data visualization.
- **six** version 1.16.0: Python 2 and 3 compatibility utilities.
- **threadpoolctl** version 3.3.0: Controls the threadpools of native libraries.
- **tzdata** version 2024.1: Timezone database for Python.
