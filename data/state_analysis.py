import state_demographics

list_of_report = state_demographics.get_all_states()

print(len(list_of_report))
print(list_of_report[0])

psm = list_of_report[0]["Population"]["Population per Square Mile"]
print(psm)
