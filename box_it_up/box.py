
# coding: utf8

# '''Python class for formatting various kinds of table data into an ascii table.'''
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

    def dummy(self):
        i = 1
        box = '{}{}{}{}{}'.format(
            self.HDR_TOP_LT[i],
            self.BAR_HRZ[i],
            self.HDR_TOP_MD[i],
            self.BAR_HRZ[i],
            self.HDR_TOP_RT[i]
        )
        print box
        box_dummy = """
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

        return box_dummy

if __name__ == '__main__':

    box = Box()
    print box.dummy()

        # ╚ ═ ╩ ═ ╝
        # ╔ ═ ╦ ═ ╗
        # ║
        # ╠ ═ ╬   ╣
        # ╚ ═ ╩ ═ ╝

