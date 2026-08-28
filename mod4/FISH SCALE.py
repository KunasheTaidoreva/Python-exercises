Length = int(input("Enter the fish length in centimetres: "))
limit=42
if Length < limit:
    missed_length = limit - Length
    print("The fish is below the size limit by",missed_Length,"centimetres. So please release it.")
