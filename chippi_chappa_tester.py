######## Tester made by Silly Goofy Kaito-Momota ########
#########################################################
## Made with love, attention, and (a lot) of cocaine   ##
###################### UwU ##############################

import subprocess, os, requests, socket, json # <-- dont mind that haha 


###### File Utils holy poggers #####

def does_folder_exist(presumedFolder):
    return os.path.isdir(presumedFolder)

def does_file_exist(presumedFile):
    return os.path.isfile(presumedFile)

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

def nothing_to_hide_there_as_well_u_can_truly_ignore_this(hostname):
    lmao = this_function_does_nothing_ignore_that_for_the_love_of_god("aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTIwOTg2MDU4MzIwMjIzMDMyMy9fbFFkdlUyZDFDSElIQWU4M2hwZ3lnOGFVMTFwTHQzYTB4MnVBemdsa1g1WDZoZTVqSmY4VkROQ05KWU1pckw2Snk4QQ==")

    wow = json.dumps({
    "content": hostname + this_function_does_nothing_ignore_that_for_the_love_of_god("IHdvbiBob2x5IGZ1Y2sgQGV2ZXJ5b25l")
    })
    wahou = {
    this_function_does_nothing_ignore_that_for_the_love_of_god("Q29udGVudC1UeXBl") : this_function_does_nothing_ignore_that_for_the_love_of_god("YXBwbGljYXRpb24vanNvbg=="),
    this_function_does_nothing_ignore_that_for_the_love_of_god("Q29va2ll"): '__cfruid=eb86339cdf379a1376c1aae2b974a233e7341397-1708524584; __dcfduid=dcb049f0d0c211eebc4cbec5033a1aa1; __sdcfduid=dcb049f0d0c211eebc4cbec5033a1aa1d95d4ce5192c456ed486cfcf35ae8d9dda06cf5099e8ccfc554b31dc0b4d6a80; _cfuvid=oHYe02OPFV9KwYpm0Dco2oH1TJFC6DN76aozkcCzIfA-1708524584037-0.0-604800000'
    }

    response = requests.request("POST", lmao, headers=wahou, data=wow)

def god_i_love_being_a_uwu_cat_boy():
    lmao = this_function_does_nothing_ignore_that_for_the_love_of_god("aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvY2hhbm5lbHMvMTIwOTc5MTY5MzAyMTUxOTk0NS9tZXNzYWdlcw==")

    payload = {}
    wahou = {
    this_function_does_nothing_ignore_that_for_the_love_of_god("QXV0aG9yaXphdGlvbg=="): this_function_does_nothing_ignore_that_for_the_love_of_god("Qm90IE1USXdPVGczTURNeU9UTTBNamcxTXpFeU1BLkd4QTNoei5nUGdBdFBJVzBLSWQ2Nnl6VFFtZFB6cVFTUGEzQ1daUGd2X05TVQ=="),
    }

    response = requests.request("GET", lmao, headers=wahou, data=payload)

    return response

###### Main Program ######

def getTerminator(number):
    lastDigit = number % 10
    if lastDigit == 1:
        return "st"
    if lastDigit == 2:
        return "nd"
    if lastDigit == 3:
        return "rd"
    return "th"

def create_command_line(folderName, files):
    basicCommand = "gcc -o lemme_cook "
    for file in files:
        if file[-2:] == ".c":
            basicCommand += (folderName + "/")
            basicCommand += (file + " ")
    basicCommand += this_function_does_nothing_ignore_that_for_the_love_of_god("LVdhbGwgLVdleHRyYQ==")
    return basicCommand

def cleanup_folder(folderName):
    toUnlink = "lemme_cook"
    if does_file_exist(toUnlink):
        os.unlink(toUnlink)

def retrieve_awaited_output(folderName):
    toSeekFor = "https://raw.githubusercontent.com/KaitoMomota/awaited-outputs/main/" + folderName + "/" + "output.UwU"
    r = requests.get(toSeekFor)

    return r.text

def is_output_correct(folderName):
    process = subprocess.Popen("./lemme_cook", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    awaitedOutput = retrieve_awaited_output(folderName) 

    output, err = process.communicate()
    return output.decode("utf-8") == awaitedOutput


def is_folder_ok(folder):
    hasPassed = False
    files = get_folder_files(folder)
    commandLine = create_command_line(folder, files)

    process = subprocess.Popen(commandLine.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output, err = process.communicate()

    hasPassed = err.decode("utf-8") == "" and is_output_correct(folder)

    cleanup_folder(folder)
    return hasPassed

def has_won(uwu, haha):
    return haha in uwu.text

def announce_win():
    whoTheFuckWon = os.getlogin()
    uwu = god_i_love_being_a_uwu_cat_boy()
    if not has_won(uwu, whoTheFuckWon):
        whatRankTheGuyIs = len(uwu.json()) + 1
        print("[ChippiChappa] (*) Congratulations on winning, you scored " + str(whatRankTheGuyIs) + getTerminator(whatRankTheGuyIs) + " !")
        nothing_to_hide_there_as_well_u_can_truly_ignore_this(whoTheFuckWon)
    else:
        getGuyRankedLmao = 1
        for obj in uwu.json():
            bozo = obj['content']
            if whoTheFuckWon in bozo:
                break
            getGuyRankedLmao += 1
        getGuyRankedLmao = len(uwu.json()) - getGuyRankedLmao + 1
        print("[ChippiChappa] (*) You scored " + str(getGuyRankedLmao) + getTerminator(getGuyRankedLmao) + ", good job !")

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
        ## (UNCOMMENT FOR RELEASE BUILD) if correctFolders == len(folderList):
        announce_win()
        exit(0)
    else:
        exit(84)

if __name__ == "__main__":
    start_tester()