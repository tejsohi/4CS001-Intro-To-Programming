# Coding Challenge 2, morse.py
# Name:Tejvir Sohi
# Student No:1926434

# Morse Encoder/Decoder

# Morse code translations, use this to perform encoding/decoding

MORSE_CODE = (
    ("-...", "B"),
    (".-", "A"),
    ("-.-.", "C"),
    ("-..", "D"),
    (".", "E"),
    ("..-.", "F"),
    ("--.", "G"),
    ("....", "H"),
    ("..", "I"),
    (".---", "J"),
    ("-.-", "K"),
    (".-..", "L"),
    ("--", "M"),
    ("-.", "N"),
    ("---", "O"),
    (".--.", "P"),
    ("--.-", "Q"),
    (".-.", "R"),
    ("...", "S"),
    ("-", "T"),
    ("..-", "U"),
    ("...-", "V"),
    (".--", "W"),
    ("-..-", "X"),
    ("-.--", "Y"),
    ("--..", "Z"),
    ("-----", "0"),
    (".----", "1"),
    ("..---", "2"),
    ("...--", "3"),
    ("....-", "4"),
    (".....", "5"),
    ("-....", "6"),
    ("--...", "7"),
    ("---..", "8"),
    ("----.", "9"),
    (".-.-.-", "."),
    ("--..--", ","),
    ("..--..", "?"),
    (".----.", "'"),
    ("-.-.--", "!"),
    ("-..-.", "/"),
    ("-.--.", "("),
    ("-.--.-", ")"),
    (".-...", "&"),
    ("---...", ":"),
    ("-.-.-.", ";"),
    ("-...-", "="),
    (".-.-.", "+"),
    ("-....-", "-"),
    ("..--.-", "_"),
    (".-..-.", '"'),
    ("...-..-", "$"),
    (".--.-.", "@"),
)
"""
Requirements:
    • Prompt users to select a mode: encode (e) or decode (d).
    • Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    • Prompt the user for the message they would like to encode/decode.
        • Check if the message contains valid characters.
          If not, continue to prompt the user until a valid message is selected
          (dependent upon the mode selected).
    • Encode/decode the message as appropriate and print the output.
    • Prompt the user whether they would like to encode/decode another message.
        • Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            • End the program if the user selects no.
            • Proceed directly to step 2 if the user says yes.
    • Your program should be as close as possible to the example shown in the assessment brief.

Hints:
    • Use the tuple of tuples above to convert between plain text/Morse code
    • You can make use of str.split() to generate a list of Morse words and characters
      by using the spaces between words and characters as a separator.
    • You will also find str.join() useful for constructing a string from a list of strings.
    • You should use a loop to keep the programming running if the user says that would like to
      encode/decode another message after the first.
    • Your program should handle both uppercase and lowercase inputs. You can make use of str.upper()
      and str.lower() to convert a message to that case.
    • Check the assessment brief for code examples.
"""

# TODO: Write your code here!

  
'''
The method encode is declared below. No values are passed through but a string of morse characters is outputted.
The method runs under a loop to determine if the user would like to encode another message.
The message is split into a list with each position being each word in the message.
I then loop through the variable and put each character in each word to a list. 
I then loop through each character in that list to check if it is in the tuple and if it is,
I will get the opposite value of it and append that to a seperate list.  
I also append a space at the end of looping through each word to add the necessary.
I then join all the words together and output the result to the user.
I then ask the user if they wish to encode anthoer message. If they do then the method will run again.
If not then, they are returned to the main menu.
'''
def encode():
  
  encodeAgain = True
  while(encodeAgain):

    encodeMessage  = input(str("What message would you like to encode: \n"))
    encodeMessage = encodeMessage.upper()
    morWords = []

    words = encodeMessage.split(" ")

    for words in words:
      langCharacters = list(words)
      

      for langCharacter in langCharacters:
        for (code, letter) in MORSE_CODE:
          if langCharacter == letter:
            morWords.append(code)
          elif langCharacter == "  " or langCharacter != letter:
            continue          
      
      morWords.append("  ")

    encodeMessage = " ".join(morWords)
    print(f"Here is your encoded message \n{encodeMessage}")
    programAgain = input(str("Would you like to encode another message(yes/no): "))
    if not "yes" in programAgain and not "no" in programAgain:
      print("Invalid input entered, you will be returned to the main menu") 
      mode()
    elif "yes" in programAgain:
      continue
    elif "no" in programAgain:
      encodeAgain = False
      mode()



'''
The method decode is declared below. The values of morse and telegram are passed through. Morse is a string and telegram is a boolean.
The method checks if telgram is true. This is to determine if the method has been called from the main menu or the decode telgraph method.
The way the morse is decoded is done the same on either side of the telegram if statement.
I split all of the morse words into variable and then loop through each word.
I spilt each character and loop through each character and I then loop through the tuple.
If the character is in the tuple, I then get the opposite character and append that to a seperate list.  
I also append a space at the end of looping through each word to add the necessary.
I then join all the words together and output the result to the user.
I then ask the user if they wish to encode anthoer message. If they do then the method will run again.
If not then, they are returned to the main menu. 
'''
def decode(morse, telegram):
  
  if telegram == True:
    langWords = []
    morse = morse.split('   ')

    for words in morse:
      morCharacters = words.split(' ')
      
      for morCharacter in morCharacters:
        for (code, letter) in MORSE_CODE:
          if morCharacter == code:
            langWords.append(letter)
          elif morCharacter == "   " or morCharacter == "":
            continue

      langWords.append(" ")

    decodeMessage = "".join(langWords)
    return decodeMessage
  else:
    decodeAgain = True
    while(decodeAgain):        
      
      print("What message would you like to decode")
      print("Please space each morse word with 3 spaces ")

      decodeMessage = input(str("and please space each morse character with 1 space to avoid any errors: "))
      langWords = []
      words = decodeMessage.split('   ')

      for word in words:
        morCharacters = word.split(' ')
        
        for morCharacter in morCharacters:
          for (code, letter) in MORSE_CODE:
            if morCharacter == code:
              langWords.append(letter)
            elif morCharacter == "   " or morCharacter == "":
              continue

        langWords.append(" ")
          
      decodeMessage = "".join(langWords)
      print(f"Here is your decoded message \n{decodeMessage}")
      programAgain = input(str("Would you like to decode another message(yes/no): "))
      
      if not "yes" in programAgain and not "no" in programAgain:
        print("Invalid input entered, you will be returned to the main menu") 
        mode()
      elif "yes" in programAgain:
        continue
      elif "no" in programAgain:
        decodeAgain = False
        mode()
        



'''
The method decodeTelegraph is declared below. No values are passed through but a string of morse characters and text is outputted.
The user inputs their message and the mssage is put to a list.
while the first value of the list is 0, then remove that value from the list.
the list is then joined back together into a string.
The transmission speed is then detecteded depending on the biggest combinations of 1s and 0s.
The code variable then searches for specific combinations of numbers and replaces them with a morse value.
telgram is set to true and the morse message is passed through to the decode method with returns a string of text.
The user is tehn asked if they would like to decode another messge.
If yes, the method runs again. If no then the user is returned to the main menu.
'''
def decodeTelegraph():
  decodeAgain = True
  while decodeAgain:
    transmission = True

    if transmission == True:
        code = str(input("What message would you like to decode: ")) 
        codeList = list(code)
        while codeList[0] == "0":
          codeList.pop(0)
        code = ''.join(codeList)
        
        ones = list(filter(None, code.split('0')))
        minOnes = min(len(num) for num in ones)
        zeros = list(filter(None, code.split('1')))
        minZeros = min(len(num) for num in zeros)

        transmissionSpeed = min(minOnes, minZeros)

        code = code.replace('111' * transmissionSpeed + '0' * transmissionSpeed, '-')
        code = code.replace('1' * transmissionSpeed + '0'* transmissionSpeed, '.')
        code = code.replace('111' * transmissionSpeed, '-')

        code = code.replace('1' * transmissionSpeed, '.')
        code = code.replace('00' * transmissionSpeed, ' ')

        telegram = True
        text = decode(code, telegram)
        print(f"{code}\n {text}")

        again = str(input("Would you like to decode another message(yes/no):"))
        if "yes" in again:
          decodeAgain = True
        else:
          decodeAgain = False
          mode()


'''
The method mode is delcared below.
This is the method that acts as the main menu. 
Depending on what the user wants to do. Then they will will be sent to the corresponding method. 
The user will always be returned to this method at the end of every other method.
'''
def mode():
  print("This program encodes and decodes Morse code.")
  userMode = str(input("Would you like to encode (e), decode (d), decode telegraph (dt) or quit(q): "))

  if userMode != 'e' and userMode != 'd' and userMode != 'dt' and userMode !='q':
    print("Invalid mode entered")
    print("Please enter a choice from the menu using a the letter indicators.")
    mode()
  elif userMode == 'e':
    encode()
  elif  userMode == 'd':
    morse = None
    telegram = False
    decode(morse, telegram)
  elif  userMode == 'dt':
    decodeTelegraph()
  elif  userMode == 'q':
    print("Thank you for using Morse Code translator")
    exit()

#The method mode is called.
mode()