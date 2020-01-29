#!/usr/bin/python3

import sys, os
from datetime import date

def main(argv):
   #Variables
   today = datetime.date.today()
   yesterday = today - datetime.timedelta(days = 1)
   flags = ''
   ip = ''
   
   #take in arguments
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
   print ('flags are "', flags)
   print ('IP is "', ip)
   
   #call nmap with args
   os.system('nmap ' + flags + ' ' + ip + ' -oX /opt/nmap_diff/scan_'+today+' > /dev/null 2>&1')

   #diff with previous day

   #if difference exists send message to slack (poss as seperate function)


if __name__ == "__main__":
   main(sys.argv[1:])














