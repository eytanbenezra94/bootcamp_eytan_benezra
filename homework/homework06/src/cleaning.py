import pandas as pd


def fill_missing_median(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Fill missing values in the given numeric columns with their median.

    Assumptions: columns are numeric; median is a reasonable stand-in
    for missing values without being skewed by outliers (unlike mean).
    """
    df = df.copy()
    for col in columns:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)
    return df


def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """Drop columns where the fraction of missing values exceeds threshold.

    Assumptions: a column missing more than `threshold` of its values
    is too sparse to be reliably imputed and is better dropped than filled.
    """
    df = df.copy()
    missing_frac = df.isna().mean()
    cols_to_drop = missing_frac[missing_frac > threshold].index
    return df.drop(columns=cols_to_drop)


def normalize_data(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Min-max normalize the given numeric columns to a 0-1 range.

    Assumptions: columns are numeric with no remaining missing values
    (run fill_missing_median or drop_missing first); min != max.
    """
    df = df.copy()
    for col in columns:
        col_min = df[col].min()
        col_max = df[col].max()
        if col_max != col_min:
            df[col] = (df[col] - col_min) / (col_max - col_min)
        else:
            df[col] = 0.0
    return df