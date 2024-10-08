import machine, onewire, ds18x20, time
import wifi
import thingspeak

ds_pin = machine.Pin(5)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

def run():
    wifi.connect()
    while True:
        ds_sensor.convert_temp()
        time.sleep_ms(750)
        for rom in roms:
            print(rom)
            temp = ds_sensor.read_temp(rom)
            print(temp)
            thingspeak.send(temp)
        time.sleep(600)
        
