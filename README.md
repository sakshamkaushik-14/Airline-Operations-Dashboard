# Airline-Operations-Dashboard

## Overview
### Project Summary:

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
- **Data Analysis**: Pandas, Data Transformation
- **Dashboarding**: Streamlit (Interactive Dashboard Design)
- **Database Management**: SQLite/MySQL, Query Optimization
- **Backend Development**: API Integration, CRUD Operations
- **Performance Optimization**: Query Efficiency, Data Retrieval Optimization

## Screenshots - 
- <img width="1440" alt="Screenshot 2024-11-07 at 8 30 25 PM" src="https://github.com/user-attachments/assets/4fbeae6d-c064-4f26-b597-c3389f678e8b"> 
- <img width="1440" alt="Screenshot 2024-11-07 at 8 41 50 PM" src="https://github.com/user-attachments/assets/896dffde-dc3a-4572-8405-f87832418675">
- <img width="1440" alt="Screenshot 2024-11-07 at 8 42 00 PM" src="https://github.com/user-attachments/assets/37108ea8-ddb5-4ea8-9ca8-855b3cdea39d">
- <img width="1440" alt="Screenshot 2024-11-07 at 8 42 09 PM" src="https://github.com/user-attachments/assets/3d44619e-e1f2-4fbd-bc05-b39821804682">
- <img width="1440" alt="Screenshot 2024-11-07 at 8 50 40 PM" src="https://github.com/user-attachments/assets/a1c9b7f8-5993-44f1-9be1-5d2809be0ce6">


 

