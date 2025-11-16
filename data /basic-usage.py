import json
from typing import Iterator, Dict, Any


def load_becia_samples(path: str) -> Iterator[Dict[str, Any]]:
    """
    Stream BECIA samples from a JSONL file.
    Each line is a separate JSON object.
    """
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)


def print_first_samples(n: int = 5) -> None:
    """
    Print the first N BECIA samples with tone and intention.
    """
    samples = list(load_becia_samples("data/samples.jsonl"))

    for sample in samples[:n]:
        sample_id = sample.get("id")
        text = sample.get("text")
        emojis = sample.get("emojis")
        tone = sample.get("tone")
        intention = sample.get("intention")  # None for older samples
        context_note = sample.get("context_note")

        print(f"{sample_id}: {text}")
        print(f"  emojis     : {emojis}")
        print(f"  tone       : {tone}")
        print(f"  intention  : {intention}")
        print(f"  note       : {context_note}")
        print()


if __name__ == "__main__":
    print("=== BECIA Sample Preview ===\n")
    print_first_samples(5)
