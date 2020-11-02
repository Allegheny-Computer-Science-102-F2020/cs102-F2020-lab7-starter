"""Define the command-line interface for the datauniquifier program."""

from pathlib import Path

import os
import psutil

from resource import getrusage, RUSAGE_SELF

import typer

from datauniquifier import analyze
from datauniquifier import extract
from datauniquifier import uniquify

UNIQUE_FUNCTION_BASE = "unique"
UNDERSCORE = "_"


def main(
    approach: str = typer.Option(...),
    column: int = typer.Option(...),
    data_file: Path = typer.Option(...),
    display: bool = typer.Option(False, "--display"),
):
    """Create the list of data values in stored in the specified file and then uniquify the file contents."""
    # display the debugging output for the program's command-line arguments
    typer.echo("")
    typer.echo(f"The chosen approach to uniquify the file is: {approach}")
    typer.echo("")
    typer.echo(f"The data file that contains the input is: {data_file}")
    typer.echo("")
    # TODO: construct the full name of the function to call
    function = ""
    # TODO: construct the requested function from the compute module
    # Reference: https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
    function_to_call = ""
    # declare the variables that will store file content for a valid file
    data_text = ""
    data_column_text_list = []
    # --> the file was not specified so we cannot continue using program
    if data_file is None:
        typer.echo("No data file specified!")
        raise typer.Abort()
    # --> the file was specified and it is valid so we should read and check it
    if data_file.is_file():
        data_text = data_file.read_text()
        data_line_count = len(data_text.splitlines())
        typer.echo(f"The data file contains {data_line_count} data values in it!")
        typer.echo("Let's do some uniquification! 🚀")
        typer.echo("")
        # display a final message and some extra spacing, asking a question
        # about the efficiency of the approach to computing the number sequence
        typer.echo("So, was this an efficient approach to uniquifying the data? 🔍")
        typer.echo("")
        data_column_text_list = extract.extract_data_given_column(data_text, column)
    # TODO: call the constructed function and capture the result
    unique_result_list = ""
    typer.echo("")
    # display debugging information with the function's output
    if display:
        typer.echo(f"  This is the output from using the {approach}:")
        typer.echo("")
        typer.echo("   " + str(unique_result_list))
        typer.echo("")
    process = psutil.Process(os.getpid())
    # TODO: display the estimated overall memory use as reported by the operating system
    # Reference:
    # https://stackoverflow.com/questions/938733/total-memory-used-by-python-process
    # TODO: display the estimated peak memory use as reported by the operating system
    # Reference:
    # https://pythonspeed.com/articles/estimating-memory-usage/
    # Display the percent reduction that is a result of the uniquification process
    typer.echo("")
    typer.echo("So, did this remove a lot of duplicate data? 🔍")
    typer.echo("")
    reduction = analyze.calculate_reduction(data_column_text_list, unique_result_list)
    percent_reduction = analyze.calculate_percent_reduction(
        data_column_text_list, unique_result_list
    )
    typer.echo(f"The number of values removed from the data: {reduction}")
    typer.echo(f"The percent reduction due to uniquification: {percent_reduction:.2f}%")
    typer.echo("")


if __name__ == "__main__":
    typer.run(main)
