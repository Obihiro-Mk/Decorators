from datetime import datetime

log_txt = 'log.txt'


def logger(function):
    def new_function(*args, **kwargs):
        result = function(*args, **kwargs)
        log_string = f"Функция: {function.__name__}. Вызвана: {datetime.today()}. Аргументы: {args}, {kwargs}, " \
                     f"Результат действия: {result}"
        with open(log_txt, 'a', encoding='utf-8') as f:
            f.write(log_string + '\n')
            print('Информация была записана в', log_txt)
        return result
    return new_function


@logger
def operation(x, y):
    return x + y


if __name__ == '__main__':
    operation(54353, 2345)
