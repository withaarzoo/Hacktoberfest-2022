# LANGUAGE: Python Language
# ENV: Terminal
# AUTHOR: KryPtoN
# GITHUB: https://github.com/kry9ton

class OpenSource():
    def __init__(self, name):
        self.name = name

    def name(self):
        return f"Helo {self.name}, welcome to opensource"

me = OpenSource("krypton")
print(me.name())