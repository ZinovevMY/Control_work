from datetime import *


class Editnote:

    def __init__(self):
        pass

    def note_editor(self):
        note = []
        i = 0
        while i < 3:
            match i:
                case 0:
                    header = input('Тема заметки: ')
                    note.append(header)
                case 1:
                    text = input('Текст заметки: ')
                    note.append(text)
                case 2:
                    dtm = datetime.now()
                    note.append(dtm)
            i += 1
        return note


