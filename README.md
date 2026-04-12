# 🇬🇭 Ghana Measles-Rubella Surveillance Analysis (2010–2023)

A comprehensive epidemiological data analysis project examining measles and rubella disease burden, vaccination coverage trends, and regional equity across Ghana's 10 administrative regions.

---

## 📊 Key Findings

| Metric | 2010 | 2023 | Change |
|--------|------|------|--------|
| National Avg Coverage | 68.3% | 89.4% | **+21.1pp** |
| Total Annual Cases | 3,910 | 276 | **−92.9%** |
| Northern Coverage | ~53% | ~82% | +29pp |
| Southern Coverage | ~76% | ~93% | +17pp |
| Doses Administered | ~4.2M | ~5.9M | +40% |

- **3,634 cases eliminated** over the 14-year programme period
- **Strong negative correlation** between coverage and cases (r = −0.78, p < 0.001)
- **10.6pp North–South equity gap** remains a priority concern
- **2 of 10 regions** (Greater Accra, Ashanti) meet WHO 95% elimination target

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| **Microsoft Excel** | Data structuring, pivot analysis, summary statistics |
| **Python** (pandas, matplotlib, scipy) | EDA, statistical analysis, 8 visualizations |
| **Power BI** | Interactive 3-page executive dashboard |
| **GitHub Pages** | Portfolio hosting (`index.html`) |

---

## 📁 Repository Structure

```
ghana-mr-analysis/
├── data/
│   ├── Ghana_MR_Analysis.xlsx    # Excel workbook (3 sheets)
│   ├── ghana_mr_data.csv         # Clean long-format dataset (140 records)
│   └── create_dataset.py         # Generates data + Excel workbook
├── python/
│   ├── visualizations.py         # All 8 charts (run this first)
│   └── eda_analysis.py           # Statistical EDA output
├── powerbi/
│   └── POWERBI_GUIDE.md          # Step-by-step Power BI setup
├── assets/
│   └── charts/                   # 8 exported PNG visualizations
├── index.html                    # GitHub Pages portfolio page
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/ghana-mr-analysis.git
cd ghana-mr-analysis
```

### 2. Install Python Dependencies
```bash
pip install pandas matplotlib seaborn scipy openpyxl
```

### 3. Generate Dataset & Excel
```bash
python data/create_dataset.py
```

### 4. Run Visualizations
```bash
python python/visualizations.py
```

### 5. Run EDA Analysis
```bash
python python/eda_analysis.py
```

### 6. Open Excel Workbook
Open `data/Ghana_MR_Analysis.xlsx` in Microsoft Excel or LibreOffice.

### 7. Power BI Dashboard
Follow the step-by-step guide in `powerbi/POWERBI_GUIDE.md`.

---

## 📈 Visualizations

| # | Chart | Insight |
|---|-------|---------|
| 1 | National Burden Trend (Stacked Area) | 92.9% total reduction |
| 2 | Coverage Heatmap (Region × Year) | Persistent northern deficit |
| 3 | Regional Coverage Snapshot 2023 | 2 regions at WHO target |
| 4 | Coverage–Cases Scatter | r = −0.78 correlation |
| 5 | North–South Disparity | Gap narrowing but persistent |
| 6 | Doses vs Cases (Dual Axis) | Programme efficiency |
| 7 | Case Comparison 2010 vs 2023 | Regional absolute reduction |
| 8 | 4-Panel Summary Dashboard | Complete overview |

---

## 🌐 Portfolio Page

Live at: `https://YOUR_USERNAME.github.io/ghana-mr-analysis/`

To enable GitHub Pages:
1. Go to repository **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: **main** / **root**
4. Save and visit the URL above

---

## 📚 Data Sources

Data is constructed to align with publicly available Ghana Health Service (GHS) and
WHO AFRO regional immunization reports. For production research, use official sources:

- [WHO AFRO Immunization Data](https://www.who.int/docs/default-source/immunization/)
- [Ghana Health Service Annual Reports](https://www.ghanahealthservice.org)
- [UNICEF State of the World's Children](https://www.unicef.org/sowc)

---

## 🏥 Recommendations

1. **Intensify northern outreach** — Upper West at only 80%; mobile vaccination units needed
2. **Catch-up campaigns** — Target children missed during 2020–2021 due to COVID-19
3. **Equity monitoring** — Track N/S gap as a KPI in national immunization plans
4. **Community health workers** — Expand CHW network in Northern, Upper East & Upper West

---

*Public Health Data Analysis Portfolio Project | Ghana 🇬🇭*
