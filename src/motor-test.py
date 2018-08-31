import machine

spda = machine.Pin(5)
dira = machine.Pin(0)
spda_pwm = machine.PWM(spda)
spda_pwm.duty(512)

spdb = machine.Pin(4)
dirb = machine.Pin(2)
spdb_pwm = machine.PWM(spdb)
spdb_pwm.duty(512)
