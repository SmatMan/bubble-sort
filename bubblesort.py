input = [7, 3, 8, 4, 12, 9, 1, 2, 1, 7]
starting = str(input)

prevoutput = []

position = 0

length = len(input) - 1

print(length)
while True:
    sorted = True
    position = 0
    for i in range(length):
        if not input[position + 1] > length and input[position] > input[position + 1]:
            temp = input[position]
            input[position] = input[position + 1]
            input[position + 1] = temp
            sorted = False
        print(input)
        print(position)
        position += 1
    if sorted == True:
        print(f"Finished! {starting} -> {input}")
        break