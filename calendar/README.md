Script that reads in a JSON object to bulk add all-day events to a google calendar.

Steps:
1. Turn on the Google Calendar API
    - Download client configuration and save the file credentials.json to your working directory.
2. Install the Google Client Library
    - pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
3. Create a new calendar for these events (optional)
    - Save the corresponding Calendar ID for later.
    - Edit all-day event notifications setting to set when to be alerted about all-day events
4. Construct JSON file as specified below named `input.json`
    - If updating main calendar and not newly created calendar, set `calendarID` to "primary"
    - `yearPreset` will preset all dates in the `events` list with this year. Leave blank if the year will be inserted manually for each event.
5. Run `python update_calendar.py`
    - NOTE: You will be taken to a browser to authorize access to your calendar the first time the program is run.

JSON format:
```JSON
{
  "calendarID": "something like abc123xyz@group.calendar.google.com or primary",
  "yearPreset": "2019",
  "events": [
    {
      "title": "Event 1",
      "date": "yyyy-mm-dd (or just mm-dd if yearPreset is in the JSON object)"
    },
    {
      "title": "Event 2",
      "date": "yyyy-mm-dd"
    }
  ]
}
```