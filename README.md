Collect old and new data files
	1. Open Teams and download the file SiteTimeZones.json from the channel AVE Portfolio/Standards in the Files/Design Team folder. 
	2. Convert the json file into a csv file by running the Python program. Input  SiteTimeZones.json and output file name old_SiteTimeZones.csv. 
	3. Run in CRM the report crmNewSitesTimeZones, and save the report in a CSV file format. Rename the file to new_SiteTimeZones.csv

Update Information
	1. Run the Python program 'Compare_ToAdd.py' to add new records from the new_SiteTimeZones.csv file into the old sites old_SiteTimeZones.csv file. 
	2. Open the old_SiteTimeZones.csv file in Excel to complete the Time Zone data for each new site record. The new records must match the same data structure of the old records.
	 
Create the new json file
	1. Run the Python program 'Convert csv to json.py'. The input should be old_SiteTimeZones.csv and the output SiteTimeZones.json for distribution. (Keep a backup copy in an archive.)
	2. Copy the new file into the channel AVE Portfolio/Standards in the Files/Design Team folder. 


