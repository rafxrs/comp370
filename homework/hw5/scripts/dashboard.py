from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Select, LegendItem
from bokeh.plotting import figure
from bokeh.layouts import column
import pandas as pd

# Load preprocessed data
df = pd.read_csv("monthly_response_times_by_zip.csv")
df = df[df["month"].str.startswith("2024-")]
months = sorted(df["month"].unique())


# Separate overall data
df_all = df[df["Incident Zip"] == "ALL"]

# Define available zipcodes (exclude ALL and NaN)
zipcodes = sorted(z for z in df["Incident Zip"].unique() if str(z) != "ALL" and pd.notna(z))
default_zip1, default_zip2 = zipcodes[0], zipcodes[1]

# Function to extract monthly data for a given zipcode
def zip_data(zipcode):
    data = df[df["Incident Zip"] == zipcode]
    return pd.DataFrame({"month": months}).merge(data, on="month", how="left").fillna(0)

# Data sources
src_all = ColumnDataSource(zip_data("ALL"))
src_zip1 = ColumnDataSource(zip_data(default_zip1))
src_zip2 = ColumnDataSource(zip_data(default_zip2))

# Create figure
p = figure(
    title="Monthly Average Response Time by Zip (2024)",
    x_range=months,
    height=400, width=700,
    x_axis_label="Month", y_axis_label="Response Time (hours)",
    toolbar_location=None
)
p.background_fill_color = "#fafafa"
p.border_fill_color = "white"
p.outline_line_color = None


# Add line renderers and keep references
r_all = p.line("month", "response_hours", source=src_all, color="black", line_width=2, legend_label="All 2024")
r_zip1 = p.line("month", "response_hours", source=src_zip1, color="steelblue", line_width=2, legend_label=f"Zip {default_zip1}")
r_zip2 = p.line("month", "response_hours", source=src_zip2, color="tomato", line_width=2, legend_label=f"Zip {default_zip2}")

p.legend.location = "top_left"
p.xaxis.major_label_orientation = 1.2

# Dropdowns
select1 = Select(title="Zipcode 1:", value=default_zip1, options=[str(z) for z in zipcodes])
select2 = Select(title="Zipcode 2:", value=default_zip2, options=[str(z) for z in zipcodes])

# Callback
def update_plot(attr, old, new):
    zip1, zip2 = select1.value, select2.value

    # Update data sources
    src_zip1.data = dict(ColumnDataSource(zip_data(zip1)).data)
    src_zip2.data = dict(ColumnDataSource(zip_data(zip2)).data)

    # Rebuild legend safely
    p.legend.items = [
        LegendItem(label="All 2024", renderers=[r_all]),
        LegendItem(label=f"Zip {zip1}", renderers=[r_zip1]),
        LegendItem(label=f"Zip {zip2}", renderers=[r_zip2]),
    ]

# Wire dropdowns to callback
select1.on_change("value", update_plot)
select2.on_change("value", update_plot)

# Layout
curdoc().add_root(column(select1, select2, p))
curdoc().title = "311 Response Time Dashboard"
