import os
import sys
import cv2
import matplotlib.pyplot as plt


READ_PATH = "Files"
SAVE_PATH = "Processed"
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)


def show(image, cmap: str = "gnuplot2") -> None:
    plt.figure()
    plt.imshow(image, cmap=cmap)
    plt.axis("off")
    figmanager = plt.get_current_fig_manager()
    figmanager.window.state("zoomed")
    plt.show()


def run():
    args_1: tuple = ("--file", "-f")
    args_2: tuple = ("--width", "-w")
    args_3: tuple = ("--height", "-h")
    args_4: tuple = ("--save", "-s")

    filename: str = None
    width: int = None
    height: int = None
    save: bool = False

    if args_1[0] in sys.argv: filename = sys.argv[sys.argv.index(args_1[0]) + 1]
    if args_1[1] in sys.argv: filename = sys.argv[sys.argv.index(args_1[1]) + 1]

    if args_2[0] in sys.argv: width = int(sys.argv[sys.argv.index(args_2[0]) + 1])
    if args_2[1] in sys.argv: width = int(sys.argv[sys.argv.index(args_2[1]) + 1])

    if args_3[0] in sys.argv: height = int(sys.argv[sys.argv.index(args_3[0]) + 1])
    if args_3[1] in sys.argv: height = int(sys.argv[sys.argv.index(args_3[1]) + 1])

    if args_4[0] in sys.argv or args_4[1] in sys.argv: save = True

    assert filename is not None, "Enter an argument for --file | -f"
    assert filename in os.listdir(READ_PATH), "File Not Found"
    
    image = cv2.imread(os.path.join(READ_PATH, filename))

    if isinstance(width, int) and height is None:
        h, _, _ = image.shape
        image = cv2.resize(src=image, dsize=(width, h), interpolation=cv2.INTER_LINEAR)

    if width is None and isinstance(height, int):
        _, w, _ = image.shape
        image = cv2.resize(src=image, dsize=(w, height), interpolation=cv2.INTER_LINEAR)

    if isinstance(width, int) and isinstance(height, int):
        image = cv2.resize(src=image, dsize=(width, height), interpolation=cv2.INTER_LINEAR)

    if save:
        cv2.imwrite(os.path.join(SAVE_PATH, filename.split(".")[0] + " - Resized.jpg"), image)
    else:
        show(cv2.cvtColor(src=image, code=cv2.COLOR_BGR2RGB))
