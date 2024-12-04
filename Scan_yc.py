import socket
import ipaddress

#---------------------------------------------------------------Se valida que sea una ip valida
def validar_ip():
    while True:
        ip_string = input("Ingrese la IP que desea escanear: ")
        try:
            ip_object = ipaddress.ip_address(ip_string)
            return str(ip_object)
        except ValueError:
            print("Dirección IP inválida. Por favor, intente nuevamente.")

#---------------------------------------------------------------Se selecciona el tipo de escaneo
def tipo_escaneo():
    while True:
        t_escaneo = input("Seleccione el tipo de escaneo que desea realizar \n EE - Escaneo a un puerto especifico \n EC - Escaneo completo (Escanea todos los 65535) \n ER - Escaneo rapido (Escanea el rango de puerto 0 al 1023) \n >>>")
        if t_escaneo.upper() == "EE" : #upper para convertir en minusculas
            print("Selecciono escanear un puerto especifico")
            opcion = 0
            print("Escaneo terminado")
            return int(opcion)
            break
        elif t_escaneo.upper() == "EC" : #upper para convertir en minusculas
            print("Selecciono el escaneo completo")
            opcion = 1
            return int(opcion)
            break
        elif t_escaneo.lower() == "er" : #lower para convertir en minusculas
            print("Selecciono el escaneo rapido")
            opcion = 2
            return int(opcion)
            break
        else :
            print("No a seleccionado una opcion valida")
#--------------------------------------------------------------- Se ejecuta op1 
def escaner1(ip):
    puerto = int(input("Ingrese el puerto a escanear: "))
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.0001)  # Establece un tiempo de espera de 1 segundo 1 
            s.connect((ip, puerto))
            print(f"- El puerto {puerto} está abierto.")
    except socket.timeout:
        print(f"El puerto {puerto} del host {ip} no responde.")
    except socket.error as e:
        print(f"Error al conectar al puerto {puerto}: {e}")

#---------------------------------------------------------------Se ejecuta op2

def escaner2(ip):
    ip = ip
    print(f"Escaneando puertos de {ip}")
    for puerto in range(1, 65536):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.0001)
            try:
                s.connect((ip, puerto))
                print(f"- El puerto {puerto} está abierto.")
            except (socket.timeout, ConnectionRefusedError):
                pass  # Puerto cerrado o timeout
            except OSError as e:
                print(f"Error de sistema: {e}")
    print("Escaneo terminado")
#---------------------------------------------------------------Se ejecuta op3

def escaner3(ip):
    ip = ip
    print(f"Escaneando puertos de {ip}")
    for puerto in range(1, 1023):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.0001)
            try:
                s.connect((ip, puerto))
                print(f"- El puerto {puerto} está abierto.")
            except (socket.timeout, ConnectionRefusedError):
                pass  # Puerto cerrado o timeout
            except OSError as e:
                print(f"Error de sistema: {e}")
    print("Escaneo terminado")

#---------------------------------------------------------------
#Banner
print("""

 ____                                    _                
/ ___|  ___ __ _ _ __    _ __   ___  _ __| |_   _   _  ___ 
\___ \ / __/ _` | '_ \  | '_ \ / _ \| '__| __| | | | |/ __|
 ___) | (_| (_| | | | | | |_) | (_) | |  | |_  | |_| | (__ 
|____/ \___\__,_|_| |_| | .__/ \___/|_|   \__|  \__, |\___|
                        |_|                     |___/                                                               
""" )
print("/*/*/*/ Bienvenido /*/*/*/")

#---------------------------------------------------------------Orden de ejecucion
ip = validar_ip()
opcion=tipo_escaneo()

if (opcion==0):
    escaner1(ip)
elif (opcion==1):
    escaner2(ip)
else:
    print("op3")

