from rembg import remove
from PIL import Image
from pathlib import Path

list_file_permission = ['*.png', '*.jpeg', '*.jpg']


def path_files():
    """
    Записываем пути к файлам в лист all_files.

    :return:
    """

    all_files = []

    for permission in list_file_permission:
        all_files.extend(
            Path('C:/programing/Python/1_skript_my/My_project/Parsing/background_removal/image_file').glob(permission))

    return all_files


# def name_files(list_files):
#     """
#     Получаем имена новых файлов.
#
#     :return:
#     """
#
#     for elem in list_files:
#         input_path = Path(elem)
#         file_name = input_path.stem
#
#         output_path = f'C:/programing/Python/1_skript_my/My_project/Parsing/background_removal/processed_images/{file_name}_output.png'


def remove_bg(list_files):
    """
    Функция удаляет фон на изображении.
    :return:
    """

    for index, elem in enumerate(list_files):
        input_path = Path(elem)
        file_name = input_path.stem

        output_path = f'C:/programing/Python/1_skript_my/My_project/Parsing/background_removal/processed_images/{file_name}_output.png'

        input_img = Image.open(input_path)
        output_img = remove(input_img)
        output_img.save(output_path)

        print(f'Completed: {index + 1}/{len(list_files)}')


def main():
    """
    старт
    :return:
    """

    a = path_files()
    remove_bg(a)


if __name__ == '__main__':
    main()
