
import json
from html import escape


def load_data(file_path):
    """Load animal data from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Convert one animal into an HTML card."""
    name = escape(animal_obj["name"])
    characteristics = animal_obj["characteristics"]

    diet = escape(characteristics["diet"])
    location = escape(animal_obj["locations"][0])

    # Start the HTML card with the animal name.
    output = '<li class="cards__item">\n'
    output += f'    <div class="card__title">{name}</div>\n'
    output += '    <p class="card__text">\n'

    # Add the animal's diet and location.
    output += f'        <strong>Diet:</strong> {diet}<br/>\n'
    output += (
        f'        <strong>Location:</strong> {location}<br/>\n'
    )

    # Add the type only if it exists in the JSON data.
    if "type" in characteristics:
        animal_type = escape(characteristics["type"])
        output += (
            f'        <strong>Type:</strong> {animal_type}<br/>\n'
        )

    # Close the HTML card.
    output += "    </p>\n"
    output += "</li>\n"

    return output


def main():
    """Generate the HTML page from the animal data."""
    # Load the animal data from the JSON file.
    animals_data = load_data("animals_data.json")

    # Serialize each animal into an HTML card.
    output = ""

    for animal in animals_data:
        output += serialize_animal(animal)

    # Load the HTML template.
    with open(
        "animals_template.html", "r", encoding="utf-8"
    ) as handle:
        template = handle.read()

    # Replace the placeholder with the generated animal cards.
    html_content = template.replace(
        "__REPLACE_ANIMALS_INFO__",
        output
    )

    # Write the completed HTML page.
    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(html_content)


if __name__ == "__main__":
    main()
