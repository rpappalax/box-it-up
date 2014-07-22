box-it-up
=========

Python class for formatting various kinds of table data into an ascii table.


## Features
- Provides ASCII table formatting for tabular list data  
- Table Types (see: [Examples/table_types.txt](https://github.com/rpappalax/box-it-up/blob/master/Examples/table_types.txt):  
  * MINIMAL          - asterisks underline column headers, no column dividers, no outline  
  * SIMPLE (Default) - single line header and column dividers, no outline  
  * SIMPLE_OUTLINE   - single line header, column dividers & outline  
  * OUTLINE          - single line header, column dividers & outline (extended ascii connectors)  
  * OUTLINE_DBL      - double line header, column dividers & outline (extended ascii connectors)  

- Examples
  * To see examples in action simply run `$ python box_it_up.py`

## Installation
- `$ pip install box-it-up`

## Usage

### Example \#1 
- uses column headers
- pass in data and settings as init args 
- demonstrate different box_types
- optional: define and pass in field orientations as a list
  (default: left-orientation)
```
from box_it_up import Box

test_results = [
    [ 'aaa','bbb','ccc','dddd','eeee'],
    [ 'ffff','gggg','hhh','iiiiiiiiiiiii','jjjjjj'],
    [ 'kk','lllllll','m','nnnnnn','oooooo'],
    [ 'ppppp','qq','rrrr','sssss','t'],
    [ 'u','vvv','ww','xxx','yyyyyyyyyyyyyyyy']
]
orientations = [ '>', '<', '^', '>', '>']

# input params: we can pass them all in at once
box = Box(table_data=test_results, type='OUTLINE', header=True, col_orientations=orientations)

# box.table_data = test_results
box.box_type = 'MINIMAL'
print box.box_it()
box.box_type = 'SIMPLE'
print box.box_it()
box.box_type = 'SIMPLE_OUTLINE'
print box.box_it()
box.box_type = 'OUTLINE'
print box.box_it()
box.box_type = 'OUTLINE_DBL'
print box.box_it()
```

### Example \#2 
- left column labels
- no header
- declare class & set data & settings afterwards
- demonstrate different box_types

```
from box_it_up import Box 

box = Box()
test_results = [
    ( 'AVG TEST DURATION', '2s' ),
    ( 'TEST RESULTS', 'PASS: 2, FAIL: 0, ERROR: 3' ),
    ( 'MORE RESULTS', 'Yes!!!' ),
    ( 'EVEN MORE RESULTS', 'No!!!')
]
box.table_data = test_results
box.col_orientations = [ '<', '<' ]
box.header = False
box.box_type = 'SIMPLE_OUTLINE'
print box.box_it()
box.box_type = 'OUTLINE_DBL'
print box.box_it()
```
