from ascii_magic import AsciiArt, from_image, Back
import argparse
import sys

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

def convert_to_ascii(img, columns=100, width_ratio=4, 
                     monochrome=False, char=None, 
                     front=None, back=None, output_file=None, grayscale=False, saturation=None):
    art = AsciiArt.from_image(img)
    
    # apply greyscale
    if grayscale:
        art.grayscale()

    # apply saturation
    if saturation is not None:
        art.supply_saturation(saturation)

    output = art.to_ascii(columns=columns, width_ratio=width_ratio, 
                          monochrome=monochrome, char=char, front=front, back=back)


    if output_file:
        try:
            with open(output_file, 'w') as f:
                f.write(output)
            print(f"ASCII art saved to file {output_file}")
        except Exception as e:
            print(f"Error writing to file: {e}")
    else:
        print(output)

def main():
    parser = argparse.ArgumentParser(description="Convert images to ASCII art.")
    parser.add_argument("image", help="Path to input image.")
    parser.add_argument("--width", type=int, help="Width of th eoutput ASCII art.", default=100)
    parser.add_argument("--color", action="store_true", help="Enable color ouput.")
    parser.add_argument("--output", help="Path to save the ascii art to a file")
    parser.add_argument("--char-set", help="Character set to use for ASCII art (e.g, block).")
    parser.add_argument("--grayscale", action="store_true", help="Convert the image to grascale before generating ASCII art.")

    args = parser.parse_args()

    convert_to_ascii(
            args.image,
            columns=args.width,
            monochrome=not args.color,
            char=args.char_set,
            output_file=args.output,
            grayscale=args.grayscale)

if __name__ == '__main__':
    main()
