def is_palindrome(x):

    x_str = str(x)
    
 
    x_str = x_str.replace(" ", "").lower()
    

    return x_str == x_str[::-1]


print(is_palindrome(12321))          
print(is_palindrome("A man a plan a canal Panama"))  
print(is_palindrome((1, 2, 3, 2, 1)))  
print(is_palindrome([1, 2, 3, 2, 1]))  
print(is_palindrome("Hello"))         
print(is_palindrome(12345))           
