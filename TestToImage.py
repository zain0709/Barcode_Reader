# from PIL import Image as PIL
# from pdf417decoder import PDF417Decoder

# image = PIL.open("images/images.jpg")
# decoder = PDF417Decoder(image)

# if (decoder.decode() > 0):
#     decoded = decoder.barcode_data_index_to_string(0)
# print(decoded)



from PIL import Image as PIL
from pdf417decoder import PDF417Decoder

# Load the image
image = PIL.open("images/imagesss.jpg")

# Decode the PDF417 barcode
decoder = PDF417Decoder(image)
if decoder.decode() > 0:
    decoded = decoder.barcode_data_index_to_string(0)

    # Parse the decoded data
    data = {
        "Last Name": decoded.split("DCS")[1].split("\n")[0].strip(),
        "First Name": decoded.split("DAC")[1].split("\n")[0].strip(),
        "Middle Name": decoded.split("DAD")[1].split("\n")[0].strip(),
        "Date of Birth (DOB)": f"{decoded.split('DBB')[1][:4]}-{decoded.split('DBB')[1][4:6]}-{decoded.split('DBB')[1][6:]}",
        "Driver's License Number": decoded.split("DAQ")[1].split("\n")[0].strip(),
        "Address": decoded.split("DAG")[1].split("\n")[0].strip(),
        "City": decoded.split("DAI")[1].split("\n")[0].strip(),
        "Province": decoded.split("DAJ")[1].split("\n")[0].strip(),
        "Postal Code": decoded.split("DAK")[1].split("\n")[0].strip(),
        "Height": decoded.split("DAU")[1].split("\n")[0].strip(),
        "Gender": "Male" if decoded.split("DBC")[1][0] == "1" else "Female",
        "Expiration Date": f"{decoded.split('DBA')[1][:4]}-{decoded.split('DBA')[1][4:6]}-{decoded.split('DBA')[1][6:]}",
        "Issue Date": f"{decoded.split('DBD')[1][:4]}-{decoded.split('DBD')[1][4:6]}-{decoded.split('DBD')[1][6:]}",
        "Country": "Canada",
        "Class": decoded.split("DCA")[1].split("\n")[0].strip(),
    }

    print(data)