from datetime import datetime

log_txt = 'log.txt'


def logger(log_path):
    def _logger(function):
        def new_function(*args, **kwargs):
            result = function(*args, **kwargs)
            log_string = f"Функция: {function.__name__}. Вызвана: {datetime.today()}. Аргументы: {args}, {kwargs}, " \
                         f"Результат действия: {result}"
            with open(log_path, 'a', encoding='utf-8') as f:
                f.write(log_string + '\n')
                print('Информация была записана в', log_path)
            return result
        return new_function
    return _logger


@logger(log_txt)
def operation_2(x, y):
    return x * y


if __name__ == '__main__':
    operation_2(66, 6)
