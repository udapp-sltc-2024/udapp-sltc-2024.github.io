import csv

with open("sheet.tsv") as sheet_handle:
    reader = csv.DictReader(sheet_handle,delimiter="\t")

    for submission in reader:
        if submission["presenting"] == "Yes":
            print("### _{}_".format(submission["title"]))
            print("#### {} ({})".format(
                submission["author"],
                submission["affiliation"]))
            print(submission["abstract"])
            print()