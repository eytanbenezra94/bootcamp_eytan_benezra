import numpy as np
import pandas as pd


def add_spend_income_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """Add monthly_spend / income as a proportionality feature."""
    df = df.copy()
    df['spend_income_ratio'] = df['monthly_spend'] / df['income']
    return df


def add_log_income(df: pd.DataFrame) -> pd.DataFrame:
    """Add log(income) to reduce right-skew."""
    df = df.copy()
    df['log_income'] = np.log(df['income'])
    return df


def add_region_frequency(df: pd.DataFrame, column: str = 'region') -> pd.DataFrame:
    """Frequency-encode a categorical column (no assumed ordering)."""
    df = df.copy()
    df[f'{column}_freq'] = df[column].map(df[column].value_counts(normalize=True))
    return df