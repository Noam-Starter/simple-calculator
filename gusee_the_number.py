print("ברוך הבא למשחק ניחוש המספר!")
secret_number = random.randint(1, 100)
guess = None
tries = 0

while guess != secret_number:
    guess = int(input("נחש מספר בין 1 ל-100: "))
    tries += 1

    if guess < secret_number:
        print("קטן מדי!")
    elif guess > secret_number:
        print("גדול מדי!")

print(f"כל הכבוד! ניחשת את המספר {secret_number} ב-{tries} נסיונות."
