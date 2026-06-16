from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DEMO_DIR = DATA_DIR / "demo"
UPLOAD_DIR = DATA_DIR / "upload"
PROCESSED_DIR = DATA_DIR / "processed"


def load_csv(filename: str) -> pd.DataFrame:
    """Load a CSV from data/ first, then data/demo/ for backward compatibility."""
    candidates = [DATA_DIR / filename, DEMO_DIR / filename]
    for path in candidates:
        if path.exists():
            return pd.read_csv(path)
    raise FileNotFoundError(f"Missing data file: {filename}. Checked: {candidates}")


def list_demo_files():
    return sorted(p.name for p in DEMO_DIR.glob("*.csv"))


def save_uploaded_file(uploaded_file, subfolder="csv"):
    """Save a Streamlit uploaded file into data/upload/<subfolder>."""
    target_dir = UPLOAD_DIR / subfolder
    target_dir.mkdir(parents=True, exist_ok=True)
    out = target_dir / uploaded_file.name
    out.write_bytes(uploaded_file.getbuffer())
    return out
