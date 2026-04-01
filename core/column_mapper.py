import json

def load_synonyms():
    with open("data/synonym_dict.json") as f:
        return json.load(f)

def map_columns(columns):
    synonyms = load_synonyms()
    mapped = {}

    for col in columns:
        col_lower = col.lower()

        for standard, syns in synonyms.items():
            if col_lower in syns:
                mapped[col] = standard

    return mapped
