#!/usr/bin/python3
import gspread
import sys
from oauth2client.service_account import ServiceAccountCredentials

# connect to the google sheet and get the contents of the SSH Keys sheet
def getSheet(sheetName):
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('homenetwork_secret.json', scope)
	client = gspread.authorize(creds)

	sheet = client.open('Home Network').worksheet(sheetName)

	keys = sheet.get_all_records()
	return keys

# generate authorized_keys file from column name
def genAuthKeys(colName=""):
	allKeys = getSheet("SSH Keys")
	for key in allKeys:
		if colName == "":
			print(key['Key'])
		elif key[colName] == 'TRUE':
			print(key['Key'])

# generate .ssh/config file
def getSSHConfig():
	schema = getSheet("IP Schema")
	for device in schema:
		if (device['SSH Alias'] != ""):
			print("Host " + device['SSH Alias'])
			print(" "*4 + "HostName " + device['IP Address'])
			if (device['SSH Port'] != ""):
				print(" "*4 + "Port " + str(device['SSH Port']))
			if (device['SSH User'] != ""):
				print(" "*4 + "User " + device['SSH User'])


if __name__ == "__main__":
	getSSHConfig()
