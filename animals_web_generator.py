import json
from html import escape


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Converts one animal into an HTML card."""
    name = escape(animal_obj["name"])
    characteristics = animal_obj["characteristics"]
    
    diet = escape(characteristics["diet"])
    location = escape(animal_obj["locations"][0])
    
    output = '<li class="cards__item">\n'
    output += f'    <div class="card__title">{name}</div>\n'
    output += '    <p class="card__text">\n'
    output += f'        <strong>Diet:</strong> {diet}<br/>\n'
    output += f'        <strong>Location:</strong> {location}<br/>\n'
    
    if "type" in characteristics:
        animal_type = escape(characteristics["type"])
        output += (
                f'        <strong>Type:</strong> {animal_type}<br/>\n'
        )
    
    output += "    </p>\n"
    output += "</li>\n"
    
    return output


def main():
    animals_data = load_data("animals_data.json")
    
    output = ""
    
    for animal in animals_data:
        output += serialize_animal(animal)
    
    with open("animals_template.html", "r", encoding="utf-8") as handle:
        template = handle.read()
    
    html_content = template.replace(
            "__REPLACE_ANIMALS_INFO__",
            output
            )
    
    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(html_content)


if __name__ == "__main__":
    main()
