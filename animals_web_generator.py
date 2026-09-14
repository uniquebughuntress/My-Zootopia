
import json
from html import escape


# File paths used by the application.
DATA_FILE = "animals_data.json"
TEMPLATE_FILE = "animals_template.html"
OUTPUT_FILE = "animals.html"

# Placeholder in the HTML template.
TEMPLATE_PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
    """Load animal data from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Convert one animal object into an HTML card."""
    name = escape(animal_obj["name"])
    characteristics = animal_obj["characteristics"]

    diet = escape(characteristics["diet"])
    location = escape(animal_obj["locations"][0])

    # Build the HTML card for one animal.
    output = '<li class="cards__item">\n'
    output += f'    <div class="card__title">{name}</div>\n'
    output += '    <p class="card__text">\n'

    output += f'        <strong>Diet:</strong> {diet}<br/>\n'
    output += (
        f'        <strong>Location:</strong> {location}<br/>\n'
    )

    # Add the type only when it is available.
    if "type" in characteristics:
        animal_type = escape(characteristics["type"])
        output += (
            f'        <strong>Type:</strong> {animal_type}<br/>\n'
        )

    output += "    </p>\n"
    output += "</li>\n"

    return output


def generate_animal_cards(animals):
    """Generate HTML cards for all animals."""
    output = ""

    for animal in animals:
        output += serialize_animal(animal)

    return output


def load_template(file_path):
    """Load the HTML template from a file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_html(file_path, html_content):
    """Write HTML content to a file."""
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(html_content)


def main():
    """Generate the animal website from the JSON data."""
    # Load the animal data.
    animals_data = load_data(DATA_FILE)

    # Convert the animal data into HTML cards.
    animal_cards = generate_animal_cards(animals_data)

    # Load the HTML template.
    template = load_template(TEMPLATE_FILE)

    # Insert the animal cards into the template.
    html_content = template.replace(
        TEMPLATE_PLACEHOLDER,
        animal_cards
    )

    # Save the completed HTML page.
    write_html(OUTPUT_FILE, html_content)


if __name__ == "__main__":
    main()
