# OAuth 2.0 Setup
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=SCOPES)

flow.run_local_server()

creds = flow.credentials

import pickle
pickle.dump(creds, open("token.pkl", "wb"))
credentials = pickle.load(open("token.pkl", "rb"))

service = build('calendar', 'v3', credentials=credentials)
# Get My Calenders go to list API
result = service.calendarList().list().execute()
result['items'][0]
# return result 
# create an event on my calendar
calendar_id = result['items'][0]['id']
result = service.events().list(calendarId = calendar_id).execute()
result['items'][0]



# create a new event on my calendar
# You first create an event then you can edit it
# starttime = datetime(2023, 11, 1, 8, 00)
# endtime = starttime + timedelta(hours = 8)
# event = 999
# service.events().insert(calendarId = calendar_id, body = event).execute
# # import datefinder
# datefinder.find_dates AOB but you have to install it first
# check create event function