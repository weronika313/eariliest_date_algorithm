import sys
from file_reader import FileReader
from eariliest_date_creator import EarliestDateCreator


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_name = sys.argv[1]

    if len(file_name) <= 0:
        print("Please input a file path")
        exit(-1)

    r = FileReader(file_name)
    numbers = r.read_file()

    earliest_date_creator = EarliestDateCreator(numbers)
    print(earliest_date_creator.get_earliest_date())