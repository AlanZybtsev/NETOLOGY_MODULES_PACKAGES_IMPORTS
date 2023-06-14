import sys
import datetime

if __name__ == '__main__':
    salary_way = 'B:/_PYTHON_/НЕТОЛОГИЯ/pd-77/05_Профессиональная_работа_с_Python/01_Модули, пакеты, импорты в Python/ДЗ/application'
    sys.path.insert(1, salary_way)
    from salary import calculate_salary

    people_way = 'B:/_PYTHON_/НЕТОЛОГИЯ/pd-77/05_Профессиональная_работа_с_Python/01_Модули, пакеты, импорты в Python/ДЗ/application/db'
    sys.path.insert(1, people_way)
    import people

    now = datetime.datetime.now()
    print(f'Today\'s date - {now.date()}')

    # help('modules')