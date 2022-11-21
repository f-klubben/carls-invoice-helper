from itertools import combinations

# Loopi de loop
# subset sum problem

def findMatchesForAllStatements(statements: list[float], invoices: dict[int, float]):
    matches =  dict()

    for statement in statements:
        finds = findMatchesForStatement(statement, invoices)
        if len(finds) > 0:
            matches[statement] = finds
    
    return matches, getDuplicates(matches)

def findMatchesForStatement(statement: float, invoices: dict[int, float]):
    """
    Find all invoices that sum up to the statement
    2^n-1 combinations
    """
    ids = list(invoices.keys())
    matches: list[dict[int, float]]= []
    for length in range(len(ids) + 1):
        for subset in combinations(ids, length):
            subsetSum = round(sum([invoices[id] for id in subset]), 2)
            if subsetSum == statement:
                matches.append({id: invoices[id] for id in subset})
    return matches

def getDuplicates(matches: dict[float, list[dict[int, float]]]):
    invoiceIds = []
    for invoices in matches.values():
        for invoice in invoices:
            invoiceIds = [*invoiceIds, *list(invoice.keys())]
    seen = set()
    duplicates = set()
    for id in invoiceIds:
        if id in seen:
            duplicates.add(id)
        seen.add(id)
    return duplicates

