import csv
import os
import random
import time

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
    """Loads CSV and returns a dictionary of columns with non-empty values."""
    data = {
        "conspirator": set(),  # Use sets to prevent duplicates
        "conspirator_link": [],
        "victim_link": [],
        "victim": set(),
        "non_sequitur": [],
    }

    with open(csv_file, newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)

        for row in reader:
            for key in data:
                value = row.get(key, "").strip()
                if value:
                    if key in ["conspirator", "victim"]:  # Ensure unique conspirators & victims
                        data[key].add(value)
                    else:
                        data[key].append(value)  # Store non-empty values only

    # Convert sets back to lists for random selection
    data["conspirator"] = list(data["conspirator"])
    data["victim"] = list(data["victim"])
    return data


def get_random_entry(data, key, category=None, used_items=set()):
    """Returns a highlighted random entry from a column, avoiding duplicates when necessary."""
    available_choices = list(set(data[key]) - used_items) if key in data else []
    
    if not available_choices:
        return "Unknown"  # Fallback when no available choices left
    
    entry = random.choice(available_choices)
    used_items.add(entry)
    return highlight_text(entry, category) if category else entry


def display_random_dialogue_sample(data):
    """Displays the dialogue with fresh randomness at every print, ensuring unique conspirators."""
    used_conspirators = set()

    print("\n--- Random Dialogue State ---")

    conspirator1 = get_random_entry(data, "conspirator", "conspirator", used_conspirators)
    conspirator_link = get_random_entry(data, "conspirator_link")
    conspirator2 = get_random_entry(data, "conspirator", "conspirator", used_conspirators)
    victim_link = get_random_entry(data, "victim_link")
    victim = get_random_entry(data, "victim", "victim")
    non_sequitur = get_random_entry(data, "non_sequitur")

    print(f"🔹 Conspirator01: {conspirator1}")
    time.sleep(1)
    print(f"🔄 Conspirator Link: {conspirator_link}")
    time.sleep(1)
    print(f"🔹 Conspirator02: {conspirator2}")
    time.sleep(1)
    print(f"🔗 Victim Link: {victim_link}")
    time.sleep(1)
    print(f"🎯 Victim: {victim}")
    time.sleep(1)
    print(f"🤯 Non-Sequitur: {non_sequitur}")
    time.sleep(5)

def display_random_dialogue(data):
    """Displays the dialogue with fresh randomness at every print, ensuring unique conspirators."""
    used_conspirators = set()

    conspirator1 = get_random_entry(data, "conspirator", "conspirator", used_conspirators)
    conspirator_link = get_random_entry(data, "conspirator_link")
    conspirator2 = get_random_entry(data, "conspirator", "conspirator", used_conspirators)
    victim_link = get_random_entry(data, "victim_link")
    victim = get_random_entry(data, "victim", "victim")
    non_sequitur = get_random_entry(data, "non_sequitur")

    print(f"The {conspirator1}")
    time.sleep(1)
    print(f"{conspirator_link}")
    time.sleep(1)
    print(f"the {conspirator2}")
    time.sleep(1)
    print(f"{victim_link}")
    time.sleep(1)
    print(f"{victim}")
    time.sleep(1)
    print("\n")
    print(f"{non_sequitur}")
    time.sleep(5)


if __name__ == "__main__":
    while True:
        # Clear screen before displaying dialogue
        os.system('cls' if os.name == 'nt' else 'clear')
        csv_data = load_csv_data(DATA_FILE)
        display_random_dialogue(csv_data)
