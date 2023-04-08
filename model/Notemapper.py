from model.Note import Note


class Notemapper:

    def __init__(self):
        pass

    def load_map(self, line: list):
        note = Note(id=line[0], header=line[1],text=line[2],date=line[3])
        return note

    def save_map(self, note: Note):
        file_record = [note.get_id(), note.get_header(), note.get_text(), note.get_date()]
        return file_record