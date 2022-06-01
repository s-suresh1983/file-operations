# creating lists using secret and key files
with open('secret.txt', 'r') as file1:
    secret = file1.readlines()
with open('key.txt', 'r') as file2:
    key = file2.readlines()
# creating rows and columns using the created list rows incremented by 1 for 20 rows otherwise only 19 rows printed
columns = int(key[0].strip())
rows = int(key[1].strip()) + 1
# creating helper variable for row and column
row = 1
column = 1
# creating list and empty string for filling rows and columns
secret_word = ''
secret_list = []
# filing the rows and columns
for i in secret:
    if row < rows:
        if column < columns:
            column += 1
            secret_word += i.strip()
        else:
            secret_word += i.strip()
            secret_word += '\n'
            secret_list.append(secret_word)
            row += 1
            column = 1
            secret_word = ''
# writing the secret list to public.txt file
with open('public.txt', 'w') as file3:
    for j in secret_list:
        file3.write(j)
