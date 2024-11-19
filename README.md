# WHO-Global-Observatory

WHO makes an extremely large amount of data available to the public - we work on the Life Expectancy and Healthy Life Expectancy Data

Extracting data from .csv files (obtained from WHO) - Data munging, cleaning and arranging it into dataframes (DF) using NumPandas

- New Dataframe object is further saved to a file using the command .to_pickle


Generated a pandas Dataframe based on the raw data provided

- Corrected the headers: Reassigned the names of columns as follows
  - Use “Country” and “Year” for the first two columns
  - For the remaining columns, Use the following format: Measure + Year + M/F, where Measure is either “LE” or “HALE”, Year is either 0 or 60, and M/F is optional for Male/Female only data, or blank for columns giving universal data. Two examples would then be “LE0” and “HALE60F”


- Use the pivot function to create a new DataFrame object, with an index corresponding to “Country”, columns for each “Year”, and values assigned using the “LE0” column.
 
- Add a column called ‘Mean’ and fill it with the average life expectancy for each Country across all available data. Skip missing data. Also create columns for ‘Max’, ‘Min’, and ’Std’ and fill them with appropriate values.
