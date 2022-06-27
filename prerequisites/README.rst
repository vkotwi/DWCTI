PREREQUISISTES
TODO:
- Cache info if fails at any point ??

SUMMARY:
The program attempts to establish a connection to the mongo database (specified in the config.ini file). The program then attempts to establish a connection to TOR and compares the exit node to the IP of known bad exit nodes. If the connection is found to be using known bad exit node, the session using the bad exit node is closed and a new session established. This is repeated untill a non-bad exit node is found.

NOTE:
This folder [prerequisistes] contains python files that run before the program starts performing is various functions (scraping, crawling etc.) once the main.py in the main folder [DWCC] has started running.

ORDER:
1. IF establish_db_connection.py == FALSE
2. 	RETURN ERROR
3. update_malicious_exit_nodes_list.py
4. tor_connect_and_check.py
5. IF tor_connect_and_check.py == FALSE
6.	GOTO 3
7. END

EXPLANATION:
This part of the program runs files which establish specific connections which all the program to work. 
[1] The program establishes a connection to the specificed mongoDB set up either on the host system or remotely. If the host fails to connect to the DB for whatever reason, the program exits with an error explaining what went wrong. 
[3] The program then  creates/updates the list of known bad exit nodes.
[4] The program then starts up the tor.exe process, establishes a connection to a random TOR exit node and then compares the exit node IP to the list of known bad exit nodes generated in step [3]. 
[5] If the TOR exit node is found in the list of bad exit nodes, the session will be terminated, and a new connection established. If the TOR exit node is not in the list, the session is kept and the program can run as normal. Then, the program checks to see if the database is up an running

[7] All python processes associated with this part of the program will close, the database will be connected (??) and the tor.exe software will now be running on the device.