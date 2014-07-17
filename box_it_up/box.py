
# coding: utf8
import sys

# '''Python class for formatting various kinds of table data into an ascii table.'''
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

    Table Types:
    SIMPLE (Default) - asterisks underline column headers
    OUTLINE          - single line blocks entire table & header: optional: HEADER_OFF
    OUTLINE_DBL      - double line blocks entire table & header w/ optional: HEADER_OFF

    Default
        #   TIME   RESULT
    ****** ****** ********
        1     2s    PASS
        2     2s    FAIL
        3     2s   ERROR
        4     2s    PASS
        5     2s    FAIL


    @TODO:
    * Add 'colspan' type capability
    """

    def __init__(self):

        self._box = ''

        # table char types
        self.HDR_NW = [ '.', u'┌', u'╔' ]
        self.HDR_N = [ '+', u'┬', u'╦' ]
        self.HDR_NW = [ '.', u'┐', u'╗' ]
        self.HDR_SW = [ '+', u'├', u'╠']
        self.HDR_S = [ '+', u'┼',  u'╬' ]
        self.HDR_SE = [ '+', u'┤',  u'╣' ]
        self.DATA_SW = [ '+', u'└',  u'╚' ]
        self.DATA_S = [ '+', u'┴',  u'╩' ]
        self.DATA_SE = [ '+', u'┘',  u'╝' ]
        self.HLINE = [ '-', u'─', u'═' ]
        self.VLINE = [ '|', u'│', u'║' ]

    @property
    def box(self):
        return self._box

    @box.setter
    def box(self, data):
        """Use box setter only for processing table data (rows x columns) in one fell swoop (vs. row-by-row)"""
        try:
            assert(self.is_tabular(data))
            self._box = data
            self._rows = len(data)
            self._cols = len(data[0])
        except Exception as e:
            print 'ERROR: Data is NOT tabular! (lists are not of same length)'
            sys.exit()

    def is_tabular(self, data):
        """Checks if data is tabular (each list in list must be of same length)"""
        lengths = [len(x) for x in data]
        return len(set(lengths))==1

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

    def box_it_new(self):

        for row in self._box:
            for i, col in enumerate(row):
                print '{} - {}'.format(row[i], i)



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
    print box.box_it(results, SIMPLE)
    # print box.box_it(results, OUTLINE)
    print box.box_it(results, OUTLINE_DBL)
    box.box = results
    box.box_it_new()

