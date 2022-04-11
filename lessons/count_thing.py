
from data_utils import read_csv_rows
from data_utils import columnar
from data_utils import head
from tabulate import tabulate
from data_utils import select
from data_utils import count


SURVEY_DATA_CSV_FILE_PATH: str = "../../data/survey.csv"
data_rows: list[dict[str, str]] = read_csv_rows(SURVEY_DATA_CSV_FILE_PATH)

if len(data_rows) == 0:
    print("Go implement read_csv_rows in data_utils.py")
    print("Be sure to save your work before re-evaluating this cell!")
else:
    print(f"Data File Read: {SURVEY_DATA_CSV_FILE_PATH}")
    print(f"{len(data_rows)} rows")
    print(f"{len(data_rows[0].keys())} columns")
    print(f"Columns names: {data_rows[0].keys()}")


data_cols: dict[str, list[str]] = columnar(data_rows)

if len(data_cols.keys()) == 0:
    print("Complete your implementation of columnar in data_utils.py")
    print("Be sure to follow the guidelines above and save your work before re-evaluating!")
else:
    print(f"{len(data_cols.keys())} columns")
    # print(f"{len(data_cols['subject_age'])} rows")
    print(f"Columns names: {data_cols.keys()}")


data_cols_head: dict[str, list[str]] = head(data_cols, 25)

if len(data_cols_head.keys()) != len(data_cols.keys()) or len(data_cols_head["year"]) != 25:
    print("Complete your implementation of columnar in data_utils.py")
    print("Be sure to follow the guidelines above and save your work before re-evaluating!")

tabulate(data_cols_head, data_cols_head.keys(), "html")

selected_data: dict[str, list[str]] = select(data_cols,["row", "year", "hours_online_work", "ls_effective", "programming_effective"])  

tabulate(head(selected_data, 25), selected_data.keys(), "html")


hours_online_work_counts: dict[str, int] = count(selected_data["hours_online_work"])
print(f"hours_online_work: {hours_online_work_counts}")

ls_effective_counts: dict[str, int] = count(selected_data["ls_effective"])
print(f"lesson_time: {ls_effective_counts}")

programming_effective_counts: dict[str, int] = count(selected_data["programming_effective"])
print(f"Programming_effectiveness: {programming_effective_counts}")