```bash
head -n 2 COMP370/homework/311_Service_Requests_from_2010_to_Present_20250928.csv
head -n 1 COMP370/homework/311_Service_Requests_from_2010_to_Present_20250928.csv > COMP370/homework/311_2024.csv
awk -F',' '$3 ~ /2024/' COMP370/homework/311_Service_Requests_from_2010_to_Present_20250928.csv >> COMP370/homework/311_2024.csv # take only 2024 data
awk -F',' 'NR==1 || $9 != ""' COMP370/homework/311_2024.csv > COMP370/homework/311_2024_z.csv # take only rows with valid zip codes
awk -F',' 'NR==1 || ((substr($3,7,4) substr($3,1,2) substr($3,4,2)) >= (substr($2,7,4) substr($2,1,2) substr($2,4,2)))' 311_2024_z.csv > 311.csv # rewrite date format and filter out invalid dates
```