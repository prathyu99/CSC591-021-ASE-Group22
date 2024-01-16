import re
import sym
import num
class COLS:
    def __init__(self, row):
        x, y, allColumns = {}, {}, {}
        klass = ""
        col = ""
        for at, txt in row.cells.items():
            col = num.NUM(txt, at) if re.search("^[A-Z]", txt) else sym.SYM(txt, at)
            allColumns.append(col)
            if not re.search("X$", txt):
                if re.search("!$", txt):
                    klass = col
                (y if re.search("[!+-]$", txt) else x)[at] = col
        self.x = x
        self.y = y
        self.all = all
        self.klass = klass
        self.names = row.cells
    
    def add(self, row):
        for cols in [self.x, self.y]:
            for _, col in cols.items():
                col.add(row.cells[col.at])
        return row



