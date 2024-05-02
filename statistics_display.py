from matplotlib import pyplot as plt


def stat_output_as_img(stat_output_str, title_str):
    # stat_output_str caan be the anova_table or tukey_interaction
    fig, ax = plt.subplots(figsize=(12, 6))
    table_output = str(stat_output_str)
    ax.text(0, 1, table_output, fontfamily='monospace', fontsize=15,
            verticalalignment='top')
    ax.axis('off')
    ax.set_title(title_str, fontsize=15, y=1,
                 horizontalalignment='right')  # Adjust the
    # y parameter to control title position

    plt.tight_layout()