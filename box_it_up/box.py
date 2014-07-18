
# coding: utf8
import sys

# '''Python class for formatting various kinds of table data into an ascii table.'''
MINIMAL = 3
SIMPLE = 0
OUTLINE = 1
OUTLINE_DBL = 2

POS_NW = 0
POS_N = 1
POS_NE = 2
POS_W = 3
POS_E = 4
POS_SW = 5
POS_S = 6
POS_SE = 7

class Box(object):
    """
    Description:
    Each data cell is surrounded by six positions most easily represented by cardinal directions (see below)

    NW   N   NE
         |
    W -- X -- W
         |
    SW   S   SE

    Table Types (see: Examples/table_types.txt):
    SIMPLE (Default) - asterisks underline column headers
    OUTLINE          - single line blocks entire table & header: optional: HEADER_OFF
    OUTLINE_DBL      - double line blocks entire table & header w/ optional: HEADER_OFF


    @TODO:
    * Add simple means to specify column orientation
    * >> default: left-orientation all cols
    * Add 'colspan' type capability
    """

    def __init__(self):

        self._box = ''

        # table char types
        # corners
        self.HDR_NW = [ '.', u'┌', u'╔' ]
        self.HDR_NE = [ '.', u'┐', u'╗' ]
        self.DATA_SW = [ '+', u'└',  u'╚' ]
        self.DATA_SE = [ '+', u'┘',  u'╝' ]

        # middle
        self.HDR_N = [ '+', u'┬', u'╦' ]
        self.DATA_X = [ '+', u'┼',  u'╬' ]
        self.DATA_S = [ '+', u'┴',  u'╩' ]

        # sides
        self.DATA_W = [ '+', u'├', u'╠']
        self.DATA_E = [ '+', u'┤',  u'╣' ]
        self.HLINE = [ '-', u'─', u'═' ]
        self.VLINE = [ '|', u'│', u'║' ]

        self._col_orientations = []


    @property
    def box(self):
        return self._box

    @box.setter
    def box(self, data):
        """Use box setter only for processing table data (rows x columns) in one fell swoop (vs. row-by-row)"""
        try:
            assert(self.is_tabular(data))
            self._box = data
            self._cols = len(data[0])
            self._rows = len(data)

            # default: left-orientation
            for i in xrange(0, self._rows):
                self._col_orientations.append('<')
            self.max_col_lens = data
        except Exception as e:
            print 'ERROR: Data is NOT tabular! (lists are not of same length)'
            sys.exit()

    @property
    def max_col_lens(self):
        return self._max_col_lens

    @max_col_lens.setter
    def max_col_lens(self, table_data):
        self._max_col_lens = [max(len(str(x)) for x in line) for line in zip(*table_data)]

    @property
    def col_orientations(self):
        return self._col_orientations

    @col_orientations.setter
    def col_orientations(self, list_orientations):
        """optional parameter: set column orientations in a list
        default: all cols are left-oriented
        Example:
        list_orientations = [ '<', '<', '^', '>', '>' ]"""
        self._col_orientations = list_orientations

    def get_header_row(self, col, type=MINIMAL):
        this_row = ''
        # data = self.get_col_formatted(col)
        if self.is_col_first(col):
            this_row += self.HDR_NW[type]
        else:
            this_row += self.HDR_N[type]
        this_row += self.HLINE[type] * (self._max_col_lens[col] + 1)

        if self.is_col_last(col):
            this_row += self.HDR_NE[type]
        return this_row

    def get_data_row(self, col, data, type=MINIMAL):
        this_row = ''
        data = self.get_col_formatted(col, data)
        if self.is_col_first(col):
            this_row += '\n'
            this_row += self.DATA_W[type]
        else:
            this_row += self.DATA_X[type]

        this_row += str(data)
        if self.is_col_last(col):
            this_row += self.DATA_E[type]
        return this_row

    def get_footer_row(self, col, type=MINIMAL):
        this_row = ''
        if self.is_col_first(col):
            this_row += '\n'
            this_row += self.DATA_SW[type]
            for i in xrange(0, self._max_col_lens[col] + 1):
                this_row += self.HLINE[type]
        else:
            this_row += self.DATA_S[type]
            for i in xrange(0, self._max_col_lens[col] + 1):
                this_row += self.HLINE[type]

        if self.is_col_last(col):
            this_row += self.DATA_SE[type]
        return this_row

    def get_col_formatted(self, col, data=''):

        spacer_len = (self._max_col_lens[col] - len(str(data)))
        spacer = spacer_len * ' '
        if self._col_orientations[col] == '<':
            cell = ' {}{} '.format(data,spacer)
            # cell = ' ' + data + spacer
        elif self._col_orientations[col] == '>':
            # cell = spacer + data + ' '
            cell = ' {}{} '.format(spacer,data)
        else:
            spacer_len = spacer_len // 2
            print spacer_len
            spacer, remainder = divmod(spacer_len, 2)
            spacer = spacer_len * ' '
            extra = remainder * ' '
            # cell = spacer  + data + spacer
            cell = ' {}{}{} '.format(spacer,data,spacer,extra)

        return cell

    def box_it_new(self, type=MINIMAL):
        box = ''
        """
        To format each column we need a list containing:
        1) max str length of each column
        2) optional:  orientation of each column: <, >, ^ (default: <)
        """

        for row, row_list in enumerate(self._box):
            for col, data in enumerate(row_list):
                if self.is_header(row):
                    box += self.get_header_row(col, type)
                else:
                    box += self.get_data_row(col, data, type)
        for col, data in enumerate(row_list):
            box += self.get_footer_row(col, type)
        return box



    def is_tabular(self, data):
        """Checks if data is tabular (each list in list must be of same length)"""
        lengths = [len(x) for x in data]
        return len(set(lengths))==1

    def is_header(self, row_pos):
        return (row_pos == 0)

    def is_col_first(self, col_pos):
        return (col_pos == 0)

    def is_col_last(self, col_pos):
        return (self._cols - 1 == col_pos)

    def is_row_last(self, row_pos):
        return (self._rows - 1 == row_pos)

    def box_double(self, list_data, header=False):
        """Returns table data as double-bar formatted string table."""
        pass

    def get_box_specify(self, type = 'SIMPLE'):
        print self.HDR_NW[type]
        box = u'{}{}{}{}{}'.format(
            self.HDR_NW[type],
            self.HLINE[type],
            self.HDR_N[type],
            self.HLINE[type],
            self.HDR_NW[type]
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
        line_k= (max_len_keys + len_spacer) * self.HLINE[type]
        line_v= (len_spacer + max_len_vals + len_spacer) * self.HLINE[type]
        len_cell_k = max_len_keys + len_spacer
        # len_cell_v = max_len_vals + len_spacer
        i =0
        box = ''
        for k, v in results:
            spacer_k = (len_cell_k - len(k)) * ' '
            box +=  u'{}{}{}'.format(k + spacer_k, self.VLINE[type], spacer + v) + '\n'
            if len(results) > 1 and i < len(results) - 1:
                box += u'{}{}{}'.format(line_k, self.HDR_S[type], line_v) + '\n'
            i += 1
        return box





if __name__ == '__main__':

    box = Box()
    # print box.get_box_specify(SIMPLE)
    # print box.get_box_specify(OUTLINE)
    # print box.get_box_specify(OUTLINE_DBL)

    # results = [
    #         [ 'AVG TEST DURATION', '2s' ],
    #         [ 'TEST RESULTS', 'PASS: 2, FAIL: 0, ERROR: 3' ],
    #         [ 'XXXXXXXXXXXXXXXXXXXXXXX', 'YYYYYYYYYY' ],
    #         [ 'AAA', 'BBBB' ]
    # ]
    results = [
            ( 'AVG TEST DURATION', '2s' ),
            ( 'TEST RESULTS', 'PASS: 2, FAIL: 0, ERROR: 3' ),
            ( 'XXXXXXXXXXXXXXXXXXXXXXX', 'YYYYYYYYYY' ),
            ( 'AAA', 'BBBB')
    ]

    results = [
        [ 'aaa','bbb','ccc','dddd','eeee'],
        [ 'ffff','gggg','hhh','iiiiiiiiiiiii','jjjjjj'],
        [ 'kk','lllllll','m','nnnnnn','oooooo'],
        [ 'ppppp','qq','rrr','sssss','t'],
        [ 'u','vvv','ww','xxx','yyyyyyyyyyyyyyyy']
    ]
    box.col_orientations = [ '>', '<', '^', '>', '>']

    # print box.box_it(results, SIMPLE)
    # print box.box_it(results, OUTLINE)
    # print box.box_it(results, OUTLINE_DBL)
    box.box = results
    print box.box_it_new(OUTLINE_DBL)
    print box.box_it_new(OUTLINE)

