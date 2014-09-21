__author__ = 'trebushet'
def fixedEmail(email):
    email=email.strip(' \t\n\r')
    #replace all substring to @
    email=email.replace("[sobaka]","@")
    email=email.replace("[at]", "@")
    email=email.replace("[dog]","@")
    #find last char '_'and replace on '.'
    indLast=email.rfind("_");
    if indLast!=-1 and indLast!=len(email):
        email=email[:indLast]+"."+email[indLast+1:]
    if email[0]!='@' and email.count("@")==1 and email[-1:].isalpha():
        return email
    else:
        return "fail"

fInput = open("input.txt",'r')
fOutput=open("output.txt",'w')
fFail=open("failOutput.txt",'w')
for line in fInput:
    res=fixedEmail(line)
    if res=="fail":
        fFail.write(line+'\n')
    else:
        fOutput.write(res+'\n')
fInput.close()
fOutput.close()
fFail.close()





