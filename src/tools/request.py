import tkinter as tk

from src.config.output_mess import output_msg


class RequestUser:

    @staticmethod
    def get_max_screen_size():
        root = tk.Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.destroy()

        return width, height

    @staticmethod
    def get_screen_size():
        size = RequestUser.get_max_screen_size()

        print(output_msg.get('screen_size'))

        while True:
            screen_width = int(input(f"Введите ширину окна (максимум {size[0]}): "))
            screen_height = int(input(f"Введите высоту окна (максимум {size[1]}): "))

            if screen_width > size[0] or screen_height > size[1]:
                print("Размеры окна превышают разрешение экрана. Пожалуйста, введите меньшие значения.")
                continue

            return screen_width, screen_height


