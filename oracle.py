import subprocess
import time

# Inicializar el indicador de recuperación de la contraseña
password_retrieved = False

while not password_retrieved:
    # Ejecutar el comando para obtener la contraseña
    result = subprocess.run(
        [
            "/opt/CARKaim/sdk/clipasswordsdk", "GetPassword",
            "-p", "AppDescs.AppID=ORAASDIKU_U_AIM_178435_User",
            "-p", "Query=Safe=ORAASDIKU_U_AIM_178435_Safe;Folder=Root;Object=ORAAS_MXCGN1U_oraasqrp024_ORAASDIKU_OAAS_UAT_RW",
            "-p", "Reason=test",
            "-p", "FailRequestOnPasswordChange=false",
            "-o", "Password,PasswordChangeInProcess"
        ],
        capture_output=True, text=True, shell=False
    )

    # Verificar el código de retorno del comando
    if result.returncode != 0:
        # Si el comando falla, verificar el contenido de la salida
        if not result.stdout.startswith("APPAP282E"):
            break
        else:
            # Si el comando falla con un código de error específico, espera y reintenta
            time.sleep(1.5)
    else:
        # Si el comando es exitoso, marcar que la contraseña ha sido recuperada
        password_retrieved = True

# Imprimir la salida dependiendo si se recuperó la contraseña
if not password_retrieved:
    print(result.stdout.strip())
else:
    # Extraer y mostrar solo la contraseña
    password_info = result.stdout.strip().split(',')
    print(password_info[0], password_info[1] if len(password_info) > 1 else "")

