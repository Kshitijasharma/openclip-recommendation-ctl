from pathlib import Path

import pandas as pd


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
METADATA_PATH = PROJECT_ROOT / "models" / "retrieval" / "metadata.csv"
IMAGE_DIR_RELATIVE = Path("data/polyvore_images")


def main():
    if not METADATA_PATH.exists():
        print(f"Error: Metadata file not found at {METADATA_PATH}")
        return

    print(f"Loading metadata from {METADATA_PATH}...")
    metadata = pd.read_csv(METADATA_PATH)

    print("Updating image_path column...")
    metadata["image_path"] = metadata["item_ID"].apply(
        lambda x: str(IMAGE_DIR_RELATIVE / f"{x}.jpg").replace("\\", "/")
    )

    print(f"Saving updated metadata to {METADATA_PATH}...")
    metadata.to_csv(METADATA_PATH, index=False)

    print("metadata.csv updated successfully!")


if __name__ == "__main__":
    main()
