import pandas as pd

def clean_and_merge(file1, file2, column):
    """
    Parameters:
        file1 = file path to csv file in quotes
        file2 = file path to csv file in quotes
        column = column name of column to merge on
    Returns:
        a dataframe merged on the column "State" with null values replaced by averages
    """
    df1 = pd.read_csv(file1)
    df1 = df1.fillna(df1.mean(numeric_only=True))
    if column in df1.columns:
        df1[column] = df1[column].str.strip()

    df2 = pd.read_csv(file2)
    df2 = df2.fillna(df2.mean(numeric_only=True))
    if column in df2.columns:
        df2[column] = df2[column].str.strip()

    merged_df = pd.merge(df1, df2, on="State")
    merged_df.columns = merged_df.columns.str.replace('\n', ' ', regex=True).str.strip()
    return merged_df

