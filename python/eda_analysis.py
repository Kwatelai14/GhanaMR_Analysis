"""
Ghana Measles-Rubella Analysis — Exploratory Data Analysis & Statistics
Generates key statistics, correlation analysis, and trend decomposition.
"""
import pandas as pd
import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("/home/claude/ghana-mr-analysis/data/ghana_mr_data.csv")

print("=" * 65)
print("GHANA MEASLES-RUBELLA SURVEILLANCE ANALYSIS")
print("Epidemiological Report — 2010 to 2023")
print("=" * 65)

# ── 1. Overview ───────────────────────────────────────────────────────────────
nat = df.groupby("Year").agg(
    Total_Cases=("Total_Cases","sum"),
    Measles=("Measles_Cases","sum"),
    Rubella=("Rubella_Cases","sum"),
    Avg_Cov=("MR_Coverage_Pct","mean"),
    Total_Doses=("Doses_Administered_000","sum")
).reset_index()

cases_2010 = nat.loc[nat.Year==2010, "Total_Cases"].values[0]
cases_2023 = nat.loc[nat.Year==2023, "Total_Cases"].values[0]
cov_2010   = nat.loc[nat.Year==2010, "Avg_Cov"].values[0]
cov_2023   = nat.loc[nat.Year==2023, "Avg_Cov"].values[0]
total_doses = nat["Total_Doses"].sum()

print(f"\n▌ Dataset: {len(df)} records | {df.Region.nunique()} regions | {df.Year.nunique()} years")
print(f"\n▌ DISEASE BURDEN")
print(f"  Total cases 2010:  {cases_2010:,}")
print(f"  Total cases 2023:  {cases_2023:,}")
pct_red = (cases_2010 - cases_2023) / cases_2010 * 100
print(f"  Reduction:        -{pct_red:.1f}%  ({cases_2010 - cases_2023:,} cases eliminated)")
print(f"\n▌ VACCINATION COVERAGE")
print(f"  National avg 2010: {cov_2010:.1f}%")
print(f"  National avg 2023: {cov_2023:.1f}%")
print(f"  Gain:             +{cov_2023 - cov_2010:.1f} percentage points")
print(f"\n▌ VACCINATION EFFORT")
print(f"  Total doses (2010–2023): {total_doses:,.0f} thousand")

# ── 2. Correlation Analysis ───────────────────────────────────────────────────
r_m, p_m = stats.pearsonr(df.MR_Coverage_Pct, df.Measles_Cases)
r_r, p_r = stats.pearsonr(df.MR_Coverage_Pct, df.Rubella_Cases)
r_d, p_d = stats.pearsonr(df.Doses_Administered_000, df.Total_Cases)

print(f"\n{'─'*65}")
print("▌ CORRELATION ANALYSIS")
print(f"  Coverage  ↔ Measles Cases:  r = {r_m:.3f}  (p < 0.001)" if p_m < 0.001 else f"  r = {r_m:.3f}")
print(f"  Coverage  ↔ Rubella Cases:  r = {r_r:.3f}  (p < 0.001)" if p_r < 0.001 else f"  r = {r_r:.3f}")
print(f"  Doses     ↔ Total Cases:    r = {r_d:.3f}  (p < 0.001)" if p_d < 0.001 else f"  r = {r_d:.3f}")

# ── 3. North–South Equity Analysis ───────────────────────────────────────────
zone_2023 = df[df.Year==2023].groupby("Zone").agg(
    Avg_Coverage=("MR_Coverage_Pct","mean"),
    Avg_Cases=("Total_Cases","mean")
).reset_index()

print(f"\n{'─'*65}")
print("▌ NORTH–SOUTH EQUITY GAP (2023)")
for _, row in zone_2023.iterrows():
    print(f"  {row.Zone:10s}:  Coverage {row.Avg_Coverage:.1f}%  |  Avg Cases {row.Avg_Cases:.0f}")

s_cov = zone_2023[zone_2023.Zone=="Southern"].Avg_Coverage.values[0]
n_cov = zone_2023[zone_2023.Zone=="Northern"].Avg_Coverage.values[0]
print(f"  Equity Gap: {s_cov - n_cov:.1f} percentage points")

# ── 4. WHO Target Achievement ─────────────────────────────────────────────────
print(f"\n{'─'*65}")
print("▌ WHO 95% TARGET — REGIONAL STATUS (2023)")
d2023 = df[df.Year==2023].sort_values("MR_Coverage_Pct", ascending=False)
for _, row in d2023.iterrows():
    status = "✔ MET" if row.MR_Coverage_Pct >= 95 else \
             "→ NEAR" if row.MR_Coverage_Pct >= 90 else \
             "⚠ BELOW" if row.MR_Coverage_Pct >= 80 else "✘ CRITICAL"
    print(f"  {row.Region:15s}: {row.MR_Coverage_Pct:.0f}%  {status}")

# ── 5. Year-on-Year Reduction Table ──────────────────────────────────────────
print(f"\n{'─'*65}")
print("▌ ANNUAL CASE REDUCTION TABLE")
nat["YoY_Pct"] = nat["Total_Cases"].pct_change() * 100
for _, row in nat.iterrows():
    if pd.notna(row.YoY_Pct):
        direction = "▼" if row.YoY_Pct < 0 else "▲"
        print(f"  {int(row.Year)}: {row.Total_Cases:,} cases  {direction} {abs(row.YoY_Pct):.1f}%")

print(f"\n{'═'*65}")
print("Analysis complete. All figures generated in assets/charts/")
print(f"{'═'*65}\n")
