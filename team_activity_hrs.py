
with open("hr_system.txt") as f:

    for line in f:

        line = line.strip()

        parts = line.split(" ")

        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3])

        biweekly_payment = salary / 24

        if job_title == "Engineer":
            biweekly_payment += 1000


        print(f"{name} (ID: {id_number}), {job_title} - ${biweekly_payment:.2f}")
