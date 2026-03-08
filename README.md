# Zurich Housing Market Analysis (2009-2025)

## Project Overview
This project analyzes housing price dynamics in Zurich using aggregated transaction data from 2009 to 2025. The objective is to identify key market patterns across districts and room-size segments, and to provide business-oriented insights that support pricing, investment, and market monitoring decisions.

## Business Questions
1. How has Zurich's housing price per square meter evolved from 2009 to 2025?
2. Which districts are consistently the most expensive when prices are weighted by transaction volume?
3. Which districts show the strongest and weakest short-term momentum (YoY 2025 vs 2024)?
4. How do prices differ across room-size segments, and which segment is currently priced highest?
5. Where are potential market pressure signals (high price growth + low transaction volume)?

## Dataset
- **Source file:** `bau515od5155.csv`
- **Cleaned output:** `data/zurich_housing_clean.csv`
- **Analysis-ready output:** `data/zurich_housing_analysis_ready.csv`
- **Observations:** 1,209 rows (analysis-ready file)
- **Time range:** 2009-2025
- **Granularity:** Aggregated by year, area, and room segment
- **Key fields:** `year`, `area_name`, `area_level`, `rooms_num`, `rooms_label`, `num_transactions`, `price_per_sqm_chf`, `median_price_chf`, `total_price_chf`

## Data Cleaning
**Script:** `clean_zurich_housing.py`

Main actions:
- Renamed columns to consistent English names
- Converted numeric fields safely with coercion
- Removed duplicates
- Created helper fields (`area_level`, `rooms_num`, `has_price_data`)
- Built analysis-ready subset: valid price metrics, positive transaction counts, excluded city-total aggregates

## Methodology
**Exploratory Analysis**
- Weighted yearly trend of CHF/sqm (by `num_transactions`)
- District ranking by weighted average price
- Room-segment comparison (latest year)
- YoY district momentum (2025 vs 2024)

**Market Pressure Heuristic**
Flags districts with high recent price growth and low transaction activity. Exploratory indicator only, not a causal model.

## Key Findings
- **Overall growth:** CHF 8,363/sqm (2009) -> CHF 18,254/sqm (2025); ~5.0% CAGR
- **Most expensive districts (weighted):** Kreis 8, Kreis 7, Kreis 1
- **Strongest 2025 momentum:** Kreis 10, Kreis 7, Kreis 5
- **Highest segment pricing:** 1-room and 2-room units in latest year

## Business Interpretation
- Premium central districts maintain price leadership
- YoY momentum differences reflect localized demand/supply dynamics
- Smaller units show higher CHF/sqm, indicating affordability pressure and urban concentration
- Districts with high growth and low volume warrant closer monitoring

## Project Structure
```text
project1.housing/
|-- bau515od5155.csv
|-- clean_zurich_housing.py
|-- housing_analysis.ipynb
`-- data/
    |-- zurich_housing_clean.csv
    `-- zurich_housing_analysis_ready.csv
```
