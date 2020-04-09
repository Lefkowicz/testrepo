
"""
Solutions to the programming problems from quiz #7.

Author: Henry Lefkowicz
Date: 29/03/2020
"""


def count_cheeseburgers(filename):
    """Returns the number of lines in the file that start with the word
    cheeseburger.

    Parameters:
        filename - the name of the file to be read (a string)

    Returns:
        The number of lines in the specified file that begin with the word
        cheeseburger.
    """
    
    counter = 0
    split_list = []
    
    #opens the file and reads in the lines
    
    with open(filename, 'r') as f:
        file = f.readlines()
    
    #splits the line into their individual words
        for i in file:
            split_list.append(i.split())
    #checks to see if the first word is cheeseburger and increments counter if it is
        for i in range(len(split_list)):
            if split_list[i][0] =='cheeseburger':
                counter += 1
    #returns counter
        
        return counter
        

def min_cost_palindrome(string_to_change, o_cost, x_cost):
    
    
    '''
    
    Takes a potential palendrome and then calculates the cost of making it a palendrome, and returns the cost
    if it is already one, returns 0, if it can't ever be, returns -1

    '''

    string = []
    cost = 0
    
    # turns string into list
    
    for i in string_to_change:
        string.append(i)
        
    # if '?' isn't there, check to see if it's already a palendrome or if it can't be and return 0 and -1
    # respectivley
    
    if '?' not in string and string[::-1] == string:
        cost = 0
    if '?' not in string and string[::-1] != string:
        cost = -1

    # runs through the string on both sides and checks to see if they're the same. If they aren't,
    # makes the one that is the '?' equal to the one that isn't and increments by the cost of that
    
    for i in range(len(string)):
        front = string[i-1]
        back = string[-i]
        if front > back:
        # if front is greater than back, ie, you get -1 as your first value and the 0 as your last number 
        # ( 8 and 1 instead
        # of 1 and 8), just skip that interation and move on. It only happens once, so essentially,
        # it just protects
        # against the weird list slicing becuse lists start at 0 instead of one. 
            continue
        if front != back and front == '?':
            front = back
            if front == 'x':
                cost += x_cost
            elif front == 'o':
                cost += o_cost
      
        if front != back and back == '?':
            back = front
            if front == 'x':
                cost += x_cost
            elif front == 'o':
                cost += o_cost
        # if both front and back are question marks, set them to be the cheapest letter
    
        if front == '?' and back == '?':
            cost += 2 * min(o_cost, x_cost)
        
        # once i has reached the middle of the string, break out of the function.
        
        if i >= len(string)/2:
            break
    
    return(cost)

def main():
    
    count_cheeseburgers('file1.txt')
    min_cost_palindrome('xoxoxoxoxox', 3, 4)


if __name__ == "__main__":
    main()
