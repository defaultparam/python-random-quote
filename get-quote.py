import random

def main():
  print("Keep it logically awesome.")
  print("There's your quote")
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes)
  i = random.randint(0,last)
  
  print(quotes[i])
if __name__== "__main__":
  main()
