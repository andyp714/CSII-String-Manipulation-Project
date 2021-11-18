'''
Created on Oct 18, 2021

@author: apauley24
'''
def main():
    '''
    This function is to take the user input, run the functions, and print the output
    :param: 
    :type name:
    :returns:
    :raises: General try and except
    '''
    
    try:
        functionCheck = False
        userInput = input("Input Here > ")
        listInput = userInput.split("/")
        inputLength = len(listInput)
        stringInput = listInput[-1]
        newList = listInput[0:inputLength -1]
        for item in newList:
            if item[0:2] == "LS":
                shiftDistance = int(item[3:])
                stringInput = LS_X(stringInput, shiftDistance)
                functionCheck = True
            elif item[0:2] == "RS":
                shiftDistance = int(item[3:])
                stringInput = RS_X(stringInput, shiftDistance)
                functionCheck = True
            elif item[0:2] == "LC":
                characterAmount = int(item[3:])
                stringInput = left_cir(stringInput, characterAmount)
                functionCheck = True
            elif item[0:2] == "RC":
                characterAmount = int(item[3:])
                stringInput = right_cir(stringInput, characterAmount)
                functionCheck = True
            elif item[0:2] == "MC":
                startingPosition = int(item[3])
                characterAmount = int(item[5])
                circulateLength = int(item[4])
                circulateDirection = item[6]
                stringInput = MC_SLXD(startingPosition, characterAmount, circulateLength, circulateDirection, stringInput)
                functionCheck = True
            elif item[0:3] == "REV":
                reversePosition = int(item[4])
                reverseLength = int(item[5])
                stringInput = REV_SL(reversePosition, reverseLength, stringInput)
                functionCheck = True
            else:
                print("Input Error")
                break
        if functionCheck == True:
            print("Final Output:", stringInput)
        else:
            print("Input Error")
    
    except:
        print("Input Error")  

def RS_X(stringInput, shiftDistance):
    '''
    This function shifts the characters of the string x places to the right
    :param stringInput, shiftDistance: User Input, User Input
    :type name: string, integer
    :type state:
    :returns: The result as a string
    :raises: General try and except
    '''
    
    my_string = stringInput #asking to type in a word in to the function 
    my_string = my_string[-shiftDistance:] + my_string[:-shiftDistance] 
    
    #replace the first x characters to the left with hash_tags 
    old_string = my_string #the new word replaces the word that was put into the function 

    
    string_list = list(old_string) # the new word gets put into a list(brackets) 
    

    string_list[0:shiftDistance] = "#" * shiftDistance #Depending on the number of shift distance, the hash_tags are going to replace some letters from the right side 
    
    
         
    return ''.join(string_list) #the new string list gets put into a string from the string list 

def LS_X(stringInput, shiftDistance):
    '''
    This function shifts the characters of the string x places to the left
    :param stringInput, shiftDistance: User Input, User Input
    :type name: string, integer
    :type state:
    :returns: The result as a string
    :raises: General try and except
    '''
    
    my_string = stringInput #asking the type in a word into the function 
    my_string = my_string[shiftDistance:] + my_string[:shiftDistance] 
    
    
    
    old_string = my_string # the new string replaces the old string 

    
    string_list = list(old_string) #so, the new string gets put into a list 

    
    string_list[len(string_list) - shiftDistance:] = "#" * shiftDistance #depending on the number of shift distance, the hashtags are going to replace some letters
    
          
    return ''.join(string_list)


def left_cir(stringInput,characterAmount):
    
    '''
    This function circulates the leftmost X characters to the right side of the string
    :param stringInput, characterAmount: User Input, User Input
    :type name: string, integer
    :type state:
    :returns: The result as a string
    :raises: General try and except
    '''
    
    tmp = stringInput[characterAmount : ] + stringInput[0 : characterAmount]
    return tmp

def right_cir(stringInput, characterAmount):
    
    '''
    This function circulates the rightmost X characters to the left side of the string
    :param stringInput, characterAmount: User Input, User Input
    :type name: string, integer
    :type state:
    :returns: The result as a string
    :raises: General try and except
    '''
      
    return left_cir(stringInput, len(stringInput) - characterAmount)

def rightrotate(j, f):
    
        return leftrotate(j, len(j) - f)
    
def leftrotate(j,f):
        
        tmp = j[f : ] + j[0 : f]  #Rotates the word, f characters 
        
        return tmp


def MC_SLXD(startingPosition ,characterAmount, circulateLength,circulateDirection, stringInput):
    '''
    This function circulates the sub-string starting in position S with a length of L, X characters, in the direction D
    :param stringInput, startingPostion, circulateLength, characterAmount, circulateDirection: User Input, User Input, User Input, User Input, User Input
    :type name: string
    :type state:
    :returns: The result as a string
    :raises:
    '''
    
    
    
    
    if circulateDirection == "L":
        startingPosition = startingPosition - 1
        L = circulateLength + startingPosition     #Redefining circulate amount to the entire string
        str = stringInput[startingPosition:L]      #Making a substring 
        return (stringInput[:startingPosition] + leftrotate(str,characterAmount) + stringInput[L:]) #appending the rest of the sting as a result
    
    if circulateDirection == "R":
        startingPosition = startingPosition - 1
        L = circulateLength + startingPosition     #Same thing but right this time
        str = stringInput[startingPosition:L]
        return (stringInput[:startingPosition] + rightrotate(str, characterAmount) + stringInput[L:])   


def REV_SL(reversePosition, reverseLength , stringInput):
    '''
    This function reverses  the order of the characters starting at position S with a length of L
    :param stringInput, reversePosition, reverseLength: User Input, User Input, User Input
    :type name: string
    :type state:
    :returns: The result as a string
    :raises:
    '''
    if reversePosition <= 0:
        print("Error: Starting position must be greater then 0.") #DEBUG REMOVE WHEN NEEDED
        return "Error: Starting position must be greater then 0."
    start = reversePosition - 1                                                           #Dealing with offset by subtracting 1
    total = reverseLength - 1                                                                 #Dealing with offset by subtracting 1
    end = start + total                                                             #This calculates the end point by adding the total amount of chars effected
    wordList = list(stringInput)                                                         #Converts desired word to list
    if start > 0:
        revChar = wordList[end:start-1:-1]
    else:
        revChar = wordList[:end+1]
        revChar = revChar[::-1]
    del wordList[start:end+1]                                                #deletes section from original function
    wordList.insert(start, revChar)                                          #This puts the reversed segment list into the wordList list
    flatList = [item for sublist in wordList for item in sublist]        #This flattens the list inside the list into one list            
    output = ''.join(flatList)                                                          #This converts the list into a string
    return output
    
if __name__ == "__main__":
    main()
    