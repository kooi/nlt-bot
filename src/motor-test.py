import machine

spda = machine.Pin(5, machine.Pin.OUT)
spda_pwm = machine.PWM(spda)
dira = machine.Pin(0, machine.Pin.OUT)
dira.value(1) #reverse
spda_pwm.duty(512)

spdb = machine.Pin(4, machine.Pin.OUT)
spdb_pwm = machine.PWM(spdb)
dirb = machine.Pin(2, machine.Pin.OUT)
dirb.value(0) #forward
spdb_pwm.duty(512)
