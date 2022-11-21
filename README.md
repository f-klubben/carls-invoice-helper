# What is this?
This is a tool to help log carlsberg invoice when doing accounting for F-Klubben.

## Getting started

1. Download invoices from Dinero, and delete all entries, that have been paid, so that only approved and overdue invoices are present.
2. Make a `.txt` file with bank statements from Carlsberg, where each statement is on a new line, formatted in this manner: `-2.000,50`

Now you're ready to run the script, do the following:
```console
./invoiceHelper ./samples/statements.txt ./samples/invoices.csv
```

The program will then return each statement and the invoices that match. 

it will also tell you if it have found invoices that are used in multiple statement.

**You should always check the results before plotting it into dinero!**

*This script can probably be used for other invoices as well*