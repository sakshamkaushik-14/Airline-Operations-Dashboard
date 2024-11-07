import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px


st.sidebar.title('Flights Analytics')
user_option = st.sidebar.selectbox('Menu',['About the Project','Check Flights','Analytics'])

db = DB()


if user_option == 'Check Flights':
    st.title('Check Flights')

    col1,col2 = st.columns(2)

    city = db.fetch_city_names()

    with col1:
        source = st.selectbox('Source',sorted(city))
    with col2:
        destination = st.selectbox('Destination', sorted(city))

    if st.button('Search'):
        results = db.fetch_all_flights(source,destination)
        df = pd.DataFrame(results, columns=['Airline', 'Route', 'Dep_Time', 'Duration', 'Price'])  # Rename columns
        st.dataframe(df)

elif user_option == 'Analytics':
    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("Pie chart")
    st.plotly_chart(fig)

    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x=city,
        y=frequency1
    )
    fig.update_layout(
        title={
        'text': 'Busiest Airport Bar Chart',
        'font': {'size': 24}},  # Adjust title font size here,  # Chart title
        xaxis_title='Airport',  # X-axis title
        yaxis_title='Frequency'  # Y-axis title
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    date, frequency2 = db.daily_frequency()

    print(len(date))
    print(len(frequency2))
    fig = px.line(
        x=date,
        y=frequency2
    )
    fig.update_layout(
        title={
            'text': 'Daily Number of Flights',
            'font': {'size': 24}  # Adjust title font size here
        },
        xaxis_title='Dates',
        yaxis_title='Number of Flights'
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

else:

    st.title("Project Summary: Flight Analytics Dashboard")

    st.write("""
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

    Together, this dashboard provides an interactive and user-friendly tool for exploring key trends and patterns in flight data.
    """)
