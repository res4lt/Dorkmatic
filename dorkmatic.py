import argparse
import os
from colorama import Fore
import time

parser = argparse.ArgumentParser(description='"Dorkmatic" applies each Google dork to the target and displays the corresponding results.')
parser.add_argument('-s', '--site', help='Target site for the Google search')
parser.add_argument('-d', '--dork_file', help='File containing a list of dorks')

args = parser.parse_args()

site = args.site
dork_file = args.dork_file
print("""
%%%%%%% \033[92mres4lt\033[0m %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%%%%%%%%%%% Date: February 16, 03:32, 2023 %%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%% Weather: It's always cool in the lab %%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%% Health: Weak but Strong %%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%% Caffeine: 00.61 mg %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%% Hacked: All the things %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
""")

user_agents = [
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.3',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',

]

with open(dork_file, 'r') as f:
    dorks = f.readlines()

for i, dork in enumerate(dorks):
    dork = dork.strip()
    user_agent = user_agents[i % len(user_agents)]
    url = f'https://www.google.com/search?q=site%3A{site}+{dork}'
    output = os.popen(f'curl --silent --max-time 2 -A "{user_agent}" -s "{url}" | '
                      'grep -Eo \'<a[^>]+>\' | grep -Eo \'href="[^"]+"\' | cut -d\'"\' -f2 | grep -E \'^http\'| sed \'1,3d\' | head -n -3').read()

    print(f'\n{Fore.LIGHTMAGENTA_EX}[{i + 1}] site:{site} {dork} {Fore.RESET}\n')

    print(f'\n{Fore.LIGHTYELLOW_EX}{output}{Fore.RESET}\n')

    time.sleep(3)
