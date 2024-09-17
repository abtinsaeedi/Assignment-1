##Translate hello world into binary

#Translate H into binary
hOrdinal = ord('H')
hBinValue = bin(hOrdinal)
hBinOutput = hBinValue[2:]

#Translate e into binary
eBinOutput = bin(ord('e'))[2:]

#translate l into binary
lBinOutput = bin(ord('l'))[2:]

#translate o into binary
oBinOutput = bin(ord('o'))[2:]

#compose greeting
greeting = f"{hBinOutput} {eBinOutput} {lBinOutput} {lBinOutput} {oBinOutput}"

#another way ro compose the greeting is by concatation
concatGreeting = hBinOutput + " " + eBinOutput + " " + lBinOutput + " " + lBinOutput + " " + oBinOutput

#print the greeting
print(greeting)

#another way ro compose the greeting is by concatation
concatGreeting = hBinOutput + " " + eBinOutput + " " + lBinOutput + " " + lBinOutput + " " + oBinOutput

print(concatGreeting)

#another way to print
print(hBinOutput, eBinOutput, lBinOutput, lBinOutput, oBinOutput, sep = "|") # can use sep command to separate strings however u want

