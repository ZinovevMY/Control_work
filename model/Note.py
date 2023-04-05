class Note:

    def __init__(self, note_id, note_header, note_text, note_date):
        self.__note_id = note_id
        self.__note_header = note_header
        self.__note_text = note_text
        self.__note_date = note_date

    def get_note_id(self):
        return self.__note_id

    def get_note_text(self):
        return self.__note_text

    def get_note_header(self):
        return self.__note_header

    def get_note_date(self):
        return self.__note_date

    def set_note_text(self, note_text):
        self.__note_text = note_text

    def set_note_header(self, note_header):
        self.__note_header = note_header

    def set_note_date(self, note_date):
        self.__note_date = note_date
