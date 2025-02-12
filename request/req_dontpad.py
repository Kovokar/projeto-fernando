import requests as r

# response = r.get('https://example.com')

def post():

    print("FAZENDO REQUEST...\n\n")
    
    texto = 'PEDRO PICA'
    last = '1739323122827'
    boolean = 'false'
    token = '-449589abc997470c1967'

    cont = 0
    for i in range(4):
        cont += 1
        payload = {
            'text': f'{texto}',
            'lastModified': f'{last}',
            'force': f'{boolean}',
            'session-token': f'{token}'
                }

        texto = f'{texto}' 
        responde = r.post("https://api.dontpad.com/cebola_emo/goo", params=payload)
        last = responde.text

        print(responde.text)
