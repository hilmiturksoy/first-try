def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':  # Görev Ekle
            print()
            try:
                n_tasks = int(input("How many tasks do you want to add: "))
                if n_tasks <= 0:
                    print("Please enter a positive number.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            for i in range(n_tasks):
                task = input(f"Enter task {i + 1}: ").strip()
                if not task:  # Boş görev kontrolü
                    print("Task cannot be empty. Please try again.")
                    continue
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':  # Görevleri Göster
            if not tasks:  # Liste boşsa uyarı ver
                print("\nNo tasks in the list.")
            else:
                print("\nTasks:")
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':  # Görevi Tamamlandı Olarak İşaretle
            if not tasks:  # Liste boşsa uyarı ver
                print("\nNo tasks to mark as done.")
            else:
                try:
                    task_index = int(input("Enter the task number to mark as done: ")) - 1
                    if 0 <= task_index < len(tasks):
                        tasks[task_index]["done"] = True
                        print(f"Task {task_index + 1} marked as done!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input! Please enter a valid task number.")

        elif choice == '4':  # Çıkış
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
