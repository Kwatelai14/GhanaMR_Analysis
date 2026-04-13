# Power BI Dashboard Guide — Ghana MR Surveillance

## Overview

This guide explains how to replicate the Ghana Measles-Rubella analysis in **Power BI Desktop** using the provided dataset (`ghana_mr_data.csv`).

---

## 1. Data Import

1. Open **Power BI Desktop**
2. **Home → Get Data → Text/CSV**
3. Select `data/ghana_mr_data.csv`
4. Click **Load**

---

## 2. Data Model & Transformations

In **Power Query Editor (Home → Transform Data)**:

### Create a Date Table
```
= List.Generate(
    () => #date(2010,1,1),
    each _ <= #date(2023,12,31),
    each Date.AddYears(_, 1)
)
```

### Key Calculated Columns (DAX)
Add these in the **Data view → New Column**:

```dax
-- Cases Reduction from 2010 Baseline
Cases Reduction % = 
VAR base2010 = CALCULATE(SUM('Data'[Total_Cases]), 'Data'[Year] = 2010)
RETURN DIVIDE(base2010 - SUM('Data'[Total_Cases]), base2010) * 100

-- Coverage Status Category
Coverage Status = 
SWITCH(
    TRUE(),
    'Data'[MR_Coverage_Pct] >= 95, "✔ WHO Target Met",
    'Data'[MR_Coverage_Pct] >= 80, "⚠ Below Target",
    "✘ Critical"
)

-- North-South Zone Label
Zone Label = 
IF('Data'[Zone] = "Northern", "Northern Ghana", "Southern Ghana")
```

### Key Measures (DAX)
Create these in **Home → New Measure**:

```dax
Total Cases = SUM('Data'[Total_Cases])

Avg Coverage = AVERAGE('Data'[MR_Coverage_Pct])

YoY Case Change % = 
VAR CurrentYear = MAX('Data'[Year])
VAR PrevYear = CurrentYear - 1
VAR CasesNow = CALCULATE([Total Cases], 'Data'[Year] = CurrentYear)
VAR CasesPrev = CALCULATE([Total Cases], 'Data'[Year] = PrevYear)
RETURN DIVIDE(CasesNow - CasesPrev, CasesPrev) * 100

Coverage Gap (N vs S) =
VAR S = CALCULATE([Avg Coverage], 'Data'[Zone] = "Southern")
VAR N = CALCULATE([Avg Coverage], 'Data'[Zone] = "Northern")
RETURN S - N

Cases Eliminated = 
VAR base = CALCULATE(SUM('Data'[Total_Cases]), 'Data'[Year] = 2010)
RETURN base - SUM('Data'[Total_Cases])
```

---

## 3. Recommended Dashboard Layout (3 Pages)

### Page 1 — National Overview
| Visual | Fields | Purpose |
|--------|--------|---------|
| **KPI Card** | Avg Coverage (latest year) | Headline metric |
| **KPI Card** | Total Cases (latest year) | Burden snapshot |
| **KPI Card** | Cases Eliminated | Impact story |
| **Line + Clustered Column Chart** | X: Year, Column: Total Cases, Line: Avg Coverage | Trend overview |
| **Stacked Area Chart** | X: Year, Values: Measles_Cases, Rubella_Cases | Disease split |
| **Slicer** | Year (range slider) | Interactivity |

### Page 2 — Regional Deep-Dive
| Visual | Fields | Purpose |
|--------|--------|---------|
| **Filled Map** | Region → MR Coverage | Geographic heatmap |
| **Bar Chart** | Region, MR Coverage (sorted desc) | Coverage ranking |
| **Matrix** | Rows: Region, Cols: Year, Values: MR Coverage | Heatmap table |
| **Scatter Chart** | X: MR Coverage, Y: Total Cases, Size: Doses, Legend: Region | Correlation |
| **Slicer** | Year | Interactivity |

### Page 3 — Equity & Forecast
| Visual | Fields | Purpose |
|--------|--------|---------|
| **Line Chart** | X: Year, Series: Zone, Values: Avg Coverage | N vs S disparity |
| **Gauge** | [Coverage Gap (N vs S)] | Equity gap KPI |
| **Waterfall Chart** | YoY Cases Change | Year-by-year progress |
| **100% Stacked Bar** | X: Year, Values: Zone totals | Zone share |
| **Forecast Line** | Time series → Cases with built-in forecast | Projection |

---

## 4. Colour Theme (Ghana Flag Palette)

Go to **View → Themes → Customize current theme** and set:

```json
{
  "name": "Ghana Health",
  "dataColors": [
    "#006B3F", "#CE1126", "#FCD116", "#2196F3",
    "#9C27B0", "#FF5722", "#00BCD4", "#795548"
  ],
  "background": "#F5F7FA",
  "foreground": "#1A2B3C",
  "tableAccent": "#006B3F"
}
```

---

## 5. Conditional Formatting for Coverage Table

In the Matrix visual → **Format → Conditional formatting → Background color**:

| Rule | Color |
|------|-------|
| Value ≥ 90 | `#27AE60` (Green) |
| Value ≥ 80 and < 90 | `#F39C12` (Amber) |
| Value ≥ 70 and < 80 | `#E67E22` (Orange) |
| Value < 70 | `#E74C3C` (Red) |

---

## 6. Publishing
1. **File → Publish → To Power BI Service**
2. Add report to a **Dashboard** via "Pin Live Page"
3. Share the workspace link in your portfolio README

---

*Data source: Ghana Health Service / WHO AFRO aligned estimates. See `README.md` for full methodology.*
