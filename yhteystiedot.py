"""
Contacts

In this program, a semicolon will be used as the separator character of CSV
format input files. The separator character could also be any other
character. The program reads the contact information from a file that contains
the contact information in CSV-format so that the first line contains the titles
of the columns. The information can be accessed from dict by the title of the 
CSV-file column. The information can be accessed by the key presented in the 
first column of the line.

Writer of the program: EILeh

"""

def read_file(input_filename):
    """Create a dictionary with individual contact information
       contained in nested dictionaries.

    :param input_filename: str, the name of the CSV-file
                           the information extracted from.
    :return: dict, the created dictionary with categorized contact information.
    """
    
    data_file = open(input_filename, mode="r")

    info = {}
    count = 0
    individual_info_keys = ""

    # Goes through every line in the file.
    for line in data_file:
        line = line.rstrip()

        individual_info = {}

        # If count is zero, then splitting from the ";" gets you the keys.
        if count == 0:
            individual_info_keys = line.split(";")

        else:
            parts = line.split(";")

            # Goes through the parts after the index 0.
            for index in range(1, len(parts)):

                # Creates a new key-value pair where the value is a nested
                # dictionary;
                # - individual_info = line
                # - individual_info_keys = the key that can be used to search
                # the wanted information
                # - index = what do you want to search
                # - parts = everything on a line except the key
                individual_info[individual_info_keys[index]] = parts[index]

                # info at parts at index zero contains the key and the
                # individual_info contains the keys info as a nested dictionary.
                info[parts[0]] = individual_info

        count += 1

    return info


def main():

    info = read_file("contacts.csv")
    
    print(info["Mike"]["skype"])

if __name__ == "__main__":
    main()


