#!/usr/bin/env python3
import argparse
from pprint import pprint

from loader import loadInvoices, loadStatements
from finder import findMatchesForAllStatements

def printer(matches: dict[float, list[dict[int, float]]], duplicates: set[int]):
    for statement, invoices in matches.items():
        print(f"statement: {statement}")
        for invoice in invoices:
            print(f"invoice: {invoice}")
        print()
    
    if len(duplicates) > 0:
        print("Duplicates:")
        for duplicate in duplicates:
            print(duplicate)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(
        prog="Carlsberg Invoice Helper",
        description="This program helps you choose carlsberg invoices for bank statements",
        )
    argparser.add_argument("statements", help="Path to the statements file (*.txt)")
    argparser.add_argument("invoices", help="Path to the invoices file (*.csv)")
    args = argparser.parse_args()

    statements: list[float] = loadStatements(args.statements)
    invoices: dict[int, float] = loadInvoices(args.invoices)
    printer(*findMatchesForAllStatements(statements, invoices))