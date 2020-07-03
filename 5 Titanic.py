print("Titanic érettségi feladat")
print("\n-------------------------------------------------------------\n")
print("1.Feladat: Beolvasás")
titanic_adatok=[]
db=0
with open("titanic.txt","r", encoding="utf-8") as titanicAdatok:
    for egySor in titanicAdatok:
        egyTitanic=egySor.strip().split(";")
        titanic_adatok.append([egyTitanic[0], int(egyTitanic[1]), int(egyTitanic[2])])
        db+=1
if(db>0):
    print("\tSikeres beolvasás")
else:
    print("\tSikertelen beolvasás")
#for i in range(len(titanic_adatok)):
#   print(titanic_adatok[i])
print("\n-------------------------------------------------------------\n")
print("2.Feladat: beolvasott sorok száma:")
print("\tBeolvasott sorok: ",len(titanic_adatok),"db")
print("\n-------------------------------------------------------------\n")
print("3.Feladat: Személyek száma")
Osszeg1=0
for i in range(len(titanic_adatok)):
    #print(titanic_adatok[i][1])
    Osszeg1+=titanic_adatok[i][1]+titanic_adatok[i][2]
print("Összesen ennyi utas volt: ",Osszeg1)
print("\n-------------------------------------------------------------\n")
print("4.Feladat: Keresés")
Kulcs=input("\tKérem adja meg a keresett kategoriát: ")
db=0
for i in range(len(titanic_adatok)):
    if(titanic_adatok[i][0].__contains__(Kulcs)):
        db+=1
        #print("\t",titanic_adatok[i][0])
if db>0:
    print("\tVan ilyen")
else:
    print("\tNincs ilyen")
print("\n-------------------------------------------------------------\n")
print("5.Feladat: Keresés eredménye:")
for i in range(len(titanic_adatok)):
    if(titanic_adatok[i][0].__contains__(Kulcs)):
        print("\t",titanic_adatok[i][0], "\t",titanic_adatok[i][1]+titanic_adatok[i][2]," fő")
print("\n-------------------------------------------------------------\n")
print("6.Feladat: eltüntek aránya nagyobb mint 60%")

for i in range(len(titanic_adatok)):
    Arany=(titanic_adatok[i][2]/(titanic_adatok[i][1]+titanic_adatok[i][2]))*100
    if Arany>60:
        print("\t",titanic_adatok[i][0],"\t",Arany)
print("\n-------------------------------------------------------------\n")
print("7.Feladat: melyik kategoriában volt a legtöbb túlélő")
Maxtulelo=0
MaxKategoria="cica"
for i in range(len(titanic_adatok)):
    if(Maxtulelo<titanic_adatok[i][1]):
        Maxtulelo=titanic_adatok[i][1]
        MaxKategoria=titanic_adatok[i][0]
print("\t",MaxKategoria,"\t:",Maxtulelo)
