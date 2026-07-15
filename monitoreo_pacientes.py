#monitoreo de pacientes
pacientes = []
def clasificar(temp, sat):
    if temp >= 39 or sat < 92:
        return "Alerta"
    elif (37.5 <= temp <= 38.9) or (92 <= sat <= 94):
        return "Observacion"
    return "Estable"
def buscar_por_codigo(codigo):
    codigo = codigo.lower()
    for p in pacientes:
        if p["codigo"].lower() == codigo:
            return p
    return None
def registrar_paciente():
    codigo = input("Codigo del paciente: ").strip()
    if buscar_por_codigo(codigo):
        print("Ya existe un paciente con ese codigo intente nuevamenete muchas gracias."); return
    nombre = input("Nombre: ").strip()
    try:
        edad = int(input("Edad: "))
        temp = float(input("Temperatura (C): "))
        sat = float(input("Saturacion (%): "))
    except ValueError:
        print("Ingreso un dato no numerico."); return
    if not (0 < edad <= 120) or not (36 <= temp <= 40.5) or not (0 <= sat <= 100):
        print("Alguno de los valores esta fuera de rango."); return
    estado = clasificar(temp, sat)
    pacientes.append({"codigo": codigo, "nombre": nombre, "edad": edad,
                       "temp": temp, "sat": sat, "estado": estado})
    print(f"Paciente {nombre} registrado. Clasificacion: {estado}")
def mostrar_pacientes():
    if not pacientes:
        print(" no hay pacientes en el sistema...AUN aprovecha de descansar"); return
    for p in pacientes:
        print(f"{p['codigo']} | {p['nombre']} | {p['edad']} anos | {p['temp']}C | {p['sat']}% | {p['estado']}")
def buscar_paciente():
    p = buscar_por_codigo(input("Codigo a buscar: ").strip())
    mensaje = f"Nombre: {p['nombre']}, Estado: {p['estado']}, Temp: {p['temp']}C, Sat: {p['sat']}%" if p else "No se encontro un paciente con ese codigo."
    print(mensaje)
def modificar_signos():
    p = buscar_por_codigo(input("Codigo del paciente a modificar: ").strip())
    if not p:
        print("Paciente no reconocido por este sistema."); return
    try:
        p["temp"] = float(input("Nueva temperatura: "))
        p["sat"] = float(input("Nueva saturacion: "))
    except ValueError:
        print("Datos invalidos, no se modifico ABSOLUTAMENTE NADA!"); return
    p["estado"] = clasificar(p["temp"], p["sat"])
    print(f"Signos actualizados. Nuevo estado: {p['estado']}")
def eliminar_paciente():
    p = buscar_por_codigo(input("Codigo del paciente a eliminar: ").strip())
    if p: pacientes.remove(p); print("Paciente eliminado del sistema pero no de la memoria del personal de enfermeria.")
    else: print("Paciente no reconocido por este sistema.")
def mostrar_resumen():
    if not pacientes:
        print("No hay pacientes para generar el resumen debes ingresar algunos datos."); return
    conteo = {"Alerta": 0, "Observacion": 0, "Estable": 0}
    suma_temp = 0
    for p in pacientes:
        suma_temp += p["temp"]
        conteo[p["estado"]] += 1
    print(f"Total pacientes: {len(pacientes)} | Temp. promedio: {suma_temp / len(pacientes):.1f}C")
    print(f"Alerta: {conteo['Alerta']} | Observacion: {conteo['Observacion']} | Estable: {conteo['Estable']}")
def mostrar_menu():
    opcion = ""
    acciones = {"1": registrar_paciente, "2": mostrar_pacientes, "3": buscar_paciente,
                "4": modificar_signos, "5": eliminar_paciente, "6": mostrar_resumen}
    while opcion != "7":
        print("\n1.Registrar 2.Mostrar 3.Buscar 4.Modificar 5.Eliminar 6.Resumen 7.Salir")
        opcion = input("Elige una opcion: ")
        if opcion in acciones:
            acciones[opcion]()
        elif opcion == "7":
            print("Cerrando el sistema hasta luego gracias por utilizar el sistema de monitoreo de pacientes que tengas un buen turno.")
        else:
            print("Esa opcion no existe  vuelve intentarlo de nuevo pero no con tu ex.")
mostrar_menu()