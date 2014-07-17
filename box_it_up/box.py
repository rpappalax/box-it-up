
# coding: utf8

# '''Python class for formatting various kinds of table data into an ascii table.'''
SIMPLE = 1
OUTLINE = 2
OUTLINE_DBL = 0

class Box(object):
    """
    @TODO:
    * Add 'colspan' type capability
    """

    def __init__(self):

        self._box = ''
        self.HDR_TOP_LT = [ u'╔', '.', '┌' ]
        self.HDR_TOP_MD = [ u'╦', '+', '┬' ]
        self.HDR_TOP_RT = [ u'╗', '.', '┐']
        self.HDR_BOT_LT = [ u'╠', '+', '├']
        self.HDR_BOT_MD = [ u'╬', '+', '┼' ]
        self.HDR_BOT_RT = [ u'╣', '+', '┤' ]
        self.BOX_BOT_LT = [ u'╚', '+', '└' ]
        self.BOX_BOT_MD = [ u'╩', '+', '┴' ]
        self.BOX_BOT_RT = [ u'╝', '+', '┘' ]
        self.BAR_HRZ = [ u'═', '-', '─' ]
        self.BAR_VRT = [ u'║', '|', '│' ]


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

    def box_it(self, results, type=SIMPLE):
        """takes a list of lists (key, value pairs) and wraps them in a grid
        results = [
            [ 'AVG TEST DURATION', '2s' ],
            [ 'TEST RESULTS', 'PASS: 2, FAIL: 0, ERROR: 3' ],
            [ 'XXXXXXXXXXXXXXXXXXXXXXX', 'YYYYYYYYYY' ],
            [ 'AAA', 'BBBB' ]
        ] """
        spacer = '   '
        len_spacer = len(spacer)
        max_len_keys = max([ len(str(key)) for key, val  in results])
        results_reversed = [(t[1], t[0]) for t in results]
        max_len_vals = max([ len(str(val)) for val, key  in results_reversed])
        line_k= (max_len_keys + len_spacer) * self.BAR_HRZ[type]
        line_v= (len_spacer + max_len_vals + len_spacer) * self.BAR_HRZ[type]
        len_cell_k = max_len_keys + len_spacer
        # len_cell_v = max_len_vals + len_spacer
        i =0
        box = ''
        for k, v in results:
            spacer_k = (len_cell_k - len(k)) * ' '
            box +=  u'{}{}{}'.format(k + spacer_k, self.BAR_VRT[type], spacer + v) + '\n'
            if len(results) > 1 and i < len(results) - 1:
                box += u'{}{}{}'.format(line_k, self.HDR_BOT_MD[type], line_v) + '\n'
            i += 1
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
    # print box.get_box_specify(OUTLINE)
    print box.get_box_specify(OUTLINE_DBL)

    table_data = ''
    print box.get_box_no_outline(table_data)
    print box.get_box_outline(table_data)

    results = [
            [ 'AVG TEST DURATION', '2s' ],
            [ 'TEST RESULTS', 'PASS: 2, FAIL: 0, ERROR: 3' ],
            [ 'XXXXXXXXXXXXXXXXXXXXXXX', 'YYYYYYYYYY' ],
            [ 'AAA', 'BBBB' ]
    ]
    print box.box_it(results, SIMPLE)
    print box.box_it(results, OUTLINE_DBL)
        # ╚ ═ ╩ ═ ╝
        # ╔ ═ ╦ ═ ╗
        # ║
        # ╠ ═ ╬   ╣
        # ╚ ═ ╩ ═ ╝

