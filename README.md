# NMap-Differ
Script to be run by cron jobs to diff Nmap scan of an ip and alert to changes via slack

Load as daily cronjob in order to run everyday and identify newly open ports. This is to identify newly opened or closed ports as part of a pentest.

This script has been adapted from the bash nmap differ in 'The Hacker Playbook 3' by Peter Kim, with some of the suggested extra functions.

Replace the * in the slack URL with the details of your slack channel.
***Only use NMAP and this script on systems you have explicit permission to port scan***


To do:
Write a version that uses Shodan scan tokens instead to hide IP of scanner.
