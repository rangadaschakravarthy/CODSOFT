import random
import string
def generate(length=12):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=[
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
        ]
    password.extend(random.choice(characters)for _ in range(length-len(password)))
    random.shuffle(password)
    password="".join(password)
    return password
generatedpassword=generate()
print("Generated Password:",generatedpassword)