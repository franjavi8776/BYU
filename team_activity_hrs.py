
with open("hr_system.txt") as f:

    for line in f:

        line = line.strip()

        parts = line.split(" ")

        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3])

        print(f"Name: {name}, Title: {job_title}")
