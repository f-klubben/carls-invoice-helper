import os
import csv 

def loadStatements(path: str):
    statements: list[float] = []
    with open(os.path.abspath(path), "r") as f:
        raw = f.readlines()
        for rawStatement in raw:
            statement = rawStatement.replace("\n", "").replace(".", "").replace(",", ".")
            statements.append(float(statement))
    return statements

def loadInvoices(path: str):
    bilagMap: dict[int, float]  = dict()
    with open(os.path.abspath(path), "r") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            id = int(row.get("ï»¿Bilagsnummer",row["\ufeffBilagsnummer"]))
            amount = float(row["Total i DKK"].replace(".", "").replace(",", "."))
            bilagMap[id] = amount
    return bilagMap