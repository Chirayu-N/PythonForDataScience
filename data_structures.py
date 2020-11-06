# -*- coding: utf-8 -*-
"""Data Structures

# Tuple

*   A `tuple` is an ordered collection of elements enclosed in `()`
*   Tuples are immutable
"""

example_tuple = (1, 'hey', True)
example_tuple[0]

"""# List (array)

*   A `list` is an ordered collection of elements enclosed in `[]`
*   Lists are mutable
"""

example_list = [1, 'hey', True]

example_list[2] = False
example_list.append('New String')
example_list.pop()
example_list.append(['A list inside a list', True])

example_list

"""# Dictionary

*   A `dictionary` is an unordered collection of key-value pairs enclosed in `{}`
*   Dictionaries are mutable
"""

example_dictionary = {
    'fact' : True,
    'fake' : False
}

# example_dictionary.keys()
# example_dictionary.values()

example_dictionary['fact'] = False
example_dictionary

"""# Set

*   A `set` is an unordered collection of elements enclosed in `{}`
*   Duplicates are not allowed in sets
*   Sets are usually mutable
"""

example_set = {1, 'string', False}

duplicates = {1, 1, 1, 1, 2, 2, False, False, 'string', 'unique', 'string'}
print(f'This set does not have the duplicates: {duplicates}')

example_set.add('new element')
example_set.update([1, 2, 3, 'string', True])
print(example_set)
