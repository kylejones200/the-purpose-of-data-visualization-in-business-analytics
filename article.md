---
author: "Kyle Jones"
date_published: "May 12, 2025"
date_exported_from_medium: "November 10, 2025"
canonical_link: "https://medium.com/@kyle-t-jones/the-purpose-of-data-visualization-in-business-analytics-8c9992df73eb"
---

# The Purpose of Data Visualization in Business Analytics Data visualization is a form of reasoning. It is how we surface patterns
and gaps, how we test hypotheses, how we communicate arguments...

### **The Purpose of Data Visualization in Business Analytics**
Data visualization is a form of reasoning. It is how we surface patterns and gaps, how we test hypotheses, how we communicate arguments, and how we make decisions.

> Code is available on
> [github](https://github.com/kylejones200/medium/tree/main/article-2025-05-12-data-visualization)

A good visual clarifies something essential. A bad viz distorts or conceals. Every visual carries assumptions. The decision to use a bar chart over a line chart, the scale of the y-axis, the ordering of categories, the use of red to mark one data point instead of another --- these are all choices that shape how someone interprets your message.

Good visual communication starts with a commitment to honesty. This does not mean neutrality. Every chart is selective. But it must not be deceptive. We are not neutral, but we are responsible.

The phrase "lying with statistics" has been around for over a century. Darrell Huff's book *How to Lie with Statistics* is still quoted because the problems it identified never went away. Truncated y-axes, distorted proportions, misleading averages, selective samples, overuse of 3D --- these visual lies have taken new forms in modern dashboards and interactive plots.

But the harm is no longer just a misleading infographic in a magazine. Today, charts drive decision-making software, shape investor dashboards, and power policy models. If we mislead through visual design --- whether intentionally or due to carelessness --- we produce real-world consequences.

Here's the test: If someone reads your chart and walks away with the wrong conclusion, even though you showed "the data," you failed.

So how do we get it right?

We start by respecting the cognitive burden of interpretation. People are busy. They glance. They skim. Their brains are wired for patterns, not precision. If your graph hints at a relationship, they will assume one. If your bar chart exaggerates a difference, they will believe the difference is large --- even if the numbers are close.

This chapter teaches you how to avoid those traps. You will learn to create plots that respect your audience's time and attention. You will learn to highlight the signal and suppress the noise. You will learn to use tools like Matplotlib, Seaborn, Plotly, Altair, and Streamlit to build graphics that are not only correct, but useful.

But we begin with the core principle: Your visualizations must tell the truth. If they don't, your analytics has no value.

#### **Foundations of Good Visual Communication**
Clear charts do not emerge by accident. They are built on a foundation of design principles that reduce friction between the data and the viewer's understanding. This is not about beauty or artistic style. It is about signal clarity.

Start with the principle of simplicity. Simplicity is not minimalism for its own sake. It means showing what matters and removing what doesn't. Every pixel on the screen should serve a purpose. If it doesn't, get rid of it.

The term chartjunk refers to unnecessary visual elements that clutter a plot --- shadows, gradient fills, 3D bars, glossy effects, unnecessary labels, clipart, and dense grid lines. These add noise without meaning. Edward Tufte coined the term and spent decades fighting it. In his books, especially *The Visual Display of Quantitative Information*, he argues for a high data-ink ratio: the proportion of a graphic's ink devoted to data rather than decoration.

Tufte's philosophy encourages a clean, direct, and meaningful presentation of data. He values subtlety and trust in the viewer's intelligence. This does not mean avoiding emphasis --- it means emphasizing only what matters.

One of the most important tools for emphasis is color. Used well, color draws attention to key features. Used poorly, it confuses and misleads. You do not need a rainbow palette. You need contrast, harmony, and consistency. Color should do one of three things: group items, differentiate them, or direct the eye. For dashboards, this often means using muted tones for background data and one bold color for the current value or anomaly.

But color comes with ethical responsibility. Not all viewers perceive it the same way. Use colorblind-friendly palettes when possible. Do not rely on red/green distinctions alone. Test your plots in grayscale. Your insights should not depend on color alone to be legible.

Alignment and scale matter too. A common mistake is to misalign plots with inconsistent y-axes, or use dual axes without clarifying what's being compared. When in doubt, use a single axis and annotate directly. Tufte recommends eliminating legends by labeling series directly within the plot. This reduces eye movement and enhances understanding.

Another Tufte insight: avoid the "duck" --- a graphic that draws more attention to its visual flourish than its content. He borrows the term from architecture, where buildings shaped like ducks were once popular for advertising. In charts, a duck is a visual stunt. The goal is to build bridges, not ducks.

These principles apply whether you're building a single figure or a full dashboard. The job of the visualizer is to guide, not overwhelm. The user should not have to decode the chart. The story should reveal itself naturally through the layout, typography, and contrast.

Next, we turn to dashboards --- how they function, who they serve, and how their design principles differ.

#### **Strategic Use of Dashboards**
A dashboard is a system of charts arranged to answer a set of questions at a glance. It is meant to be consulted, not read. And its design should reflect its purpose.

Broadly, there are two categories of dashboards: those for executives and those for operations. Each has a different audience, rhythm, and visual grammar.

Executive dashboards are strategic. Their job is to present a limited set of Key Performance Indicators (KPIs) that summarize the health of a business unit, product line, or market segment. These metrics should not require interpretation. They should be self-evident, clearly labeled, and updated on a consistent schedule --- daily, weekly, or monthly. Executive dashboards are read on phones and laptops, glanced at between meetings, and shared with other stakeholders. That means you must eliminate anything that adds cognitive load.

Keep it simple. Use horizontal bar charts for rankings. Use line charts for trends. Use big numbers with arrows and percentage deltas to signal direction. Avoid interactivity unless it directly supports exploration of trends over time or segmentation by category.

Operational dashboards are tactical. They show what's happening right now. Think of a logistics dashboard tracking shipments, or a factory monitoring throughput and machine state. These dashboards are closer to instrumentation than to storytelling. They must respond to real-time data, highlight anomalies, and offer drill-down paths for diagnosis.

Here, layout becomes critical. You may need visual hierarchy (top-down or left-right), alert zones (red or yellow indicators), and modular cards. Colors must signal status: green for within bounds, yellow for warning, red for out-of-bounds. But resist the urge to use color for decoration. If everything is red, nothing is urgent.

Some dashboards are temporal, showing how metrics shift over time. These need consistent time axes, side-by-side comparisons, and careful use of smoothing or rolling averages. Time series charts should always use consistent intervals and mark gaps in the data explicitly.

You also need to consider layout design. The most common layouts follow either a rule-of-thirds grid (dividing the screen into three clear zones) or a Z-pattern (left to right, top to bottom, following the eye's natural motion). Avoid stacking similar visuals --- group by function or category. Prioritize top-left placement for the most important metric. If users scroll to see key data, the dashboard has failed.

Tools like Streamlit make it easy to convert Python notebooks into dashboards. But ease of creation does not guarantee quality of presentation. You must still define your audience, their goals, and the rhythms of their use. You must decide what stays visible at all times and what is accessible only through filters or tabs.

The dashboard is a lens. Your job is to polish it until the signal is clear.

#### **Visualization Libraries in Python**
Python provides several mature and flexible libraries for data visualization. Each one reflects a different philosophy. Understanding these differences helps you choose the right tool for the task.

**Matplotlib** is the foundational library. Almost every other visualization library in Python builds on it. Think of it as a low-level drawing interface --- precise, stable, and endlessly customizable. It supports every chart type you might need: line plots, bar charts, histograms, scatter plots, pie charts, and more. But it can be verbose. You must specify many parameters directly, which gives you control but requires discipline.

Use Matplotlib when you need publication-quality plots, when you want full control over every axis and label, or when integrating with other scientific libraries like NumPy, pandas, or SciPy. Matplotlib is also ideal when you want to export vector graphics, control font rendering, or embed plots in reports.

**Seaborn** builds on Matplotlib and focuses on statistical plotting. It simplifies common tasks: showing distributions, adding confidence intervals, fitting regression lines, comparing grouped data, and building heatmaps. Seaborn manages color palettes, figure aesthetics, and subplot alignment automatically.

Use Seaborn when you want to explore relationships quickly and cleanly. It handles grouped data directly from pandas DataFrames and adjusts plot elements to highlight statistical insights. Seaborn makes it easy to spot correlations, clusters, and anomalies in structured data.

**Plotly** shifts to interactivity. It creates web-native, zoomable, clickable, and animated charts. It supports many advanced types: treemaps, sunbursts, 3D plots, choropleths, and time sliders. It works well in Jupyter notebooks and can be embedded into dashboards or exported as HTML.

Use Plotly when you need to interact with your data, hover over points for details, or build charts that adapt as users click and zoom. It is excellent for storytelling, public dashboards, and exploratory analysis where readers control the lens.

**Altair** is different. It is declarative: you don't describe how to draw the chart, you describe what the chart means. Altair uses a grammar of graphics based on Vega-Lite. This means every chart is a statement about encoding --- mapping data fields to visual properties like position, color, shape, or size.

Use Altair when you want to create layered or faceted charts with minimal code. It's perfect for filtering, highlighting, brushing, and other interactive behaviors. Altair is more expressive than it is flexible. It won't give you the same control as Matplotlib, but it will give you clarity and speed.

**Streamlit** is an application framework. It lets you turn Python scripts into web apps with widgets, sliders, and dropdowns. You can display Matplotlib, Plotly, and Altair charts inside a Streamlit app and add interactivity without writing HTML or JavaScript.

Use Streamlit when you want to share your analysis with non-technical users, build quick prototypes, or construct dashboards where filters and inputs matter. It's especially useful for data teams that want to distribute insights without deploying a full web app.

Together, these libraries cover almost every visualization need in business analytics. In the next section, we build examples using each tool and compare their outputs in practice.

#### **Examples and Implementations**
Let's walk through practical examples that demonstrate how each visualization tool functions in Python. These examples use the same dataset to highlight style, syntax, and strengths across tools. We'll use a simple but realistic dataset: monthly sales data across three regions.

Start by creating a sample DataFrame:

```python
import pandas as pd
import numpy as np

np.random.seed(42)
months = pd.date_range("2022-01-01", periods=12, freq="M")
regions = ["North", "South", "West"]
data = {
    "Month": np.tile(months, len(regions)),
    "Region": np.repeat(regions, len(months)),
    "Sales": np.random.randint(90, 150, size=len(months) * len(regions))
}
df = pd.DataFrame(data)
```

**Time Series Plot with Matplotlib and Seaborn**

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="Month", y="Sales", hue="Region", marker="o")
plt.title("Monthly Sales by Region", fontsize=14, weight="bold")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_seaborn.png", dpi=300)
plt.show()
```


This shows a clear line chart with region-specific colors and trend lines. It uses Seaborn for simplicity but relies on Matplotlib for axis control and styling.

**Interactive Plot with Plotly**

```python
import plotly.express as px

fig = px.line(df, x="Month", y="Sales", color="Region",
              markers=True, title="Monthly Sales by Region")
fig.update_layout(title_font=dict(size=18), template="simple_white")
fig.show()
```


Users can hover over points, zoom in, and export the plot. Plotly is ideal when you need interaction without additional dashboard logic.

**Annotated Bar Chart with Altair**

```python
import altair as alt

alt_df = df[df["Month"].dt.month == 6]  # Filter to show June sales
bar = alt.Chart(alt_df).mark_bar().encode(
    x=alt.X("Region:N", title="Region"),
    y=alt.Y("Sales:Q", title="Sales"),
    color="Region:N"
).properties(title="June Sales by Region")
text = bar.mark_text(
    align="center", baseline="bottom", dy=-2
).encode(text="Sales:Q")
(bar + text).configure_view(stroke=None).show()
```


Altair uses declarative syntax to stack and annotate bars automatically, ideal for quick faceted or annotated views.

**Streamlit Dashboard**

Save the following as `app.py` and run with `streamlit run app.py`:

```python
import streamlit as st

st.title("Regional Sales Dashboard")
selected_region = st.selectbox("Select Region", df["Region"].unique())
filtered = df[df["Region"] == selected_region]
st.line_chart(filtered.set_index("Month")["Sales"])
st.metric("Average Sales", f"{filtered['Sales'].mean():.2f}")
st.metric("Max Sales", f"{filtered['Sales'].max()}")
if st.checkbox("Show raw data"):
    st.write(filtered)
```


This dashboard allows filtering by region, displays line charts, KPIs, and optional raw data. It demonstrates how to move from analysis to app with no web dev experience.

- Matplotlib: full control, sharp output, best for reports.
- Seaborn: concise, statistical, well-aligned.
- Plotly: interactive, modern, web-friendly.
- Altair: declarative, expressive, minimalist.
- Streamlit: full dashboard with inputs, good for sharing.

Each tool serves a purpose. The skill lies in choosing the right one for the audience, the question, and the context.

#### **Wrapping Up**
Visualization is not about drawing. It's about thinking. The process of building a plot forces you to ask what story the data tells, and how to make that story clear to someone else. This is where analytical skill meets design judgment.

You now have a foundation in both theory and practice. You've seen that honest visualization begins with intent. It continues with clarity --- removing chartjunk, avoiding misleading scales, choosing color with care, and respecting cognitive limits. These choices are not aesthetic flourishes. They are ethical responsibilities.

You've also learned that different audiences demand different tools. A time-constrained executive needs a dashboard that communicates instantly. An operator needs one that alerts, filters, and refreshes. A data scientist might want interactivity to explore patterns. A decision-maker might just want a clear answer. Your tools --- Matplotlib, Seaborn, Plotly, Altair, Streamlit --- give you a wide spectrum of options. But they are only as effective as the logic that guides them.

You must ask: what am I showing, to whom, and why?

There is no default answer. The same data can be shown as a static bar chart in a report, as an interactive heatmap on the web, or as a KPI tile in a live dashboard. The best visualizations make those choices intentionally. They do not merely "visualize." They inform, guide, and sometimes provoke. But they never confuse.

In an age where dashboards shape decisions at scale --- governing budgets, directing attention, even triggering automation --- the stakes are high. Clear thinking leads to clear plots. And clear plots lead to better decisions.

Your job as an analyst is to show (truthfully and thoughtfully). To show in a way that lets people see.
