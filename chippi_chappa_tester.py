######## Tester made by Silly Goofy Kaito-Momota ########
#########################################################
## Made with love, attention, and (a lot) of cocaine   ##
###################### UwU ##############################

import subprocess, os, requests, socket # <-- dont mind that haha 


###### File Utils holy poggers #####

def does_folder_exist(presumedFolder):
    return os.path.isdir(presumedFolder)

def retrieve_all_test_folders():
    folderTest = []
    for i in range(1, 21):
        folderTest.append("test" + str(i))
    return folderTest


def get_folder_file_count(folder):
    return len(os.listdir(folder))

def get_folder_files(folder):
    return os.listdir(folder)

def has_file(fileName, folder):
    return os.listdir(folder)

def has_minimum_files(folder):
    hasMakefile = False
    hasCFile = False
    files = get_folder_files(folder)
    for file in files:
        if file[-2:] == ".c":
            hasCFile = True
        if file == "Makefile":
            hasMakefile = True
    return hasCFile and hasMakefile

##### Logger Utils thats crazy #####

def log_error(error):
    print("[ChippiChappa] (!)", error, file=sys.stderr)

####### Environement Utils >\\< #######

def is_environement_ok():
    folderList = get_folder_files(".")
    for i in range (1, 21): # do we have all the folders lmao
        folderName = "test" + str(i)
        if not does_folder_exist(folderName) or (does_folder_exist(folderName) and get_folder_file_count(folderName) < 2):
            log_error("Bro.. would you please stop running that tester in another folder that where its supposed to be ran")
            return False
        if not has_minimum_files(folderName):
            log_error("Bro.. would you please not remove the files that i need for me to do my job....")
            return False
    return True
    

##### haha dw thats really nothing you should really not be looking here #####

def this_function_does_nothing_ignore_that_for_the_love_of_god(text):
    bins = str()
    table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    for c in text:
        if c == '=':
            bins += '000000'
        else:
            bins += '{:0>6}'.format(str(bin(table.index(c)))[2:])
    for i in range(8, len(bins) + int(len(bins) / 8), 9):
        bins = bins[:i] + ' ' + bins[i:]
    bins = bins.split(' ')
    if '' in bins:
        bins.remove('')
    text = str()
    for b in bins:
        if not b == '00000000':
            text += chr(int(b, 2))
    return text

###### Main Program ######

def create_command_line(folderName, files):
    basicCommand = "gcc -o lemme_cook "
    for file in files:
        if file[-2:] == ".c":
            basicCommand += (folderName + "/")
            basicCommand += (file + " ")
    basicCommand += this_function_does_nothing_ignore_that_for_the_love_of_god("LVdhbGwgLVdleHRyYQ==")
    return basicCommand

def cleanup_folder(folderName):
    toUnlink = folderName + "/" + "lemme_cook"
    if does_folder_exist(toUnlink):
        os.unlink(folderName + "/" + "lemme_cook")

def retrieve_awaited_output(folderName):
    toSeekFor = "https://raw.githubusercontent.com/KaitoMomota/awaited-outputs/main/" + folderName + "/" + "output.UwU"
    r = requests.get(toSeekFor)

    return r.text

def is_folder_ok(folder):
    hasPassed = False
    files = get_folder_files(folder)
    commandLine = create_command_line(folder, files)

    process = subprocess.Popen(commandLine.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output, err = process.communicate()

    hasPassed = err.decode("utf-8") == "" # and output.decode("utf-8") == retrieve_awaited_output(folder) (uncomment for the release)

    cleanup_folder(folder)
    return hasPassed

def announce_win():
    whoTheFuckWon = socket.gethostname()
    print(whoTheFuckWon)


def start_tester():
    if is_environement_ok():
        correctFolders = 0
        folderList = retrieve_all_test_folders()
        print("[ChippiChappa] (*) Retrieved the %d folders !\n" % (len(folderList)))
        for folder in folderList:
            if is_folder_ok(folder):
                correctFolders += 1
                print("[ChippiChappa] (*)", folder, "did pass ! good job.")
            else:
                print("[ChippiChappa] (*)", folder, "did not pass :( !")
        print("\n[ChippiChappa] (*) RESULT: (%d/%d) passed." % (correctFolders, len(folderList)))
        if correctFolders == len(folderList):
            announce_win()
        exit(0)
    else:
        exit(84)

if __name__ == "__main__":
    start_tester()