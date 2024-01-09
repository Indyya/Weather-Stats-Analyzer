"""A project about weather stats."""


__author__ = "730430031"


import sys


from typing import Dict, List
from csv import DictReader


READ_MODE = "r"


def main() -> None:
    """Entrypoint to our program."""
    args: Dict[str, str] = read_args()
    results: List[float] = list(args["file"], args["column"])
    if args["operation"] == "min":
        print(min(results))
    elif args["operation"] == "max":
        print(max(results))
    elif args["operation"] == "avg":
        print(sum(results) / len(results))
    elif args["operation"] == "chart":
        column: List[float] = list(args["file"], args["column"])
        date: List[str] = listsdates(args["file"]) 
        chart_data(column, date) 
    elif args["operation"] == "list":
        print(results)
    else:
        print("Invalid operation: " + args["operation"])
        exit()


def read_args() -> Dict[str, str]:
    """Check for valid CLI argumnets and return them in a dictionary."""
    if len(sys.argv) != 4:
        raise ValueError("Usage: python -m lessons.ls29_questions [FILE] [COLUMN] [OPERATION]")
    return {
        "file": sys.argv[1],
        "column": sys.argv[2],
        "operation": sys.argv[3]
    
    }


def list(file: str, column: str) -> List[float]:
    """Opens file_path, reads each line, returns a List of lines w/keyword."""
    matches: List[float] = []
    file_handle = open(file, "r", encoding="utf8")  # The path to the CSV FILE to process
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        if column not in row.keys():
            print("Invalid column: " + column)
            exit()
        if row["REPORT_TYPE"] == "SOD  ":
            try:
                matches.append(float(row[column]))
            except ValueError: 
                ...
    file_handle.close()
    return matches


def listsdates(file: str) -> List[str]:
    """Opens file_path, reads each line, returns a List of lines w/keyword."""
    matches: List[str] = []
    file_handle = open(file, "r", encoding="utf8")  # The path to the CSV FILE to process
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        if row["REPORT_TYPE"] == "SOD  ":
            matches.append(row["DATE"][0:10])
    file_handle.close()
    return matches


def read_float_data(file: str) -> Dict[str, float]:
    """Given a filename, read its contests and count its charater."""
    counts: Dict[str, float] = {}
    file_handle = open(file, READ_MODE)  # read through the file
    file_handle.close() 
    return counts


def chart_data(column: List[float], date: List[str]) -> None: 
    """Chart for the data."""
    import matplotlib.pyplot as plt
    plt.plot(date, column)
    plt.xlabel("date")
    plt.ylabel("column")
    plt.xticks(rotation=90)
    plt.show()


if __name__ == "__main__":
    main()