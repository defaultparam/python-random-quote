import random

def main():
  print("Keep it logically awesome.")
  print("There's your quote")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)

  i = random.randint(0,(last-1))
  print(quotes[i], end="")
  i = random.randint(0,(last-1))
  print(quotes[i], end="")

  quote = input('Add a quote of your own now: ')
  f = open('quotes.txt', 'a')
  f.write(quote+'\n')
  f.close()
if __name__== "__main__":
  main()
