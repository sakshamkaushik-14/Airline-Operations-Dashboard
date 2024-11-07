# Airline-Operations-Dashboard

## Overview
### Project Summary: Flight Analytics Dashboard

This project is a **Flight Analytics Dashboard** developed using Streamlit, Plotly, and MySQL, designed to visualize and analyze flight data. It consists of two primary components:

1. **Front-end Application (app.py)**: The Streamlit application provides an intuitive user interface with three main sections accessible via a sidebar:
   - **About the Project**: Brief overview of the dashboard.
   - **Check Flights**: Allows users to select source and destination cities to view flight details, such as airline, route, departure time, duration, and price, in a structured data frame.
   - **Analytics**: Offers various data visualizations, including:
     - **Airline Frequency Pie Chart**: Visualizes the number of flights per airline.
     - **Busiest Airport Bar Chart**: Shows the most frequently visited airports.
     - **Daily Flights Line Chart**: Plots the daily frequency of flights over time.

2. **Database Helper (dbhelper.py)**: This module establishes a connection to a MySQL database, retrieves data, and executes the necessary SQL queries for the analytics dashboard. The functions include:
   - Fetching distinct city names for the flight routes.
   - Retrieving flight details based on source and destination.
   - Calculating airline frequency for pie chart visualization.
   - Identifying busy airports.
   - Aggregating daily flight frequency for time-series analysis.

This dashboard provides an interactive and user-friendly tool for exploring key trends and patterns in flight data.

## Features
- Manage and analyze **10,000+ flight records**.
- Interactive and user-friendly dashboard for real-time data visualization.
- CRUD operations for flight data using RESTful APIs.
- Optimized SQL queries for improved database performance.
- Data processing and cleaning using Pandas.

## Technologies Used
- **Programming Languages**: Python, SQL
- **Data Analysis**: Pandas, Data Cleaning, Data Transformation
- **Web Development**: Flask, RESTful API Development
- **Dashboarding**: Streamlit (Interactive Dashboard Design)
- **Database Management**: SQLite/MySQL, Query Optimization
- **Backend Development**: API Integration, CRUD Operations
- **Performance Optimization**: Query Efficiency, Data Retrieval Optimization
