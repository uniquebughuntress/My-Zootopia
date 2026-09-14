
import json
from html import escape


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_skin_types(animals):
    """Returns all available skin types."""
    skin_types = set()

    for animal in animals:
        skin_type = animal["characteristics"].get("skin_type")

        if skin_type:
            skin_types.add(skin_type)

    return sorted(skin_types)


def choose_skin_type(skin_types):
    """Asks the user to select a skin type."""
    print("Available skin types:")

    for skin_type in skin_types:
        print(f"- {skin_type}")

    print("- No skin_type")

    selected_type = input(
        "\nEnter a skin_type (or 'all' for all animals): "
    ).strip()

    if selected_type.lower() == "all":
        return None

    if selected_type.lower() == "no skin_type":
        return ""

    return selected_type


def filter_animals(animals, selected_type):
    """Returns animals matching the selected skin type."""
    if selected_type is None:
        return animals

    filtered_animals = []

    for animal in animals:
        skin_type = animal["characteristics"].get("skin_type", "")

        if skin_type.lower() == selected_type.lower():
            filtered_animals.append(animal)

    return filtered_animals


def serialize_animal(animal_obj):
    """Converts one animal into an HTML card."""
    name = escape(animal_obj["name"])
    characteristics = animal_obj["characteristics"]

    diet = escape(characteristics["diet"])
    location = escape(animal_obj["locations"][0])

    output = '<li class="cards__item">\n'
    output += f'    <div class="card__title">{name}</div>\n'
    output += '    <div class="card__text">\n'
    output += '        <ul class="card__list">\n'

    output += (
        f'            <li><strong>Diet:</strong> {diet}</li>\n'
    )

    output += (
        f'            <li><strong>Location:</strong> {location}</li>\n'
    )

    if "type" in characteristics:
        animal_type = escape(characteristics["type"])
        output += (
            f'            <li><strong>Type:</strong> {animal_type}</li>\n'
        )

    output += "        </ul>\n"
    output += "    </div>\n"
    output += "</li>\n"

    return output


def main():
    animals_data = load_data("animals_data.json")

    skin_types = get_skin_types(animals_data)
    selected_type = choose_skin_type(skin_types)

    filtered_animals = filter_animals(
        animals_data,
        selected_type
    )

    output = ""

    for animal in filtered_animals:
        output += serialize_animal(animal)

    with open("animals_template.html", "r", encoding="utf-8") as handle:
        template = handle.read()

    html_content = template.replace(
        "__REPLACE_ANIMALS_INFO__",
        output
    )

    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(html_content)

    print("\nWebsite generated successfully!")
    print(f"Animals displayed: {len(filtered_animals)}")


if __name__ == "__main__":
    main()
