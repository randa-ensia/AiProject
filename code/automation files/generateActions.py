conditions = ['above average','ideal'];

products = ['Wheat','Corn'];

wilayas = [
    "ADRAR", "CHLEF", "LAGHOUAT", "O.E.BOUAGHI", "BATNA", "BEJAIA", "BISKRA", "BECHAR", 
    "BLIDA", "BOUIRA", "TAMANRASSET", "TEBESSA", "TLEMCEN", "TIARET", "TIZI-OUZOU", "ALGER", 
    "DJELFA", "JIJEL", "SETIF", "SAIDA", "SKIKDA", "S.B.ABBES", "ANNABA", "GUELMA", 
    "CONSTANTINE", "MEDEA", "MOSTAGANEM", "MSILA", "MASCARA", "OUARGLA", "ORAN", 
    "EL-BAYADH", "ILLIZI", "B.B.ARRERIDJ", "BOUMERDES", "EL-TARF", "TINDOUF", 
    "TISSEMSILT", "EL-OUED", "KHENCHELA", "SOUK-AHRAS", "TIPAZA", "MILA", "AIN-DEFLA", 
    "NAAMA", "A.TEMOUCHENT", "GHARDAIA", "RELIZANE"]

ranges = [0.5];

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
                print(LIST,',');


                
