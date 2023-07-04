from numpy import array
import pykicad
from pykicad.pcb import *
from pykicad.module import *
import math


# export KISYSMOD=/home/taylor/pcb/library/kicad-footprints/:/home/taylor/pcb/dancing_forest/parts; python3 generate.py


# Define nets
vi, vo, gnd = Net('VI'), Net('VO'), Net('GND')

CENTER = (200,200)

# Load footprints
led_list = []


def led_loop(led_count, led_radius, led_count_sum, offset, lib, name, reference, bottom=False, start_angle_offset=0, rotation_angle_offset=0):
    for lednum in range(led_count):
        led = Module.from_library(lib, name)
        angle = (lednum+offset) * 2*math.pi/led_count + start_angle_offset
        x_coord = led_radius * math.sin(angle)
        y_coord = led_radius * math.cos(angle)
        led.at = (CENTER[0] + x_coord, CENTER[1] + y_coord, math.degrees(angle+rotation_angle_offset))
        led.set_reference(f"{reference}{led_count_sum}")
        led_count_sum+=1
        if bottom:
            led.flip()
        led.pads_by_name("1")[0].at.append(math.degrees(angle+rotation_angle_offset))
        led.pads_by_name("2")[0].at.append(math.degrees(angle+rotation_angle_offset))
        led.pads_by_name("3")[0].at.append(math.degrees(angle+rotation_angle_offset))
        led.pads_by_name("4")[0].at.append(math.degrees(angle+rotation_angle_offset))
        try:
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

led_count = 16
led_radius = 41
led_count_sum = 1

led_loop(led_count, led_radius, led_count_sum, offset=0.5, lib = 'LED_SMD', name = "LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm", reference="RGBWD")

led_count = 24
led_radius = 55.5
led_count_sum = 1
led_count_sum += led_loop(led_count, led_radius, led_count_sum, offset=0, lib = 'LED_SMD', name = "LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm", reference="RGBD")

led_count = 24
led_radius = 70
led_count_sum += led_loop(led_count, led_radius, led_count_sum, offset=0.5, lib = 'LED_SMD', name = "LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm", reference="RGBD")

led_count = 12
led_radius = 41
led_loop(led_count, led_radius, led_count_sum, offset=0.5, lib = 'LED_SMD', name = "LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm", reference="RGBD", bottom=True)

led_count = 12
led_radius = 72.5
led_count_sum = 1
led_loop(led_count, led_radius, led_count_sum, offset=0, lib = 'led', name = "SK6812SIDE", reference="RGBSIDE",start_angle_offset=math.pi/6*1.5)


led_count = 3
led_radius = 71
led_count_sum = 1
led_loop(led_count, led_radius, led_count_sum, offset=0, lib = 'Sensor_Distance', name = "ST_VL53L1x", reference="DIST", start_angle_offset=0, rotation_angle_offset=math.pi/2.0)


#
#

#
# for lednum in range(led_count):
#     led = Module.from_library('LED_SMD', "LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm")
#     angle = lednum * 2*math.pi/led_count
#     x_coord = led_radius * math.sin(angle)
#     y_coord = led_radius * math.cos(angle)
#     led.at = (CENTER[0] + x_coord, CENTER[1] + y_coord, math.degrees(angle))
#     led.set_reference(f"D_{led_count_sum}")
#     led_count_sum+=1
#     led_list.append(led)
#
#
# led_count = 24
# led_radius = 130
#
# for lednum in range(led_count):
#     led = Module.from_library('LED_SMD', "LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm")
#     angle = lednum * 2*math.pi/led_count
#     x_coord = led_radius * math.sin(angle)
#     y_coord = led_radius * math.cos(angle)
#     led.at = (CENTER[0] + x_coord, CENTER[1] + y_coord, math.degrees(angle))
#     led.set_reference(f"D_{led_count_sum}")
#     led_count_sum+=1
#     led_list.append(led)



# # Connect pads
# r1.pads[0].net = vi
# r1.pads[1].net = vo
# r2.pads[0].net = vo
# r2.pads[1].net = gnd
#
# # Place components
# r1.at = [200, 100]
# r2.at = [100, 200]

# # Compute positions
# start = array(r1.pads[1].at) + array(r1.at)
# end = array(r2.pads[0].at) + array(r2.at)
# pos = start + (end - start) / 2
#
# # Create vias
# v1 = Via(at=pos.tolist(), size=.8, drill=.6, net=vo.code)
#
# # Create segments
# s1 = Segment(start=start.tolist(), end=pos.tolist(), net=vo.code)
# s2 = Segment(start=pos.tolist(), end=end.tolist(), net=vo.code)

c1 = pykicad.pcb.GrCircle(CENTER, (CENTER[0],CENTER[1]+72/2), "Edge.Cuts", 0.25)
c2 = pykicad.pcb.GrCircle(CENTER, (CENTER[0],CENTER[1]+148/2), "Edge.Cuts", 0.25)
# print(c1)
# import sys
# sys.exit()

# # Create zones
# coords = [(0, 0), (10, 0), (10, 10), (0, 10)]
# gndplane_top = Zone(net_name='GND', layer='F.Cu', polygon=coords, clearance=0.3)


layers = [
    Layer('F.Cu'),
    Layer('Inner1.Cu'),
    Layer('Inner2.Cu'),
    Layer('B.Cu'),
    Layer('Edge.Cuts', type='user')
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
# pcb.segments += [s1, s2]
# pcb.vias += [v1]
# pcb.zones += [gndplane_top]
pcb.circles+=[c1, c2]

pcb.to_file('project')
