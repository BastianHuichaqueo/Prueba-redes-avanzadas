import os

campus = ["zona core", "campus uno", "campus matriz", "sector outsourcing"]
dispositivos_por_campus = {campus_name: [] for campus_name in campus}

def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    else:
        print("\n" * 100)

def print_menu():
    print("¿Qué desea hacer?")
    print("1. Ver los dispositivos.")
    print("2. Ver los campus.")
    print("3. Añadir dispositivo.")
    print("4. Añadir campus.")
    print("5. Borrar dispositivo.")
    print("6. Borrar campus.")

def print_campus():
    clear_screen()
    print("Campus disponibles:")
    for idx, item in enumerate(campus, 1):
        print(f"{idx}. {item}")
        devices = dispositivos_por_campus[item]
        if devices:
            print("   Dispositivos:")
            for device in devices:
                print(f"   - {device}")
        else:
            print("   No hay dispositivos en este campus.")
    
    # Agregar opción para regresar al menú principal
    print("\n0. Regresar al menú principal.")

    choice = input("Elija una opción: ")
    if choice == "0":
        return -1  # Devolver -1 para indicar que se seleccionó "Regresar al menú principal"
    else:
        return int(choice) - 1

def add_device():
    clear_screen()
    print("Elija un dispositivo:")
    print("1. Router.")
    print("2. Switch.")
    print("3. Switch multicapa.")
    
    device_choice = input("Elija su opción: ")
    device_name = input("Agregue el nombre de su dispositivo: ")

    if device_choice == "1":  # Si se elige la opción 1 (Router)
        campus_choice = print_campus()
        if campus_choice == -1:
            main()  # Si se selecciona "Regresar al menú principal", volver al menú principal
        if 0 <= campus_choice < len(campus):
            campus_name = campus[campus_choice]
            filename = f"{campus_name}.txt"
            with open(filename, "a") as file:
                dispositivos_por_campus[campus_name].append(device_name)
                # Llamar a la función para configurar el router después de agregarlo al campus
                configure_router(device_name)
    elif device_choice == "2":  # Si se elige la opción 2 (Switch)
        campus_choice = print_campus()
        if campus_choice == -1:
            main()  # Si se selecciona "Regresar al menú principal", volver al menú principal
        if 0 <= campus_choice < len(campus):
            campus_name = campus[campus_choice]
            dispositivos_por_campus[campus_name].append(device_name)
            print(f"{device_name} asignado correctamente al campus {campus_name}.")
            configure_switch(device_name)  # Llamar a la función para configurar el switch después de agregarlo al campus
    elif device_choice == "3":  # Si se elige la opción 3 (Switch multicapa)
        campus_choice = print_campus()
        if campus_choice == -1:
            main()  # Si se selecciona "Regresar al menú principal", volver al menú principal
        if 0 <= campus_choice < len(campus):
            campus_name = campus[campus_choice]
            dispositivos_por_campus[campus_name].append(device_name)
            print(f"{device_name} asignado correctamente al campus {campus_name}.")
            configure_switch_multilayer(device_name)  # Llamar a la función para configurar el switch multicapa después de agregarlo al campus
    else:
        print("La opción seleccionada no es válida para asignar un dispositivo.")
        input("Presione Enter para continuar...")
        main()

def list_devices():
    clear_screen()
    devices_exist = False
    for campus_name, devices in dispositivos_por_campus.items():
        if devices:
            print(f"Dispositivos en {campus_name}:")
            for device in devices:
                print(f"- {device}")
            devices_exist = True
    if not devices_exist:
        print("No se encuentra ningún dispositivo creado.")
    
    # Agregar opción para regresar al menú principal
    print("\n0. Regresar al menú principal.")

    choice = input("Elija una opción: ")
    if choice == "0":
        main()

def delete_device():
    clear_screen()
    print("Seleccione el campus del cual desea borrar un dispositivo:")
    choice = print_campus()
    if choice == -1:
        main()  # Si se selecciona "Regresar al menú principal", volver al menú principal
    if 0 <= choice < len(campus):
        campus_name = campus[choice]
        devices = dispositivos_por_campus[campus_name]
        if devices:
            print(f"Dispositivos en {campus_name}:")
            for idx, device in enumerate(devices, 1):
                print(f"{idx}. {device}")
            device_choice = int(input("Elija el dispositivo que desea borrar: ")) - 1
            if 0 <= device_choice < len(devices):
                del devices[device_choice]
                print("Dispositivo eliminado exitosamente.")
            else:
                print("Opción inválida.")
        else:
            print("No hay dispositivos en este campus.")
    
    input("Presione Enter para continuar...")
    main()

def delete_campus():
    clear_screen()
    print("Seleccione el campus que desea borrar:")
    choice = print_campus()
    if choice == -1:
        main()  # Si se selecciona "Regresar al menú principal", volver al menú principal
    if 0 <= choice < len(campus):
        campus_name = campus[choice]
        del dispositivos_por_campus[campus_name]
        campus_removed = campus.pop(choice)
        print(f"Campus '{campus_removed}' y todos sus dispositivos asociados han sido eliminados exitosamente.")
    
    input("Presione Enter para continuar...")
    main()

def add_campus():
    clear_screen()
    print("Ingrese el nombre del nuevo campus:")
    new_campus_name = input("Nombre del nuevo campus: ")
    campus.append(new_campus_name)
    dispositivos_por_campus[new_campus_name] = []
    print(f"Nuevo campus '{new_campus_name}' agregado exitosamente.")
    input("Presione Enter para continuar...")
    main()

def configure_router(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE ROUTER")
    print("1. Configuración de enrutamiento")
    print("2. NAT (Network Address Translation)")
    print("3. Firewall y ACL (Access Control Lists)")
    print("4. Servicios de red")
    print("5. Seguridad de gestión")
    print("6. Actualizaciones de firmware y seguridad")
    print("0. Regresar al menú principal")

    choice = input("Elija una opción para configurar el router: ")

    # Aquí puedes agregar lógica para manejar cada opción elegida por el usuario
    # Por ejemplo, podrías solicitar más información al usuario o ejecutar comandos específicos del router.

    if choice == "0":
        main()  # Regresar al menú principal
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
        configure_router(device_name)  # Volver a llamar a la función si la opción no es válida

def configure_switch(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE SWITCH")
    print("1. Configuración de VLAN (Virtual LAN)")
    print("2. STP (Spanning Tree Protocol) o RSTP (Rapid Spanning Tree Protocol)")
    print("3. Troncales (Trunks) y enlaces agregados (EtherChannels)")
    print("4. Seguridad de puerto")
    print("5. Seguridad de VLAN")
    print("6. Actualizaciones de firmware y seguridad")
    print("0. Regresar al menú principal")

    choice = input("Elija una opción para configurar el switch: ")

    # Aquí puedes agregar lógica para manejar cada opción elegida por el usuario
    # Por ejemplo, podrías solicitar más información al usuario o ejecutar comandos específicos del switch.

    if choice == "0":
        main()  # Regresar al menú principal
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
        configure_switch(device_name)  # Volver a llamar a la función si la opción no es válida

def configure_switch_multilayer(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE SWITCH MULTICAPA")
    print("1. Enrutamiento inter-VLAN")
    print("2. Configuración de protocolos de enrutamiento")
    print("3. Acceso a listas de control (ACL)")
    print("4. Calidad de servicio (QoS)")
    print("5. Seguridad de puerto")
    print("6. Actualizaciones de firmware y seguridad")
    print("0. Regresar al menú principal")

    choice = input("Elija una opción para configurar el switch multicapa: ")

    # Aquí puedes agregar lógica para manejar cada opción elegida por el usuario
    # Por ejemplo, podrías solicitar más información al usuario o ejecutar comandos específicos del switch.

    if choice == "0":
        main()  # Regresar al menú principal
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
        configure_switch_multilayer(device_name)  # Volver a llamar a la función si la opción no es válida

def main():
    clear_screen()
    print_menu()
    choice = int(input("Elija una opción: "))
    if choice == 1:
        list_devices()
    elif choice == 2:
        campus_choice = print_campus()
        if campus_choice == -1:
            main()  # Si se selecciona "Regresar al menú principal", volver al menú principal
        # Aquí puedes continuar con la lógica de la opción seleccionada del campus
    elif choice == 3:
        add_device()
    elif choice == 4:
        add_campus()
    elif choice == 5:
        delete_device()
    elif choice == 6:
        delete_campus()
    # Puedes continuar con las otras opciones del menú

if __name__ == "__main__":
    main()

