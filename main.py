from PIL import Image


def main():
    try:
        print("trying")
        # Relative Path
        img = Image.open("testing.jpg")

        # Angle given
        img = img.rotate(180)

        # Saved in the same relative location
        img.save("rotated_picture.jpg")
    except IOError:
        print("ERROR")
        pass


if __name__ == "__main__":
    main()
