# Домашняя работа по уроку "Пространство имен."

def test_function():
    print("Функция test_function()")
    def inner_function():
        print("Функция inner_function()")
        print("Завершение работы inner_function()")


    inner_function()
    print("Завершение работы test_function()")


test_function()

# не вызывается в данном пространстве имен при раскомментирование подсвечивается как ошибка
#inner_function()





