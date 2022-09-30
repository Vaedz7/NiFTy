import nifty

nifty.set_layers(2)

nifty.set_directory(1, "users/vaedz/documents/layer1/")
nifty.set_directory(2, "users/vaedz/documents/layer2/")

nifty.save_to("users/vaedz/documents/generations/")

nifty.generate(69)

result = open("users/vaedz/documents/generations/69.png", rb)
result.show()
result.close()
