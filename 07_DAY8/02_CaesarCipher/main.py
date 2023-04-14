import os
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar( cipher_direction , start_text , shift_amount ):
    end_text = ''

    if cipher_direction == 'decode':
        shift_amount *= -1

    for letter in start_text:
        if letter.isalpha():
            i = alphabet.index( letter )
            new_index = i + shift_amount

            if   new_index >= len( alphabet ) : new_index %= 26
            elif new_index < 0                : new_index += len( alphabet )

            end_text += alphabet[ new_index ]
        else : 
            end_text += letter

    print(f'\nThe { cipher_direction }d text is:\n{ end_text.capitalize() }\n')

def askUser():
    os.system('clear')
    print( logo )
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        
    try:
        os.system('clear')
        if direction == 'encode' or direction == 'decode':
            text = input("Type your message:\n").lower()
                
            if direction == 'decode':
                have_shift = input("\nDo you know the shift? Y or N:\n").upper()
                if have_shift == 'Y':
                    shift = int(input("\nType the shift number:\n"))
                    caesar( direction , text , shift )
                else: 
                    for n in range( 0 , len( alphabet )):
                        print(f'----------------\n\nShift: {n}')
                        caesar( direction , text , n )
            else:
                shift = int(input("\nType the shift number:\n"))
                caesar( direction , text , shift )
            
            restart = input('Type YES to start again, otherwhise type NO\n').upper()
            if restart == 'YES':
                askUser()
            else:
                print('\nThank you for trying my program! Have a nice day! ❤ \n')

        else: 
            raise Exception

    except Exception:
        askUser()

askUser()

