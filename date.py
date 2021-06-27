import sys
from file_reader import FileReader
from eariliest_date_creator import EarliestDateCreator


if __name__ == "__main__":

    try:
        file_name = sys.argv[1]

        r = FileReader(file_name)
        numbers = r.read_file()

        earliest_date_creator = EarliestDateCreator(numbers)
        print(earliest_date_creator.get_earliest_date())

    except IndexError:
        print("Please input a file path")
