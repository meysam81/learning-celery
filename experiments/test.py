class SalaryError(Exception):
    pass


while True:
    try:
        salary = int(input("Please input your salary: "))
        print(salary)
        raise SalaryError("custom error")
    except ValueError:
        print('invalid input, try again...')
    except SalaryError as e:
        print(e)
        break
