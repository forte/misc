import datetime
import json
import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def auth():
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/calendar']

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
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)

if __name__ == '__main__':
    service = auth()

    with open('input.json') as json_file:
        data = json.load(json_file)
        
        try:
            calendarId = data['calendarID']
        except KeyError:
            raise Exception('Must include calendarID in input JSON file.')

        try:
            events = data['events']
        except KeyError:
            raise Exception('Must include array of events in input JSON file.')

        if 'yearPreset' in data:
            year_prepend = data['yearPreset'] + '-'
        else:
            year_prepend = ''

        for event in events:
            title = event['title']
            date = year_prepend + event['date'] # format 'yyyy-mm-dd', for all-day event

            body = {
                'summary': title,
                'start': {
                    'date': date,
                },
                'end': {
                    'date': date,
                },
                'recurrence': [
                    'RRULE:FREQ=YEARLY',
                ],
                'reminders': {
                     'useDefault': 'True',
                }
            }

            service.events().insert(calendarId=calendarId, body=body).execute()
