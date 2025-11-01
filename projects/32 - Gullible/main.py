while True:
    ans = input("Do you want to know how to keep a gullible person busy for hours? (yes/no): ")
    if ans.strip().lower() == "no":
        break
    elif ans.strip().lower() == "yes":
        continue
    
    print("Not a valid answer. Please type 'yes' or 'no'.")