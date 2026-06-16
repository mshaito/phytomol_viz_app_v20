# PhytoMol-Viz Architecture

PhytoMol-Viz is organized as a modular Streamlit application.

## Layers

1. User interface, Streamlit pages.
2. Data input, demo CSV files and future uploads.
3. Processing, Pandas, NetworkX, SciPy, and future RDKit support.
4. Visualization, Plotly and future py3Dmol support.
5. Export, report tables, figures, PDF, and HTML.

## Main folders

- `pages/`, Streamlit multipage modules.
- `data/demo/`, synthetic demonstration datasets.
- `data/upload/`, future user uploads.
- `data/processed/`, processed or derived outputs.
- `utils/`, reusable helper functions.
- `models/`, future predictive models.
- `reports/`, generated outputs.
- `docs/`, documentation.
- `tests/`, quality checks.
