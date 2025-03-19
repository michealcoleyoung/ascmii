from ascii_magic import AsciiArt, from_image, Back

# my_art = AsciiArt.from_image('cross-surreal.jpg')
# my_art.to_terminal()

def ascmii_doc():
    """
       d8888  .d8888b.   .d8888b.  888b     d888 8888888 8888888 
      d88888 d88P  Y88b d88P  Y88b 8888b   d8888   888     888   
     d88P888 Y88b.      888    888 88888b.d88888   888     888   
    d88P 888  "Y888b.   888        888Y88888P888   888     888   
   d88P  888     "Y88b. 888        888 Y888P 888   888     888   
  d88P   888       "888 888    888 888  Y8P  888   888     888   
 d8888888888 Y88b  d88P Y88b  d88P 888   "   888   888     888   
d88P     888  "Y8888P"   "Y8888P"  888       888 8888888 8888888 
    """
    print(ascmii_doc.__doc__)

def convert_to_ascii(img, columns=100, width_ratio=4, monochrome=False, char=None, front=None, back=None):
    art = AsciiArt.from_image(img)
    output = art.to_ascii()
    print(output)

def main():
    ascmii_doc()
    image = input("Enter the image that you want to convert: ")
    convert_to_ascii(image)

if __name__ == '__main__':
    main()
