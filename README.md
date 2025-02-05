# Laboratorio No. 02 - Robótica Industrial - Análisis y Operación del Manipulador Motoman MH6: Comparativa y Aplicaciones Prácticas

## Autores

Johan López - [@ElJoho](https://github.com/ElJoho)

Christian Cuestas - [@ChrisCuestas](https://github.com/ChrisCuestas)

## __1. Comparación de características técnicas__

| Especificación           | ABB IRB 140                                                                 | Motoman MH6                                                                 |
|--------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Número de ejes (Grados de libertad)** | 6                                                                           | 6                                                                          |
| **Carga útil máxima**    | 6 kg                                                                        | 6 kg                                                                       |
| **Alcance máximo**       | 810 mm                                                                     | 1,377 mm                                                                   |
| **Repetibilidad**        | ±0.03 mm                                                                   | ±0.08 mm                                                                   |
| **Velocidad máxima de TCP** | 2.5 m/s                                                                    | 2.0 m/s                                                                    |
| **Montaje**              | Piso, techo o pared                                                         | Piso, techo o pared                                                        |
| **Protección**           | IP67                                                                       | IP54                                                                       |
| **Controlador**          | IRC5 Compact / IRC5 Gabinete simple, gabinete doble, montaje en panel       | DX100                                                                      |
| **Aplicaciones**         | Soldadura por arco, mecanizado, manipulación de piezas, montaje de piezas   | Soldadura por arco, manipulación de materiales, montaje de piezas, paletizado |

## __2. Comparación de home1 y home2 en Motoman MH6__

El Motoman MH6 está diseñado para operar con dos posiciones de referencia conocidas como "Home Position" y "Second Home Position". A continuación, se describen estas configuraciones:

### 2.1. Home Position (Posición de Origen):

- Es la posición “de fábrica” o estándar definida para el robot.
- Se utiliza como punto de partida para la calibración, verificación de la alineación de los ejes y reinicios del sistema.

Su ventaja radica en la consistencia y confiabilidad, ya que es la posición a la que se retorna habitualmente para iniciar operaciones y garantizar que las mediciones sean precisas.

### 2.2. Second Home Position (Segunda Posición de Origen):

- Es una posición adicional que puede ser definida por el usuario para adaptarse a necesidades específicas de la aplicación o a la optimización de trayectorias.
- Puede usarse como un “punto de descanso” o como una posición intermedia que permita reducir tiempos de desplazamiento en ciertos procesos.

Su ventaja es la flexibilidad, ya que se puede configurar para mejorar la eficiencia operativa en contextos particulares.

### 2.3 ¿Cuál es mejor?

- Si la prioridad es contar con un punto de referencia estándar y confiable para la calibración y reinicio del sistema, la posición Home1 es la más indicada.
- Si se busca optimizar rutas, minimizar tiempos de desplazamiento o adaptar la operación a un entorno de trabajo concreto, la posición Home2 puede ser configurada de manera que resulte más ventajosa para ese escenario en particular.

## __3. Procedimiento detallado para realizar movimientos manuales__

## __4. Niveles de velocidad para movimientos manuales__

## __5. Principales funcionalidades de RoboDK__

A continuación se presentan las principales funcionalidades del software RoboDK:

### Simulación y Programación Offline:
RoboDK permite crear y simular programas para robots en un entorno virtual en 3D. Esto posibilita desarrollar y validar la estrategia de movimiento sin detener la producción ni estar físicamente en la planta, lo que reduce el tiempo de integración y los riesgos asociados a pruebas en el robot real.

### Generación Automática de Código:
El software es capaz de generar el código específico para el robot seleccionado, compatible con una amplia variedad de marcas y modelos. Esto facilita la transferencia de los programas simulados al robot y minimiza errores en la programación manual. 

### Compatibilidad con Múltiples Robots y Equipos:
RoboDK soporta cientos de robots industriales de distintos fabricantes, permitiendo que los usuarios trabajen en un entorno homogéneo sin importar la marca del robot. Esto resulta especialmente útil en entornos de producción con flotas heterogéneas o cuando se evalúa la viabilidad de nuevos equipos.

### Integración con CAD/CAM y Herramientas Externas:
El software facilita la importación de modelos y trayectorias desde programas CAD/CAM, permitiendo al usuario planificar y optimizar la ruta del robot basándose en diseños reales y actualizados.

### Verificación de Colisiones y Optimización de Trayectorias:
RoboDK incluye herramientas para detectar posibles colisiones y optimizar los movimientos del robot, lo que ayuda a asegurar la seguridad en la planta y a mejorar la eficiencia de los procesos. 

### Interfaz Intuitiva y Personalizable:
Con una interfaz gráfica fácil de usar, el software permite a los usuarios configurar y modificar sus simulaciones de manera rápida. Además, ofrece soporte para scripting (por ejemplo, en Python) y una API que facilita la integración con otros sistemas o la personalización de flujos de trabajo. 

## __6. Análisis comparativo entre RoboDK y RobotStudio__

| Categoría                           | RoboDK                                                                                                                                         | RobotStudio                                                                                                                                                         |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Compatibilidad y Enfoque**        | - Multimarca: Soporta robots de diversos fabricantes (ABB, KUKA, FANUC, Motoman, etc.)<br>- Enfoque en versatilidad y flexibilidad             | - Exclusivo para robots ABB<br>- Integración estrecha con el ecosistema ABB<br>- Enfoque en simulaciones de alta fidelidad y creación de gemelos digitales       |
| **Funcionalidades de Programación y Simulación** | - Programación offline con simulación 3D<br>- Generación automática de código para distintos robots<br>- Optimización de trayectorias y verificación de colisiones<br>- Soporte para scripting (p. ej., Python) | - Simulación offline de alta fidelidad adaptada a robots ABB<br>- Programación offline integrada con datos reales<br>- Funcionalidad de gemelo digital para simular entornos reales |
| **Usabilidad y Extensibilidad**     | - Interfaz intuitiva y personalizable<br>- Soporte multiplataforma<br>- API y scripting para personalización<br>- Amplia comunidad y recursos | - Interfaz especializada para usuarios ABB<br>- Integración cerrada optimizada para el ecosistema ABB<br>- Soporte técnico y actualizaciones oficiales de ABB    |
| **Costo y Licenciamiento**          | - Licenciamiento comercial con costos variables según funcionalidades<br>- Versiones demo disponibles                                             | - Generalmente incluido para usuarios ABB, aunque en algunos casos pueden aplicarse costos adicionales<br>- Optimizado para el entorno ABB                     |
| **Conclusión**                      | Ideal para entornos heterogéneos que utilizan robots de distintas marcas y que requieren flexibilidad e integración con diversas herramientas. | Ideal para usuarios que trabajan exclusivamente con robots ABB y que requieren simulaciones y programación offline altamente integradas y precisas.           |

## __7. Código de trayectoria polar__

## __8. Videos__

- Video de simulación:

- Video de implementación en manipulador:

