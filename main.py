import pandas as pd
from data.cleaning import clean_and_merge

joined_data = clean_and_merge("data/Average ACT scores and percentage of graduates taking the ACT by state 2017 and 2021.csv",
                              "data/expenditures per pupil by public schools 2017 via Nation Center for Education Statistics.csv",
                              "State")

year_data = joined_data[joined_data["Year"] == 2017]
filtered_data = year_data[[
    'State', 'Composite score', 'English score', 'Mathematics score',
    'Reading score', 'Science score', 'All districts',
    'Low-poverty districts', 'Low-middle poverty districts',
    'High-middle poverty districts', 'High-poverty districts'
    ]]
filtered_data.to_csv("data/filtered_data.csv", index=False)