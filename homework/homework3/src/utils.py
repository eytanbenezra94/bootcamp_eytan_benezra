def get_summary_stats(df):
    """Return describe() stats and NA counts for a DataFrame."""
    return {
        "describe": df.describe(),
        "na_counts": df.isna().sum()
    }