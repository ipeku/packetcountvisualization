# Packet Count Visualization

This project visualizes packet counts over time, resampled to 1-second intervals, using data from a CSV file.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Prerequisites](#prerequisites)

  
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

