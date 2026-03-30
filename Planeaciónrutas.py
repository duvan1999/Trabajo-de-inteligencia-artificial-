"""
Sistema principal de planificación de rutas
Interfaz de usuario para consultar rutas óptimas
"""

from knowledge_base import KnowledgeBase
from inference_engine import InferenceEngine

class RoutePlanner:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.engine = InferenceEngine(self.kb)
        
    def plan_route(self, start_id, end_id):
        """
        Planifica la mejor ruta entre dos estaciones
        """
        print(f"\n{'='*60}")
        print(f"PLANIFICANDO RUTA: {self.kb.get_station_name(start_id)} → {self.kb.get_station_name(end_id)}")
        print(f"{'='*60}")
        
        # Validar que las estaciones existen
        all_stations = self.kb.get_all_stations()
        if start_id not in all_stations:
            print(f"Error: La estación '{start_id}' no existe en la base de conocimiento")
            print(f"Estaciones disponibles: {', '.join(all_stations)}")
            return None
        
        if end_id not in all_stations:
            print(f"Error: La estación '{end_id}' no existe en la base de conocimiento")
            print(f"Estaciones disponibles: {', '.join(all_stations)}")
            return None
        
        # Buscar mejor ruta
        route, total_time = self.engine.find_best_route(start_id, end_id)
        
        if route:
            print(f"\n✅ MEJOR RUTA ENCONTRADA:")
            print(f"   Ruta: {self.engine.format_route(route)}")
            print(f"   Tiempo total estimado: {total_time} minutos")
            
            print(f"\n📋 EXPLICACIÓN DE LA RUTA (Reglas aplicadas):")
            print(self.engine.explain_route(route))
            
            return {"route": route, "total_time": total_time}
        else:
            print(f"\n❌ No se encontró una ruta entre {start_id} y {end_id}")
            return None
    
    def show_all_stations(self):
        """Muestra todas las estaciones disponibles"""
        stations = self.kb.get_all_stations()
        print("\n📌 ESTACIONES DISPONIBLES:")
        for station in stations:
            print(f"   • {self.kb.get_station_name(station)} ({station})")
    
    def interactive_mode(self):
        """Modo interactivo para consultas de rutas"""
        print("\n" + "="*60)
        print("SISTEMA INTELIGENTE DE RUTAS - TRANSPORTE MASIVO")
        print("="*60)
        
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Ver todas las estaciones")
            print("2. Planificar una ruta")
            print("3. Salir")
            
            option = input("\nSeleccione una opción (1-3): ").strip()
            
            if option == "1":
                self.show_all_stations()
            elif option == "2":
                print("\n--- PLANIFICAR RUTA ---")
                start = input("Estación de origen (ej: estacion_a): ").strip()
                end = input("Estación de destino (ej: estacion_f): ").strip()
                self.plan_route(start, end)
            elif option == "3":
                print("\n¡Gracias por usar el sistema!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    planner = RoutePlanner()
    
    # Ejemplo de uso directo
    print("\n" + "="*60)
    print("EJEMPLOS DE RUTAS")
    print("="*60)
    
    # Ejemplo 1: Ruta dentro de la línea A
    planner.plan_route("estacion_j", "estacion_f")
    
    # Ejemplo 2: Ruta con alimentador
    planner.plan_route("estacion_g", "terminal_sur")
    
    # Iniciar modo interactivo
    planner.interactive_mode()
