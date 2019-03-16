from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import RPi.GPIO as GPIO
import time
import dht11

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1-m7jTqyiXbUfFnEb9MoXcNahHEokHokM-HK3ziLStuk'
RANGE_NAME = 'Weather Data!A2:C'
time = time=time.asctime(time.localtime(time.time()))

def main():

    #	This script will check for a log file for sensor data. 
    #	If log file exists, it will append with new sensor data 
    #	(to include date and time as given by the OS.) 
    #	If log file does not exist, it will create a new file 
    #	and add a title.

    #initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    # read data using pin 17
    instance = dht11.DHT11(pin=17)

    # set data to variable
    weather = instance.read()
    temperature=(((weather.temperature)*9/5)+32)
    humidity=weather.humidity
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
    values = [
        [
            time,
            temperature,
            humidity
            ]
        ]
    #seralizes list variable values to json variable named mbody
    mbody = {
            'values': values
            }        

    #sets the row to be written to the next empty row
    r='A'+str(rowcount)+':C'+str(rowcount)
    #sets the range of cells to be written
    rangeName='Weather Data!'+r
    #writes the data from mbody to the spreadsheet
    result=service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range=rangeName,valueInputOption='RAW',body=mbody).execute()
       
if __name__ == '__main__':
    main()
