from os import listdir

from PIL import Image, UnidentifiedImageError

input_path = './inputs'
output_path = './outputs'


def main():
    inputs = [file for file in listdir(input_path)]

    if len(inputs) == 0:
        print('Not exist files in inputs.')
        return

    size = input_size()

    for file in inputs:
        split_file_name = file.split(".")
        file_name = ''.join(split_file_name[:-1])
        extension = split_file_name[-1]

        format_to = 'png'

        convert_image(file_name, extension, format_to, size)


def input_size() -> tuple[int, int]:
    print('width: ', end='')
    width = int(input())

    print('height: ', end='')
    height = int(input())

    return width, height


# todo(kondo): svgも変換したい
def convert_image(
    file_name: str,
    extension: str,
    format_to: str,
    size: tuple[int, int]
):
    print(f'Start to convert {input_path}/{file_name}.{extension}.')

    try:
        img = Image.open(f'{input_path}/{file_name}.{extension}')
        resized_img = img.resize(size)
        resized_img.save(f'{output_path}/{file_name}.{format_to}')
    except UnidentifiedImageError as e:
        print(e)
        return

    print(
        f'Finish to convert and saved {output_path}/{file_name}.{format_to}.')


if __name__ == '__main__':
    main()
