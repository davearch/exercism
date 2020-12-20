drops = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))

def convert(n):
    speak = [s for f,s in drops if n % f == 0]
    return "".join(speak) if speak else str(n)