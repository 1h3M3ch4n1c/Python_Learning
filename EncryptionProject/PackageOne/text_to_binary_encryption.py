#this program converts text into binary
text = input("Enter the text:\n")   #input from the user
binary_number = ""  #variable to store the converted binary number

def binary_conversion(input_text):
    #binary number conversion function
    input_text_number = ord(input_text)
    binary_number = ""

    #code to convert to binary number
    while(input_text_number>0):
        binary_number = str(input_text_number%2)+binary_number
        input_text_number = int(input_text_number/2)
    if (ord(input_text) < 64):
        binary_number = "0"+binary_number
    return binary_number

#function calling
binary_equivalent_text = ""
for each_letter in text:
    binary_equivalent_text = str(binary_conversion(each_letter))+binary_equivalent_text
print(binary_equivalent_text)
