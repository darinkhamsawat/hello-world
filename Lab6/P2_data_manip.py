""" 
Darin Khamsawat
683040489-2
P2
"""
import json
import pandas as pd
import pyqtgraph as pg

from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

REQUIRED_COLS = {"date", "city", "temp_c", "humidity", "rainfall_mm", "condition"}
CONDITIONS    = ["Sunny", "Cloudy", "Rainy", "Stormy"]
CITIES        = ["Bangkok", "Chiang Mai", "Phuket"]



def _normalize_columns(df):
    df.columns = df.columns.str.lower()
    return df


# TODO 1
def read_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    df = _normalize_columns(df)

    if df.empty:
        raise ValueError("CSV file is empty")

    if not REQUIRED_COLS.issubset(df.columns):
        raise ValueError("Missing required columns")

    return df


# TODO 2

def read_json(path: str) -> pd.DataFrame:
    df = pd.read_json(path)

    df = _normalize_columns(df)

    if df.empty:
        raise ValueError("JSON file is empty")

    if not REQUIRED_COLS.issubset(df.columns):
        raise ValueError("Missing required columns")

    return df


# TODO 3
def write_csv(df: pd.DataFrame, path: str) -> None:
    if df is None or df.empty:
        raise ValueError("No data to save")

    df.to_csv(path, index=False)



# TODO 4
def write_json(df: pd.DataFrame, path: str) -> None:
    if df is None or df.empty:
        raise ValueError("No data to save")

    df.to_json(path, orient="records", indent=4)


# TODO 5

def build_stats(df: pd.DataFrame) -> QTableWidget:
    df = _normalize_columns(df)

    if df is None or df.empty:
        raise ValueError("No data")

    grouped = df.groupby("city")

    stats = {
        "avg_temp": grouped["temp_c"].mean().round(1),
        "max_temp": grouped["temp_c"].max().round(1),
        "min_temp": grouped["temp_c"].min().round(1),
        "total_rain": grouped["rainfall_mm"].sum().round(1),
        "avg_humidity": grouped["humidity"].mean().round(1),
    }

    table = QTableWidget()
    table.setRowCount(len(stats))
    table.setColumnCount(len(stats["avg_temp"]))

    table.setVerticalHeaderLabels(list(stats.keys()))
    table.setHorizontalHeaderLabels(stats["avg_temp"].index.tolist())

    for row, key in enumerate(stats):
        for col, value in enumerate(stats[key]):
            table.setItem(row, col, QTableWidgetItem(str(value)))

    return table


# TODO 6

def show_chart(df: pd.DataFrame, chart_type: str) -> pg.PlotWidget:
    df = _normalize_columns(df)

    if df is None or df.empty:
        raise ValueError("No data")

    data = df["rainfall_mm"]

    counts, bins = pd.cut(data, bins=10, retbins=True)
    counts = counts.value_counts().sort_index()

    plot = pg.PlotWidget()
    plot.setTitle("Rainfall Histogram")

    x_vals = list(range(len(counts)))
    y_vals = counts.values

    bar = pg.BarGraphItem(x=x_vals, height=y_vals, width=0.6)
    plot.addItem(bar)

    return plot