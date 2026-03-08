from pathlib import Path

import pandas as pd


INPUT_CSV = Path("bau515od5155.csv")
OUTPUT_DIR = Path("data")
OUTPUT_CLEAN = OUTPUT_DIR / "zurich_housing_clean.csv"
OUTPUT_ANALYSIS = OUTPUT_DIR / "zurich_housing_analysis_ready.csv"


def classify_area(area_name: str) -> str:
    if area_name == "Ganze Stadt":
        return "city_total"
    if area_name.startswith("Kreis "):
        return "district"
    return "quarter"


def parse_room_count(room_label: str):
    if pd.isna(room_label):
        return pd.NA
    text = str(room_label).strip()
    if text.startswith("6-"):
        return 6
    first_chunk = text.split("-")[0]
    if first_chunk.isdigit():
        return int(first_chunk)
    return pd.NA


def load_and_clean(path: Path):
    df = pd.read_csv(path)

    rename_map = {
        "Stichtagdatjahr": "year",
        "DatenstandCd": "data_status_cd",
        "HAArtLevel1Sort": "deal_type_sort",
        "HAArtLevel1Cd": "deal_type_cd",
        "HAArtLevel1Lang": "deal_type",
        "HASTWESort": "new_build_sort",
        "HASTWECd": "new_build_cd",
        "HASTWELang": "new_build",
        "RaumSort": "area_sort",
        "RaumCd": "area_cd",
        "RaumLang": "area_name",
        "AnzZimmerLevel2Sort_noDM": "rooms_sort",
        "AnzZimmerLevel2Cd_noDM": "rooms_cd",
        "AnzZimmerLevel2Lang_noDM": "rooms_label",
        "AnzHA": "num_transactions",
        "HAPreisWohnflaeche": "price_per_sqm_chf",
        "HAMedianPreis": "median_price_chf",
        "HASumPreis": "total_price_chf",
    }
    df = df.rename(columns=rename_map)

    numeric_cols = [
        "year",
        "deal_type_sort",
        "new_build_sort",
        "area_sort",
        "rooms_sort",
        "num_transactions",
        "price_per_sqm_chf",
        "median_price_chf",
        "total_price_chf",
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    string_cols = [
        "deal_type_cd",
        "deal_type",
        "new_build_cd",
        "new_build",
        "area_cd",
        "area_name",
        "rooms_cd",
        "rooms_label",
        "data_status_cd",
    ]
    for col in string_cols:
        df[col] = df[col].astype("string").str.strip()

    df = df.drop_duplicates().sort_values(
        by=["year", "area_sort", "rooms_sort"], kind="stable"
    )

    df["area_level"] = df["area_name"].apply(classify_area).astype("string")
    df["rooms_num"] = df["rooms_label"].apply(parse_room_count).astype("Int64")
    df["has_price_data"] = (
        df["price_per_sqm_chf"].notna()
        & df["median_price_chf"].notna()
        & df["total_price_chf"].notna()
    )

    analysis_df = df[
        (df["num_transactions"] > 0)
        & df["has_price_data"]
        & (df["area_level"] != "city_total")
    ].copy()

    return df, analysis_df


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    clean_df, analysis_df = load_and_clean(INPUT_CSV)
    clean_df.to_csv(OUTPUT_CLEAN, index=False, encoding="utf-8")
    analysis_df.to_csv(OUTPUT_ANALYSIS, index=False, encoding="utf-8")

    print(f"Clean file: {OUTPUT_CLEAN} ({len(clean_df)} rows)")
    print(f"Analysis-ready file: {OUTPUT_ANALYSIS} ({len(analysis_df)} rows)")


if __name__ == "__main__":
    main()
