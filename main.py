from os import listdir

from PIL import Image, UnidentifiedImageError

input_path = './inputs'
output_path = './outputs'


def main():
    inputs = [file for file in listdir(input_path)]

    if len(inputs) == 0:
        print('Not exist files in inputs.')
        return

    # size = input_size()
    width = input_width()

    format_to = 'png'

    for file in inputs:
        split_file_name = file.split(".")
        file_name = ''.join(split_file_name[:-1])
        extension = split_file_name[-1]

        convert_image(file_name, extension, format_to, width)


# 将来的にはこっちだけ使いたい
# def input_size() -> tuple[int, int]:
#     print('width: ', end='')
#     width = int(input())
#
#     print('height: ', end='')
#     height = int(input())
#
#     return width, height


def input_width() -> int:
    print('width: ', end='')
    width = int(input())

    return width


# todo(kondo): svgも変換したい
def convert_image(
    file_name: str,
    extension: str,
    format_to: str,
    width: int = None,
    height: int = None
):
    print(f'Start to convert {input_path}/{file_name}.{extension}.')

    try:
        img = Image.open(f'{input_path}/{file_name}.{extension}')
        img_width, img_height = img.size

        if width is not None and height is not None:
            resized_img = img.resize((width, height))

        elif width is not None:
            height = round(img_height * (width / img_width))
            resized_img = img.resize((width, height))

        elif height is not None:
            width = round(img_width * (height / img_height))
            resized_img = img.resize((width, height))

        else:
            raise ValueError('Both width and height are None.')

        resized_img.save(f'{output_path}/{file_name}.{format_to}')
    except UnidentifiedImageError as e:
        print(e)
        return

    print(
        f'Finish to convert and saved {output_path}/{file_name}.{format_to}.'
    )


if __name__ == '__main__':
    main()
