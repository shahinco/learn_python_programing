class DriverException(Exception):
    pass

people = [('James', 17), ('Kirik', 9), ('Lars', 13), ('Robert', 8)]
driver = None

for person,age in people:
    if age >= 18:
        driver = (people, age)
        break

if driver is None:
    raise DriverException('Driver not found.')
