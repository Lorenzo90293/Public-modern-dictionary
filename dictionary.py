parola = input()
dizionario = {'Lit': 'si usa per descrivere qualcosa di molto bello, divertente o eccitante. Es: \"Questa festa è lit!\"',
            'Cringe': 'si usa per esprimere imbarazzo o disgusto per qualcosa o qualcuno. Es: \"Quel video è cringe!\"',
            'Flex': 'si usa per vantarsi di qualcosa che si possiede o che si è fatto. Es: \"Ho comprato l\'ultimo iPhone, flex!\"',
            'Ghostare': 'si usa per indicare il fatto di interrompere improvvisamente ogni contatto con una persona senza spiegazioni. Es: \"Mi ha ghostato dopo due appuntamenti!\"',
            'Hype': 'si usa per indicare l\'entusiasmo o l\'aspettativa per qualcosa. Es: \"C\'è tanto hype per il nuovo film di Marvel!\"',
            'Tossico/a': 'si usa per descrivere una persona o una relazione che fa male, che manipola o che crea dipendenza. Es: \"Lascia perdere, lui è tossico!\"',
            'Stan': 'si usa per indicare il fatto di essere un fan appassionato e devoto di qualcuno o qualcosa. Es: \"Sono una stan di Harry Potter!\"',
            'Shippare': 'si usa per indicare il fatto di sostenere o desiderare una relazione sentimentale tra due persone, reali o immaginarie. Es: \"Shippo troppo Ross e Rachel!\"',
            'Mood': 'si usa per esprimere il proprio stato d\'animo o per identificarsi con qualcosa o qualcuno. Es: \"Questo meme è il mio mood oggi!\"',
            'Savage': 'si usa per descrivere una persona o un\'azione che è audace, spietata o senza peli sulla lingua. Es: \"Ha risposto in modo savage al suo commento!\"'}
if parola in dizionario.keys():
    print(dizionario[parola])
else:
    print('La parola non è stata trovata o non esiste, provvederemo ad aggiungerla con il prossimo aggiornamento del dizionario.')