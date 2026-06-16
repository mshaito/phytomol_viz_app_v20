from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_required_demo_files_exist():
    required = [
        "gcms_compounds.csv",
        "cytotoxicity.csv",
        "admet_properties.csv",
        "target_links.csv",
        "ppi_network.csv",
        "compound_pathways.csv",
        "docking_scores.csv",
        "md_metrics.csv",
        "rmsf.csv",
    ]
    for name in required:
        assert (ROOT / "data" / "demo" / name).exists()
