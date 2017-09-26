1. Double click "sync_pacfile.exe" file to run the application
2. There are four buttons:
	1) "Sync EMEA Pacfile": Main function, click this button to start sync EMEA pacfile "global.pac"
	2) "Show Status": click this button to check current sync status; there are four status:
		a) 'Sync has not start, please click "Sync EMEA Pacfile"', means you haven't click button "Sync EMEA Pacfile"
		b) 'Sync finish, please verify', means sync process finish successfully
		c) 'Fail to sync, please check log file', means sync process fail and you could see related logs to see sync process stops at which step
		d) 'Sync is in process, please wait', means process is on
	3) "Clear Status", clear currnt status in the status window
	4) "Close Window", close current appliaction window
3. There are four folders:
	1) "pacfile_test", this is used to simulate production apa pacfile folder "D:\pacfile"
	2) "pacfile_download", the downloaded emea pacfile is stored here
	3) "pacfile_backup", everytime before apa production pacfile replacement, 
		the application will backup current production apa pacfile first with name "global.pac_date_time", for example "global.pac_20170925_151731"
	4) "pacfile_synclog"， log file folders, the logs will rotate when file size exceed 10M Bytes.
4. When sync start, finish and error happens, there will be mail sending to related person
	