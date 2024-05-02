import pandas as pd
import os
import re


def calculate_weighted_average(input_df, bin_start_column='bin_start',
                               count_column='count'):
    weighted_average = (input_df[bin_start_column] * input_df[
        count_column]).sum() / input_df[count_column].sum()
    return weighted_average


def calculate_weighted_median(input_df, bin_start_column='bin_start',
                              count_column='count'):
    # Flatten the DataFrame based on the count column
    flattened_data = pd.DataFrame({
        bin_start_column: input_df[bin_start_column].repeat(
            input_df[count_column]),
    })

    # Calculate the median from the flattened data
    median_value = flattened_data[bin_start_column].median()

    return median_value


def calculate_mode(input_df, bin_start_column='bin_start',
                   count_column='count'):
    max_count_row = input_df.loc[input_df[count_column].idxmax()]
    mode_value = max_count_row[bin_start_column]

    return mode_value


def csv_files_in_dir(input_dir_str, pattern=re.compile(r'\d{2}\.\d{2}\.\d{'
                                                         r'2}\.csv$')):
    # r'\d{2}\.\d{2}\.\d{2}\.csv$' is the regex pattern that end my image
    # files by default. It means a time stamp in short
    output_list = []
    for root, dirs, files in os.walk(input_dir_str):
        for file in files:
            if pattern.search(file):
                full_csv_file_dir = os.path.join(root, file)  # Obtain
                # the absolute directory for file
                output_list.append(full_csv_file_dir)

    return output_list


def process_single_csv(csv_file_dir):
    df = pd.read_csv(csv_file_dir)

    df = df[df['bin_start'] != 0]  # Remove the count if bin_start = 0. This
    # is because if the ratio of Ex405/Ex488 = 0, it doesn't have
    # physiological meaning

    try:  # Some files might have invalid values and this will skip those files
        mean_val = calculate_weighted_average(df, 'bin_start', 'count')
        median_val = calculate_weighted_median(df, 'bin_start', 'count')
        mode_val = calculate_mode(df, 'bin_start', 'count')
    except:
        print('File {} runs into error(s)!'.format(csv_file_dir))
    else:
        return pd.DataFrame({
            'csv_file_name': [os.path.abspath(csv_file_dir)],
            # Use .abspath() rather than .basename() so later if you want to
            # add additional labels to a big chunk of csv files, you can
            # just put them in a sub-folder with the label's string rather
            # than renaming all the csv files to contain that string for
            # having that information
            'mean': [mean_val],
            'median': [median_val],
            'mode': [mode_val]
        })


def extract_all_parameters_from_csv_files(csv_files_list,
                                          output_csv_saving_dir='output'
                                                                '\\meta_data'
                                                                '.csv'):
    parameter_df = pd.concat(
        [process_single_csv(file) for file in csv_files_list],
        ignore_index=True
    )

    parameter_df.to_csv(
        output_csv_saving_dir,
        index=False
    )  # Save the csv locally, so you can split on the csv_file_name column
    # into several meaningful columns

    print('meta_data.csv has been saved to {}. Label the data as you like '
          'locally using Excel before import it back for later steps!'.format(
        output_csv_saving_dir))

    return parameter_df
