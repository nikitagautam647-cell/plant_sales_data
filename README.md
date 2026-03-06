# Plant Sales Data — Sample Dataset and Analysis

This repository provides a small, self-contained sample dataset for a plant nursery/garden store. It's designed for learning and prototyping Power BI reports.

---

## Table of Contents

1. [Overview](#overview)
2. [Data Files](#data-files)
3. [Tech Stack](#tech-stack)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Analysis & Questions](#analysis--questions)
7. [Results & Insights](#results--insights)
8. [Project Structure](#project-structure)
9. [Contributing](#contributing)
10. [License](#license)
11. [Contact](#contact)

---

## Overview

Plant Sales Data contains example sales transactions from a fictional botanical supply store, including comprehensive data cleaning workflows and analysis examples. Perfect for building Power BI dashboards.

**Dataset Highlights:**
- 40 sales transactions across 3 months (January - March 2025)
- 5 product categories: Vegetables, Herbs, Flowering Plants, Indoor Plants, Succulents
- 4 sales regions: North, South, East, West
- Multiple customer accounts with repeat business patterns
- Preprocessed and production-ready data

## Data Files

| File | Description |
|------|-------------|
| `data/raw_sales.txt` | Raw export of 40 sales transactions with original formatting and notes |
| `data/clean_sales.txt` | Cleaned, normalized dataset with calculated fields (Month, TotalSales, etc.) - ready for analysis |
| `data/result_summary.txt` | Comprehensive analysis summary with key metrics, trends, and business insights |

**Note:** These are small, synthetic datasets intended as working examples. Replace with your own data as needed.

## Tech Stack

- **Power BI Desktop** - Report building and visualization (Primary tool)
- **Delimited Text Files** (pipe-separated) - Data interchange format

## Installation

### Clone the Repository
```bash
git clone <repository-url>
cd plant_sales_data
```




```



## Usage

### Power BI Analysis (Recommended)
1. Open **Power BI Desktop**
2. Import `data/clean_sales.txt` as a data source
3. Build visual reports and interactive dashboards
4. Export reports as PDF or save as `.pbix` file
5. See `data/result_summary.txt` for analysis examples

### Data Cloning with Python *(Optional)*
If you need to automate data cloning or preprocessing:
```bash
python clone_data.py
```

## Analysis & Questions

Use this dataset to explore questions like:

- **Product Performance:** Which products and categories sell best?
- **Seasonal Trends:** How do sales patterns change by month or season?
- **Geographic Insights:** Which regions drive the most revenue and volume?
- **Customer Behavior:** What are the top-performing customer segments?
- **Pricing Strategy:** How do price and quantity interact across categories?
- **Inventory Planning:** Which items need higher stock levels?

## Results & Insights

### Key Findings (Sample Data)

| Metric | Value |
|--------|-------|
| **Total Revenue** | $3,614.88 |
| **Total Transactions** | 40 |
| **Average Transaction** | $90.37 |
| **Top Category** | Flowering Plants (30.3% of revenue) |
| **Peak Month** | January ($1,350.23) |
| **Best Region** | West (avg $97.46 per transaction) |
| **Most Popular Product** | Tulips (20 units) |

### Observations
1. Flowering plants outperform other categories - strong seasonal demand
2. March shows recovery after February dip - spring season effect
3. West region delivers highest-value transactions despite lower volume
4. Herb products maintain steady volume despite lower average prices
5. Top 5 customers represent 62% of total revenue - concentration risk

For detailed analysis, see `data/result_summary.txt`

## Project Structure

```
.
├── README.md                        # This file
├── LICENSE                          # MIT License
│
├── data/
│   ├── raw_sales.txt               # Raw transaction export
│   ├── clean_sales.txt             # Cleaned dataset for Power BI
│   ├── result_summary.txt          # Analysis summary and insights
│   └── clone_data.py               # Python data cloning script (optional)
│
├── reports/
│   └── [Power BI exports, PDFs]
│
└── results/
    └── [Generated outputs, repository]
```

## Contributing

1. **Fork** this repository
2. **Create** a feature branch: `git checkout -b feature/my-enhancement`
3. **Make** your changes and test thoroughly
4. **Commit** with clear messages: `git commit -m "Add new analysis"`
5. **Push** to your fork: `git push origin feature/my-enhancement`
6. **Open** a pull request describing your changes

**Contribution Ideas:**
- Additional analysis scripts
- Power BI template files (.pbit)
- Data validation rules
- Visualization examples
- Documentation improvements

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

## Contact

**Project Maintainer:** Nikita Gautam  
📧 **Email:** nikitagautam647@gmail.com

For questions, feedback, or issues:
1. Open an issue in this repository
2. Contact the maintainer directly
3. Check existing documentation in the README or result files

---

**Last Updated:** March 2025  
**Data Period:** January - March 2025  
**Status:** Active & Maintained