import funciones.mis_funciones as mis_funciones 

def mostrar_estadisticas(lista_paises):
    try:
        if not isinstance(lista_paises, list):
            print("❌ Error: se esperaba una lista de países.")
            return

        if not lista_paises:
            print("📊 No hay datos para calcular estadísticas.")
            return

        paises_validos = []
        continentes_validos = []

        for pais in lista_paises:
            if not isinstance(pais, dict):
                continue
            try:
                nombre = pais.get("nombre", "Desconocido")
                poblacion = int(pais.get("poblacion", 0))
                superficie = int(pais.get("superficie", 0))
                continente = str(pais.get("continente", "Desconocido")).strip()

                if poblacion < 0 or superficie < 0:
                    continue 

                paises_validos.append({
                    "nombre": nombre,
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": continente
                })
                continentes_validos.append(continente)
            except (ValueError, TypeError):
                continue

        if not paises_validos:
            print("❌ No se encontraron países con datos válidos para estadísticas.")
            return

        pais_mayor_pob = max(paises_validos, key=lambda x: x["poblacion"])
        pais_menor_pob = min(paises_validos, key=lambda x: x["poblacion"])

        total_poblacion = sum(p["poblacion"] for p in paises_validos)
        total_superficie = sum(p["superficie"] for p in paises_validos)
        n = len(paises_validos)

        prom_poblacion = total_poblacion / n
        prom_superficie = total_superficie / n

        from collections import Counter
        conteo_continentes = Counter(continentes_validos)

        print("=" * mis_funciones.ANCHO_TOTAL)
        print(mis_funciones.menu_centro(("ESTADÍSTICAS GENERALES")))
        print("=" * mis_funciones.ANCHO_TOTAL)

        print(f"🌍 País con mayor población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']:,} habitantes)")
        print(f"🌍 País con menor población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']:,} habitantes)")

        print(f"\n📈 Población promedio: {prom_poblacion:,.2f} habitantes")
        print(f"📐 Superficie promedio: {prom_superficie:,.2f} km²")

        print("\n🗺️ Países por continente:")
        for continente, cantidad in sorted(conteo_continentes.items()):
            print(f"   • {continente}: {cantidad} país(es)")

        print("=" * mis_funciones.ANCHO_TOTAL)

    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"❌ Error al calcular estadísticas: {e}")
        