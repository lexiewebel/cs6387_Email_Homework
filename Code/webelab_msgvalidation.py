def getInputFile():
    flag = True
    while flag:
        inputFile  = input("Please enter a header file: ")
        try:
            f = open(inputFile, "r")
            flag = False
            return inputFile
        except: 
            print("ERROR: Invalid file.")
            flag = True


def validateMSG(inputFile):
    validMsg = "not valid."

    with open(inputFile, 'r') as header:
            headerRead = header.read()
            if 'dkim=pass' in headerRead and 'spf=pass' in headerRead:
                validMsg = "valid."
            if 'dkim=pass' not in headerRead and 'spf=pass' not in headerRead:
                validMsg = "not valid. DKIM and SPF is invalid."           
            elif 'dkim=pass' not in headerRead:
                validMsg = "not valid. DKIM is invalid."
            elif 'spf=pass' not in headerRead:
                validMsg = "not valid. SPF is invalid."

    print("Your message is " + validMsg)

def fullTest():
    validateMSG(getInputFile())

fullTest()