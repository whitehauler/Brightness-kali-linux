x="/sys/class/backlight/amdgpu_bl0/brightness"
def set_brightness(brightness):
    if int(brightness) > 90:
        raise TypeError("Need int 0 < and > 15")
    elif int(brightness) < 0:
        raise TypeError("Need int 0 < and > 15")
    with open(x,"w") as bright:
         bright.write(str(brightness))
         bright.close()

a=input("Brightness <5-50> : ")
set_brightness(a)
