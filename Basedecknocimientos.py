"""
Base de conocimiento del sistema de transporte masivo
Reglas lógicas que definen conexiones entre estaciones
"""

class KnowledgeBase:
    def __init__(self):
        # Hechos: estaciones existentes
        self.facts = {
            "estacion_a": "El Poblado",
            "estacion_b": "Aguacatala",
            "estacion_c": "Ayurá",
            "estacion_d": "Envigado",
            "estacion_e": "Itagüí",
            "estacion_f": "Sabaneta",
            "estacion_g": "Estación Central",
            "estacion_h": "San Antonio",
            "estacion_i": "Parque Berrío",
            "estacion_j": "Caribe"
        }
        
        # Reglas: conexiones directas entre estaciones (línea A - Metro)
        self.rules = [
            # Línea A (Norte-Sur)
            {"origen": "estacion_j", "destino": "estacion_i", "linea": "A", "tiempo": 3},
            {"origen": "estacion_i", "destino": "estacion_h", "linea": "A", "tiempo": 2},
            {"origen": "estacion_h", "destino": "estacion_g", "linea": "A", "tiempo": 2},
            {"origen": "estacion_g", "destino": "estacion_a", "linea": "A", "tiempo": 4},
            {"origen": "estacion_a", "destino": "estacion_b", "linea": "A", "tiempo": 2},
            {"origen": "estacion_b", "destino": "estacion_c", "linea": "A", "tiempo": 3},
            {"origen": "estacion_c", "destino": "estacion_d", "linea": "A", "tiempo": 2},
            {"origen": "estacion_d", "destino": "estacion_e", "linea": "A", "tiempo": 2},
            {"origen": "estacion_e", "destino": "estacion_f", "linea": "A", "tiempo": 3},
            # Conexiones bidireccionales (reglas inversas implícitas)
        ]
        
        # Reglas adicionales: conexiones con líneas alimentadoras
        self.feeder_rules = [
            {"origen": "estacion_g", "destino": "terminal_sur", "linea": "Alimentador", "tiempo": 10},
            {"origen": "estacion_j", "destino": "terminal_norte", "linea": "Alimentador", "tiempo": 8},
            {"origen": "estacion_f", "destino": "parque_industrial", "linea": "Alimentador", "tiempo": 5},
        ]
    
    def get_connections(self, station):
        """
        Obtiene todas las conexiones desde una estación
        Regla lógica: Si hay una regla con origen = station, entonces es conexión válida
        """
        connections = []
        
        # Conexiones directas desde la estación
        for rule in self.rules:
            if rule["origen"] == station:
                connections.append({
                    "destino": rule["destino"],
                    "linea": rule["linea"],
                    "tiempo": rule["tiempo"]
                })
            # Conexiones inversas (bidireccionalidad)
            elif rule["destino"] == station:
                connections.append({
                    "destino": rule["origen"],
                    "linea": rule["linea"],
                    "tiempo": rule["tiempo"]
                })
        
        # Conexiones con alimentadores
        for rule in self.feeder_rules:
            if rule["origen"] == station:
                connections.append({
                    "destino": rule["destino"],
                    "linea": rule["linea"],
                    "tiempo": rule["tiempo"]
                })
        
        return connections
    
    def get_station_name(self, station_id):
        """Obtiene el nombre real de la estación"""
        return self.facts.get(station_id, station_id)
    
    def get_all_stations(self):
        """Obtiene todas las estaciones disponibles"""
        return list(self.facts.keys())
