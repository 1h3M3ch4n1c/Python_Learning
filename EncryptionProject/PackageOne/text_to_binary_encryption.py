#this program converts text into binary
text = input("Enter the text:\n")
binary_number = ""

def binary_conversion(input_text):
    #binary number conversion function
    input_text_number = ord(input_text)

    binary_number = ""

    while(input_text_number>0):
        binary_number = str(input_text_number%2)+binary_number
        input_text_number = int(input_text_number/2)
    return binary_number

binary_equivalent_text = ""
for each_letter in text:
    binary_equivalent_text = binary_conversion(each_letter)+binary_equivalent_text
print(binary_equivalent_text)
