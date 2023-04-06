from datetime import *


class Note:

    def __init__(self, id: str = "", header: str = "", text: str = "", date: datetime = ""):
        self.__id = id
        self.__header = header
        self.__text = text
        self.__date = date

    def get_id(self):
        return self.__id

    def get_text(self):
        return self.__text

    def get_header(self):
        return self.__header

    def get_date(self):
        return self.__date

    def set_text(self, note_text):
        self.__text = note_text

    def set_header(self, note_header):
        self.__header = note_header

    def set_date(self, note_date):
        self.__date = note_date

    def __str__(self):
        return f"Номер заметки: {self.__id}\nТема: {self.__header}\nТекст заметки:\n{self.__text}\n" \
               f"Дата создания/изменения: {self.__date}"
