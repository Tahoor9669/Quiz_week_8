import sqlite3

# Connect to the database
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

# Define lists to store the data
years = []
temperatures = []
precipitation = []

# Fetch data from the database
cursor.execute("SELECT year, temperature, precipitation FROM climate_data")
data = cursor.fetchall()

for row in data:
    year, temp, precip = row
    years.append(year)
    temperatures.append(temp)
    precipitation.append(precip)

# Close the database connection
conn.close()

# Now you can use the 'years', 'temperatures', and 'precipitation' lists for plotting

# Example: Print the first 5 years and corresponding temperatures
print("Years:", years[:5])
print("Temperatures:", temperatures[:5])
