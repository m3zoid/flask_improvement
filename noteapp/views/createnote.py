from flask import Blueprint, render_template, request, redirect
import os.path
import random
import time


bp = Blueprint(__name__, __name__, template_folder='templates')

def random_string(lenght=16):
    final_string = '{}_'.format(int(time.time()))
    chars = 'abcdefghijklmnopqrstuvxyz0123456789'
    for i in range(0, lenght):
        final_string += chars[random.randint(0, len(chars) - 1)]

    return final_string

@bp.route('/createnote', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        if request.form.get('createnote'):
            text = request.form.get('notetext')
            path = os.path.join('noteapp', 'notes', '{}.note'.format(random_string()))
            with open(path, 'w+') as _file:
                _file.write(text)

            return redirect('/')

    return render_template('createnote.html')