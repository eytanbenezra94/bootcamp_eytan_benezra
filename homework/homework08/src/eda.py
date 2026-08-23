import pandas as pd


def eda_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return a one-row-per-column summary: dtype, missing %, unique count,
    and (for numeric columns) mean/std. Quick first look at any dataset.
    """
    summary = pd.DataFrame({
        'dtype': df.dtypes,
        'missing_pct': (df.isna().mean() * 100).round(2),
        'n_unique': df.nunique(),
    })
    numeric_cols = df.select_dtypes(include='number').columns
    summary['mean'] = df[numeric_cols].mean().reindex(summary.index)
    summary['std'] = df[numeric_cols].std().reindex(summary.index)
    return summary