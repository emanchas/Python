def output_without_whitespace():
    string = input("Enter a sentence or phrase: ")
    string = string.replace(' ', '')
    print ('String with no whitespace:', string)

def get_num_chars():
    string = input("Enter a sentence or phrase: ")
    print ('You entered:', string)
    print('Number of characters:', len(string) - string.count(" "))
    print ()
    output_without_whitespace()


get_num_chars()

