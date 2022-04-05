import paramiko
import sys
import getopt
global info, target, usernames, passwords, port
# Options
options = "hu:p:t:w:"
# Long options
long_options = ["help", "user_file =", "pass_file =", "target =", "word_list ="]
ssh = paramiko.SSHClient()


def main(argumentlist):
    global info, target, usernames, passwords, port
    info = False

    try:
        arguments, values = getopt.getopt(argumentlist, options, long_options)

        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--help"):         # test if there is -h or --help
                infos()                                     # print help
            elif currentArgument in ("-u", "--user_file "):    # test if there is -o --output
                usernames = open(currentValue, "r")
            elif currentArgument in ("-p", "--pass_file "):
                passwords = open(currentValue, "r")
            elif currentArgument in ("-t", "--target "):
                target = currentValue
            elif currentArgument in ("-w", "--word_list"):
                passwords = currentValue
            else:
                print(infos())
        if not info:                                        # if the help was not printed then
            print("hello")
            ssh.connect(hostname=target, username=usernames, password=passwords, port=port)
    except getopt.error as err:                             # if there is an error
        # output error, and return with an error code
        print(str(err))                                     # print it
        print(infos())                                             # and print the help
        sys.exit()


def infos():
    global info
    info = True
    print("Keylogger.py\n"
          "OPTION\n"
          "-h   --help      <Show this page>\n"
          "-o   --output    <output-directory>\n"
          "\n"
          "EXAMPLES:\n"
          "Keylogger.py -o C:\\Users\Admin\Documents\logs \n"
          "Keylogger.py -h\n"
          "\n"
          "SEE THE MAN PAGE https://github.com/M0ShYy/PyKeylogger FOR MORE OPTIONS AND EXAMPLES\n")

argumentList = (sys.argv[1:])                               # make a list of all the option wrote by the user
main(argumentList)



