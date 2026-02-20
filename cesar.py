# en sträng med alla bokstäver i det svenska alfabetet
alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

# meddelandet som ska krypteras
meddelande = "hej"
# nyckeln är antalet positioner varje bokstav ska flyttas
nyckel = 1
# variabel för att lagra det krypterade meddelandet


# UPPDRAG: Skriv en loop som skriver ut "ifk"
# Tips: Använd .index() och []

for bokstav in meddelande:
    position = alfabet.index(bokstav)
    p = position + len(bokstav)
    
    print()
  
