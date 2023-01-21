from menu import Menu
import function as fn
import ConvertTo as ct


if __name__ == "__main__":
    # основной блок
    menuitems = [
        ("1", "Вывод автобусов", fn.print_bus),
        ("2", "Добавление автобуса", fn.add_bus),
        ("3", "Вывод водителей", fn.print_drivers),
        ("4", "Добавление водителей", fn.add_driver),
        ("5", "Вывод маршрута", fn.print_routes),
        ("6", "Добавление маршрута", fn.add_route),
        ("7", "Конвертировать данные в другой формат", ct.letsConvertIt),
        ("8", "Выход", lambda: exit())]

    menu = Menu(menuitems)
    menu.run()

