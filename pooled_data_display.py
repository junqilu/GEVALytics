import pandas as pd


def remove_outliers_by_group(df, group_cols_list, value_col):
    groups = df.groupby(group_cols_list)
    filtered_data = []

    for _, group in groups:  # Using the IQR method to get rid of outliers
        Q1 = group[value_col].quantile(0.25)
        Q3 = group[value_col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outlier_mask = (group[value_col] >= lower_bound) & (
                group[value_col] <= upper_bound)
        filtered_data.append(group[outlier_mask])

    return pd.concat(filtered_data)
