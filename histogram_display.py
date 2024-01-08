import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def plot_lines(file_names, line_labels, color, label_prefix,
               bin_start_column='bin_start', count_column='count'):
    # Lines plot here are actually the histogram. Since I have lots of
    # histograms to plot, I plot them as lines to save space below the lines
    dfs = []

    # Read each file into a DataFrame and append it to the list
    for file_name, line_label in zip(file_names, line_labels):
        df = pd.read_csv(file_name)
        dfs.append(df)
        plt.plot(df[bin_start_column], df[count_column], color=color)


def display_all_histogram_as_line_plots(input_csv_files_list,
                                        split_filename_components_list, xlim_min,
                                        xlim_max, ylim_min, ylim_max,
                                        color_lists=['red', 'green', 'blue', 'orange',
                                       'purple', 'brown', 'pink', 'gray']):
    filtered_files_lists_dict = {}
    line_labels_lists_dict = {}

    for split_filename_component in split_filename_components_list:
        filtered_files_list = [file_name for file_name in input_csv_files_list
                               if
                               split_filename_component in file_name]
        filtered_files_lists_dict[
            split_filename_component] = filtered_files_list

        line_labels_list = [
            '{} Line {}'.format(split_filename_component, i + 1) for i in
            range(len(filtered_files_list))]

    # Plot lines for each group on the same plot
    plt.figure(figsize=(8, 6))

    plt.xlim(xlim_min, xlim_max)  # Set the x-axis limits
    plt.ylim(ylim_min, ylim_max)  # Set the y-axis limits

    color_counter = 0
    legend_lines_list = []
    for split_filename_component, filtered_files_list in filtered_files_lists_dict.items():
        # Plot lines for each group
        plot_lines(filtered_files_list, line_labels_list, color=color_lists[
            color_counter],
                   label_prefix=split_filename_component)

        # Create a custom legend with separate Line2D instances
        legend_lines_list.append(Line2D([0], [0], color=color_lists[
            color_counter], label=split_filename_component))

        # Change to another color
        color_counter += 1

        if color_counter > len(color_lists) - 1:
            print('You have run out of colors. Add more colors!')

    plt.xlabel('Bin start value')
    plt.ylabel('Count')
    plt.title(
        'Line Plots for Different Groups Resembling Histograms')

    legend = plt.legend(handles=legend_lines_list, frameon=True,
                        facecolor='white')
    legend.get_frame().set_edgecolor('black')  # Set legend border color

    plt.show()
