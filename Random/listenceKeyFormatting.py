
def licenseKeyFormatting(S: str, K: int) -> str:
    ID = S.replace("-","").upper()

    length = len(ID)
    for i in range(length):
        if i % K == 0:
            index = length - i
            ID = ID[0:index] + "-" + ID[index:]

    return ID[0:-1]


# print(licenseKeyFormatting("5F3Z-2e-9-w", 2))
# print(licenseKeyFormatting("2-5g-3-J", 2))