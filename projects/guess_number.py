import random

def guess(x):
  random_number = random.randint(1, x) # komputer menggunakan fungsi random.randint() untuk menghasilkan sebuah angka acak antara 1 dan x.
  guess = 0 # variable ini digunakan untuk menyimpan tebakan
  while guess != random_number: # selama tebakan (guess) tidak sama dengan angka yang dibuat oleh komputer (random_number), permainan akna terus berlanjut
    guess = int(input(f'Guess a number between 1 and {x}: ')) # komputer meminta untuk memasukkan tebakan dan disimpan ke variable guess
    if guess < random_number:
      print('Sorry, guess again. Too low.')
    elif guess > random_number:
      print('Sorry, guess again. To high.')
  print(f'Yay, congrats. You have guessed the number {random_number} correct')


guess(25)
