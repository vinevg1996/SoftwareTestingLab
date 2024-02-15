#file_csv = input()
#file_csv_changed = input()

file_csv = "pap3.csv"
file_csv_changed = "pap3_lib.csv"

f_csv = open(file_csv, "r")
f_csv_out = open(file_csv_changed, "w")
for line in f_csv:
    print("line_start =", line)
    new_line = line.replace(",", ";")
    print("line_end =", new_line)
    f_csv_out.write(new_line)
