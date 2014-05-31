 #coding=utf-8 
print "Τεστ: Που θες να πας διακοπές το καλοκαίρι?"

lista = ["0) Το πρωι μ αρέσει να ξυπνάω και na παίρνω καθαρό αέρα ",
	 "1) Θέλω να κάνω πολλά μπάνια",
	 "2) Θέλω να κάνω ορειβασία",
	 "3) Θέλω να πάω σε μουσεία",
         "4) Θέλω να παίζω ρακέτες",
         "5) Μ αρέσει να πηγαίνω για ψάρεμα",
         "6) Μ αρέσει το mountain bike",
         "7) Θέλω να πηγαίνω σε beach parties",
         "8) Δεν θέλω να κάνω τίποτα!"]
for i in range (9):
    print lista[i]

a= raw_input()
lista2= a.split()
vouna=0
nhsi=0
athina=0
i=0
while i<len(lista2):
    print lista2[i]
    if int(lista2[i]) in [0,2,5,6]:
       vouna=vouna+1
    elif int(lista2[i]) in [1, 4, 7]:
        nhsi=nhsi+1
    elif int(lista2[i]) in [3, 8]:
        athina=athina+1
    i=i+1


if vouna>nhsi and vouna>athina:
    print "Πήγαινε σε βουνό"
elif nhsi> vouna and nhsi>athina:
    print "Πηγαινε σε νησι"
else:
    print "Μείνε στην αθήνα"
    
    
