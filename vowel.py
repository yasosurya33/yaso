a=input()
vowels = ['a','e','i','o','u','A','E','I','O','U']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z',]
if(a in vowels) :
    print('Vowel')
elif(a in consonant):
    print('Consonant')
else:
    print('Invalid')
