#this program converts binary number sequence into text
input_number = str(input("Enter the binary sequnce:\n"))
binary_sequence_index = len(input_number)

def decimal_conversion(input_number):
    input_number_len = len(input_number)
    input_number_decimal = 0
    iItr = 0
    while (iItr < input_number_len):
        input_number_decimal += int(input_number[input_number_len-iItr-1])*pow(2,iItr)
        iItr +=1
    return input_number_decimal

while (binary_sequence_index>=0):
    binary_sequence_cut = input_number[binary_sequence_index:binary_sequence_index+7]
    binary_sequence_index -= 7
    if (binary_sequence_cut != ""):
        print (chr(decimal_conversion(binary_sequence_cut)),end="")