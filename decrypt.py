from enigma.machine import EnigmaMachine

### Enigma Machine Initalization
##machine = EnigmaMachine.from_key_sheet(
##    rotors = 'II IV V',
##    reflector = 'B',
##    ring_settings = '1 20 11',
##    plugboard_settings = 'AV BS CG DL FU HZ IN KM OW RX')
##
###Initial Rotor Position (UNENCRYPTED)
##machine.set_display('WXC')
##
###Decrypt Cipher Key
##public_msg_key = 'FDH' #(ENCRYPTED) given from encrypt.py @ generation
##private_msg_key = machine.process_text(public_msg_key)
##print(private_msg_key)
##
###Decrypt message key
##machine.set_display(private_msg_key)
###Input Cipher Text
##cipherText = 'SNRWJTYIAEE'
###Output Plaintext
##plainText = machine.process_text(cipherText)
##print(plainText)



#Large Message------------------------------------------------------------
with open('message.txt') as f:
    fullMessage = f.readlines()
#print(fullMessage)
header = fullMessage[0]
Kenngruppen = fullMessage[1].split()[0]
cipherText = fullMessage[1].split()[1]
print('Kenngruppen:')
print(Kenngruppen)
print('Initiate New Machine Settings:')
#defaults
userRotors = 'II IV V' 
userReflector = 'B'
userRing_settings = '1 20 11'
userPlugboard_settings = 'AV BS CG DL FU HZ IN KM OW RX'

userRotors = input('Rotors: ') #Walzenlage
userReflector = input('Reflector: ') #Set usually to the same everytime
userRing_settings = input('Ring Settings: ') #Ringstellung
userPlugboard_settings= input('Plugboard Settings: ') #Steckerverbindungen

# User Enigma Machine
machine2 = EnigmaMachine.from_key_sheet(
    rotors = userRotors,
    reflector = userReflector,
    ring_settings = userRing_settings,
    plugboard_settings = userPlugboard_settings)


recipient = header.split()[0]
daySent = header.split()[1]
sender = header.split()[2]
timeSent = header.split()[3]
#print(header.split()[4])
transmissionLength = header.split()[5]
#print(header.split()[6])
startingPosition = header.split()[7]
public_msg_key = header.split()[8]
#print(header.split()[9])


#Initial Rotor Position (UNENCRYPTED)
machine2.set_display(startingPosition)

#Decrypt Cipher Key
private_msg_key = machine2.process_text(public_msg_key)
print(private_msg_key)

#Decrypt message key
machine2.set_display(private_msg_key)
#Output Plaintext
plainText = machine2.process_text(cipherText)
print(plainText)
















