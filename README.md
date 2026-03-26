# Zurich Housing Market Analysis (2009-2025)

Analytics project on long-term Zurich housing price dynamics with a business interpretation layer for market monitoring and decision support.

- Coverage: 2009 to 2025
- Analysis-ready sample: 1,209 records
- Focus: price-per-sqm trends, district ranking, and short-term momentum

## Business Problem
How has Zurich's housing market evolved over time, which districts remain structurally expensive, and where are short-term pressure signals emerging? This project translates aggregated housing data into interpretable indicators for pricing, monitoring, and planning discussions.

## Dataset
- Raw source file: `bau515od5155.csv`
- Cleaned output: `data/zurich_housing_clean.csv`
- Analysis-ready output: `data/zurich_housing_analysis_ready.csv`
- Granularity: year x area x room-segment aggregates
- Key fields: `year`, `area_name`, `rooms_label`, `num_transactions`, `price_per_sqm_chf`, `median_price_chf`

## Methodology
1. Standardize and rename source columns.
2. Convert key numeric fields and remove invalid records.
3. Classify area level (district/quarter/city aggregate).
4. Build analysis-ready subset with valid price and transaction data.
5. Analyze weighted long-term trend, district ranking, and YoY momentum.

## Key Findings
- Zurich weighted price-per-sqm increased from about **CHF 8,363 (2009)** to **CHF 18,254 (2025)**.
- Estimated long-term growth is roughly **5.0% CAGR**.
- Premium districts remain consistently more expensive than the citywide average.
- YoY momentum (2025 vs 2024) differs across districts, suggesting localized market dynamics.

## Recommendations
- Track district-level YoY momentum alongside transaction counts to detect pressure zones early.
- Separate strategic decisions for premium districts vs value-oriented districts.
- Monitor smaller-unit pricing trends as a signal of affordability stress.

## Tech Stack
- Python
- pandas
- Jupyter Notebook

## Repository Structure
```text
zurich-housing-market-analysis/
|-- bau515od5155.csv
|-- clean_zurich_housing.py
|-- housing_analysis.ipynb
|-- data/
|   |-- zurich_housing_clean.csv
|   `-- zurich_housing_analysis_ready.csv
|-- requirements.txt
`-- README.md
```

## How to Run
```bash
pip install -r requirements.txt
python clean_zurich_housing.py
```

Then open and run:
- `housing_analysis.ipynb`

## CV-Ready Impact
- Built a reproducible housing analytics workflow from raw dataset to analysis-ready outputs.
- Quantified long-term market growth (~5.0% CAGR) and district-level differences.
- Produced business-oriented insights for pricing and market monitoring discussions.

## Limitations
- Source data is aggregated, limiting micro-level causal interpretation.
- Findings are descriptive and exploratory, not predictive modeling.

## Next Steps
- Add visual exports (trend and district ranking charts) under a `visuals/` folder.
- Introduce a small KPI dashboard (e.g., Streamlit or Power BI) for recruiter-ready presentation.
- Expand with external variables (rates, macro indicators) for richer context.
