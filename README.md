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

### **Procedimiento para Mover Manualmente el Manipulador Motoman**

#### **1. Configuración para el Movimiento Manual**
Para mover manualmente el robot Yaskawa (Motoman), sigue estos pasos:

1. **Cambiar al Modo Enseñanza (Teach Mode)**  
   - Gira el selector de llave a **Modo Enseñanza** (icono de mano).

2. **Activar el Servo**  
   - Presiona **Servo On** hasta que se encienda la luz verde.

3. **Presionar el Interruptor de Seguridad (Deadman Switch)**  
   - Mantén presionado el **Deadman Switch** en el teach pendant. Esto libera los frenos y permite el movimiento.

---

#### **2. Movimiento del Robot por Ejes (Joints)**
- Una vez activado el **Deadman Switch**:
  - Usa las teclas **S+ y S-** para mover cada eje individualmente.
  - Los **movimientos por ejes** corresponden a:
    - **S** (Eje 1)
    - **L** (Eje 2)
    - **U** (Eje 3)
    - **R** (Eje 4)
    - **B** (Eje 5)
    - **T** (Eje 6)

---

#### **3. Cambio al Movimiento Cartesiano**
- Para cambiar al modo cartesiano:
  - Presiona el botón **COORD** (Sistema de Coordenadas) en la parte superior del teach pendant.
  - Esto alternará entre los siguientes sistemas de coordenadas:
    - **Coordenadas Mundo (World)**
    - **Coordenadas Herramienta (Tool)**
    - **Coordenadas Cartesianas**
    - **Modo Joints (Ejes Articulares)**

---

#### **4. Movimiento de Traslación y Rotación en Modo Cartesiano**
Una vez en **Modo Cartesiano**, usa las siguientes teclas:

- **Movimientos de Traslación (X, Y, Z)**
  - **X+ / X-** → Mueve en el eje X.
  - **Y+ / Y-** → Mueve en el eje Y.
  - **Z+ / Z-** → Mueve en el eje Z.

- **Movimientos de Rotación (Alrededor de X, Y, Z)**
  - **Rx+ / Rx-** → Rota alrededor del eje X.
  - **Ry+ / Ry-** → Rota alrededor del eje Y.
  - **Rz+ / Rz-** → Rota alrededor del eje Z.
  - 
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
```
from robodk.robolink import *    # API para comunicarte con RoboDK
from robodk.robomath import *     # Funciones matemáticas
import math

#------------------------------------------------
# 1) Conexión a RoboDK e inicialización
#------------------------------------------------
RDK = Robolink()

# Elegir un robot (si hay varios, aparecerá un popup)
robot = RDK.ItemUserPick("Selecciona un robot", ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception("No se ha seleccionado un robot válido.")

#------------------------------------------------
# 2) Tomar el Frame ya creado en RoboDK
#    (ejemplo: "Frame_from_Target1")
#------------------------------------------------
frame_name = "Frame_from_Target1"
frame_inclinado = RDK.Item(frame_name, ITEM_TYPE_FRAME)
if not frame_inclinado.Valid():
    raise Exception(f'No se encontró el Frame "{frame_name}" en la estación.')

# Configuramos el robot para que use este frame y la herramienta activa
robot.setPoseFrame(frame_inclinado)
robot.setPoseTool(robot.PoseTool())

# Ajustes de velocidad y blending
robot.setSpeed(100)   # mm/s
robot.setRounding(5)  # radio de curvatura (blend)

#------------------------------------------------
# 3) Parámetros para posicionar las letras sobre una línea recta
#    Usando coordenadas polares con ángulo fijo.
#------------------------------------------------
# Ajusta estos parámetros según el área de trabajo de tu robot:
baseline_center_x = -50   # Centro base X (ajusta para que esté en zona alcanzable)
baseline_center_y = 0     # Centro base Y
baseline_angle = 0        # 0° = línea horizontal hacia la derecha
start_distance = 50       # Distancia radial inicial (posición de la 1ª letra)
letter_width = 10 * 1.0   # Ancho aproximado de cada letra (basado en la definición)
spacing = 20              # Espaciado adicional entre letras

# La palabra a escribir:
word_to_write = "CRIS Y JOHO"
scale = 1.0         # Escala de las letras
z_draw = 0          # Altura de dibujo en el frame
pen_up_dist = 15    # Altura para levantar la herramienta entre trazos

#------------------------------------------------
# 4) Definición de las letras (coordenadas locales cartesianas)
#------------------------------------------------
letter_C = [
    [(10, 0), (0, 0), (0, 30), (10, 30)]
]

letter_R = [
    [(0, 0), (0, 30)],
    [(0, 30), (10, 25), (0, 15)],
    [(0, 15), (10, 0)]
]

letter_I = [
    [(5, 0), (5, 30)]
]

letter_S = [
    [(10, 0), (0, 0), (0, 15), (10, 15), (10, 30), (0, 30)]
]

letter_T = [
    [(0, 30), (10, 30)],
    [(5, 30), (5, 0)]
]

letter_N = [
    [(0, 0), (0, 30)],
    [(0, 30), (10, 0)],
    [(10, 0), (10, 30)]
]

letter_Y = [
    [(0, 30), (5, 15), (10, 30)],
    [(5, 15), (5, 0)]
]

letters = {
    'C': letter_C,
    'R': letter_R,
    'I': letter_I,
    'S': letter_S,
    'T': letter_T,
    'A': [
        [(0, 0), (5, 30), (10, 0)],
        [(2, 15), (8, 15)]
    ],
    'N': letter_N,
    'Y': letter_Y,
    'J': [
        [(10, 30), (10, 0), (5, -5), (0, 0)]
    ],
    'O': [
        [(0, 0), (0, 30), (10, 30), (10, 0), (0, 0)]
    ],
    'H': [
        [(0, 0), (0, 30)],
        [(0, 15), (10, 15)],
        [(10, 0), (10, 30)]
    ]
}

#------------------------------------------------
# 5) Función para dibujar una letra con corrección de orientación
#    Se aplica rotation=0 y se invierte la coordenada Y (flip Y)
#------------------------------------------------
def draw_letter(letter, offset_x, offset_y, rotation=0):
    """
    Dibuja la letra usando las coordenadas locales definidas en 'letters'.
    Se le aplica una rotación (en grados) y se traslada al offset (offset_x, offset_y).
    Además, se invierte la coordenada Y para que la orientación sea la correcta.
    """
    polylines = letters.get(letter, [])
    last_x, last_y = offset_x, offset_y
    rot = math.radians(rotation)  # Convertir grados a radianes
    for pline in polylines:
        # Primer punto de la polilínea:
        local_x = scale * pline[0][0]
        local_y = scale * pline[0][1]
        # Aplicar la rotación
        x0 = local_x * math.cos(rot) - local_y * math.sin(rot)
        y0 = local_x * math.sin(rot) + local_y * math.cos(rot)
        # Flip Y: invertir la coordenada Y
        y0 = -y0  # <--- Aquí se invierte el eje Y
        # Trasladar al offset global:
        x0 += offset_x
        y0 += offset_y
        pose_move = eye(4)
        pose_move.setPos([x0, y0, z_draw])
        robot.MoveL(pose_move)
        
        for pt in pline[1:]:
            local_x = scale * pt[0]
            local_y = scale * pt[1]
            x = local_x * math.cos(rot) - local_y * math.sin(rot)
            y = local_x * math.sin(rot) + local_y * math.cos(rot)
            # Flip Y
            y = -y  # <--- Inversión de Y para cada punto
            x += offset_x
            y += offset_y
            pose_line = eye(4)
            pose_line.setPos([x, y, z_draw])
            robot.MoveL(pose_line)
            last_x, last_y = x, y
    return last_x, last_y

#------------------------------------------------
# 6) Dibujar la palabra sobre una línea recta
#    Se calcula la posición de cada letra usando coordenadas polares con ángulo fijo.
#------------------------------------------------
current_distance = start_distance
for letter in word_to_write:
    # Calcular la posición de la letra en la línea base
    offset_x = baseline_center_x + current_distance * math.cos(math.radians(baseline_angle))
    offset_y = baseline_center_y + current_distance * math.sin(math.radians(baseline_angle))
    
    # Posición de aproximación (pen up)
    pose_up = transl(offset_x, offset_y, z_draw + pen_up_dist)
    try:
        robot.MoveJ(pose_up)
    except Exception as e:
        print(f"Error moviendo a pose_up ({offset_x:.2f}, {offset_y:.2f}): {e}")
        current_distance += letter_width + spacing
        continue

    # Posición de inicio de dibujo (pen down)
    pose_down = transl(offset_x, offset_y, z_draw)
    try:
        robot.MoveL(pose_down)
    except Exception as e:
        print(f"Error moviendo a pose_down ({offset_x:.2f}, {offset_y:.2f}): {e}")
        current_distance += letter_width + spacing
        continue
    
    if letter == ' ':
        # Para un espacio solo aumentar la distancia
        current_distance += letter_width + spacing
        continue
    
    # Dibujar la letra con orientación horizontal (rotation=0)
    draw_letter(letter, offset_x, offset_y, rotation=0)
    
    # Levantar la herramienta al terminar la letra
    pose_after = transl(offset_x, offset_y, z_draw + pen_up_dist)
    try:
        robot.MoveL(pose_after)
    except Exception as e:
        print(f"Error levantando la herramienta en ({offset_x:.2f}, {offset_y:.2f}): {e}")
    
    # Actualizar la distancia para la siguiente letra
    current_distance += letter_width + spacing

print("¡Escritura sobre línea recta terminada!")

```
## __8. Videos__

- Video de simulación:
https://youtu.be/Sm6kdJNh65E

  [![Video en YouTube](https://img.youtube.com/vi/Sm6kdJNh65E/0.jpg)](https://youtu.be/Sm6kdJNh65E)
- Video de implementación en manipulador:
  https://youtu.be/35M9gzuCKwA
  [![Video en YouTube](https://img.youtube.com/vi/35M9gzuCKwA/0.jpg)](https://youtu.be/35M9gzuCKwA)
