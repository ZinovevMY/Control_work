from datetime import *
from model.Note import Note
from model.Repository import Repository
from view.Editnote import Editnote


class Controller:
    def __init__(self, note_repo: Repository):
        self.__note_repo = note_repo

    @classmethod
    def id_validate(cls, id: str):
        try:
            int_id = int(id)
            if int_id>= 0:
                return True
        except:
            print("Неверный формат ID!")
            return False


    @staticmethod
    def search_by_id(note_id: str, notes: list[Note]):
        for note in notes:
            if note_id == note.get_id():
                return note

    def get_note_id(self):
        return input('Введите ID заметки: ')

    def read_all_notes(self):
        return self.__note_repo.read_all_notes()

    def add_new_note(self):
        note =
        self.__note_repo.add_new_note()

    def overwrite_all_notes(self, notes: list[Note]):
        self.__note_repo.overwrite_all_notes(notes)

    def get_note_by_id(self):
        notes = self.read_all_notes()
        note_id = self.get_note_id()
        if self.id_validate(note_id):
            return self.search_by_id(note_id, notes)

    def delete_note_by_id(self):
        notes = self.read_all_notes()
        note_id = self.get_note_id()
        if self.id_validate(note_id):
            for note in notes:
                if note_id == note.get_id():
                    notes.remove(note)
            self.overwrite_all_notes(notes)

