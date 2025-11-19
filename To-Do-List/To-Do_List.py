from csv import DictReader, DictWriter
import os

print()
print("Welcome to Task Manager!")
print()
print("Show pending task(s): Press 's'\n Add Task(s): Press 'a'\n To Quit: Press 'q'\n To Check Completed Tasks: Press 'd'")

while True:
    function = input("What do you want to do?: ").lower()

    if function == "a":


        while True:
            text1 = "Add A Task"
            print(f"{text1:^20}")
            print()
            tasks = input("Enter a task: ").rstrip()
            if tasks == "q":
                print()
                print("Press q again to quit the whole manager")
                print()
                break
            if not os.path.exists("task.csv") or os.path.getsize("task.csv") == 0:
                with open("task.csv", "w") as file:
                    writer = DictWriter(file, fieldnames=["tasks", "times", "am_pm"])
                    writer.writeheader()
            
            times = input("Enter a time: ").rstrip()
            am_pm = input("AM / PM?: ").rstrip()
            print()
            print("Enter another task! (q to Quit)")
            print()
            with open("task.csv", "a") as file:
                writer = DictWriter(file, fieldnames=["tasks", "times", "am_pm"])
                writer.writerow({"tasks": tasks, "times":times, "am_pm":am_pm})



    elif function == "s":
        i = 0
        text2 = "TASKS"
        print(f"{text2:^20}")
        print("--------------------")
        with open("task.csv") as file:
            reader = DictReader (file)
            for row in reader:
                i += 1
                print(f"{i}) {row['tasks']} : {row['times']} {row['am_pm']}")
                print()
        break

    elif function == "d":
        i = 0
        rows = []
        with open("task.csv") as file:
            reader = DictReader(file, fieldnames=["tasks", "times", "am_pm"])
            for row in reader:
                i += 1
                print(f"{i}) {row['tasks']} : {row['times']} {row['am_pm']}")
                print()

        dltTask = input("Enter the name of the task: ")
        with open("task.csv") as file:
            dltReader = DictReader(file)

            for row in dltReader:
                if row["tasks"].strip().lower() != dltTask:
                    rows.append(row)
            
        with open("task.csv", "w") as file:
            dltWriter = DictWriter(file, fieldnames=["tasks", "times", "am_pm"])
            dltWriter.writeheader()
            dltWriter.writerows(rows)

    elif function == "q":
        print()
        print("Visit Again!")
        break

    else:
        print()
        print("ENTER A VALID FUNCTION")
        print()
        pass
