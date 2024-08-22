import subprocess

# Ruta al script en el nodo donde está instalado Dataiku
script_path = '/opt/dataiku/scripts/oracca.sh'

# Ejecuta el script en el nodo
result = subprocess.run([script_path], capture_output=True, text=True, shell=True)

# Captura la salida del script (la contraseña)
password = result.stdout.strip()

# Imprime o almacena la contraseña para su uso posterior
print(password)

