from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
 import  math

hub = PrimeHub()

#vai p frente 
motor_pair = MotorPair('B', 'A')
motor_pair.move_tank(15, 'cm', left_speed=50, right_speed=50)

#vai p frente com possibilidade de giro (depende do valor atribuído )
motor_pair.move(8.1 * math.pi / 2, 'cm', steering=0)

#giro 
motor_pair.move(8.1 * math.pi / 2, 'cm', steering=100)

#bya