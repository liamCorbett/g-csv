import csv
import pickle
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class GCSV:

    def __init__(self, csv_filepath):
        self.csv = csv_filepath
        self.service = self.get_service()

    def get_service(self):
        # If modifying these scopes, delete the file "token.pickle".
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        creds = None

        # The file token.pickle stores the user's access and refresh tokens,
        # and is created automatically when the authorization flow completes
        # for the first time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)

        return service

    def paste_to(self, spreadsheet_id, worksheet_name, paste_start_row,
                 paste_start_col):
        """

        :param spreadsheet_id: The ID (or "key") of a spreadsheet; can
                               be found in the spreadsheet URL after
                               the "/d/" but before "/edit"
        :param worksheet_name: Worksheet (or "tab") name of
                               paste destination
        :param paste_start_row: The starting row of the paste
                                destination
        :param paste_start_col: The starting column of the paste
                                destination
        :return:
        """
        with open(self.csv, 'r') as f:
            csv_data = f.read()

        request_body = {
            'requests': [{
                'pasteData': {
                    "coordinate": {
                        "sheetId": worksheet_name,
                        "rowIndex": paste_start_row - 1,
                        "columnIndex": paste_start_col - 1,
                    },
                    "data": csv_data,
                    "type": 'PASTE_NORMAL',
                    "delimiter": ',',
                }
            }]
        }

        request = self.service.spreadsheets().batch_update(
            spreadsheetId=spreadsheet_id,
            body=request_body)

        response = request.execute()

        return response
