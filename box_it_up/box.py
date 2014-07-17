
# coding: utf8

# '''Python class for formatting various kinds of table data into an ascii table.'''
SIMPLE = 0
OUTLINE = 1
OUTLINE_DBL = 2

class Box(object):
    """
    @TODO:
    * Add 'colspan' type capability
    """

    def __init__(self):
        self._box = ''
        self.HDR_TOP_LT = [ u'╔', '.' ]
        self.HDR_TOP_MD = [ u'╦', '+' ]
        self.HDR_TOP_RT = [ u'╗', '.']

        self.HDR_BOT_LT = [ u'╠', '+' ]
        self.HDR_BOT_MD = [ u'╬', '+' ]
        self.HDR_BOT_RT = [ u'╣', '+' ]

        self.BOX_BOT_LT = [ u'╚', '+' ]
        self.BOX_BOT_MD = [ u'╩', '+' ]
        self.BOX_BOT_RT = [ u'╝', '+' ]
        self.BAR_HRZ = [ u'═', '-' ]
        self.BAR_VRT = [ u'║', '|' ]


    @property
    def box(self):
        return self._box

    @box.setter
    def box(self, table_data):
        """Use box setter only for processing table data (rows x columns) in one fell swoop (vs. row-by-row)"""
        self._box = table_data

    def box_double(self, list_data, header=False):
        """Returns table data as double-bar formatted string table."""
        pass

    def get_box_specify(self, type = 'SIMPLE'):
        print self.HDR_TOP_RT[type]
        box = u'{}{}{}{}{}'.format(
            self.HDR_TOP_LT[type],
            self.BAR_HRZ[type],
            self.HDR_TOP_MD[type],
            self.BAR_HRZ[type],
            self.HDR_TOP_RT[type]
        )
        return box

    def get_box_outline(self, data):
        box = """
        .------------------------------.
        |            Basket            |
        +----+-----------------+-------+
        | Id | Name            | Price |
        +----+-----------------+-------+
        |  1 | Dummy product 1 |  24.4 |
        |  2 | Dummy product 2 |  21.2 |
        |  3 | Dummy product 3 |  12.3 |
        +----+-----------------+-------+
        |    | Total           |  57.9 |
        '----+-----------------+-------'"""
        return box

    def get_box_no_outline(self, data):
        box = """
         Row  | Name     | Year   | Priority
        ------------------------------------
         1    | Cat      | 1998   | 1
         2    | Fish     | 1998   | 2
         3    | Dog      | 1999   | 1
         4    | Aardvark | 2000   | 1
         5    | Wallaby  | 2000   | 1
         6    | Zebra    | 2001   | 3
        """
        return box

if __name__ == '__main__':

    box = Box()
    print box.get_box_specify(SIMPLE)
    print box.get_box_specify(OUTLINE)
    # print box.get_box_specify(OUTLINE_DBL)

    table_data = ''
    print box.get_box_no_outline(table_data)
    print box.get_box_outline(table_data)
        # ╚ ═ ╩ ═ ╝
        # ╔ ═ ╦ ═ ╗
        # ║
        # ╠ ═ ╬   ╣
        # ╚ ═ ╩ ═ ╝

