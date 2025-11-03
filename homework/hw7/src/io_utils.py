import json

def save_to_json(data, output_path):
    """Save list of dicts to JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
