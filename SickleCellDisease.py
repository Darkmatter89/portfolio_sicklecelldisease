def translate(dna):

# Storing codon sequences in seperate lists
    
    isoleucine  = ["ATT","ATC","ATA"]
    leucine = ["CTT","CTC","CTA","CTG","TTA","TTG"]
    valine = ["GTT","GTC","GTA","GTG"]
    phenylalanine   = ["TTT","TTC"]
    methionine = ["ATG"]
    
    aminoList = [isoleucine,leucine,valine,phenylalanine,methionine]
    dnaDict ={0:"I",1:"L",2:"V",3:"F",4:"M"}
    
    
    startPos = 0
    endPos = 3
    dnaLength = len(dna)
    aminoSequence = ""


# Checking if every 3 letters of input are in the above lists and then adding the appropriate letter if found in list
# else adding "X" if not found
    
    if dnaLength % 3 == 0:
        endRange = int(dnaLength / 3) + 1
    else:
        endRange = int((dnaLength - (dnaLength % 3)) / 3) + 1
    
    for i in range(1,endRange):
        notFound = False                
        for a in range(0,len(aminoList)):
            if dna[startPos:endPos] in aminoList[a][:]:
                aminoSequence = aminoSequence + dnaDict[a]
                startPos = endPos
                endPos = endPos + 3
                notFound = True
                
        if not notFound:
            aminoSequence = aminoSequence + "X"
            notFound = False
            startPos = endPos
            endPos = endPos + 3  
            
    return (aminoSequence)


def mutate():
    dnaFile = open('DNA.txt','r+')
    normalFile = open('normalDNA.txt','w')
    mutatedFile = open('mutatedDNA.txt','w')
    
# Reading each letter in line for "a" and and concatenating each letter to a new string
    
    for line in dnaFile:
        stringLine = ""
        for i in range(0,len(line[:])):
            if line[i] == "a":
                stringLine = stringLine + "A"
            else:
                stringLine = stringLine + line[i]
        print(stringLine + "\n")
        normalFile.writelines(stringLine)
        
        stringLine = ""
        for i in range(0,len(line[:])):
            if line[i] == "a":
                stringLine = stringLine + "T"
            else:
                stringLine = stringLine + line[i]
                
        mutatedFile.writelines(stringLine)
    
    dnaFile.close()
    normalFile.close()
    mutatedFile.close()
     
    
def txtTranslate():
    normalFile = open('normalDNA.txt','r')
    mutatedFile = open('mutatedDNA.txt','r')
    
    print("NORMAL DNA OUPUT: \n")
    for line in normalFile:
        print(translate(line.upper()))
    
    print("\nMUTATED DNA OUPUT: \n")
    for line in mutatedFile:
        print(translate(line.upper()))
    
    normalFile.close()
    mutatedFile.close()
    

mutate()
txtTranslate()
    
    