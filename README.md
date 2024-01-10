# Weather Stats Analyzer
This Python script is designed for analyzing weather statistics from CSV files. It provides various functionalities to help you gain insights into your weather data. Whether you want to calculate basic statistics, generate charts for visual analysis, or simply list the raw data, this tool has you covered.
## Features
1. **Minimum, Maximum, and Average Calculation:**
  Compute the minimum, maximum, or average value for a specified column in your weather data.
2. **Chart Generation:**
Generate charts to visualize the trends in your weather data. The script uses Matplotlib to create informative and visually appealing graphs.
3. **Raw Data Listing:**
Print the raw data for the specified column, giving you a detailed view of the weather statistics in your CSV file.
## Getting Started 
### Prerequisites
Python 3.x
Matplotlib library 
```
pip install matplotlib
```
### Usage
1. Clone the repository 
```
git clone https://github.com/your-username/Weather-Stats-Analyzer.git
cd Weather-Stats-Analyzer
```
2. Run the Script:
```
python weather_stats_analyzer.py [FILE] [COLUMN] [OPERATION]
```
Replace **[FILE]**, **[COLUMN]**, and **[OPERATION]** with your specific CSV file, column name, and operation (e.g., min, max, avg, chart, list).
## Examples
Calculate the minimum value for the "Temperature" column:
```
python weather_stats_analyzer.py weather_data.csv Temperature min
```
Generate a chart for the "Humidity" column:
```
python weather_stats_analyzer.py weather_data.csv Temperature min
```
List the raw data for the "Wind Speed" column:
```
python weather_stats_analyzer.py weather_data.csv "Wind Speed" list
```
