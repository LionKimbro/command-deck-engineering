from pathlib import Path
import shutil

ROOT = Path(__file__).parent
RAW = ROOT / "docs" / "raw"
DOCS = ROOT / "docs"

mapping_dictionary = {
    "0001": "",   # project to docs/
    "0002": None  # ignore
}


def main():

    for file in RAW.iterdir():

        if not file.is_file():
            continue

        if "__" not in file.name:
            continue

        doc_id, remainder = file.name.split("__", 1)

        if doc_id not in mapping_dictionary:
            continue

        target_folder = mapping_dictionary[doc_id]

        if target_folder is None:
            continue

        target_dir = DOCS if target_folder == "" else DOCS / target_folder
        target_dir.mkdir(parents=True, exist_ok=True)

        target = target_dir / file.name

        shutil.copy2(file, target)

        print("Copied:", file, "→", target)


if __name__ == "__main__":
    main()