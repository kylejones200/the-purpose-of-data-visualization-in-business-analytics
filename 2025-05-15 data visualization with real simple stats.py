"""Generated from Jupyter notebook: 2025-05-15 data visualization with real simple stats

Magics and shell lines are commented out. Run with a normal Python interpreter."""


# --- code cell ---

# !pip install real-simple-stats  # Jupyter-only


# --- code cell ---

from real_simple_stats import lookup, mean, z_score

print(mean([1, 2, 3]))
print(z_score(85, 80, 5))
print(lookup("μ"))  # Population mean


# --- code cell ---

import pandas as pd

# Load the dataset
df = pd.read_csv("CalaverasData.csv")
df = df[df["jump #"].isin([1, 2])]
df = df[["jump distance", "jump #", "rent/ind/pro"]].dropna()
df.columns = ["jump_distance", "jump_number", "group"]

# Extract jump1 values
jump1_values = df[df["jump_number"] == 1]["jump_distance"].tolist()

# Display values to validate before updating tutorial code
jump1_values[:5], df.head()


# --- code cell ---

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from real_simple_stats.descriptive_statistics import (
    coefficient_of_variation,
    draw_cumulative_frequency_table,
    draw_frequency_table,
    five_number_summary,
    interquartile_range,
    is_continuous,
    is_discrete,
    mean,
    median,
    sample_std_dev,
    sample_variance,
)

# Load and clean the dataset
df = pd.read_csv("CalaverasData.csv")
df = df[df["jump #"].isin([1, 2])]
df = df[["jump distance", "jump #", "rent/ind/pro"]].dropna()
df.columns = ["jump_distance", "jump_number", "group"]

# Filter to Jump #1
jump1 = df[df["jump_number"] == 1]["jump_distance"].tolist()

# Basic stats
print("➡️ Mean:", mean(jump1))
print("➡️ Median:", median(jump1))
print("➡️ Sample Standard Deviation:", sample_std_dev(jump1))
print("➡️ Sample Variance:", sample_variance(jump1))
print("➡️ Coefficient of Variation (%):", coefficient_of_variation(jump1))
print("➡️ Interquartile Range:", interquartile_range(jump1))
print("➡️ Five Number Summary:", five_number_summary(jump1))

# Variable type
print("➡️ Is Discrete?", is_discrete(jump1))
print("➡️ Is Continuous?", is_continuous(jump1))

# Group Frequency Table
group_labels = df[df["jump_number"] == 1]["group"].astype(str).tolist()
freq_table = draw_frequency_table(group_labels)
print("➡️ Frequency Table (Group):", freq_table)

# Cumulative Frequency Table (rounded distances for grouping)
jump1_rounded = [round(x) for x in jump1 if x > 0]
cum_freq_table = draw_cumulative_frequency_table(jump1_rounded)
print("➡️ Cumulative Frequency Table (Jump1 rounded):", cum_freq_table)

# --- Plots ---

# Histogram
plt.hist(jump1, bins=15, color="black", edgecolor="white")
plt.title("Histogram of Jump 1 Distances")
plt.xlabel("Distance (cm)")
plt.ylabel("Frequency")
plt.savefig("jump1_hist.png")
plt.show()

# Boxplot
plt.boxplot(jump1, vert=False)
plt.title("Boxplot of Jump 1 Distances")
plt.xlabel("Distance (cm)")
plt.savefig("jump1_box.png")
plt.show()

# Violin plot by group
jump1_df = df[df["jump_number"] == 1]
sns.violinplot(data=jump1_df, x="group", y="jump_distance")
plt.title("Jump 1 Distance by Group (Rent/Ind/Pro)")
plt.xlabel("Group")
plt.ylabel("Jump Distance (cm)")
plt.savefig("jump1_violin.png")
plt.show()


# --- code cell ---

from real_simple_stats.descriptive_statistics import mean, sample_std_dev
from real_simple_stats.normal_distributions import normal_cdf, normal_pdf

mu = mean(jump1)
sigma = sample_std_dev(jump1)

xs = [x for x in range(100, 200)]
ys_pdf = [normal_pdf(x, mu, sigma) for x in xs]
ys_cdf = [normal_cdf(x, mu, sigma) for x in xs]

# Plot PDF
plt.plot(xs, ys_pdf, color="black")
plt.title("Normal PDF of Jump 1 Distances")
plt.xlabel("Jump Distance (cm)")
plt.ylabel("Density")
plt.savefig("jump1_normal_pdf.png")
plt.show()

# Plot CDF
plt.plot(xs, ys_cdf, color="black")
plt.title("Normal CDF of Jump 1 Distances")
plt.xlabel("Jump Distance (cm)")
plt.ylabel("Cumulative Probability")
plt.savefig("jump1_normal_cdf.png")
plt.show()


# --- code cell ---

import matplotlib.pyplot as plt
import numpy as np


def set_minimalist_style():
    """Apply a Tufte-inspired minimalist style to Matplotlib."""
    plt.rcParams.update(
        {
            "font.family": "serif",
            "axes.spines.right": False,
            "axes.spines.top": False,
            "axes.edgecolor": "black",
            "axes.linewidth": 0.8,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "xtick.major.size": 4,
            "ytick.major.size": 4,
            "axes.labelsize": 12,
            "axes.titlesize": 13,
            "legend.frameon": False,
            "axes.grid": False,
            "grid.color": "white",
        }
    )


def plot_norm_hist(
    data, mean, std, bins=30, show_pdf=True, show_lines=True, title=True
):
    """Plot a histogram of data with optional normal curve and markers."""
    set_minimalist_style()

    _, bins_edges, _ = plt.hist(
        data, bins=bins, density=True, alpha=0.5, edgecolor="black"
    )

    if show_pdf:
        x = np.linspace(min(bins_edges), max(bins_edges), 300)
        y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * std**2))
        plt.plot(x, y, color="black", linewidth=1.5)

    if show_lines:
        plt.axvline(mean - 2 * std, color="black", linestyle="--", linewidth=1)
        plt.axvline(mean + 2 * std, color="black", linestyle="--", linewidth=1)

    if title:
        plt.title(f"Normal Distribution (μ = {mean:.2f}, σ = {std:.2f})")

    plt.savefig("norm_hist.png", bbox_inches="tight", dpi=300)
    plt.show()


def plot_box(data, showfliers=False):
    """Plot a horizontal boxplot without outliers."""
    set_minimalist_style()

    fig, ax = plt.subplots()
    ax.boxplot(
        data,
        vert=False,
        showfliers=showfliers,
        patch_artist=True,
        boxprops=dict(facecolor="white", edgecolor="black"),
        whiskerprops=dict(color="black"),
        capprops=dict(color="black"),
        medianprops=dict(color="black"),
    )

    ax.set_title("Boxplot")

    plt.savefig("boxplot.png", bbox_inches="tight", dpi=300)
    plt.show()


# --- code cell ---

import numpy as np

mu, sigma = 50, 10
data = np.random.normal(mu, sigma, 1000)

plot_norm_hist(data, mu, sigma)
plot_box(data)


# --- code cell ---

import matplotlib.pyplot as plt
import numpy as np


def set_minimalist_style():
    """Apply a Tufte-inspired minimalist style to Matplotlib."""
    plt.rcParams.update(
        {
            "font.family": "serif",
            "axes.spines.right": False,
            "axes.spines.top": False,
            "axes.edgecolor": "black",
            "axes.linewidth": 0.8,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "xtick.major.size": 4,
            "ytick.major.size": 4,
            "axes.labelsize": 12,
            "axes.titlesize": 13,
            "legend.frameon": False,
            "axes.grid": False,
            "grid.color": "white",
        }
    )


def plot_norm_hist(
    data, mean, std, bins=30, show_pdf=True, show_lines=True, title=True
):
    """Plot a histogram of data with optional normal curve and markers."""
    set_minimalist_style()

    _, bins_edges, _ = plt.hist(
        data, bins=bins, density=True, alpha=0.5, edgecolor="black"
    )

    if show_pdf:
        x = np.linspace(min(bins_edges), max(bins_edges), 300)
        y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * std**2))
        plt.plot(x, y, color="black", linewidth=1.5)

    if show_lines:
        plt.axvline(mean - 2 * std, color="black", linestyle="--", linewidth=1)
        plt.axvline(mean + 2 * std, color="black", linestyle="--", linewidth=1)

    if title:
        plt.title(f"Normal Distribution (μ = {mean:.2f}, σ = {std:.2f})")

    plt.savefig("norm_hist.png", bbox_inches="tight", dpi=300)
    plt.show()


def plot_box(data, showfliers=False):
    """Plot a horizontal boxplot without outliers."""
    set_minimalist_style()

    fig, ax = plt.subplots()
    ax.boxplot(
        data,
        vert=False,
        showfliers=showfliers,
        patch_artist=True,
        boxprops=dict(facecolor="white", edgecolor="black"),
        whiskerprops=dict(color="black"),
        capprops=dict(color="black"),
        medianprops=dict(color="black"),
    )

    ax.set_title("Boxplot")

    plt.savefig("boxplot.png", bbox_inches="tight", dpi=300)
    plt.show()


if __name__ == "__main__":
    # Example usage
    import numpy as np

    mu, sigma = 50, 10
    data = np.random.normal(mu, sigma, 1000)

    plot_norm_hist(data, mu, sigma)
    plot_box(data)
