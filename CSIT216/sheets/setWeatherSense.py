from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from sense_hat import SenseHat
import time

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1-m7jTqyiXbUfFnEb9MoXcNahHEokHokM-HK3ziLStuk'
# Replace John with your name and ensure data range is accurate
RANGE_NAME = 'John\'s Data!E3:H'

sense = SenseHat()
sense.clear()

def main():

    #sets time variable
    local_time = time.asctime(time.localtime(time.time()))
    temperature = '%2d'% (((sense.get_temperature())*9/5)+32)
    humidity = '%2d'% sense.get_humidity()
    pressure = '%2d'% sense.get_pressure()
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
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

    # Call the Sheets API
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    #iterates through the sheet to find the next empty row as indicated by rowcount int
    rowcount=1
    for row in values:
        if row:
            rowcount+=1

    #sets values to be sent to spreadsheet from sensor to list variable named values
    if temperature==32 and humidity==0:
        temperature = 'Sensor error'
        humidity = 'Sensor error'
        pressure = 'Sensor error'
        values = [
            [
                local_time,
                temperature,
                humidity,
                pressure
                ]
            ]
    else:
        values = [
        [
            local_time,
            temperature,
            humidity,
            pressure
            ]
        ]
    #seralizes list variable values to json variable named mbody
    mbody = {
            'values': values
            }        

    #sets the row to be written to the next empty row
    r='E'+str(rowcount)+':H'+str(rowcount)
    #sets the range of cells to be written
    rangeName='John\'s Data!'+r
    #writes the data from mbody to the spreadsheet
    result=service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range=rangeName,valueInputOption='RAW',body=mbody).execute()
       
if __name__ == '__main__':
    main()
