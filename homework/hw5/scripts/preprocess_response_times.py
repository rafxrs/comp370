#!/usr/bin/env python3
import pandas as pd
from datetime import datetime

INPUT = "311.csv" 
OUTPUT = "monthly_response_times_by_zip.csv"

def main():
    print("Loading data...")
    df = pd.read_csv(INPUT, low_memory=False)

    # Ensure proper datetime parsing
    df["Created Date"] = pd.to_datetime(df["Created Date"], errors="coerce")
    df["Closed Date"] = pd.to_datetime(df["Closed Date"], errors="coerce")

    # Compute response time in hours
    df = df.dropna(subset=["Created Date", "Closed Date"])
    df["response_hours"] = (df["Closed Date"] - df["Created Date"]).dt.total_seconds() / 3600

    # Keep only valid and positive durations
    df = df[df["response_hours"] > 0]

    # Extract month for grouping
    df["month"] = df["Created Date"].dt.to_period("M").astype(str)

    # Compute average response time per (month, zip)
    monthly_zip = (
        df.groupby(["Incident Zip", "month"])["response_hours"]
        .mean()
        .reset_index()
    )

    # Compute overall citywide averages
    monthly_all = (
        df.groupby("month")["response_hours"]
        .mean()
        .reset_index()
    )
    monthly_all["Incident Zip"] = "ALL"

    # Combine and save
    out = pd.concat([monthly_zip, monthly_all])
    out.to_csv(OUTPUT, index=False)
    print(f"Saved {OUTPUT} with {len(out)} rows")

if __name__ == "__main__":
    main()