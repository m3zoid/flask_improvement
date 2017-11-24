from flask import Blueprint, render_template
import os.path
import glob


bp = Blueprint(__name__, __name__, template_folder='templates')

def fetch_notes():
    final_notes = []
    notes = glob.glob(os.path.join('noteapp', 'notes', '*.note'))
    for note in notes:
        with open(note) as _file:
            final_notes.append(_file.read())

    return reversed(final_notes)

@bp.route('/')
def show():
    return render_template('index.html', notes=fetch_notes())