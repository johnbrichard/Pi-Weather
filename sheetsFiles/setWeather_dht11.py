# If you haven't visited the Google Sheets API page
# (https://developers.google.com/sheets/api/quickstart/python)
# do so now.
# Follow the instructions to install the proper modules via pip.
# Ensure the Adafruit_DHT module is installed via pip.
# On initial run, you will be required to log into the your Google
# account that was used when you visited the Sheets API page to sign up for Google Developer.
# This will populate a token.pickle file that will be a part of your credentials to access
# the API once we've automated the process.
# Assuming you've done everything listed above, the file should execute

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import Adafruit_DHT
import time

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1-m7jTqyiXbUfFnEb9MoXcNahHEokHokM-HK3ziLStuk'
# Be sure to change John to your name and ensure the data range is correct
RANGE_NAME = 'John\'s Data!A3:C'

#initialize DHT11 sensor using Adafruit_DHT module
sensor=Adafruit_DHT.DHT11
#set gpio variable to the appropriate GPIO pin
gpio=17

def main():

    local_time = time.asctime(time.localtime(time.time()))
    # read data from sensor and set data to appropriate variables
    humidity, temperature = Adafruit_DHT.read_retry(sensor,gpio)
    temperature='%2d'% ((temperature*9/5)+32)

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
    if temperature is 32  and humidity is 0:
        #if the values aren't read properly from sensor
        #temp and hum values set to display read error
    	temperature="Sensor error"
	humidity="Sensor error"
        #assign variables to list structure
	values = [
        	[
            	local_time,
	        temperature,
        	humidity
            	]
       		 ]
    else:
        #assign variables to list structure
	values = [
		[
		local_time,
		temperature,
		humidity
		]
		]
	
    #seralizes list variable named values to json variable named mbody
    mbody = {
    	    'values': values
    	    }

    #sets the row to be written to the next empty row
    r='A'+str(rowcount)+':C'+str(rowcount)
    #sets the range of cells to be written
    rangeName='John\'s Data!'+r
    #writes the data from mbody to the spreadsheet
    result=service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range=rangeName,valueInputOption='RAW',body=mbody).execute()
       
if __name__ == '__main__':
    main()
