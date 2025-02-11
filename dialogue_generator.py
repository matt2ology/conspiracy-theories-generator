import csv
import os
import random
import time
from itertools import cycle

# Normalize file path for cross-platform compatibility
DATA_FILE = os.path.normpath("data/dialogue_master_list.csv")

# ANSI color codes for highlighting
BOLD_BLUE = "\033[1;34m"  # Bold Blue for Conspirators
BOLD_RED = "\033[1;31m"   # Bold Red for Victims
RESET = "\033[0m"         # Reset color


def highlight_text(text, category):
    """Highlights Conspirators and Victims in different colors."""
    if category == "conspirator":
        return f"{BOLD_BLUE}{text}{RESET}"
    elif category == "victim":
        return f"{BOLD_RED}{text}{RESET}"
    return text


def load_csv_data(csv_file):
    """Loads CSV and ensures every column has available values (no empty entries)."""
    data = {
        "conspirator": [],
        "conspirator_link": [],
        "victim_link": [],
        "victim": [],
        "non_sequitur": [],
    }

    with open(csv_file, newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)

        for row in reader:
            for key in data:
                value = row.get(key, "").strip()
                if value:
                    data[key].append(value)  # Store non-empty values only

    # Ensure every category has data by recycling values if needed
    for key in data:
        if not data[key]:
            # Use non_sequitur as fallback
            data[key] = list(data["non_sequitur"])

    # Convert all lists to cycles for endless iteration
    return {key: cycle(random.sample(values, len(values))) for key, values in data.items()}, data["conspirator"]


def get_next_entry(data, key, category=None):
    """Fetches the next random entry from the list."""
    entry = next(data[key])
    return highlight_text(entry, category) if category else entry


def display_random_dialogue_debug(data, conspirator_list):
    """Displays the dialogue with unique conspirators and randomized selections."""
    used_conspirators = set()

    def get_unique_conspirator():
        """Ensures a unique conspirator is selected per round."""
        available = [c for c in conspirator_list if c not in used_conspirators]
        if not available:
            used_conspirators.clear()  # Reset if all have been used
            available = conspirator_list[:]
        chosen = random.choice(available)
        used_conspirators.add(chosen)
        return highlight_text(chosen, "conspirator")

    print("\n--- Random Dialogue State ---")
    conspirator1 = get_unique_conspirator()
    conspirator2 = get_unique_conspirator()

    print(f"🔹 Conspirator01: {conspirator1}")
    print(f"🔄 Conspirator Link: {get_next_entry(data, 'conspirator_link')}")
    print(f"🔹 Conspirator02: {conspirator2}")
    print(f"🔗 Victim Link: {get_next_entry(data, 'victim_link')}")
    print(f"🎯 Victim: {get_next_entry(data, 'victim', 'victim')}")
    print(f"🤯 Non-Sequitur: {get_next_entry(data, 'non_sequitur')}")
    time.sleep(1)


def display_random_dialogue(data, conspirator_list):
    """Displays the dialogue with unique conspirators and randomized selections."""
    used_conspirators = set()

    def get_unique_conspirator():
        """Ensures a unique conspirator is selected per round."""
        available = [c for c in conspirator_list if c not in used_conspirators]
        if not available:
            used_conspirators.clear()  # Reset if all have been used
            available = conspirator_list[:]
        chosen = random.choice(available)
        used_conspirators.add(chosen)
        return highlight_text(chosen, "conspirator")

    conspirator1 = get_unique_conspirator()
    conspirator2 = get_unique_conspirator()

    print(f"The {conspirator1}", end="\n\n")
    time.sleep(1)
    print(f"{get_next_entry(data, 'conspirator_link')}", end="\n\n")
    time.sleep(1)
    print(f"the {conspirator2}", end="\n\n")
    time.sleep(1)
    print(f"{get_next_entry(data, 'victim_link')}", end="\n\n")
    time.sleep(1)
    print(f"{get_next_entry(data, 'victim', 'victim')}", end="\n\n")
    time.sleep(1)
    print("\n")
    print(f"{get_next_entry(data, 'non_sequitur')}")
    time.sleep(5)


if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        csv_data, conspirator_list = load_csv_data(DATA_FILE)
        display_random_dialogue(csv_data, conspirator_list)
        #display_random_dialogue_debug(csv_data, conspirator_list)

