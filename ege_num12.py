def main():
    st = "5" * 62 # Создае строку заданую в условии
    while "333" in st or "555" in st: # Пока нашлось
        if "555" in st:
            st = st.replace("555", "3", 1)# Заменяем "1111" на "7" 1 раз (ЭТО ВАЖНО)
        else:
            st = st.replace("333", "5", 1)# Заменяем "77" на "1" 1 раз (ЭТО ВАЖНО)
    print(st) # Выводим строку получивштиеся после прохода через цикл


if __name__ == '__main__':
    main()
