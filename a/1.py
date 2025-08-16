#1
with open("output.txt", "w",) as file:
    file.write("Hello, world!")
    file.close()

#2
with open("output.txt", "r") as fi:
    content = fi.read()
print(content)
file.close()

#3
with open("data.txt", "r") as source:
    content = source.read()
with open("backup.txt", "w") as backup:
    backup.write(content)

print("файл скопійовано у backup.txt")


#4
with open("data.txt", "r") as f:
    lines = f.readlines()

print("Кількість рядків у файлі:", len(lines))

#5
def analyze_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    lines = text.splitlines()
    num_lines = len(lines)
    words = text.split()
    num_words = len(words)
    num_chars = len(text)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Кількість рядків: {num_lines}\n")
        f.write(f"Кількість слів: {num_words}\n")
        f.write(f"Кількість символів: {num_chars}\n")
    print("звіт створено у", output_file)
analyze_file("data.txt", "summary.txt")

#6
def shift_letter(ch):
    if 'a' <= ch <= 'z':
        return chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
    elif 'A' <= ch <= 'Z':
        return chr((ord(ch) - ord('A') + 1) % 26 + ord('A'))
    else:
        return ch
def encrypt_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    encrypted = "".join(shift_letter(ch) for ch in text)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(encrypted)
    print("файл зашифровано у", output_file)
encrypt_file("data.txt", "encrypted.txt")

#🫃