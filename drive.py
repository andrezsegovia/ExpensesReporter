import os.path
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class Drive:

    def auth(self, scopes):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', scopes)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return creds

    def initService(self, creds):
        return build('sheets', 'v4', credentials=creds)

    def readDefaultSheet(self, service, spreadsheetId):
        return service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId,
            range='2021!A2:D').execute().get('values', [])
    
    def getLastRowRange(self, result):
        size = len(result)
        return f"A{size + 2}:D{size + 2}"

    def insertNewRecordAtRange(self, service, spreadsheetId, range, expense):
        return service.spreadsheets().values().update(
            spreadsheetId=spreadsheetId,
            range=range,
            valueInputOption="RAW",
            body={
                'values': [
                    [expense.name, expense.category, expense.value, expense.date]
                ]
            }).execute()
    
