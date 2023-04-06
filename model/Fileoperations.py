import csv


class Fileoperations:

    def __init__(self, file_name:str=""):
        self.__file_name = file_name + '.csv'
        new_file = open(f"{self.__file_name}", "a+")
        new_file.close()

    def overwrite_file(self, data:list[str]):
        with open(self.__file_name, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(data)

    def read_all_data(self):
        all_data = []
        with open(self.__file_name, "r", newline="") as file:
            all_notes = csv.reader(file, delimiter=";")
            for pos in all_notes:
                record = [pos[0], pos[1], pos[2], pos[3]]
                all_data.append(record)
        return all_data
