import os
import sys
import cv2


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH  = os.path.join(BASE_PATH, "input")
OUTPUT_PATH = os.path.join(BASE_PATH, "output")

if not os.path.exists(OUTPUT_PATH): os.makedirs(OUTPUT_PATH)


def breaker(num: int = 50, char: str = "*") -> None:
    print("\n" + num*char + "\n")


def main():
    args_1: tuple = ("--file", "-f")
    args_2: tuple = ("--width", "-w")
    args_3: tuple = ("--height", "-h")

    filename: str = "Test_1.jpg"
    width: int = None
    height: int = None

    if args_1[0] in sys.argv: filename = sys.argv[sys.argv.index(args_1[0]) + 1]
    if args_1[1] in sys.argv: filename = sys.argv[sys.argv.index(args_1[1]) + 1]

    if args_2[0] in sys.argv: width = int(sys.argv[sys.argv.index(args_2[0]) + 1])
    if args_2[1] in sys.argv: width = int(sys.argv[sys.argv.index(args_2[1]) + 1])

    if args_3[0] in sys.argv: height = int(sys.argv[sys.argv.index(args_3[0]) + 1])
    if args_3[1] in sys.argv: height = int(sys.argv[sys.argv.index(args_3[1]) + 1])

    assert filename in os.listdir(INPUT_PATH), "File Not Found"

    image = cv2.imread(os.path.join(INPUT_PATH, filename))

    if isinstance(width, int) and height is None:
        h, _, _ = image.shape
        image = cv2.resize(src=image, dsize=(width, h), interpolation=cv2.INTER_LINEAR)

    if width is None and isinstance(height, int):
        _, w, _ = image.shape
        image = cv2.resize(src=image, dsize=(w, height), interpolation=cv2.INTER_LINEAR)

    if isinstance(width, int) and isinstance(height, int): 
        image = cv2.resize(src=image, dsize=(width, height), interpolation=cv2.INTER_LINEAR)

    cv2.imwrite(os.path.join(OUTPUT_PATH, filename.split(".")[0] + " - Resized.jpg"), image)


if __name__ == "__main__":
    sys.exit(main() or 0)
