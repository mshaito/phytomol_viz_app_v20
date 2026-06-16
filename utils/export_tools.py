from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / "reports"


def save_table(df: pd.DataFrame, filename: str) -> Path:
    """Save a dataframe to reports/tables."""
    out = REPORTS_DIR / "tables" / filename
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    return out
