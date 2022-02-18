from colorama import Fore, init
init()

#$
rojo = Fore.RED
azul = Fore.BLUE
blanco = Fore.WHITE
violeta = Fore.MAGENTA
cyan = Fore.CYAN
amarillo = Fore.YELLOW
verde = Fore.GREEN
#$

def portada():
     print(f"""{violeta}

░░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄▄
░░░░░█░░░░░░░░░░░░░░░░░░▀▀▄
░░░░█░░░░░░░░░░░░░░░░░░░░░░█
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█
░▄▀░▄▄▄░░█▀▀▀▀▄▄█░░░██▄▄█░░░░█
█░░█░▄░▀▄▄▄▀░░░░░░░░█░░░░░░░░░█
█░░█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄░█
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
░░░█░░░░██░░▀█▄▄▄█▄▄█▄▄██▄░░█
░░░░█░░░░▀▀▄░█░░░█░█▀█▀█▀██░█
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
░░░░░░░▀▄▄░░░░░░░░░░░░░░░░░░░█
░░▐▌░█░░░░▀▀▄▄░░░░░░░░░░░░░░░█
░░░█▐▌░░░░░░█░▀▄▄▄▄▄░░░░░░░░█
░░███░░░░░▄▄█░▄▄░██▄▄▄▄▄▄▄▄▀
░▐████░░▄▀█▀█▄▄▄▄▄█▀▄▀▄
░░█░░▌░█░░░▀▄░█▀█░▄▀░░░█
░░█░░▌░█░░█░░█░░░█░░█░░█
░░█░░▀▀░░██░░█░░░█░░█░░█
░░░▀▀▄▄▀▀░█░░░▀▄▀▀▀▀█░░█
░░░░░░░░░░█░░░░▄░░▄██▄▄▀
░░░░░░░░░░█░░░░▄░░████
░░░░░░░░░░█▄░░▄▄▄░░▄█
░░░░░░░░░░░█▀▀░▄░▀▀█
░░░░░░░░░░░█░░░█░░░█
░░░░░░░░░░░█░░░▐░░░█
░░░░░░░░░░░█░░░▐░░░█
░░░░░░░░░░░█░░░▐░░░█
░░░░░░░░░░░█░░░▐░░░█
░░░░░░░░░░░█░░░▐░░░█
░░░░░░░░░░░█▄▄▄▐▄▄▄█
░░░░░░░▄▄▄▄▀▄▄▀█▀▄▄▀▄▄▄▄
░░░░░▄▀▄░▄░▄░░░█░░░▄░▄░▄▀▄
░░░░░█▄▄▄▄▄▄▄▄▄▀▄▄▄▄▄▄▄▄▄█{violeta}
{cyan} ＰＲＯＹＥＣＴＯ ： ＴＲＯＬＬＤＯＸ {cyan} 
{violeta} Created by Z3RO{violeta}
{rojo}[{rojo}{amarillo}+{amarillo}{rojo}]{rojo}{cyan} Dni = Informacion de un Dni Peruano
{rojo}[{rojo}{amarillo}+{amarillo}{rojo}]{rojo}{cyan}direccion = Direccion y nombres completos por dni peruano 
{rojo}[{rojo}{amarillo}+{amarillo}{rojo}]{rojo}{cyan}EpicDox = Doxeo Completo de un numero telefonico
{rojo}[{rojo}{amarillo}+{amarillo}{rojo}]{rojo}{cyan} Tool Publica De H-krs:
""")

def consulta_dni():
    dni = input("[+] Escribe el dni: ")
    def datos_del_doc():
        url = f"https://api.reniec.online/dni/{dni}"
        data1 = requests.get(url, verify=False)
        resp = data1.json()
        print(f"{azul}DNI : {blanco}"+resp['dni'])
        print(f"{azul}NOMBRES : {blanco}"+resp['nombres'])
        print(f"{azul}APELLIDO PATERNO : {blanco}"+resp['apellido_paterno'])
        print(f"{azul}APELLIDO MATERNO : {blanco}"+resp['apellido_materno'])
        #print(f"{azul}CODIGO VERIFICACIÓN : {blanco}"+resp['cui'])

    def verificar_documento():
        url2 = f"https://api.reniec.online/dni/{dni}"
        data2 = requests.get(url2, verify=False)
        respuesta = data2.json()
        # verificar la validez del documento introducido
        # en caso que exista los datos seran devueltos sean +18 o -18
        # si el dni no existe = [error:NO_DATA]
        try:
            respuesta['dni']
            datos_del_doc()
        except KeyError:
            print(f"{rojo}ERROR NO DATA")
    
    verificar_documento()
    
#sistema de verificacion de ruc
def consultaruc():
    token = '?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImdyYWR5Mzl1X24yOTFpQG5hZnhvLmNvbSJ9.cl5KQzsXaRuLuwEUWNJDLX_Zh2R_HkBsn9_YEP4keio'
    rucki = input("[+] RUC >> ")
    response = requests.get("https://dniruc.apisperu.com/api/v1/ruc/" +rucki +token)
    for key, value in response.json().items():
        print("[-] %s: %s" % (key, value))

# consulta de nombres y apellidos por dni
def consulta_por_nombres():
    name = input("ESCRIBE EL NOMBRE: ")
    apellidop = input("ESCRIBE EL APELLIDO PATERNO: ")
    apellidom = input("ESCRIBE EL APELLIDO MATERNO: ")
    url = "https://buscardni.xyz/buscador/ejemplo_ajax_proceso.php"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = f"APE_PAT={apellidop}&APE_MAT={apellidom}&NOMBRES={name}"
    resp = requests.post(url, headers=headers, data=data)
    text = resp.text
    soup = BeautifulSoup(text, "lxml")
    text2 = soup.get_text()
    new_b = text2[131:]
    characters = "ver"
    string = ''.join( x for x in new_b if x not in characters)
    print(string)

        
def eleccion():
    print(f"{verde}")
    opc = input(f"[OMG@root]>> ")
    if opc == "dni":
        consulta_dni()
        eleccion()
    elif opc == "help":
        menu_ayuda();
        eleccion()
    elif opc == "ayuda":
        menu_ayuda()
        eleccion()
    elif opc == "?":
        menu_ayuda()
        eleccion()
    elif opc == "casa":
        direccion_casa()
        eleccion()
    elif opc == "ruc":
        consultaruc()
        eleccion()
    elif opc == "numero":
        consultaindividual()
        eleccion()
    elif opc == "buscar":
        consulta_por_nombres()
        eleccion()
    elif opc == "clear":
        os.system("clear")
        portada()
        eleccion()
    elif opc == "cls":
        os.system("cls")
        portada()
        eleccion() 
    elif opc == "exit":
        exit()   
    else:
        print(f"""{rojo}
    ERROR 404 OPCIÓN INCORRECTA x_x 
        {verde}""")
        eleccion()
    
# inicio de tool
if __name__ == "__main__":
    portada()
    eleccion()
