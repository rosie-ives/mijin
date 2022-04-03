def mijin(lisa):
    sum = 0
    for p in lisa:
        sum = sum + p
    return sum/len(lisa)

bubushka = [12, 67, 9, 90, 2]
print(mijin(bubushka))