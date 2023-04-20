# Code Challenge Template

# Weather and Crop Yield Data Analysis

This project is designed to demonstrate skills in data engineering by ingesting weather and crop yield data, designing a database schema, and exposing the data through a REST API.

## Data Description

The `wx_data` directory has files containing weather data records from 1985-01-01 to 2014-12-31. Each file corresponds to a particular weather station from Nebraska, Iowa, Illinois, Indiana, or Ohio.

Each line in the file contains 4 records separated by tabs:

1. The date (YYYYMMDD format)
2. The maximum temperature for that day (in tenths of a degree Celsius)
3. The minimum temperature for that day (in tenths of a degree Celsius)
4. The amount of precipitation for that day (in tenths of a millimeter)

Missing values are indicated by the value -9999.

The crop yield data is stored in a CSV file and contains records for each state and county in the United States from 1990 to 2019. Each record contains the following fields:

1. State code (2-letter abbreviation)
2. County code (3-digit code)
3. Year
4. Commodity (corn or soybeans)
5. Value (in bushels)

## Database Schema

The weather data records will be stored in a single table named `weather_records`. The table will have the following columns:

- `id`: Unique identifier for the record (integer, primary key)
- `station_id`: The ID of the weather station (integer)
- `date`: The date of the record (YYYY-MM-DD format)
- `max_temp`: The maximum temperature for that day (in degrees Celsius)
- `min_temp`: The minimum temperature for that day (in degrees Celsius)
- `precipitation`: The amount of precipitation for that day (in centimeters)

The crop yield data will be stored in a separate table named `crop_yield`. The table will have the following columns:

- `id`: Unique identifier for the record (integer, primary key)
- `state_code`: The 2-letter abbreviation for the state (string)
- `county_code`: The 3-digit code for the county (string)
- `year`: The year of the record (integer)
- `commodity`: The type of crop (corn or soybeans)
- `value`: The yield for the crop (in bushels)

To store the results of the statistical calculations, a new table named `weather_stats` will be created. The table will have the following columns:

- `id`: Unique identifier for the record (integer, primary key)
- `station_id`: The ID of the weather station (integer)
- `year`: The year of the record (integer)
- `avg_max_temp`: The average maximum temperature for that year and station (in degrees Celsius)
- `avg_min_temp`: The average minimum temperature for that year and station (in degrees Celsius)
- `total_precipitation`: The total accumulated precipitation for that year and station (in centimeters)

## Running the Code

To run the code, you will need Python 3 installed on your system.

1. Clone the repository to your local machine.
2. Ingest the weather data by running the `ingest_weather_data.py` script. This script will read in the data files from the `wx_data` directory and store the records in the `weather_records` table in an SQLite database named `weather.db`.
3. Ingest the crop yield data by running the `ingest_crop_yield_data.py` script. This script will read in the data from the `crop_yield.csv` file and store the records in the `crop_yield` table in the same SQLite database.
4. Calculate the statistics and


# Weather API

This is a REST API that provides weather data for a given date and weather station ID. The API allows clients to filter the response by date and station ID, and data is paginated.

## Installation

To run the API, you need to have Python 3 and pip installed. You can install the required dependencies by running the following command:


`pip install -r requirements.txt` 

## Usage

To start the API, run the following command:


`python weather_flask.py` 

The API has the following endpoints:

### /api/weather

This endpoint returns a JSON-formatted response with a representation of the ingested/calculated weather data in the database. You can filter the response by date and station ID using the query string. Data is paginated.

#### Parameters

-   `date` (optional): the date in the format `YYYY-MM-DD`.
-   `station_id` (optional): the weather station ID.

#### Example



`GET /api/weather?date=2022-03-10&station_id=12345&page=1&limit=10` 

Response:



`{
  "data": [
    {
      "id": 1,
      "date": "2022-03-10",
      "station_id": "12345",
      "max_temp": 20.5,
      "min_temp": 10.5,
      "precipitation": 1.2
    },
    ...
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 100
  }
}` 

### /api/weather/stats

This endpoint returns a JSON-formatted response with average maximum temperature, average minimum temperature, and total accumulated precipitation for every year and weather station in the database.

#### Example



`GET /api/weather/stats` 

Response:

json

`{
  "data": [
    {
      "year": 2022,
      "station_id": "12345",
      "avg_max_temp": 20.5,
      "avg_min_temp": 10.5,
      "total_precipitation": 10.2
    },
    ...
  ]
}` 

## Documentation

The API documentation is available at the following endpoint:

### /api/docs

This endpoint provides automatic documentation of the API using Swagger UI.

## Testing

To run the unit tests, run the following command:


`python -m unittest discover tests/` 


