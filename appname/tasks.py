from celery import shared_task
from .models import Heroe
import requests

@shared_task
def update_data():
    input_model = [
        "id_external",
        "name",
        "intelligence",
        "strength",
        "speed",
        "durability",
        "power",
        "combat",
        "race",
        "gender",
        "alignment"
    ]
    data_out = [
        "id",
        "name",
        "powerstats.intelligence",
        "powerstats.strength",
        "powerstats.speed",
        "powerstats.durability",
        "powerstats.power",
        "powerstats.combat",
        "appearance.race",
        "appearance.gender",
        "biography.alignment"
    ]
    data = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")
    data = data.json()
    heros_to_save = []
    for hero in data:
        index = 0
        data_save = {}
        for lookup in data_out:
            value = hero
            for campo in lookup.split('.'):
                value = value[campo]
            data_save[input_model[index]] = value
            index = index + 1
        heros_to_save.append(Heroe(**data_save))
    Heroe.objects.all().delete()
    Heroe.objects.bulk_create(heros_to_save)
    print("se ejecuto")
    return True