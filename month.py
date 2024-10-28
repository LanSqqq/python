def month(num,lang):
    rus=('Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь')
    eng==('January', 'February','March','April','May','June','Julay','August','September','October','November','December')
    if lang==ru:
        return rus[num-1]
    else:
        return eng[num-1]
print(month(12,"ru"))
print(month(12,"ru"))