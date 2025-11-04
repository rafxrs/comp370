# Task 3 Explore My Little Pony Dataset Properties
Use the command line tools to answer the following questions:
-	How big is the dataset? 
```bash
wc -l data/clean_dialog.csv
```
It contains 36860 lines with headers so 36859 data points.

-	What’s the structure of the data? (i.e., what are the field and what are values in them) 
```bash
head -n 2 data/clean_dialog.csv 
```
There are 4 fields: title, writer, pony, dialog. The title field contains the episode title, the writer field contains the name of the writer of the episode, the pony field contains the name of the pony speaking the dialog, and the dialog field contains the actual dialog spoken by the pony.

-	How many episodes does it cover? 
```bash
cut -d',' -f1 data/clean_dialog.csv | sort | uniq | wc -l 
```
it covers 196 episodes. (this command outputs 197 but one of them is the header)

-	During the exploration phase, find at least one aspect of the dataset that is unexpected – meaning that it seems like it could create issues for later analysis.
```bash
shuf -n 10 data/clean_dialog.csv
```
By running this command a few times we see things in the dialog field like ad libs and unicode characters -> "[flashback]" or "[sigh]" as well as ""You<U+0097> you<U+0097> you are terminated"

# Task 4 Analyze speaker frequency
Use the grep tool to determine how often each MAIN (Twilight Sparkle, Rarity, Pinkie Pie, Rainbow Dash, and Fluttershy) pony speaks.
Now calculate the percent of lines that each pony has over the entire dataset (including all characters).
```bash
touch data/Line_percentages.csv
echo "pony_name,total_line_count,percent_all_lines" > data/Line_percentages.csv
total=$(( $(wc -l < data/clean_dialog.csv) - 1 ))  # subtract 1 for header
twilight=$(cut -d',' -f3 data/clean_dialog.csv | grep -c "Twilight Sparkle")
rarity=$(cut -d',' -f3 data/clean_dialog.csv | grep -c "Rarity")
pinkie=$(cut -d',' -f3 data/clean_dialog.csv | grep -c "Pinkie Pie")
rainbow=$(cut -d',' -f3 data/clean_dialog.csv | grep -c "Rainbow Dash")
fluttershy=$(cut -d',' -f3 data/clean_dialog.csv | grep -c "Fluttershy")
pct() {
  echo "scale=2; $1 * 100 / $total" | bc
}
echo "Twilight Sparkle,$twilight,$(pct $twilight)" >> data/Line_percentages.csv
echo "Rarity,$rarity,$(pct $rarity)" >> data/Line_percentages.csv
echo "Pinkie Pie,$pinkie,$(pct $pinkie)" >> data/Line_percentages.csv
echo "Rainbow Dash,$rainbow,$(pct $rainbow)" >> data/Line_percentages.csv
echo "Fluttershy,$fluttershy,$(pct $fluttershy)" >> data/Line_percentages.csv
```
This counts how many lines each main pony has spoken and writes the line count and percentage to Line_percentages.csv

pony_name,total_line_count,percent_all_lines
Twilight Sparkle,4381,11.88
Rarity,2433,6.60
Pinkie Pie,2690,7.29
Rainbow Dash,2848,7.72
Fluttershy,2045,5.54

