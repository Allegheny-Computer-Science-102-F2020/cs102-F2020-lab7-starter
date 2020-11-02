"""Extract the data."""

# TODO: Import the modules for typing and for CSV parsing

# Sample of the data set:

# tylernelson@gmail.com,Careers adviser
# gregory02@medina-mayer.com,"Accountant, chartered management"
# jonesmiguel@hotmail.com,Health and safety inspector
# rsanchez@yahoo.com,"Surveyor, planning and development"
# hillfrank@ward-wood.com,"Scientist, physiological"
# aaronhunter@gmail.com,"Surveyor, insurance"
# kylebarnes@hotmail.com,Records manager
# joe70@yahoo.com,Network engineer
# torresjames@white.info,Electrical engineer
# shawkins@watson.com,Science writer


def extract_data_given_column(data: str, column: int) -> List[str]:
    """Extract a specified data column from the provided textual contents."""
    # create an empty list of the data
    # note that the data file:
    # --> contains two columns
    # --> each of which contains textual data
    data_list = []
    # --> refer to the file called inputs/contacts.txt to learn more about
    # the format of the comma separated value (CSV) file that we must parse
    # --> iterate through each line of the file and extract the current job
    for line in csv.reader(
        data.splitlines(),
        quotechar='"',
        delimiter=",",
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True,
    ):
        # extract the specified column that contains the requested data
        current_column_value = line[column]
        data_list.append(current_column_value)
    # return the list of all of the specified column
    return data_list
