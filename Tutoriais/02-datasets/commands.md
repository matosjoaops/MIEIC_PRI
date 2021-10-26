# Tasks

## 1
in2csv example.xlsx > example.csv
## 2
csvcut -c ' "Wins"' example.csv (| csvlook)
## 3
csvgrep -c Team -r ".*y.*" example.csv
## 3 (count lines)
csvgrep -c Team -r ".*y.*" example.csv | wc -l
