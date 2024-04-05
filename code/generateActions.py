conditions = ['Poor','Below average','Average','Above Average','Ideal'];

products = ['Wheat','Corn','Dates','Potatoes','Tomatoes','Greenpepper','Aubergines','Onions','Carrots','Lemons','Apples'];

wilayas = [
    "ADRAR", "CHLEF", "LAGHOUAT", "O.E.BOUAGHI", "BATNA", "BEJAIA", "BISKRA", "BECHAR", 
    "BLIDA", "BOUIRA", "TAMANRASSET", "TEBESSA", "TLEMCEN", "TIARET", "TIZI-OUZOU", "ALGER", 
    "DJELFA", "JIJEL", "SETIF", "SAIDA", "SKIKDA", "S.B.ABBES", "ANNABA", "GUELMA", 
    "CONSTANTINE", "MEDEA", "MOSTAGANEM", "M'SILA", "MASCARA", "OUARGLA", "ORAN", 
    "EL-BAYADH", "ILLIZI", "B.B.ARRERIDJ", "BOUMERDES", "EL-TARF", "TINDOUF", 
    "TISSEMSILT", "EL-OUED", "KHENCHELA", "SOUK-AHRAS", "TIPAZA", "MILA", "AIN-DEFLA", 
    "NAAMA", "A.TEMOUCHENT", "GHARDAIA", "RELIZANE"]

ranges = [-0.15,-0.1 ,-0.05,0,0.05,0.10,0.15];

LIST = ["wilaya","product","condition",0];
large = list();
print(LIST);
for i in wilayas:
    for j in products:
        for e in conditions:
            for r in ranges:
                LIST[0] = i;
                LIST[1] = j;
                LIST[2] = e;
                LIST[3] = r;
                print(LIST);
                large.append(LIST);

print(len(large));
                
