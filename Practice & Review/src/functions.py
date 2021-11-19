"""
------------------------------------------------------------------------
Functions
------------------------------------------------------------------------
Author:  Chandler Mayberry
Date_last_updated = 2020-01-13
------------------------------------------------------------------------
"""
#constants
VOWEL = ['a','A','e','E','i','I','o','O','u','U']
PIG_VOWEL = ['a','A','e','E','i','I','o','O','u','U','y','Y']


def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a (int)
    -------------------------------------------------------
    """
    md = 0
    
    for position in range(len(a)-1):
        value = abs(a[position] - a[position+1])
        
        if value > md:
            md = value
    
    
    return md


def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    
    if name[0].isalpha() or name[0] == '_' and len(name)>0: 
        valid = True
    else:
        valid = False
    
    k = 0
    while k < len(name) and valid:
        if name[k]=='_' or name[k].isalnum():
            valid = True
        else: 
            valid = False
        
        k+=1
    
    return valid


def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    #var
    total = 0
    small = a[0][0]
    large = a[0][0]
    amount = 0
    
    
    for w in a:
        #each number in row
        for j in w:
            if j > large:
                large = j
                
            if j < small:
                small = j
                
            total += j
            amount += 1
    
    
    average = total/amount
    
    return small, large, total, average


def matrix_flatten(a):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list a. A 'flattened' list is a
    2D list that is converted into a 1D list.
    a must be unchanged.
    Use: b = matrix_flatten(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of ?)
    Returns:
        b - the flattened version of a (list of ?)
    -------------------------------------------------------
    """
    b = []
    
    for w in a:
        for j in w:
            
            b.append(j)
    
    return b


def matrixes_add(a, b):
    """
    -------------------------------------------------------
    Sums the contents of matrixes a and b. a and b must have
    the same number of rows and columns.
    a and b must be unchanged.
    Use: c = matrixes_add(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix sum of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    #compare to check rows and col.
    assert len(a) == len(b) and len(a[0]) == len(b[0])
    
    c = []
    
    for k in range(len(a)):
        
        inserter = []
        
        for j in range(len(a[k])):
            inserter.append(a[k][j] + b[k][j])
    
        c.append(inserter)
        
 
    return c


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    c = []
    
    for row in range(len(a)):
        sizer = []
        
        for col in range(len(b[0])):
            sizer.append(0)
            
        c.append(sizer)
    
    
    for row in range(len(a)):
        for col in range(len(b[0])):
            for row2 in range(len(b)):
                
                c[row][col] += (a[row][row2]) * (b[row2][col])
    
    
    return c


def matrix_rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    a must be unchanged.
    Use: b = matrix_rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of int/float)
    Returns:
        b - the rotated 2D list of values (2D list of int/float)
    -------------------------------------------------------
    """
    b = []
    
    #list sizer
    for q in range(len(a[0])):
        sizer = []
        for j in range(len(a)):
            sizer.append(0)
        b.append(sizer)
     
    #front-ward list input (transposing)
    for k in range(len(a)):
        for j in range(len(a[k])):
            b[j][k] = a[k][j]
    
    #reverse list
    for row_reverse in range(len(b)):
        b[row_reverse] = b[row_reverse][::-1]
        
    return b


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    r = 0
    w = 0
    d = 0
    u = 0
    l = 0
    
    for sentence in fv:
        for char in sentence:
            
            if char.islower():
                l += 1
            elif char.isupper():
                u += 1
            elif char.isdigit():
                d += 1
            elif char.isspace():
                w += 1
            else:
                r += 1
    
    
    return u, l, d, w, r


def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvwl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    out = ''
    
    for char in s:
        if char not in VOWEL:
            out += char
            
    return out


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    
    -"y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    
    -Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    """
    #i'ith letter in the word will be capitalized
    #consonants is every character that is not a vowel
    
    pl = ''    
    k = len(word)
    if word[0] in VOWEL:
        
        pl = word + 'way'
        
    else:
        
        end = ''
        if( word[0] in ['y', 'Y'] ):
            end += word[0]

            i = 1
            found_vowel = False
            
            while( not found_vowel ):
                if( word[i] not in PIG_VOWEL ):
                    end += word[i]
                    i += 1
                    
                else:
                    found_vowel = True
                    
            temp_lat = (word[i::] + end).lower()
            
        else:
            
            i = 0
            found_vowel = False
            
            while( not found_vowel ):
                if( word[i] not in PIG_VOWEL ):
                    end += word[i]
                    i += 1
                    
                else:
                    found_vowel = True
                                
            temp_lat = (word[i::] + end).lower()
            
    
        #final capitalization check
        pl = ''
        for i in range(len(word)):
            if word[i].isupper():
                pl += temp_lat[i].upper()
            else:
                pl += temp_lat[i]

        pl += 'ay'
    
    return pl





