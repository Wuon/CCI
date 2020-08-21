def classifyStrings(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    vowelThreshold = 3
    consonantThreshold = 5
    
    curVowel = 0
    curConsonant = 0
    curPattern = -1
    
    isMixed = False
    
    prevChar = ''
    
    for character in s:
        if character == '?':
            vowelThreshold -= 1
            consonantThreshold -= 1
            isMixed = True
        else:
            pattern = 1 if character in vowels else 0
            if pattern != curPattern:
                if prevChar != '?':
                    isMixed = False
                    vowelThreshold = 3
                    consonantThreshold = 5
                curVowel = 0
                curConsonant = 0
                curPattern = pattern
            if pattern == 1:
                curVowel += 1
            else:
                curConsonant += 1
        if curVowel == vowelThreshold or curConsonant == consonantThreshold:
            return 'mixed' if isMixed else 'bad'
        prevChar = character
    return 'good'
