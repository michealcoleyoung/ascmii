from ascii_magic import AsciiArt, from_image

# my_art = AsciiArt.from_image('cross-surreal.jpg')
# my_art.to_terminal()

def convert_to_ascii(img):
    AsciiArt.from_image(img).to_terminal()
    
def main():
    image = input("Enter the image that you want to convert: ")
    convert_to_ascii(image)



if __name__ == '__main__':
    main()
