from itertools import combinations

# Loopi de loop
# subset sum problem

def findMatchesForAllStatements(statements: list[int], invoices: dict[int, int]):
    matches =  dict()

    for statement in statements:
        finds = findMatchesForStatement(statement, invoices)
        if len(finds) > 0:
            matches[statement] = finds
    
    return matches, getDuplicates(matches)

def findMatchesForStatement(statement: int, invoices: dict[int, int]):
    """
    Find all invoices that sum up to the statement
    2^n-1 combinations
    """
    ids = list(invoices.keys())
    matches: list[dict[int, int]]= []
    for length in range(len(ids) + 1):
        for subset in combinations(ids, length):
            subsetSum = sum([invoices[id] for id in subset])
            if subsetSum == statement:
                matches.append({id: invoices[id] for id in subset})
    return matches

def getDuplicates(matches: dict[int, list[dict[int, int]]]):
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

