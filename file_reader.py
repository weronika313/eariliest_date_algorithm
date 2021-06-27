class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.numbers = None

    def read_file(self):
        try:
            file = open(self.file_name, "r")
            self.numbers = file.readline()
            file.close()
            return self.numbers

        except FileNotFoundError:
            print(f"The file {self.file_name} doesn't exist")
        except PermissionError:
            print(f"You don't have permission to read this file {self.file_name}")
        except Exception as e:
            print(e)
