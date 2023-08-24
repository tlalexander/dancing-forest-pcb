from numpy import array
import pykicad
from pykicad.pcb import *
from pykicad.module import *
import math
import os


if not os.path.exists('/home/taylor/'):
    print("WARNING! Base path not found. If output throws an error, make sure " \
        + "that the paths are set properly in the line below this message in the source file.")
os.environ['KISYSMOD'] = '/home/taylor/pcb/library/kicad-footprints/:/home/taylor/pcb/dancing_forest/parts'

# Define nets
vi, vo, gnd = Net('VI'), Net('VO'), Net('GND')

CENTER = (136.25,200)
CENTER_UPPER = (290,200)

# Load footprints
led_list = []


def led_loop(led_count, led_radius, led_count_sum, offset, lib, name, reference, bottom=False, start_angle_offset=0, rotation_angle_offset=0, center_position=CENTER, direction=1):
    for lednum in range(led_count):
        led = Module.from_library(lib, name)
        angle = direction * (lednum+offset) * 2*math.pi/led_count + start_angle_offset
        x_coord = led_radius * math.sin(angle)
        y_coord = led_radius * math.cos(angle)
        led.at = (center_position[0] + x_coord, center_position[1] + y_coord, math.degrees(angle+rotation_angle_offset))
        led.set_reference(f"{reference}{led_count_sum}")
        led_count_sum+=1
        if bottom:
            led.flip()

        if len(led.pads_by_name("1")[0].at) > 2:
            led.pads_by_name("1")[0].at[2] += math.degrees(angle+rotation_angle_offset)
        else:
            led.pads_by_name("1")[0].at.append(math.degrees(angle+rotation_angle_offset))


        led.pads_by_name("2")[0].at.append(math.degrees(angle+rotation_angle_offset))
        led.pads_by_name("3")[0].at.append(math.degrees(angle+rotation_angle_offset))
        led.pads_by_name("4")[0].at.append(math.degrees(angle+rotation_angle_offset))
        try:

            if len(led.pads_by_name("4")[1].at) > 2:
                led.pads_by_name("4")[1].at[2] += math.degrees(angle+rotation_angle_offset)
            else:
                led.pads_by_name("4")[1].at.append(math.degrees(angle+rotation_angle_offset))

            led.pads_by_name("1")[1].at.append(math.degrees(angle+rotation_angle_offset))
            led.pads_by_name("5")[0].at.append(math.degrees(angle+rotation_angle_offset))
            led.pads_by_name("6")[0].at.append(math.degrees(angle+rotation_angle_offset))
            led.pads_by_name("7")[0].at.append(math.degrees(angle+rotation_angle_offset))
            led.pads_by_name("8")[0].at.append(math.degrees(angle+rotation_angle_offset))
            led.pads_by_name("9")[0].at.append(math.degrees(angle+rotation_angle_offset))
            led.pads_by_name("10")[0].at.append(math.degrees(angle+rotation_angle_offset))
            led.pads_by_name("11")[0].at.append(math.degrees(angle+rotation_angle_offset))
            led.pads_by_name("12")[0].at.append(math.degrees(angle+rotation_angle_offset))
        except Exception as e:
            pass
        led.texts[0].at.append(math.degrees(angle+rotation_angle_offset))
        led_list.append(led)
    return led_count



def place_mousebite(position, index):
    lib = 'Panelization'
    name = "mouse-bite-3mm-slot-modified"
    reference="mousebite"
    led = Module.from_library(lib, name)
    led.at = (position[0],position[1], position[2])
    led.set_reference(f"{reference}{index}")
    led_list.append(led)

def place_hole(position, index):
    lib = 'led'
    name = "MountingHole_3.2mm_Plastite_#4"
    reference="H"
    led = Module.from_library(lib, name)
    led.at = (position[0],position[1], 0)
    led.set_reference(f"{reference}{index}")
    led_list.append(led)


ID = 56
OD = 165.5
c1 = pykicad.pcb.GrCircle(CENTER, (CENTER[0],CENTER[1]+ID/2), "Edge.Cuts", 0.25)
c2 = pykicad.pcb.GrCircle(CENTER, (CENTER[0],CENTER[1]+OD/2), "Dwgs.User", 0.25)



ID_UPPER = 26
OD_UPPER = 136
c1_upper = pykicad.pcb.GrCircle(CENTER_UPPER, (CENTER_UPPER[0],CENTER_UPPER[1]+ID_UPPER/2), "Edge.Cuts", 0.25)
c2_upper = pykicad.pcb.GrCircle(CENTER_UPPER, (CENTER_UPPER[0],CENTER_UPPER[1]+OD_UPPER/2), "Dwgs.User", 0.25)


ARC1_ANGLE = 85.84744391
arc1 = pykicad.pcb.GrArc((CENTER[0],CENTER[1]), (CENTER[0]-3,CENTER[1]+OD/2), ARC1_ANGLE, "Edge.Cuts", 0.25)
arc2 = pykicad.pcb.GrArc((CENTER[0],CENTER[1]), (CENTER[0]+OD/2,CENTER[1]+3), ARC1_ANGLE, "Edge.Cuts", 0.25)
arc3 = pykicad.pcb.GrArc((CENTER[0],CENTER[1]), (CENTER[0]+3,CENTER[1]-OD/2), ARC1_ANGLE, "Edge.Cuts", 0.25)
arc4 = pykicad.pcb.GrArc((CENTER[0],CENTER[1]), (CENTER[0]-OD/2,CENTER[1]-3), ARC1_ANGLE, "Edge.Cuts", 0.25)

ARC2_ANGLE = 84.94776702
arc5 = pykicad.pcb.GrArc((CENTER_UPPER[0],CENTER_UPPER[1]), (CENTER_UPPER[0]-3,CENTER_UPPER[1]+OD_UPPER/2), ARC2_ANGLE, "Edge.Cuts", 0.25)
arc6 = pykicad.pcb.GrArc((CENTER_UPPER[0],CENTER_UPPER[1]), (CENTER_UPPER[0]+OD_UPPER/2,CENTER_UPPER[1]+3), ARC2_ANGLE, "Edge.Cuts", 0.25)
arc7 = pykicad.pcb.GrArc((CENTER_UPPER[0],CENTER_UPPER[1]), (CENTER_UPPER[0]+3,CENTER_UPPER[1]-OD_UPPER/2), ARC2_ANGLE, "Edge.Cuts", 0.25)
arc8 = pykicad.pcb.GrArc((CENTER_UPPER[0],CENTER_UPPER[1]), (CENTER_UPPER[0]-OD_UPPER/2,CENTER_UPPER[1]-3), ARC2_ANGLE, "Edge.Cuts", 0.25)


line1 = pykicad.pcb.GrLine((CENTER[0]-OD/2-3,CENTER[1]-OD/2-3), (CENTER[0]-OD/2-3,CENTER[1]-3), "Edge.Cuts", 0.25)
line2 = pykicad.pcb.GrLine((CENTER[0]-OD/2-3,CENTER[1]+OD/2+3), (CENTER[0]-OD/2-3,CENTER[1]+3), "Edge.Cuts", 0.25)
line3 = pykicad.pcb.GrLine((CENTER[0]-OD/2-3,CENTER[1]-OD/2-3), (CENTER[0]-3,CENTER[1]-OD/2-3), "Edge.Cuts", 0.25)
line4 = pykicad.pcb.GrLine((CENTER[0]-OD/2-3,CENTER[1]+OD/2+3), (CENTER[0]-3,CENTER[1]+OD/2+3), "Edge.Cuts", 0.25)

line5 = pykicad.pcb.GrLine((CENTER[0]-OD/2-3-6,CENTER[1]-OD/2-3-6), (CENTER[0]-OD/2-3-6,CENTER[1]+OD/2+3+6), "Edge.Cuts", 0.25)

line6 = pykicad.pcb.GrLine((CENTER_UPPER[0]+OD_UPPER/2+3,CENTER_UPPER[1]-OD_UPPER/2-3), (CENTER_UPPER[0]+OD_UPPER/2+3,CENTER_UPPER[1]-3), "Edge.Cuts", 0.25)
line7 = pykicad.pcb.GrLine((CENTER_UPPER[0]+OD_UPPER/2+3,CENTER_UPPER[1]+OD_UPPER/2+3), (CENTER_UPPER[0]+OD_UPPER/2+3,CENTER_UPPER[1]+3), "Edge.Cuts", 0.25)
line8 = pykicad.pcb.GrLine((CENTER_UPPER[0]+OD_UPPER/2+3,CENTER_UPPER[1]-OD_UPPER/2-3), (CENTER_UPPER[0]+3,CENTER_UPPER[1]-OD_UPPER/2-3), "Edge.Cuts", 0.25)
line9 = pykicad.pcb.GrLine((CENTER_UPPER[0]+OD_UPPER/2+3,CENTER_UPPER[1]+OD_UPPER/2+3), (CENTER_UPPER[0]+3,CENTER_UPPER[1]+OD_UPPER/2+3), "Edge.Cuts", 0.25)

line10 = pykicad.pcb.GrLine((CENTER_UPPER[0]+OD_UPPER/2+3+6,CENTER_UPPER[1]-OD/2-3-6), (CENTER_UPPER[0]+OD_UPPER/2+3+6,CENTER_UPPER[1]+OD/2+3+6), "Edge.Cuts", 0.25)
line11 = pykicad.pcb.GrLine((CENTER_UPPER[0]+OD_UPPER/2+3+6,CENTER_UPPER[1]-OD/2-3-6), (CENTER[0]-OD/2-3-6,CENTER[1]-OD/2-3-6), "Edge.Cuts", 0.25)
line12 = pykicad.pcb.GrLine((CENTER[0]-OD/2-3-6,CENTER[1]+OD/2+3+6), (CENTER_UPPER[0]+OD_UPPER/2+3+6,CENTER_UPPER[1]+OD/2+3+6), "Edge.Cuts", 0.25)

line13 = pykicad.pcb.GrLine((CENTER_UPPER[0]-3,CENTER_UPPER[1]-OD_UPPER/2-3), (CENTER[0]+3,CENTER[1]-OD/2-3), "Edge.Cuts", 0.25)
line14 = pykicad.pcb.GrLine((CENTER_UPPER[0]-3,CENTER_UPPER[1]+OD_UPPER/2+3), (CENTER[0]+3,CENTER[1]+OD/2+3), "Edge.Cuts", 0.25)


# calculate mousebite positions
# coordinates = (left/right, up/down)
MB_WIDTH = 3

pos_left = (CENTER[0]-OD/2-MB_WIDTH/2,CENTER[1], 90)
pos_left_top = (CENTER[0],CENTER[1]-OD/2-MB_WIDTH/2, 0)
pos_left_bottom = (CENTER[0],CENTER[1]+OD/2+MB_WIDTH/2, 0)
pos_middle = (CENTER[0]+OD/2+MB_WIDTH/2,CENTER[1], 90)

pos_right = (CENTER_UPPER[0]+OD_UPPER/2+MB_WIDTH/2,CENTER_UPPER[1], 90)
pos_right_top = (CENTER_UPPER[0],CENTER_UPPER[1]-OD_UPPER/2-MB_WIDTH/2, 0)
pos_right_bottom = (CENTER_UPPER[0],CENTER_UPPER[1]+OD_UPPER/2+MB_WIDTH/2, 0)

place_mousebite(pos_left, 1)
place_mousebite(pos_left_top, 2)
place_mousebite(pos_left_bottom, 3)
place_mousebite(pos_middle, 4)
place_mousebite(pos_right, 5)
place_mousebite(pos_right_top, 6)
place_mousebite(pos_right_bottom, 7)

lower_holes_w = 78.8
lower_holes_h = 58.2

place_hole((CENTER[0]+lower_holes_w/2, CENTER[1]+lower_holes_h/2), 1)
place_hole((CENTER[0]-lower_holes_w/2, CENTER[1]+lower_holes_h/2), 2)
place_hole((CENTER[0]-lower_holes_w/2, CENTER[1]-lower_holes_h/2), 3)
place_hole((CENTER[0]+lower_holes_w/2, CENTER[1]-lower_holes_h/2), 4)

upper_holes_w = 61.5
upper_holes_h = 35.0

place_hole((CENTER_UPPER[0]+upper_holes_w/2, CENTER_UPPER[1]+upper_holes_h/2), 5)
place_hole((CENTER_UPPER[0]-upper_holes_w/2, CENTER_UPPER[1]+upper_holes_h/2), 6)
place_hole((CENTER_UPPER[0]-upper_holes_w/2, CENTER_UPPER[1]-upper_holes_h/2), 7)
place_hole((CENTER_UPPER[0]+upper_holes_w/2, CENTER_UPPER[1]-upper_holes_h/2), 8)

place_hole((CENTER_UPPER[0]+lower_holes_w/2, CENTER_UPPER[1]+lower_holes_h/2), 9)
place_hole((CENTER_UPPER[0]-lower_holes_w/2, CENTER_UPPER[1]+lower_holes_h/2), 10)
place_hole((CENTER_UPPER[0]-lower_holes_w/2, CENTER_UPPER[1]-lower_holes_h/2), 11)
place_hole((CENTER_UPPER[0]+lower_holes_w/2, CENTER_UPPER[1]-lower_holes_h/2), 12)



"""
Lower PCB
"""

led_radius = 38
led_count = 16
led_count_sum = 1

led_loop(led_count, led_radius, led_count_sum, offset=8.5, lib = 'led', name = "LED_SK6812_PLCC4_5.0x5.0mm_P3.2mm_OLD", reference="RGBWD")

led_radius = 58
led_count = 24
led_count_sum = 1
led_count_sum += led_loop(led_count, led_radius, led_count_sum, offset=12, lib = 'LED_SMD', name = "LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm", reference="RGBD")

led_radius = 77
led_count = 24
led_count_sum += led_loop(led_count, led_radius, led_count_sum, offset=12.5, lib = 'LED_SMD', name = "LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm", reference="RGBD")

rgbd_count_sum = led_count_sum

led_radius = 79
led_count = 24
led_count_sum = 1
led_loop(led_count, led_radius, led_count_sum, offset=5, lib = 'led', name = "SK6812SIDE_OLD", reference="RGBSIDE",start_angle_offset=math.pi/12)


led_radius = 76
led_count = 3
led_count_sum = 1
# led_loop(led_count, led_radius, led_count_sum, offset=0, lib = 'Sensor_Distance', name = "ST_VL53L1x", reference="DIST", start_angle_offset=math.pi/2.0, rotation_angle_offset=math.pi/2.0)

led_radius = 68
led_count = 3
led_count_sum = 1
led_loop(led_count, led_radius, led_count_sum, offset=0, lib = 'led', name = "5_pin", reference="DIST", start_angle_offset=math.pi/2.0, rotation_angle_offset=math.pi/2.0)


"""
Upper PCB
"""

led_radius = 59
led_count = 12
led_count_sum = rgbd_count_sum
led_count_sum += led_loop(led_count, led_radius, led_count_sum, offset=6.5, lib = 'LED_SMD', name = "LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm", reference="RGBD", center_position=CENTER_UPPER, direction=-1)

led_radius = 43

led_loop(led_count, led_radius, led_count_sum, offset=6, lib = 'LED_SMD', name = "LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm", reference="RGBD", center_position=CENTER_UPPER, direction=-1)


layers = [
    Layer('F.Cu'),
    Layer('Inner1.Cu'),
    Layer('Inner2.Cu'),
    Layer('B.Cu'),
    Layer('Edge.Cuts', type='user'),
    Layer('Dwgs.User', type='user'),
    Layer('Eco1.User', type='user')
]

for layer in ['Mask', 'Paste', 'SilkS', 'CrtYd', 'Fab']:
    for side in ['B', 'F']:
        layers.append(Layer('%s.%s' % (side, layer), type='user'))

nc1 = NetClass('default', trace_width=1, nets=['VI', 'VO', 'GND'])

# Create PCB
pcb = Pcb()
pcb.title = 'A title'
pcb.comment1 = 'Comment 1'
pcb.page_type = [400, 400]
pcb.num_nets = 5
pcb.setup = Setup(grid_origin=[200, 200])
pcb.layers = layers
pcb.modules += led_list
pcb.net_classes += [nc1]
pcb.nets += [vi, vo, gnd]
pcb.lines += [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14]
# pcb.vias += [v1]
# pcb.zones += [gndplane_top]
pcb.circles+=[c1, c2, c1_upper, c2_upper, arc1, arc2, arc3, arc4, arc5, arc6, arc7, arc8]

pcb.to_file('project_rev2')
