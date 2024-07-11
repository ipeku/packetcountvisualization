# Packet Count Visualization

This project is designed to visualize network traffic data of "youtube" collected using Wireshark. Our goal is to understand and analyze changes in network traffic over time.

## Table of Contents

- [Features](#features)
- [Overview](#overview)
- [Usage](#usage)
- [Prerequisites](#prerequisites)
  
## Features

- Data Collection: Packet counts of "youtube" over a specific time period were collected using Wireshark and saved into a CSV file.
- Data Processing: Data from the CSV file was processed using Python and Pandas, resampling it into 1-second intervals.
- Visualization: We used the Matplotlib library to create a time-series graph showing the packet counts over time.
- Analysis: The graphs were analyzed to understand the intensity and variations in network traffic.
  
## Overview

This script loads packet count data from a CSV file, converts the time column to a pandas `timedelta` format, resamples the data to 1-second intervals, and plots the packet counts using `matplotlib`.

## Usage

- Place your CSV file in the specified directory.
- Modify the file path in the script to point to your CSV file.
- Run the script to generate the packet count visualization.

## CSV File Format

- The CSV file should have the following columns:

  - Time: Time in seconds
  - No.: Packet number or identifier

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- pandas
- matplotlib

You can install the required Python packages using:

  ```bash
  pip install pandas matplotlib

