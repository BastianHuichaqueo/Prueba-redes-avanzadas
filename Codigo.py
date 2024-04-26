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
    
    print("\n0. Regresar al menú principal.")

    choice = input("Elija una opción: ")
    if choice == "0":
        return -1
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

    if device_choice == "1":
        add_router(device_name)
    elif device_choice == "2":
        add_switch(device_name)
    elif device_choice == "3":
        add_multilayer_switch(device_name)
    else:
        print("La opción seleccionada no es válida para asignar un dispositivo.")
        input("Presione Enter para continuar...")
        main()

def add_router(device_name):
    campus_choice = print_campus()
    if campus_choice == -1:
        main()
    if 0 <= campus_choice < len(campus):
        campus_name = campus[campus_choice]
        dispositivos_por_campus[campus_name].append(device_name)
        configure_router(device_name)

def add_switch(device_name):
    campus_choice = print_campus()
    if campus_choice == -1:
        main()
    if 0 <= campus_choice < len(campus):
        campus_name = campus[campus_choice]
        dispositivos_por_campus[campus_name].append(device_name)
        configure_switch(device_name)

def add_multilayer_switch(device_name):
    campus_choice = print_campus()
    if campus_choice == -1:
        main()
    if 0 <= campus_choice < len(campus):
        campus_name = campus[campus_choice]
        dispositivos_por_campus[campus_name].append(device_name)
        configure_switch_multilayer(device_name)
    else:
        print("La opción seleccionada no es válida para asignar un dispositivo.")
        input("Presione Enter para continuar...")
        main()

def list_devices():
    clear_screen()
    print("Dispositivos disponibles:")
    for idx, campus_name in enumerate(campus, 1):
        devices = dispositivos_por_campus[campus_name]
        if devices:
            print(f"{idx}. {campus_name}:")
            for device in devices:
                print(f"   - {device}")
    print("\n0. Regresar al menú principal.")

    choice = input("Elija una opción: ")
    if choice == "0":
        main()
    else:
        choice = int(choice) - 1
        if 0 <= choice < len(campus):
            campus_name = campus[choice]
            devices = dispositivos_por_campus[campus_name]
            if devices:
                print(f"Dispositivos en {campus_name}:")
                for idx, device in enumerate(devices, 1):
                    print(f"{idx}. {device}")
                device_choice = int(input("Elija el dispositivo para ver detalles: ")) - 1
                if 0 <= device_choice < len(devices):
                    device_name = devices[device_choice]
                    (device_name)
                else:
                    print("Opción inválida.")
            else:
                print("No hay dispositivos en este campus.")
        else:
            print("Opción inválida.")

    input("Presione Enter para continuar...")
    main()

def delete_device():
    clear_screen()
    print("Seleccione el campus del cual desea borrar un dispositivo:")
    choice = print_campus()
    if choice == -1:
        main()
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
        main()
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
    print("1. Configurar dirección IP")
    print("2. Configurar enrutamiento estático")
    print("3. Configurar enrutamiento dinámico")
    print("4. Configurar NAT (Network Address Translation)")
    print("5. Configurar Firewall y ACL (Access Control Lists)")
    print("6. Configurar servicios de red")
    print("7. Configurar seguridad de gestión")
    print("8. Actualizar firmware y seguridad")
    print("0. Regresar al menú principal")

    choice = input("Elija una opción para configurar el router: ")

    if choice == "0":
        main()
    elif choice == "1":
        configure_ip_address(device_name)
    elif choice == "2":
        configure_static_routing(device_name)
    elif choice == "3":
        configure_dynamic_routing(device_name)
    elif choice == "4":
        configure_nat(device_name)
    elif choice == "5":
        configure_firewall_acl(device_name)
    elif choice == "6":
        configure_network_services(device_name)
    elif choice == "7":
        configure_management_security(device_name)
    elif choice == "8":
        update_firmware_security(device_name)
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
        input("Presione Enter para continuar...")
        configure_router(device_name)

def configure_ip_address(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE DIRECCIÓN IP DEL ROUTER")

    interface = input("Ingrese el nombre de la interfaz (por ejemplo, GigabitEthernet0/0): ")
    ip_address = input("Ingrese la dirección IP de la interfaz (por ejemplo, 192.168.1.1): ")
    subnet_mask = input("Ingrese la máscara de subred de la interfaz (por ejemplo, 255.255.255.0): ")

    print(f"Interfaz {interface} configurada con dirección IP {ip_address} y máscara de subred {subnet_mask}")

    input("Presione Enter para continuar...")
    configure_router(device_name)

def configure_static_routing(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE ENRUTAMIENTO ESTÁTICO DEL ROUTER")
    input("Presione Enter para continuar...")
    configure_router(device_name)

def configure_dynamic_routing(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE ENRUTAMIENTO DINÁMICO DEL ROUTER")
    input("Presione Enter para continuar...")
    configure_router(device_name)

def configure_nat(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE NAT DEL ROUTER")
    input("Presione Enter para continuar...")
    configure_router(device_name)

def configure_firewall_acl(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE FIREWALL Y ACL DEL ROUTER")
    input("Presione Enter para continuar...")
    configure_router(device_name)

def configure_network_services(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE SERVICIOS DE RED DEL ROUTER")
    input("Presione Enter para continuar...")
    configure_router(device_name)

def configure_management_security(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE SEGURIDAD DE GESTIÓN DEL ROUTER")
    input("Presione Enter para continuar...")
    configure_router(device_name)

def update_firmware_security(device_name):
    clear_screen()
    print("ACTUALIZACIÓN DE FIRMWARE Y SEGURIDAD DEL ROUTER")
    input("Presione Enter para continuar...")
    configure_router(device_name)

def configure_switch(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE SWITCH")
    print("1. Configuración de VLAN (Virtual LAN)")
    print("2. Configuración de STP (Spanning Tree Protocol) o RSTP (Rapid Spanning Tree Protocol)")
    print("3. Configuración de troncales (Trunks) y enlaces agregados (EtherChannels)")
    print("4. Configuración de seguridad de puerto")
    print("5. Configuración de seguridad de VLAN")
    print("6. Actualizaciones de firmware y seguridad")
    print("0. Regresar al menú principal")

    choice = input("Elija una opción para configurar el switch: ")

    if choice == "0":
        main()
    elif choice == "1":
        configure_vlan(device_name)
    elif choice == "2":
        configure_stp(device_name)
    elif choice == "3":
        configure_trunks_and_etherchannels(device_name)
    elif choice == "4":
        configure_port_security_switch(device_name)
    elif choice == "5":
        configure_vlan_security(device_name)
    elif choice == "6":
        update_firmware_security_switch(device_name)
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
        input("Presione Enter para continuar...")
        configure_switch(device_name)

def configure_vlan(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE VLAN (Virtual LAN) DEL SWITCH")
    input("Presione Enter para continuar...")
    configure_switch(device_name)

def configure_stp(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE STP (Spanning Tree Protocol) O RSTP (Rapid Spanning Tree Protocol) DEL SWITCH")
    input("Presione Enter para continuar...")
    configure_switch(device_name)

def configure_trunks_and_etherchannels(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE TRONCALES (TRUNKS) Y ENLACES AGREGADOS (ETHERCHANNELS) DEL SWITCH")
    input("Presione Enter para continuar...")
    configure_switch(device_name)

def configure_port_security_switch(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE SEGURIDAD DE PUERTO DEL SWITCH")
    input("Presione Enter para continuar...")
    configure_switch(device_name)

def configure_vlan_security(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE SEGURIDAD DE VLAN DEL SWITCH")
    input("Presione Enter para continuar...")
    configure_switch(device_name)

def update_firmware_security_switch(device_name):
    clear_screen()
    print("ACTUALIZACIÓN DE FIRMWARE Y SEGURIDAD DEL SWITCH")
    input("Presione Enter para continuar...")
    configure_switch(device_name)

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

    if choice == "0":
        main()
    elif choice == "1":
        configure_inter_vlan_routing(device_name)
    elif choice == "2":
        configure_routing_protocols(device_name)
    elif choice == "3":
        configure_acl(device_name)
    elif choice == "4":
        configure_qos(device_name)
    elif choice == "5":
        configure_port_security(device_name)
    elif choice == "6":
        update_firmware_security_switch(device_name)
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
        input("Presione Enter para continuar...")
        configure_switch_multilayer(device_name)

def configure_inter_vlan_routing(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE ENRUTAMIENTO INTER-VLAN DEL SWITCH MULTICAPA")
    input("Presione Enter para continuar...")
    configure_switch_multilayer(device_name)

def configure_routing_protocols(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE PROTOCOLOS DE ENRUTAMIENTO DEL SWITCH MULTICAPA")
    input("Presione Enter para continuar...")
    configure_switch_multilayer(device_name)

def configure_acl(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE ACCESO A LISTAS DE CONTROL (ACL) DEL SWITCH MULTICAPA")
    input("Presione Enter para continuar...")
    configure_switch_multilayer(device_name)

def configure_qos(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE CALIDAD DE SERVICIO (QoS) DEL SWITCH MULTICAPA")
    input("Presione Enter para continuar...")
    configure_switch_multilayer(device_name)

def configure_port_security(device_name):
    clear_screen()
    print("CONFIGURACIÓN DE SEGURIDAD DE PUERTO DEL SWITCH MULTICAPA")
    input("Presione Enter para continuar...")
    configure_switch_multilayer(device_name)

def main():
    clear_screen()
    print_menu()
    choice = int(input("Elija una opción: "))
    if choice == 1:
        list_devices()
    elif choice == 2:
        campus_choice = print_campus()
        if campus_choice == -1:
            main()
    elif choice == 3:
        add_device()
    elif choice == 4:
        add_campus()
    elif choice == 5:
        delete_device()
    elif choice == 6:
        delete_campus()

if __name__ == "__main__":
    main()