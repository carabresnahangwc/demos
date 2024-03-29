# Change symbols and numbers to letters
def replace_symbols(password):
    password = password.replace("1", "l")
    password = password.replace("!", "i")
    password = password.replace("2", "z")
    password = password.replace("3", "e")
    password = password.replace("@", "a")
    password = password.replace("4", "a")
    password = password.replace("$", "s")
    password = password.replace("5", "s")
    password = password.replace("#", "n")
    password = password.replace("6", "g")
    password = password.replace("7", "t")
    password = password.replace("8", "b")
    password = password.replace("9", "g")
    password = password.replace("0", "o")
return password

def main():
    f = open("dictionary.txt","r")
    found = False

    print("Can your password survive a dictionary attack?")
    test_password = input("Type in a trial password: ")
    test_password = replace_symbols(test_password)
    
    for line in f:

        if line.strip() == test_password.strip():
          found = True
          print("Password match found: ", line.strip())
          break

    if not found:
    print("Password not found... in this dictionary attack")


if __name__ == '__main__':
  main()
