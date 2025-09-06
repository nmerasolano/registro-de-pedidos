import calendar
import datetime
import pyttsx3

engine = pyttsx3.init()

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

dias_cortos = [     "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

engine.say("Bienvenido al calendario accesible para personas con discapacidad visual")
engine.runAndWait()
print("Bienvenido al calendario accesible para personas con discapacidad visual")

while True:
    print("\nSeleccione una opción:")
    print("1. Ver calendario de un mes")
    print("2. Calcular qué día cae una fecha y cuántos días faltan")
    print("3. Salir")

    engine.say("Seleccione una opción. Uno para ver el calendario mensual, dos para calcular el día de una fecha, o tres para salir.")
    engine.runAndWait()

    opcion = input("Opción: ")

    if opcion == "1":
        try:
            numero_mes = int(input("Ingrese número del mes (1-12): "))
            if 1 <= numero_mes <= 12:
                nombre_mes = meses[numero_mes - 1]
                print(f"\n📅 Calendario de {nombre_mes} 2025:\n")
                engine.say(f"Calendario de {nombre_mes} del año 2025")
                engine.runAndWait()

                cal = calendar.TextCalendar(firstweekday=0)
                calendario_str = cal.formatmonth(2025, numero_mes)

                for eng, esp in zip(["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"], dias_cortos):
                    calendario_str = calendario_str.replace(eng, esp)

                print(calendario_str)
                engine.say("Días de la semana: " + ", ".join(dias_cortos))
                engine.runAndWait()
            else:
                print("❌ Número de mes no válido")
                engine.say("Número de mes no válido")
                engine.runAndWait()
        except ValueError:
            print("❌ Entrada inválida. Debe ser un número del 1 al 12.")
            engine.say("Entrada inválida. Debe ser un número del 1 al 12.")
            engine.runAndWait()

    elif opcion == "2":
        fecha_str = input("Ingrese una fecha (dd/mm/aaaa): ")
        try:
            fecha_obj = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
            hoy = datetime.date.today()

            nombre_dia = dias_semana[fecha_obj.weekday()]
            dias_restantes = (fecha_obj - hoy).days

            print(f"\n📅 La fecha {fecha_str} cae en {nombre_dia}.")
            engine.say(f"Esa fecha cae en {nombre_dia}")
            engine.runAndWait()

            if dias_restantes > 0:
                print(f"⏳ Faltan {dias_restantes} días para esa fecha.")
                engine.say(f"Faltan {dias_restantes} días para esa fecha.")
            elif dias_restantes == 0:
                print("✅ Esa fecha es hoy.")
                engine.say("Esa fecha es hoy.")
            else:
                print(f"📅 Esa fecha fue hace {abs(dias_restantes)} días.")
                engine.say(f"Esa fecha fue hace {abs(dias_restantes)} días.")

            engine.runAndWait()

        except ValueError:
            print("❌ Formato inválido. Use el formato dd/mm/aaaa.")
            engine.say("Formato inválido. Intente de nuevo.")
            engine.runAndWait()

    elif opcion == "3":
        print("Gracias por usar el calendario accesible.")
        engine.say("Gracias por usar el calendario accesible.")
        engine.runAndWait()
        break

    else:
        print("❌ Opción no válida, intente de nuevo.")
        engine.say("Opción no válida, intente de nuevo.")
        engine.runAndWait()
