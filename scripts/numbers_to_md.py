from typing import Any, Dict, List
import json

def gen_row(data: List[str]) -> str:
    return "|" + "|".join(data) + "|"

def gen_number_table(numbers: List[Dict[str, str]]) -> str:
    out: str = ""
    for r in numbers:
        n: str = r["number"]
        d: str = r["description"]
        out += gen_row([n, d])
    return out


if __name__ == "__main__":
    with open("data/numbers.json") as datum:
        numbers = json.load(datum)

    print(gen_row(["number", "description"]))
    print(gen_number_table(numbers))
