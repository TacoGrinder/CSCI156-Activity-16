__author__ = 'Sean'


class Employee:
    pass

class EmployeeError(ValueError):
        pass

def inp(a):
    area, group, serial = a.split('-')
    t = area, group, serial
    q = t[0]+'-'+t[1]+'-'+t[2]
    if len(t) == 3:
        if t[2] == '':
            raise EmployeeError
        elif '666' in t[0]:
            raise EmployeeError
        elif len(t[0]) != 3:
            raise EmployeeError
        elif len(t[1]) != 2:
            raise EmployeeError
        elif len(t[2]) != 4:
            raise EmployeeError
        elif '000' in t[0]:
            raise EmployeeError
        elif '00' in t[1]:
            raise EmployeeError
        elif '0000' in t[2]:
            raise EmployeeError
        elif area + group + serial == '078' + '05' + '1120':
            raise EmployeeError
    area = int(area)
    group = int(group)
    serial = int(serial)
    if 900 <= area <= 999:
        raise EmployeeError
    else:
        print(q)

def ss():
    employee = Employee()
    employee.sn = input("Input Social Security Number, AAA-GG-SSSS").strip()
    try:
        inp(employee.sn)
    except EmployeeError:
        ss()
