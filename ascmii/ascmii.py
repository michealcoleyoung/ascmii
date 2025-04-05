from ascii_magic import AsciiArt, from_image, Back, Front
import argparse
import sys

# my_art = AsciiArt.from_image('cross-surreal.jpg')
# my_art.to_terminal()
# my_art = AsciiArt.from_image('cross-surreal.jpg')
# print(my_art.to_html_file('ascii_art.html', columns=200, width_ratio=2))

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
╭───────────────────────────────────────────────────────────────╮
│                  Convert images to ASCII art                  │
╰───────────────────────────────────────────────────────────────╯
    """

    print(ascmii_doc.__doc__)

def convert_to_ascii(img_path, **kwargs):
    art = AsciiArt.from_image(img_path)
    output = art.to_ascii(**kwargs)
    print(output)
 
def convert_to_html(img_path, **kwargs):
    art = AsciiArt.from_image(img_path)
    output = art.to_html_file('art_html_test.html', columns=200, width_ratio=2)
    print(output)
    
    if output:
        print("HTML file was successfully created")

   
def convert_to_file(img_path, **kwargs):
    pass


"""
REFERENCE FOR THE TO_ASCII OBJECT
AsciiArt.to_ascii(
    columns: int = 120,
    width_ratio: float = 2.2,
    monochrome: bool = False,
    char: Optional[str],
    front: Optional[Front],
    back: Optional[Back]
) -> str
"""


def main():
    parser = argparse.ArgumentParser(usage='ascmii image.png --color', description=ascmii_doc())
    parser.add_argument('image', help='Path to the input image file')
    parser.add_argument('--columns', type=int, default=120, help='The number of characters per row, more columns = wider art')
    parser.add_argument('--width', type=float, default=2.2, help='Width of the output ASCII art (default: 2.2)')
    parser.add_argument('--monochrome', action='store_true', help='Sets ASCII art to gray')
    parser.add_argument('--char', type=str, help='Specify a character to use for the ASCII art')
    # front
    # back
    args = parser.parse_args()

    kwargs = {}

    if args.columns:
        kwargs['columns'] = args.columns
    if args.width:
        kwargs['width_ratio'] = args.width
    if args.monochrome:
        kwargs['monochrome'] = args.monochrome
    if args.char:
        kwargs['char'] = args.char
            
    convert_to_ascii(args.image, **kwargs)

    
    
if __name__ == '__main__':
    main()
