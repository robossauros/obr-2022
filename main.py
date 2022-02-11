#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#------------------------------DECLARAÇÃO DAS PORTAS------------------------------
ev3 = EV3Brick()

mtd = Motor(Port.A)
mte = Motor(Port.D)
mtg = Motor(Port.B)
mtc = Motor(Port.C)

ultral = UltrasonicSensor(Port.S2)
ultraf = UltrasonicSensor(Port.S3)

core = ColorSensor(Port.S4)
cord = ColorSensor(Port.S1)

cmt = StopWatch()
mov = DriveBase(mte, mtd, wheel_diameter=18, axle_track=104) #19

#mov.run_angle(20, 180, then=Stop.HOLD, wait=True)


kp = 7
velocidade = 110
saida = 0
RGBe = (21,26,31)

while ultral.distance() > 100 :
    
#------------------------------SEGUIDOR DE LINHA------------------------------
    ev3.screen.print(RGBe)
    RGBe = core.rgb()
    RGBd = cord.rgb()
    erro = RGBd[0] - RGBe[0]
    saida = erro*kp
    mtd.run((velocidade + saida))
    mte.run((velocidade - saida))

#------------------------------DESVIO DE OBSTACULO-----------------------------

    if ultraf.distance() < 50 :

        mov.turn(75) #angulo
        mov.stop()
        while cord.reflection() > 20:
            mtd.run(150)
            mte.run(60) 

        mov.straight(3)
        mov.stop()
        while cord.reflection() > 20:
            mtd.run(-150)
            mte.run(150)
        

#--------------------------------CURVAS VERDES--------------------------------

#                DIREITA
    if cord.color() == Color.GREEN:
        mov.straight(-20) #velocidade, tempo
        mov.stop()

        if cord.color() == Color.BLACK:
            mov.straight(40)
            mov.stop()

            while core.color() != Color.GREEN :
                RGBe = core.rgb()
                RGBd = cord.rgb()
                erro = RGBd[0] - RGBe[0]
                saida = erro*kp
                mtd.run((velocidade + saida))
                mte.run((velocidade - saida))

            mov.turn(180)
            mov.straight(-20)
            mov.stop()

        else :
            mov.straight(70) #velocidade, tempo
            mov.turn(60) #angulo (40)
            mov.stop()
            while core.color() != Color.BLACK :
                mtd.run(-100)
                mte.run(100)

#               ESQUERDA
    if core.color() == Color.GREEN:
        mov.straight(-20) #velocidade, tempo
        mov.stop()

        if core.color() == Color.BLACK:
            mov.straight(40)
            mov.stop()

            while cord.color() != Color.GREEN :
                RGBe = core.rgb()
                RGBd = cord.rgb()
                erro = RGBd[0] - RGBe[0]
                saida = erro*kp
                mtd.run((velocidade + saida))
                mte.run((velocidade - saida))

            mov.turn(180)
            mov.straight(-20)
            mov.stop()

        else :
            mov.straight(70) #velocidade, tempo
            mov.turn(-60) #angulo (-60)
            mov.stop()
            while cord.color() != Color.BLACK :
                mtd.run(100) #80
                mte.run(-100)


#-----------------------------------------------------------------------------
#-----------------------------------SALA 3------------------------------------

kp = 8
velocidade = 300
saida = 0

cmt.reset()
while cmt.time() < 25200 :
    RGBe = core.rgb()
    RGBd = cord.rgb()
    erro = RGBd[0] - RGBe[0]
    saida = erro*kp
    mtd.run((velocidade + saida))
    mte.run((velocidade - saida))


#___________________________________________________________________________________
#                                       RESGATE

#ev3.screen.print(ultraf.distance())
#wait(10000)

mov.turn(-6)
mov.straight(345)
mov.turn(-45)

#--------------------triângulo 1-----------------------

if ultral.distance() < 100:

#   posicionamento
    mov.turn(143) #era (150)
    mov.stop()

#   descer garra
    mtc.run(-360)
    mtg.run(-45)
    wait(2500)
    mtc.run(0)
    mtg.run(0)
    wait(500)

#   patrulhar
    mov.straight(-320)
    mov.straight(25)
    mov.stop()

#   recolher garra
    mtc.run(360)
    mtg.run(40)
    wait(2400)
    mtc.run(0)
    mtg.run(0)
    wait(500)

#   retornar ao triângulo
    mov.turn(-200)
    mov.straight(-200)

#   despejar bola
    mtc.run(-300)
    wait(3000)

    mtg.run(0)
    mtc.run(0)
    wait(500)

    mtg.run(20)
    wait(1500)

    mov.straight(-50)

    mtg.run(-20)
    mtc.run(300)
    wait(3000)
    
    mtg.run(0)
    mtc.run(0)
    wait(500)




#   SEGUNDA ROTA

#   posicionamento  
    mov.turn(180)
    mov.straight(-200)

#   descer garra     
    mtc.run(-360)
    mtg.run(-45)
    wait(2500)
    mtc.run(0)
    mtg.run(0)
    wait(500)

#   patrulhar
    mov.turn(-45)
    mov.straight(-80)

#   recolher garra
    mtc.run(360)
    mtg.run(40)
    wait(2400)
    mtc.run(0)
    mtg.run(0)
    wait(500)

#   retornar ao triangulo   
    mov.turn(-150)
    mov.straight(-310)

#   despejar bola
    mtc.run(-300)
    wait(3000)

    mtg.run(0)
    mtc.run(0)
    wait(500)

    mtg.run(20)
    wait(1500)

    mov.straight(-50)

    mtg.run(-20)
    mtc.run(300)
    wait(3000)
    
    mtg.run(0)
    mtc.run(0)
    wait(500)

#--------------------triângulo 2-----------------------

else:
    mov.straight(70)
    mov.turn(-90)#110
    mov.straight(260)
    ev3.screen.print(ultraf.distance())
    wait(3000)
    if ultraf.distance() < 40:

#   descer garra
        mtc.run(-360)
        mtg.run(-45)
        wait(2500)
        mtc.run(0)
        mtg.run(0)
        wait(500)

#   patrulhar
        mov.turn(-35)
        mov.straight(-280)
        mov.straight(5)

#   subir a garra
        mtc.run(-300)
        mtg.run(45)
        wait(2500)
        mtc.run(0)
        mtg.run(0)
        wait(500)

#   retornar ao triângulo     
        mov.turn(-180)
        mov.straight(-195)
        mov.turn(40)


#   despejar a bola
        mtc.run(-300)
        wait(3000)

        mtg.run(0)
        mtc.run(0)
        wait(500)

        mtg.run(20)
        wait(1500)

        mov.straight(-50)

        mtg.run(-20)
        mtc.run(300)
        wait(3000)
        
        mtg.run(0)
        mtc.run(0)
        wait(500)

#       ROTA 2
#   posicionamento
        mov.turn(-145)
    
#   descer garra
        mtc.run(300)
        mtg.run(-45)
        wait(2500)
        mtc.run(0)
        mtg.run(0)
        wait(500)
#   patrulhar
        mov.straight(-200)
#   subir garra
        mtc.run(-300)
        mtg.run(40)
        wait(2500)
        mtc.run(0)
        mtg.run(0)
        wait(500)
#   retornar ao triangulo
        mov.turn(170)
        mov.straight(-200)
#   despejar bola
        mtg.run(-10)
        mtc.run(300)
        wait(3000)

        mtg.run(0)
        mtc.run(0)
        wait(500)

        mtg.run(20)
        wait(1500)

        mov.straight(-50)

        mtg.run(40)
        mtc.run(-300)
        wait(3000)


        
    
    

#--------------------triângulo 3-----------------------
    else:
        mov.turn(-35)
        mov.straight(10)

#   descer garra
        mtc.run(300)
        mtg.run(-45)
        wait(2500)
        mtc.run(0)
        mtg.run(0)
        wait(500)

#   patrulhar
        mov.straight(-300)
        mov.straight(5)

#   subir a garra
        mtc.run(-300)
        mtg.run(45)
        wait(2500)
        mtc.run(0)
        mtg.run(0)
        wait(500)

#   retornar ao triângulo      
        mov.turn(-75)
        mov.straight(-20)

#   despejar a bola
        mtg.run(-10)
        mtc.run(300)
        wait(3000)

        mtg.run(0)
        mtc.run(0)
        wait(500)

        mtg.run(20)
        wait(1500)

        mov.straight(-50)

        mtg.run(-10) #40
        mtc.run(-300)
        wait(3000)