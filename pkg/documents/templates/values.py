from pkg.values_parser.values_section import read_and_print_values
from ...cmd.command_line import get_values_file, get_ignore_non_descriptions
import os


def get_chart_values_header():
    """
    Generates the markdown header for the 'Values' section.

    Returns:
        str: Markdown header for the 'Values' section.
    """
    values_header_markdown = "## Values\n\n"
    return values_header_markdown


def get_chart_values_table(chart_folder):
    """
    Generates markdown tables for the 'Values' section of the chart.

    Args:
        chart_folder (str): Path to the chart folder.

    Returns:
        str: Markdown tables representing the 'Values' section of the chart.
    """
    ignore_none_description = get_ignore_non_descriptions()

    values_path = get_values_file()  # Get the path to the values.yaml file from command line arguments
    values_path = os.path.join(chart_folder, values_path)  # Construct the full path to the values.yaml file
    values_tables = read_and_print_values(values_path,
                                          ignore_none_description)  # Read and print the values from the values.yaml file
    return values_tables


def get_chart_values_section(chart_folder):
    """
    Generates the complete markdown section for the 'Values' section of the chart.

    Args:
        chart_folder (str): Path to the chart folder.

    Returns:
        str: Complete markdown section for the 'Values' section of the chart.
    """
    values_section_markdown = f"{get_chart_values_header()}\n\n" + get_chart_values_table(chart_folder)
    return values_section_markdown
