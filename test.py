# function to check if small string is  
# there in big string 
def check(string, sub_str): 
    if (string.find(sub_str) == -1): 
        print("NO") 
    else: 
        print("YES") 
            
# driver code 
string = ["1 medium sweet potato", "4 red baby potatoes", "4 gold baby potatoes"]
sub_str ="potatoes"
check(string, sub_str) 
