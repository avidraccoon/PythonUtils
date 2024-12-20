import re

def lmap(func, iterable):
    return list(map(func, iterable))



class Scanner:

    int_pattern = "\d+"
    float_pattern = "\d+(\.\d*){0,1}"
    next_line_pattern = ".*?\n"

    def __init__(self, text):
        self.text = text

    def nextInt(self):
        match = re.search(self.int_pattern, self.text)
        if match:
            self.text = self.text[match.span(0)[1]:]
            return int(match.group(0))
        return 0

    def nextFloat(self):
        match = re.search(self.float_pattern, self.text)
        if match:
            self.text = self.text[match.span(0)[1]:]
            return float(match.group(0))
        return 0.0

    def nextLine(self):
        match = re.search(self.next_line_pattern, self.text)
        if match:
            self.text = self.text[match.span(0)[1]:]
            return match.group(0)[:-1]
        return 0.0

scan = Scanner("""sdf453sdfsdf435543
               dfg34.35434fds""")
print(scan.nextInt())
print(scan.nextLine())
print(scan.nextFloat())

