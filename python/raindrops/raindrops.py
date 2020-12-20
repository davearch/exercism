def convert(number):
    result = ""
    sounds = {3:'Pling', 5:'Plang', 7:'Plong'}
    for num,sound in sounds.items():
        if number % num == 0:
            result += sound
    if not result: return str(number)
    return result