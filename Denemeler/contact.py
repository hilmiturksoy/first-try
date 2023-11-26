while True:
    try:
        q = input("Add (a), Search (s), Quit (q): ")

        if q == "a":
            with open("contact.txt", "a") as f:
                name = input("Name: ")
                phone = int(input("Phone: "))
                f.write(f"{name} : {phone}\n")
                print("Contact added successfully!")

        elif q == "s":
            search = input("Search: ")
            with open("contact.txt", "r") as f:
                found = False
                for line in f:
                    if search in line:
                        print(line, end='')
                        found = True

                if not found:
                    print(f"{search} not found in contacts.")

        elif q == "q":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid input. Please try again.")

    except Exception as e:
        print("Ups try again:", e)