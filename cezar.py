def cezar(text, krok):
        alf_UA = "абвгґдуєжзиіїйкльмншщпрстуфхцчшщьюяабвгґдуєжзиіїйкльмншщпрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWABCDEFGHIJKLMNOPQRSTUVW1234567890"
        step = krok
        message = text
        result = ""
        for i in message:
            cell = alf_UA.find(i)
            new_cell = cell + step
            if i in alf_UA:
                result += alf_UA[new_cell]
            else:
                result += i
        return result


print(cezar(input(), 1))

