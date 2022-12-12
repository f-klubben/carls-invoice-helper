import os
import csv 

def loadStatements(path: str):
    statements: list[int] = []
    with open(os.path.abspath(path), "r") as f:
        raw = f.readlines()
        for rawStatement in raw:
            statement = rawStatement.replace("\n", "").replace(".", "").replace(",", "")
            statements.append(int(statement))
    return statements

def loadInvoices(path: str):
    bilagMap: dict[int, int]  = dict()
    with open(os.path.abspath(path), "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            id = int(row["Bilagsnummer"])
            amount = int(row["Total i DKK"].replace(".", "").replace(",", ""))
            bilagMap[id] = amount
    return bilagMap