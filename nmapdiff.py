#!/usr/bin/python3

import sys, os, filecmp, datetime, getopt

def slack():
   os.system('touch /opt/diff.txt')

def main(argv):
   #Variables
   today = datetime.date.today()
   yesterday = today - datetime.timedelta(days = 1)
   today = str(today)
   yesterday = str(yesterday)
   flags = ''
   ip = ''
   
   #Take in arguments
   try:
      opts, args = getopt.getopt(argv,"hf:i:",["flags=","ip="])
   except getopt.GetoptError:
      print ('test.py -f <nmap flags> -i <target IP>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -f <nmap flags> -i <target IP>')
         sys.exit()
      elif opt in ("-f", "--flags"):
         flag = arg
      elif opt in ("-i", "--ip"):
         ip = arg
   
   #Call nmap with args
   os.system('nmap ' + flags + ' ' + ip + ' -oG /opt/nmap_diff/scan_'+today+'.gnmap > /dev/null 2>&1')
   os.system("grep Host: /opt/nmap_diff/scan_" +today +".gnmap > /opt/nmap_diff/scan_" +today+ ".txt'")
   os.system("rm /opt/nmap_diff/scan_" +today+ ".gnmap")

   #Diff with previous day
   ft = '/opt/nmap_diff/scan_'+today+'.txt'
   fy = '/opt/nmap_diff/scan_'+yesterday+'.txt'
   
   #If difference exists send message to slack (poss as seperate function)
   if filecmp.cmp(ft, fy) == True:
      print("True")
   else:
      print("False")

if __name__ == "__main__":
   main(sys.argv[1:])
