from ascii_magic import AsciiArt, from_image, Back, Front
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

Convert Images to ASCII art.
    """

    print(ascmii_doc.__doc__)

def convert_to_ascii(img_path, **kwargs):
    try:
        art = AsciiArt.from_image(img_path)
        output = art.to_ascii(**kwargs)
        print(output)
    except FileNotFoundError:
        print(f"Error: Image file was not found at {img_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    

def main():
    parser = argparse.ArgumentParser(usage="ascmii image.png --color", description=ascmii_doc())
    parser.add_argument("image", help="Path to the input image file.")
    parser.add_argument("--width", type=int, default=120, help="Width of the output ASCII art (default: 120).")
    parser.add_argument("--color", action="store_true", help="Enable color output.")
    parser.add_argument("--output", help="Path to save the ASCII art to a file.")
    parser.add_argument("--char-set", default=None, help="Specify a character to use for the ASCII art.")
    parser.add_argument("--monochrome", action="store_true", help="Enable grayscale (monochrome) output.")
    parser.add_argument("--back", type=str, default=None, help="Background Color.")
    parser.add_argument("--front", type=str, default=None, help="Foreground Color.")

    args = parser.parse_args()

    kwargs = {
            'columns': args.width,
            'monochrome': args.monochrome,
            }

   
    if args.char_set:
        kwargs['char'] = args.char_set


    if args.color and args.monochrome:
        print("Error: Cannot use both --color and --monochrome options together.")
        sys.exit(1)

    if args.front:
        try:
            kwargs['front'] = Front[args.front.upper()]
        except KeyError:
            print("Error: Invalid Front Color.")
            sys.exit(1)
    
    if args.back:
        try:
            kwargs['back'] = Back[args.back.upper()]
        except KeyError:
            print("Error: Invalid Back Color.")
            sys.exit(1)


    ascii_art = AsciiArt.from_image(args.image).to_ascii(**kwargs)

    if args.output:
        try:
            with open(args.output, 'w') as f:
                f.write(ascii_art)
            print(f"ASCII art saved to {args.output}")
        except Exception as e:
            print(f"Error saving to file: {e}")
    else:
        print(ascii_art)

if __name__ == '__main__':
    main()
