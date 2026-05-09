from pathlib import Path
import kagglehub
import shutil

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def download_and_copy(dataset_name: str, output_filename: str):
    path = Path(kagglehub.dataset_download(dataset_name))

    print(f"\nDownloaded files for {dataset_name}:")
    for file in path.rglob("*"):
        if file.is_file():
            print(file)

    csv_file = next(path.rglob("*.csv"))
    shutil.copy(csv_file, RAW_DIR / output_filename)


# --- Run downloads ---
download_and_copy(
    "faresashraf1001/supermarket-sales",
    "supermarket_sales.csv"
)

download_and_copy(
    "mittalvasu95/the-bread-basket",
    "bread_basket.csv"
)