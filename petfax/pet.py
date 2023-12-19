from flask import Blueprint, render_template

import json 

pets = json.load(open('pets.json'))
print(pets)


bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

@bp.route('/kiko')
def show_kiko():
    kiko = get_pet_data('Kiko')
    return render_template('show_kiko.html', pet=kiko)

@bp.route('/thumper')
def show_thumper():
    thumper = get_pet_data('Thumper')
    return render_template('show_thumper.html', pet=thumper)

@bp.route('/max')
def show_max():
    max = get_pet_data('Max')
    return render_template('show_max.html', pet=max)

@bp.route('/create_fact', methods=['GET', 'POST'])
def create_fact():
    if request.method == 'POST':
        pass
    return render_template('create_fact.html')







