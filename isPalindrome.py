class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if not x: 
            print("There's nothing here.")
        elif len(str(x)) == 1:
            print("Not a palindrome because it has less than two digits.")
        my_string = str(x)
        pointer_one = 0
        pointer_two = len(my_string) - 1
        while pointer_one < pointer_two:
            if my_string[pointer_one] != my_string[pointer_two]:
                return False
            pointer_one += 1
            pointer_two -= 1
        return True
        
