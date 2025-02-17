import csv
import pandas as pd
import os
import matplotlib.pyplot as plt

def process_csv(file_path):
    data = []
    
    
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
            
     
    df = pd.DataFrame(data)
    
    return df

# Usage
#cls
# print(os.getcwd())
script_dir = os.path.dirname(os.path.abspath('data.csv'))
file_path = os.path.join(script_dir, 'data.csv')

df = process_csv(file_path)

df1 = df

print(df.head())
print('===========')
print(df.head(1))
print('===========')
print(df.tail(1))
print('===========###')
#Provides a summary of the DataFrame, including the number of non-null 
# values and data types.
print(df.info())
print('===========')
#Generates descriptive statistics of numeric columns 
# (count, mean, std, min, max, etc.).
print(df.describe())
print('===========')
#Returns the number of rows and columns as a tuple (n_rows, n_columns).
print(df.shape)
print('===========')
#Returns the column names of a DataFrame.
print(df.columns)
print('===========')
#Returns the data types of each column in the DataFrame.
print(df.dtypes)
print('===========')
#Sets one of the DataFrame columns as the index.
print(df.set_index('ID'))
print('===========')
#Sets one of the DataFrame columns as the index.
print(df.set_index('count'))
print('===========')
#Resets the index of the DataFrame, reverting back to the default integer index.
print(df.reset_index())
print('===========')
#Drops specific rows or columns from a DataFrame.
df = df.drop('ID', axis=1)  # Drop a column
print(df)
df = df.drop([0, 1], axis=0)  # Drop rows with indices 0 and 1
print(df)
print('===========')
#Renames columns or rows
print(df.rename(columns={'name': 'Name'}))
print('===========')
df= df1
print(df)
print('===========')
#Sorts the DataFrame by one or more columns
print(df.sort_values(by='count', ascending=False))
print('===========')
#Filters columns by a specified condition 
# (e.g., selecting columns with specific substrings).
print(df.filter(like='co', axis=1))
print('===========')
#Applies a function along a DataFrame axis (rows or columns).
df['Identity'] = df['count'].apply(lambda x: x * 2)
print(df)
df['Identity1'] = df['ID'].apply(lambda x: x * 2)
print(df)
print('===========')
#Aggregates the DataFrame with one or more functions (e.g., sum, mean, max, etc.).
print(df.agg({'ID': 'max'}))
print('===========')
#Groups the DataFrame by a specific column and performs aggregation operations.
print(df.groupby('count').agg({'name': 'max'}))
print('===========')
#Merges two DataFrames on a specific column, similar to SQL joins.
print(df)
print(df1)
print(pd.merge(df1, df, on='ID', how='inner'))
print(pd.merge(df1, df, on='ID', how='inner'))
print('===========')
#Concatenates two or more DataFrames along a particular axis (rows or columns).
print(pd.concat([df1, df], axis=0)) # Concatenate vertically (row-wise) 8 rows
print(pd.concat([df1, df], axis=1)) # Concatenate horizontally (column-wise) 8 columns
print('===========')
#Creates a pivot table for the DataFrame with specified values, rows, and columns.
print(df.pivot_table(index='count', aggfunc='max'))
print('===========')
#Checks for missing values in the DataFrame.
print(df.isnull())  # Returns a DataFrame of boolean values (True for NaN)
print(df.notnull())  # Returns a DataFrame of boolean values (True for non-NaN)
print('===========')
#Fills missing values (NaN) with a specified value or method.
print(df.fillna(0))  # Fill NaN with 0
print('===========')
#Removes rows or columns with missing values.
print(df.dropna())   # Drop rows with any NaN values
print('===========')
#Checks for duplicate rows.
print(df.duplicated())  # Returns a boolean Series indicating duplicate rows
print('===========')
#Returns the unique values of a specific column.
print(df['count'].unique())  
print('===========')
#Returns the count of unique values in a specific column
print(df['count'].value_counts())  
print('===========')
#Shifts the values of a column by a specified number of periods.
print(df1['count'].shift(0))  # Shift values down by 0
print(df1['count'].shift(1))  # Shift values down by 1
print(df1['count'].shift(2))  # Shift values down by 2
print('===========')
#Generates a cross-tabulation of two or more columns.
print(df)
print(pd.crosstab(df['count'], df['name'])) 
print(pd.crosstab(df['ID'], df['name'])) 
print(pd.crosstab(df['ID'], df['count'])) 
print('===========')
#Accesses a group of rows and columns by labels (loc) or positions (iloc).
# select columns from the csv
df_loc = df.loc[0:10, ['ID', 'name']]  # By label
print(df_loc)
df_iloc = df.iloc[0:10, [0, 1]]  # By position
print(df_iloc)
print('===========')
#Returns the top n largest values from a specific column.
#following line is needed to resolve
#error has dtype object, cannot use method 'nlargest' with this dtype
df['ID'] = pd.to_numeric(df['ID'], errors='coerce')
df_largest = df.nlargest(2, 'ID')
print(df_largest)
print('===========')
#Returns the top n smallest values from a specific column.
#once converted the column need not be transformed again 
df_smallest = df.nsmallest(2, 'ID')
print(df_smallest)
print('===========')
#Transposes the DataFrame (rows become columns and vice versa).
print(df)
df_transposed = df.transpose()
print(df)
print('===========')
#Converts a DataFrame to a NumPy array. //it will be two dimensional array 
array = df.to_numpy()
print(array)
print('===========')
#Converts a DataFrame to a dictionary.
dict_df = df.to_dict()
print(dict_df)
print('===========')
# Create a MultiIndex with tuples
arrays = [
    ['A', 'A', 'B', 'B'],
    [1, 2, 1, 2]
]
print(arrays)
index = pd.MultiIndex.from_arrays(arrays, names=('letter', 'number'))
print(index)
# Creating DataFrame with MultiIndex
df = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], columns=['col1', 'col2'], index=index)
print(df)
#==========
def get_data():
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    return df, "Dataframe fetched successfully"

data, message = get_data()
print(data)
print(message)
#==========
df1.hist(column='ID', bins=3, alpha=0.7, color='green', label='Age Distribution')
print(df1)
plt.xlabel('ID')
plt.ylabel('count')
plt.legend()
plt.show()