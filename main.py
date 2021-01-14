from drive import Drive
from expense import Expense
import createExpense

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets.readonly',
 'https://www.googleapis.com/auth/spreadsheets'
 ]

SPREADSHEET_ID = 'xxxxxxxxxxxxxxxx'

def main():
    
    expense = createExpense.read()
    print(expense)

    drive = Drive()
    service = drive.initService(drive.auth(SCOPES))
    
    result = drive.readDefaultSheet(service, SPREADSHEET_ID)
    
    if not result:
        print('No data found...')
    else: 
        range = drive.getLastRowRange(result)
        print(drive.insertNewRecordAtRange(service, SPREADSHEET_ID, range, expense))


if __name__ == "__main__":
    main()