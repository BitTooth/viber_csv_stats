# Viber chat stats

Simple statistics builder for viber chats.

## Dependencies

- _Plotly_ Can be installed by pip

## Usage

### To build staticstics from csv file

1. Backup your chats to e-mail throught Android or iOS application
2. Place .csv file from archive to folder with this script
3. See the statistics in the stats\__filename_.txt and debug messages log in debug.txt

### To build staticstics from csv file and from database output

1. Get database file viber.db from user's viber folder
	C:\Users\<user_name>\AppData\Roaming\ViberPC\<phone_number>
2. Place it in sqlite_extractor folder
3. Run sqlite.exe
4. Type in commands 
	- .open viber.db
	- .ouput ../messages.log
	- .read query.sql
	- .exit

### Building statistics

- Run script with parameters
	python stats.py -csv "file1.csv|file2.csv|..." -db "file1.out|file2.out|..."
- Use python stats.py without params to get additional options

To see additional options run script without any parameters
