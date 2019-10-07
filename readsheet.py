import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('homenetwork_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Home Network').worksheet('SSH Keys')

network = sheet.get_all_records()
print(network)
