# NMap-Differ
Script to be run by cron jobs to diff Nmap scan of an ip and alert to changes via slack

Load as daily cronjob in order to run everyday and identify newly open ports.

This script has been adapted from the bash nmap differ in 'The Hacker Playbook 3' by Peter Kim, with some of the suggested extra functions.

***Only use NMAP and this script on systems you have explicit permission to port scan***
