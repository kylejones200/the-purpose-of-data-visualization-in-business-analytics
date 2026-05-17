import logging

import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st


def prepare_fig(df) -> None:
    fig = px.line(
        df,
        x="Month",
        y="Sales",
        color="Region",
        markers=True,
        title="Monthly Sales by Region",
    )

    fig.update_layout(title_font={"size": 18}, template="simple_white")

    fig.show()

    alt_df = df[df["Month"].dt.month == 6]

    bar = (
        alt.Chart(alt_df)
        .mark_bar()
        .encode(
            x=alt.X("Region:N", title="Region"),
            y=alt.Y("Sales:Q", title="Sales"),
            color="Region:N",
        )
        .properties(title="June Sales by Region")
    )

    text = bar.mark_text(align="center", baseline="bottom", dy=-2).encode(
        text="Sales:Q"
    )

    (bar + text).configure_view(stroke=None).show()

    np.random.seed(42)

    st.title("Regional Sales Dashboard")

    selected_region = st.selectbox("Select Region", df["Region"].unique())

    filtered = df[df["Region"] == selected_region]

    st.line_chart(filtered.set_index("Month")["Sales"])

    st.metric("Average Sales", f"{filtered['Sales'].mean():.2f}")

    st.metric("Max Sales", f"{filtered['Sales'].max()}")

    if st.checkbox("Show raw data"):
        st.write(filtered)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    months = pd.date_range("2022-01-01", periods=12, freq="M")

    regions = ["North", "South", "West"]

    data = {
        "Month": np.tile(months, len(regions)),
        "Region": np.repeat(regions, len(months)),
        "Sales": np.random.randint(90, 150, size=len(months) * len(regions)),
    }

    df = pd.DataFrame(data)

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
    prepare_fig(df)


if __name__ == "__main__":
    main()
