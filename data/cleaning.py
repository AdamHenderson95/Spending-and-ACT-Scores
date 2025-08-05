import pandas as pd

def clean_and_merge(file1, file2, column):
    """
    Parameters:
        file1: path to first CSV file (str)
        file2: path to second CSV file (str)
        column: column name to merge on (e.g., 'State')

    Returns:
        Cleaned, merged DataFrame with numeric conversions and NaNs filled.
    """

    def clean_dataframe(df):
        # Clean all object (string) columns
        for col in df.select_dtypes(include='object').columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(r'[$,",\'†]', '', regex=True)  # remove unwanted symbols
                .str.strip()
            )

        # Convert all columns to numeric where possible
        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col])
            except Exception:
                pass  # leave as string if conversion fails

        # Fill NaNs in numeric columns with column mean
        df = df.fillna(df.mean(numeric_only=True))

        return df

    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    df1 = clean_dataframe(df1)
    df2 = clean_dataframe(df2)

    # Strip and normalize the merge column
    if column in df1.columns:
        df1[column] = df1[column].str.strip()
    if column in df2.columns:
        df2[column] = df2[column].str.strip()

    merged_df = pd.merge(df1, df2, on=column)

    # Standardize column names: remove newlines and collapse multiple spaces
    merged_df.columns = (
        merged_df.columns
        .str.replace(r'\n', ' ', regex=True)
        .str.replace(r'\s+', ' ', regex=True)  # collapse double spaces
        .str.strip()
    )

    return merged_df

