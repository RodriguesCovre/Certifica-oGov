import string
def isPalindrome(str):
   exclude = set(string.punctuation)
   str = ''.join(ch for ch in str if ch not in exclude)
   str = str.replace(" ", "").lower()
   return str == str[::-1]

  


# Solicitar que o usuário digite a sentença
def main():
  userInput = input("Enter a WORD to be tested as a palindrome:")

  if (isPalindrome(userInput)):
    print(userInput + " is a palindrome!")
  else:
    print(userInput + " is NOT a palindrome!")

if __name__ == "__main__":
    main()