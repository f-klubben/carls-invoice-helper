#!/usr/bin/env python3
import argparse
from pprint import pprint

from loader import loadInvoices, loadStatements
from finder import findMatchesForAllStatements

COMMA = 100

def printer(matches: dict[int, list[dict[int, int]]], duplicates: set[int]):
    for statement, invoices in matches.items():
        print(f"statement: {statement / COMMA}")
        for invoice in invoices:
            floatInvoice = {k: v / COMMA for k, v in invoice.items()}
            print(f"invoice: {floatInvoice}")
        print()
    
    if len(duplicates) > 0:
        print("Duplicates:")
        for duplicate in duplicates:
            print(duplicate / COMMA)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(
        prog="Carlsberg Invoice Helper",
        description="This program helps you choose carlsberg invoices for bank statements",
        )
    argparser.add_argument("statements", help="Path to the statements file (*.txt)")
    argparser.add_argument("invoices", help="Path to the invoices file (*.csv)")
    args = argparser.parse_args()

    statements: list[int] = loadStatements(args.statements)
    invoices: dict[int, int] = loadInvoices(args.invoices)
    printer(*findMatchesForAllStatements(statements, invoices))