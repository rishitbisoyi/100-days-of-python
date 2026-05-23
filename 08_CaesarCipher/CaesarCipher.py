import sys

# decrypt
def encrypt(shift_no):
    message=input("Enter the message to be encrypted : ")
    encrypted_message=""
    for letter in message:
        if letter.isalpha():
            base=ord('A') if letter.isupper() else ord('a')
            encrypted_message+=chr((((ord(letter)-base)+shift_no)%26)+base)
        else:
            encrypted_message+=letter
    print(f"The encrypt message for {message} after shifting {shift_no} places is {encrypted_message}")

# Decrypt
def decrypt(shift_no):
    message=input("Enter the message to be decrypted : ")
    decrypted_message=""
    for letter in message:
        if letter.isalpha():
            base=ord('A') if letter.isupper() else ord('a')
            decrypted_message+=chr((((ord(letter)-base)-shift_no)%26)+base)
        else:
            decrypted_message+=letter
    print(f"The decrypted message for {message} after shifting {shift_no} places is {decrypted_message}")

# Start of application
print('''                                    
   ****       ***       ***       ******      ***     **** ***** 
  * ****     * ***      * ***    **  ****    * ***      **   ****  
 *   ****   *   ***    *   ***  ****        *   ***     **         
**         **    **   **    ***   ***      **    **     **         
**         **    **   ********      ***    **    **     **         
**         **    **   *******         ***  **    **     **         
**         **    **   **         ****  **  **    **     **         
***        **    **   ****        **** *   **    **     ***        
 *******    ***** **   *******     ****     ***** **     ***       
  *****      ***   **   *****                ***   **           ''')
print('''                                                              
             *                **                               
            ***               **                               
             *                **                               
                      ***     **                  ***  ****    
   ****    ***       * ***    **  ***      ***     **** **** 
  * ****    ***     *   ***   ** *****    * ***     **   ****  
 *   ****    **    **    **   ***   ***  *   ***    **         
**           **    **    **   **     ** **    ***   **         
**           **    **    **   **     ** ********    **         
**           **    **    **   **     ** *******     **         
**           **    **    **   **     ** **          **         
***          **    *******    **     ** ****        ***        
 *******     ***   ******     **     **  *******     ***       
  *****       ***  **          **    **   *****                
                   **                *                         
                   **               *                          
                    **             *                           
                                  *                      ''')
while True:
    print("\nWELCOME TO THE CAESAR CIPHER\nHERE YOU CAN ENCRYPT OR DECRYPT YOUR MESSAGES AS YOU WISH")
    choice=input("Enter \"E\" to encrypt your message and \"D\" to decrypt it a message : ")
    if choice.upper()=="E":
        shift_no=int(input("Enter the shift number : "))
        encrypt(shift_no)
    elif choice.upper()=="D":
        shift_no=int(input("Enter the shift number : "))
        decrypt(shift_no)
    else:
        print("Invalid choice\nPlease check your entered letter")
    again=input("If you want to go again press \"Y\" any other key to exit : ")
    if again.upper()=="Y":
        continue
    sys.exit()