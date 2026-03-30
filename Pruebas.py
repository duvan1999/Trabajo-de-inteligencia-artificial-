"""
Archivo de pruebas para validar el sistema inteligente
"""

from knowledge_base import KnowledgeBase
from inference_engine import InferenceEngine
from route_planner import RoutePlanner

def test_knowledge_base():
    """Prueba 1: Verificar base de conocimiento"""
    print("\n=== PRUEBA 1: Base de Conocimiento ===")
    kb = KnowledgeBase()
    
    # Verificar estaciones
    stations = kb.get_all_stations()
    assert len(stations) == 10, "Deberían existir 10 estaciones"
    print(f"✅ {len(stations)} estaciones cargadas correctamente")
    
    # Verificar conexiones
    connections = kb.get_connections("estacion_h")
    assert len(connections) > 0, "Debe tener conexiones"
    print(f"✅ Estación San Antonio tiene {len(connections)} conexiones")
    
    # Verificar nombres
    name = kb.get_station_name("estacion_a")
    assert name == "El Poblado", "Nombre incorrecto"
    print(f"✅ Nombres de estaciones correctos")
    
    return True

def test_route_planning():
    """Prueba 2: Planificación de rutas"""
    print("\n=== PRUEBA 2: Planificación de Rutas ===")
    planner = RoutePlanner()
    
    # Prueba 2.1: Ruta directa
    result = planner.plan_route("estacion_a", "estacion_b")
    assert result is not None, "Ruta directa no encontrada"
    assert result["total_time"] == 2, "Tiempo incorrecto para ruta directa"
    print("✅ Ruta directa funciona correctamente")
    
    # Prueba 2.2: Ruta múltiple
    result = planner.plan_route("estacion_j", "estacion_c")
    assert result is not None, "Ruta múltiple no encontrada"
    assert len(result["route"]) >= 3, "La ruta debería tener múltiples estaciones"
    print("✅ Ruta múltiple funciona correctamente")
    
    # Prueba 2.3: Ruta con alimentador
    result = planner.plan_route("estacion_g", "terminal_sur")
    assert result is not None, "Ruta con alimentador no encontrada"
    print("✅ Ruta con alimentador funciona correctamente")
    
    # Prueba 2.4: Estación inexistente
    result = planner.plan_route("estacion_x", "estacion_a")
    assert result is None, "Debería fallar con estación inexistente"
    print("✅ Validación de estaciones funciona correctamente")
    
    return True

def test_inference_engine():
    """Prueba 3: Motor de inferencia"""
    print("\n=== PRUEBA 3: Motor de Inferencia ===")
    kb = KnowledgeBase()
    engine = InferenceEngine(kb)
    
    # Probar búsqueda
    route, total_time = engine.find_best_route("estacion_j", "estacion_f")
    
    assert route is not None, "No se encontró ruta"
    assert total_time > 0, "Tiempo debe ser positivo"
    print(f"✅ Motor de inferencia encontró ruta con {len(route)} estaciones en {total_time} min")
    
    # Probar formato
    formatted = engine.format_route(route)
    assert len(formatted) > 0, "Formato de ruta vacío"
    print(f"✅ Formato de ruta correcto")
    
    # Probar explicación
    explanation = engine.explain_route(route)
    assert len(explanation) > 0, "Explicación vacía"
    print(f"✅ Explicación de reglas generada")
    
    return True

def run_all_tests():
    """Ejecuta todas las pruebas"""
    print("\n" + "="*60)
    print("INICIANDO PRUEBAS DEL SISTEMA INTELIGENTE")
    print("="*60)
    
    tests = [
        ("Base de Conocimiento", test_knowledge_base),
        ("Planificación de Rutas", test_route_planning),
        ("Motor de Inferencia", test_inference_engine)
    ]
    
    passed = 0
    for test_name, test_func in tests:
        try:
            test_func()
            passed += 1
        except Exception as e:
            print(f"❌ Error en {test_name}: {e}")
    
    print("\n" + "="*60)
    print(f"RESUMEN: {passed}/{len(tests)} pruebas pasaron")
    print("="*60)
    
    return passed == len(tests)

if __name__ == "__main__":
    run_all_tests()
