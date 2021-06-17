from csv import reader

# open file in read mode
with open('rezultati.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Get all rows of csv from csv_reader object as list of tuples
    rezultati = list(map(tuple, csv_reader))
    # display all rows of csv
    rezultati.sort()
  #  print(rezultati)

for ime, prezime, bodovi in rezultati:
    if int(bodovi) < 49:
        print("Nedovoljan:",ime, prezime, bodovi)
for ime, prezime, bodovi in rezultati:
    if int(bodovi) > 50 and int(bodovi) < 65:
        print("Dovoljan:",ime, prezime, bodovi)
for ime, prezime, bodovi in rezultati:
    if int(bodovi) > 65 and int(bodovi) < 80:
        print("Dobar:",ime, prezime, bodovi)
for ime, prezime, bodovi in rezultati:
    if int(bodovi) > 80 and int(bodovi) < 90:
        print("Vrlo dobar:",ime, prezime, bodovi)
for ime, prezime, bodovi in rezultati:
    if int(bodovi) > 90:
        print("Odličan:",ime, prezime, bodovi)


novi_rezultati = []
for ime, prezime, bodovi in rezultati:
    novi_rezultati.append((ime, prezime, bodovi))
#print(novi_rezultati)
novi_rezultati.sort(key=lambda x: x[1])
print(novi_rezultati)
