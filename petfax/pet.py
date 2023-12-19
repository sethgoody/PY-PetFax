from flask import Blueprint, request, render_template, redirect, url_for
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

@bp.route('/<int:pet_id>')
def show_pet(pet_id):
    pet = get_pet_data(pet_id)
    if pet:
        return render_template('show_pet.html', pet=pet)
    else:
        return "Pet not found", 404

def get_pet_data(pet_id):
    for pet in pets:
        if pet['pet_id'] == pet_id:
            return pet
    return None


@bp.route('/create_fact', methods=['GET', 'POST'])
def create_fact():
    if request.method == 'POST':
        name = request.form.get('name')
        fact = request.form.get('fact')

        print(f"Name: {name}, Fact: {fact}")

        return redirect(url_for('pet.index'))

    return render_template('create_fact.html')
