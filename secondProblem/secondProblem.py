# coding=utf-8
__author__ = 'trebushet'
#в input.txt email адреса, где @ заменена на [sobaka],[at],[dog], а точка может быть
#заменена на _ в output.txt выписать исправленные адреса. в fail.txt те, которые не исправили
dogWords = ["[sobaka]", "[at]", "[dog]"]
def fixedEmail(email):
    #replace all substring to @
    for dog in dogWords:
        email = email.replace(dog, "@")
    #find last char '_'and replace on '.'
    indLast = email.rfind("_")
    if indLast != -1 and indLast != len(email):
        email = email[:indLast] + "." + email[indLast + 1:]
    if email[0] != '@' and email.count("@") == 1 and email[-1:].isalpha():
        return email
    else:
        return None

fInput = open("input.txt", 'r')
fOutput = open("output.txt", 'w')
fFail = open("failOutput.txt", 'w')
words = fInput.read().split()
for line in words:
    res = fixedEmail(line)
    if res is None:
        fFail.write("{0}\n".format(line))
    else:
        fOutput.write("{0}\n".format(res))
fInput.close()
fOutput.close()
fFail.close()





