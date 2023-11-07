#Caesar Cipher program.
import Caesar_Cipher.Art as Art
print(Art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ,
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#26 alphabets [0 - 25]

#using while loop to get multiple actions 
action = True
while action:
    Direction = input("Enter encode to Encrypt and decode to decrypt:\n ").lower()
    user_text = input("Enter the message here:\n ").lower()
    shift = int(input("Enter the shift number:\n "))

    def Caeser(direction , shift_amount , text ):
        temp = "" 
        shift_amount = shift_amount % 26 #To prevent out of index error. We knowp that there are 26 alphabets and if we type shift amount above 26 it will throw error that's why we are using modulus(%) by using it the remainder is considered as the shift amount.
        """For example, if the shift amount is 78 then
        shilft_amount =  78 % 26 and thats 3 ,so it alphabet.index(item) + 3. done it's pretty simple right."""
        if direction == "decode":
            shift_amount *= -1 #if shift is 5 for encode then for decode it become -5
        #If the user wants to enter the value such as \^$^* etc to save that we are going to use the char
        #for letter in text:
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                value = alphabet[new_position]
                temp += value
            else:   # If the alphabet doesn't containing %^&9908 any type of this then it is added to temp
                temp += char 
        print(f"The message is {user_text} as:  \n{temp}")
    Caeser(direction= Direction , shift_amount= shift , text = user_text)        
    
    choice = input("Do you want to continue (Y/N): ").lower()
    if choice == "n":
        action = False
        print("GoodBye!....")
        break