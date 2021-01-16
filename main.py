from drive import Drive
from expense import Expense
import createExpense

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets.readonly',
 'https://www.googleapis.com/auth/spreadsheets'
 ]

SPREADSHEET_ID = 'xxxx'


def getTotalExpenses(expenses): 
    print("The total is: {:,}".format(sum(int(c) for a,b,c,d in expenses)))

def main():
    
    expense = createExpense.read()

    drive = Drive()
    service = drive.initService(drive.auth(SCOPES))
    
    expenses = drive.readDefaultSheet(service, SPREADSHEET_ID)

    if not expenses:
        print('No data found...')
    else: 
        range = drive.getLastRowRange(expenses)
        result = drive.insertNewRecordAtRange(service, SPREADSHEET_ID, range, expense)
        if result and result['updatedRows'] and result['updatedRows'] == 1:
            print("New expense added.")
            expenses = drive.readDefaultSheet(service, SPREADSHEET_ID)
            getTotalExpenses(expenses)
if __name__ == "__main__":
    main()