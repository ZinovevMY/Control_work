from datetime import *
from model.Note import Note
from model.Notemapper import Notemapper
from model.Fileoperations import Fileoperations


class Repository:

    def __init__(self, file:Fileoperations, mapper:Notemapper):
        self.__file = file
        self.__mapper = mapper

    def read_all_notes(self):
        all_notes = []
        file_all_data = self.__file.read_all_data()
        for line in file_all_data:
            note = self.__mapper.load_map(line)
            all_notes.append(note)

        return all_notes

    def overwrite_all_notes(self, notes:list[Note]):
        input_data = []
        for note in notes:
            line_in_file = self.__mapper.save_map(note)
            input_data.append(line_in_file)

        self.__file.overwrite_file(input_data)

    def add_new_note(self, new_note:Note):
        all_notes = self.read_all_notes()
        max_value = 0
        for note in all_notes:
            note_id = int(note.get_id())
            if max_value < note_id:
                max_value = note_id
        new_note_id = max_value + 1
        new_note.set_id(new_note_id)
        new_note.set_date(datetime.now())

        all_notes.append(new_note)
        self.overwrite_all_notes(all_notes)
