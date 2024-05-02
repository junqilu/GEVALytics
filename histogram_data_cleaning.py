import numpy as np
import matplotlib.pyplot as plt

from basic_functions import int_to_ordinal_str


def histogram_df_to_series(input_df):
    output_series = np.repeat(input_df['bin_start'],
                              input_df['count'].astype(int))

    return output_series


def filter_series_by_iqr(input_series, starting_quantile=0.25,
                         ending_quantile=0.75,
                         iqr_multiplication_factor=1.5):
    # Usually the IQR method is using an IQR defined by the 25th and 75th
    # quantile, so it's set as the default quantiles; by default, you time the
    # IQR by 1.5 and anything outside that range is considered as outliers

    # Calculate the first and third quartiles
    Q1 = input_series.quantile(starting_quantile)
    Q3 = input_series.quantile(ending_quantile)

    # Calculate the interquartile range (IQR)
    IQR = Q3 - Q1

    # Define the lower and upper bounds for outliers
    lower_bound = Q1 - iqr_multiplication_factor * IQR
    upper_bound = Q3 + iqr_multiplication_factor * IQR

    # Filter values within the interquartile range
    filtered_series = input_series[
        (input_series >= lower_bound) & (input_series <= upper_bound)]
    return filtered_series


def series_to_histogram_df(input_series):
    output_df = input_series.value_counts().reset_index()  # Count the
    # occurrences of each unique value in the Series

    output_df.columns = ['bin_start',
                         'count']  # Rename the columns to 'bin_start' and
    # 'count'

    output_df = output_df.sort_values(
        by='bin_start')  # Sort the DataFrame by 'bin_start'

    output_df = output_df.reset_index(
        drop=True)  # Reset the index and drop the existing index

    return output_df


def filter_df_by_IQR(input_df, starting_quantile=0.25, ending_quantile=0.75,
                     iqr_multiplication_factor=1.5):
    original_series = histogram_df_to_series(input_df)

    filtered_series = filter_series_by_iqr(original_series, starting_quantile,
                                           ending_quantile,
                                           iqr_multiplication_factor)

    filtered_df = series_to_histogram_df(filtered_series)

    return filtered_df


def plot_original_vs_filtered_worker(original_df, filtered_df,
                                     starting_quantile=0.25,
                                     ending_quantile=0.75,
                                     iqr_multiplication_factor=1.5):
    plt.figure(figsize=(10, 6))

    # Plot the original histogram
    plt.plot(
        original_df['bin_start'],
        original_df['count'],
        linestyle='-',
        color='blue',
        label='Original histogram'
    )

    # Plot the filtered histogram
    plt.plot(
        filtered_df['bin_start'],
        filtered_df['count'],
        linestyle='--',
        color='orange',
        label='Filtered histogram by IQR'
    )

    # Color the area below both line plots
    plt.fill_between(
        original_df['bin_start'],
        original_df['count'],
        alpha=0.2,
        color='blue',
    )

    plt.fill_between(
        filtered_df['bin_start'],
        filtered_df['count'],
        alpha=0.2,
        color='orange'
    )

    plt.title('Original vs. filtered histogram data')
    plt.xlabel('Value')
    plt.ylabel('Count')

    plt.legend()  # Add a legend

    quantile_str_list = []
    for quantile_float in [starting_quantile, ending_quantile]:
        quantile_str_list.append(
            int_to_ordinal_str(round(quantile_float * 100)))

    iqr = ending_quantile - starting_quantile

    caption = 'Histogram data was cleaned of outliers by IQR method with\n' \
              'starting ' \
              'quantile as {}, ending quantile as {},\nIQR as {}, and IQR ' \
              'multiplication ' \
              'factor as {}'.format(
        quantile_str_list[0],  # str for starting_quantile
        quantile_str_list[1],  # str for ending_quantile
        '{:.2f}'.format(iqr),
        iqr_multiplication_factor)

    plt.text(
        0,
        -0.15,
        caption,
        ha='left',
        va='center',
        transform=plt.gca().transAxes,
        bbox=dict(
            facecolor='lightgray',
            alpha=0
        )
    )

    plt.show()


def plot_original_vs_filtered(original_df, starting_quantile=0.25,
                              ending_quantile=0.75,
                              iqr_multiplication_factor=1.5, plot_show=True):
    filtered_df = filter_df_by_IQR(original_df, starting_quantile,
                                   ending_quantile,
                                   iqr_multiplication_factor)

    if plot_show == True: # Only show the plot when the user wants to see
        # it. You need to set this to False when processing lots of csv
        # files in a batch mode. Otherwise, you'll have lots of plots
        plot_original_vs_filtered_worker(original_df, filtered_df,
                                         starting_quantile,
                                         ending_quantile,
                                         iqr_multiplication_factor)

    return filtered_df
