import barcode
from barcode import Code128
from barcode.writer import ImageWriter

def generate_barcode(data):
    code = Code128(data, writer=ImageWriter())
    filename = 'barcode'
    code.save(filename)

    print(f"Barcode generated and saved as {filename}.png")

data = "6901-5302-2345"
generate_barcode(data)

