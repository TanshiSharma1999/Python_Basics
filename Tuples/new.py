#tuple
#lists are slow
#so you use tuple

#tuple
#packing
address=(67,"skibidi street","dummyLand","Pizzasia",11676711)
print(address)
#slicing
print(address[1])
print(address[2:4])
print(address[-3:-1])
#unpacking tuple
houseno,street,city,country,postalcode=address
print(houseno)
print(city)