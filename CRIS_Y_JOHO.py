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
