from datetime import *
from model.Note import Note
from model.Repository import Repository


class Controller:
    def __init__(self, note_repo: Repository):
        self.__note_repo = note_repo

    def save_note(self, note: Note):
        self.__note_repo.add_new_note(note)

    def read_note(self, note_id: str):
        notes = self.__note_repo.read_all_notes()
        note = self.search_note(note_id, notes)
        return note

    def search_note(self, note_id: str, notes: list[Note]):
        for item in notes:
            if item.get_id() == note_id:
                return item
        print("Записи с таким ID не найдено!")

    def read_all_notes(self):
        return self.__note_repo.read_all_notes()

    def update_note(self, note_id: str, new_note: Note):
        notes = self.read_all_notes()
        note = self.search_note(note_id, notes)
        note.set_header(new_note.get_header())
        note.set_text(new_note.get_text())
        note.set_date(new_note.get_date())
        self.__note_repo.overwrite_all_notes(notes)

    def delete_note(self, note_id: str):
        notes = self.read_all_notes()
        self.__note_repo.delete_note(note_id, notes)
        self.__note_repo.save_note(notes)

    def delete_all_notes(self):
        notes = self.read_all_notes()
        for note in notes:
            notes.remove(note)
        self.__note_repo.overwrite_all_notes(notes)
