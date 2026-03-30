"""
Motor de inferencia para encontrar la mejor ruta usando reglas lógicas
Implementa búsqueda en profundidad con backtracking y optimización por tiempo
"""

class InferenceEngine:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        self.best_route = None
        self.best_time = float('inf')
        
    def find_best_route(self, start, end, max_depth=10):
        """
        Encuentra la mejor ruta desde start hasta end
        Usa búsqueda en profundidad con poda por tiempo óptimo
        """
        self.best_route = None
        self.best_time = float('inf')
        
        # Iniciar búsqueda recursiva
        self._dfs(start, end, [start], 0, 0, max_depth)
        
        return self.best_route, self.best_time
    
    def _dfs(self, current, end, path, total_time, depth, max_depth):
        """
        Búsqueda en profundidad recursiva con backtracking
        Regla lógica: Si current == end, se encontró una ruta completa
        """
        # Regla de parada: si llegamos al destino
        if current == end:
            if total_time < self.best_time:
                self.best_time = total_time
                self.best_route = path.copy()
            return
        
        # Regla de poda: si profundidad excede límite
        if depth >= max_depth:
            return
        
        # Regla de poda: si tiempo actual ya es mayor al mejor encontrado
        if total_time >= self.best_time:
            return
        
        # Obtener todas las conexiones desde la estación actual
        connections = self.kb.get_connections(current)
        
        # Regla lógica: Para cada conexión válida, explorar
        for conn in connections:
            next_station = conn["destino"]
            
            # Evitar ciclos: no visitar estaciones ya visitadas
            if next_station not in path:
                new_path = path + [next_station]
                new_time = total_time + conn["tiempo"]
                
                # Recursión: explorar siguiente nivel
                self._dfs(next_station, end, new_path, new_time, depth + 1, max_depth)
    
    def format_route(self, route):
        """Formatea la ruta con nombres legibles"""
        if not route:
            return "No se encontró ruta"
        
        formatted = []
        for i, station in enumerate(route):
            station_name = self.kb.get_station_name(station)
            formatted.append(f"{station_name} ({station})")
        
        return " → ".join(formatted)
    
    def explain_route(self, route):
        """Explica la ruta usando reglas lógicas"""
        if not route or len(route) < 2:
            return "Ruta no disponible"
        
        explanation = []
        for i in range(len(route) - 1):
            origin = route[i]
            dest = route[i + 1]
            
            # Buscar la regla aplicada
            connections = self.kb.get_connections(origin)
            applied_rule = None
            for conn in connections:
                if conn["destino"] == dest:
                    applied_rule = conn
                    break
            
            if applied_rule:
                explanation.append(
                    f"Desde {self.kb.get_station_name(origin)} hasta "
                    f"{self.kb.get_station_name(dest)} por línea {applied_rule['linea']} "
                    f"({applied_rule['tiempo']} min)"
                )
        
        return "\n".join(explanation)
