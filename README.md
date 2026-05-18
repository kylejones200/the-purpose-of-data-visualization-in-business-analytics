# Data Visualization

Published: yes
Medium: [https://medium.com/@kyle-t-jones/the-purpose-of-data-visualization-in-business-analytics-8c9992df73eb](https://medium.com/@kyle-t-jones/the-purpose-of-data-visualization-in-business-analytics-8c9992df73eb)


This project demonstrates various data visualization techniques using matplotlib, seaborn, and other libraries.

## Business context

Data visualization is a form of reasoning. It is how we surface patterns and gaps, how we test hypotheses, how we communicate arguments, and how we make decisions.

> Code is available on > [github](https://github.com/kylejones200/medium/tree/main/article-2025-05-12-data-visualization)

A good visual clarifies something essential. A bad viz distorts or conceals. Every visual carries assumptions. The decision to use a bar chart over a line chart, the scale of the y-axis, the ordering of categories, the use of red to mark one data point instead of another --- these are all choices that shape how someone interprets your message.

## Project Structure

```
.
├── README.md           # This file
├── main.py            # Main entry point
├── config.yaml        # Configuration file
├── requirements.txt   # Python dependencies
├── src/               # Core functions
│   ├── core.py        # Visualization functions
│   └── plotting.py    # Tufte-style plotting utilities
├── tests/             # Unit tests
├── data/              # Data files
└── images/            # Generated plots and figures
```

## Configuration

Edit `config.yaml` to customize:
- Data generation parameters (months, regions)
- Visualization options (seaborn, weekly trends, store comparisons)
- Output settings

## Visualization Types

- Seaborn Line Plots: Time series with multiple categories
- Weekly Trends: Aggregated sales trends
- Store Comparisons: Side-by-side store performance

## Caveats

- By default, generates synthetic sales data.
- Interactive visualizations (Plotly, Altair, Streamlit) are optional and can be enabled in config.

## Disclaimer

Educational/demo code only. Not financial, safety, or engineering advice. Use at your own risk. Verify results independently before any production or operational use.

## License

MIT — see [LICENSE](LICENSE).