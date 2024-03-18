print("Enter names, one per line (Press Ctrl+D or Ctrl+Z + Enter to finish):")
names = []

while True:
    try:
        name = input()
        names.append(name)
    except EOFError:
        break

print("Adieu to these names:")
for name in names:
    print(name)
