### Importing different packages

import pandas as pd 
import numpy as np
import altair as alt

### The code below is reading the data from astronauts csv 

astronauts_data = pd.read_csv("astronauts.csv")
astronauts_data

### My first question is: Which astronauts had the highest spaceflight to spaceflight hours ratio? 
### The code calculates the spaceflight_ratio by dividing the spaceflight hours by the number of spaceflights

astronauts_data["spaceflight_ratio"] = ((astronauts_data["Space Flight (hr)"] / astronauts_data["Space Flights"]))
astronauts_data.filter(["Name", "Gender", "spaceflight_ratio"]).sort_values(by = "spaceflight_ratio", ascending= False)

### The code below ask for the data that has a value we are looking for 
### Here I am splitting the data set by gender for future use 

female_data = astronauts_data.query("Gender == 'Female'")
female_data

male_data = astronauts_data.query("Gender == 'Male'")
male_data

### The code below gets the result for the highest spaceflight ratio for the male and female astronauts. 

female_max = female_data["spaceflight_ratio"].max()
male_max = male_data["spaceflight_ratio"].max()

print(f"The highest spaceflight ratio for the female astronauts was: {female_max}.")
print(f"The highest spaceflight_ratio for the male astronauts was: {male_max}.")

### This code will calculate the average spaceflight_ratio for all astronauts. 

average = astronauts_data["spaceflight_ratio"].mean()

print(f"The average spaceflight-ratio for all astronauts was: {average}.")

### The code below creates a chart that shows the average spaceflight hours per spaceflight for the female astronauts. 
### It only shows us the top 10 results. 

female_spaceflight_Chart = (alt.Chart(female_data.sort_values("spaceflight_ratio", ascending = False).head(10))
    .encode(
        x = 'spaceflight_ratio:Q',
        y = 'Name'
    )
    .mark_bar()
    .properties(width = 800))

female_spaceflight_Chart

### The code below creates a chart that shows the average spaceflight hours per spaceflight for the male astronauts.

male_spaceflight_Chart = (alt.Chart(male_data.sort_values("spaceflight_ratio", ascending = False).head(10))
    .encode(
        x = 'spaceflight_ratio:Q',
        y = 'Name'
    )
    .mark_bar()
    .properties(width = 800))

male_spaceflight_Chart

### My second question is: what years had the most female and male astronauts?
### This code groups female data that has the same value for year

female_data.groupby("Year").count()["Name"]

### The code below creates a chart showing the female year data we got eralier

female_chart = (alt.Chart(female_data)
    .encode(
        x = 'Year:O',
        y = 'count()'
    )
    .mark_bar()
    .properties(width = 800))

female_chart

### This code groups male data that has the same value for year

male_data.groupby("Year").count()["Name"]

### The code below creates a chart showing the male year data we got eralier

male_chart = (alt.Chart(male_data)
    .encode(
        x = 'Year:O',
        y = 'count()'
    )
    .mark_bar()
    .properties(width = 800))

male_chart

### My third question is: what are the average spacewalk hours for all the female and male astronauts? 
### The code below gets the average space walk hours for all the female astronauts 

female_average_hours = female_data["Space Walks (hr)"].mean()
female_average_hours

### The code below gets the average space walk hours for all the male astronauts

male_average_hours = male_data["Space Walks (hr)"].mean()
male_average_hours

### My fourth question is: what major is best to become an astronaut? 
### This code will calculate the percentage for each major by dividing by the number of astronauts and multiply it by 100

percent = (astronauts_data.groupby("Undergraduate Major").count() / len(astronauts_data) * 100)['Name'].sort_values()
percent