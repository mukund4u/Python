# From a given statement find vowel & consonants

def check_for_vowels_consonants(str):
    vowel_count = ""
    consonents_count = ""
    for item in str:
        if item.lower() in 'aeiou':
            vowel_count+= item
        else:
            consonents_count+= item
            
    print('vowel is present and its count:', vowel_count)
    print('consonents_count is present and its count:', consonents_count)


output = input('please enter the statement:')
check_for_vowels_consonants(output)

# Find 3rd largest number in a given array
def third_largest_number(lst):    
    lst.sort()
    out = lst[-3]
    return out

usr_inp = list(map(int,input('enter a number to find 3rd largest:').split()))  
print('3rd largest number is:', third_largest_number(usr_inp)) 