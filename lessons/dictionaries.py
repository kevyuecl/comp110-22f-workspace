schools: dict[str, int]

schools = dict()

schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

print(schools)

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")