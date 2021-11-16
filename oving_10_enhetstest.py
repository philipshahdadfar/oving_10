
import unittest
  
class Flervalgssporsmaal:
    
    def __init__(self, sporsmaal, riktig_svar, valg):
        self.__sporsmaal = sporsmaal
        self.__valg = valg
        self.__riktig_svar = riktig_svar
        
        
    @property
    def sporsmaal(self):
        return self.__sporsmaal
    @property
    def valg(self):
        return self.__valg
    @property
    def riktig_svar(self):
        return self.__riktig_svar
  
 ##########################################################   
    def sjekk_svar(self, svaret):
        if svaret == self.riktig_svar:
            return True
        else:
            return False
        
    def __str__(self):
        tekst = "Spørsmål:  " 
        tekst += self.sporsmaal + "\n"
        
        for valg_nr, svar in enumerate(self.valg):
            tekst += f"{valg_nr}: {svar} \n"
            
        return tekst
    
    def korrekt_svar_tekst(self):
        tekst = f"Korrekt svar: {self.valg[self.__riktig_svar]}"
        
        return tekst
    
#############################################################

def lag_sporsmaal():
    sporsmaalene = []
        
    file = open("sporsmaalsfil.txt", "r", encoding="UTF8")
    
    for line in file:
        
        stripped_line = line.strip()
        
        stripped_line = stripped_line.replace("[","")
        stripped_line = stripped_line.replace("]","")
                
        split_line = stripped_line.split(":")
                
        #print(split_line)
                    
            
        question = split_line[0]
            
        answer = int(split_line[1])
            
        options = split_line[2]
        
        opt1 = options.split(",")
        
        
        sporsmaalene.append(Flervalgssporsmaal(question, answer, opt1))
    
    return sporsmaalene


            
            
    
class TestFlervalgssporsmaal(unittest.TestCase):
    
    def test_sjekk_svar(self):
        flervalgssporsmaal1 = Flervalgssporsmaal("Den delen av en datamaskin som kjører programmet kalles?:", 2, ["RAM", "Harddisk", "CPU", "Sekundærlager"])
        self.assertEqual(flervalgssporsmaal1, True)
    
    
    

    
    






if __name__ == "__main__":
    unittest.main()