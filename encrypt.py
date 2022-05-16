from enigma.machine import EnigmaMachine

# Enigma Machine Initalization
machine = EnigmaMachine.from_key_sheet(
    rotors = 'V II IV',
    reflector = 'B',
    ring_settings = '17 09 02',
    plugboard_settings = 'KT AJ IV UR NY HZ OD XF PB CQ')

#Initial Rotate Position
startingPosition = 'JPH'
machine.set_display(startingPosition)

#Cipher'd Key
private_msg_key = 'TST'
public_msg_key = machine.process_text(private_msg_key)
#print(public_msg_key)

#Message
machine.set_display(private_msg_key)
plainText = 'THIS IS A ENCRYPTED MESSAGE TEST'
cipherText = machine.process_text(plainText)
#print(cipherText)


#Large Message------------------------------------------------------------
fullMessage = ''

#Header
recipient = 'B' #Recipient Designator
daySent = 'MC' #Day Transmission Sent
timeSent = '1118' #Time Transmission Sent
sender = 'A' #Sender Designator
transmissionLength = str(len(cipherText)) #Transmission Length
startingPosition = startingPosition #Starting Position
public_msg_key = public_msg_key #Encypted Key
fullMessage = fullMessage + recipient + ' '
fullMessage = fullMessage + daySent + ' '
fullMessage = fullMessage + sender + ' '
fullMessage = fullMessage + timeSent + ' '
fullMessage = fullMessage + '=' + ' '
fullMessage = fullMessage + transmissionLength + ' '
fullMessage = fullMessage + '=' + ' '
fullMessage = fullMessage + startingPosition + ' '
fullMessage = fullMessage + public_msg_key + ' '
fullMessage = fullMessage + '=' + ' '

fullMessage = fullMessage + '\n'

#Kenngruppen(shared, 2 garbage chars total)
prepend = 'UH'
append = ''
Kenngruppen = 'AZY' #3 chars (not garbage)
fullMessage = fullMessage + prepend
fullMessage = fullMessage + Kenngruppen
fullMessage = fullMessage + append + ' '

#Message
fullMessage = fullMessage + cipherText
print(fullMessage)
with open('message.txt', 'w') as f:
    f.write(fullMessage)




