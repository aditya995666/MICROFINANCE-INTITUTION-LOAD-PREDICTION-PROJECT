import pandas as pd
import numpy as np
import re

def normalize_col(col):
    col = col.lower().strip()
    col = re.sub(r"[^\w]+", "_", col)
    return col

def match_columns(df, feature_columns):
    df.columns = [normalize_col(c) for c in df.columns]
    feature_map = {normalize_col(c): c for c in feature_columns}

    matched_df = {}

    for norm_col, original_col in feature_map.items():
        if norm_col in df.columns:
            matched_df[original_col] = df[norm_col]
        else:
            matched_df[original_col] = 0.0  

    return pd.DataFrame(matched_df)

def preprocess_input(df, feature_columns):

    df.columns = [normalize_col(c) for c in df.columns]

    df = match_columns(df, feature_columns)

    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.fillna(df.median(numeric_only=True))

    df = df[feature_columns]

    return df
