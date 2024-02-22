class DataProcessor:
    def __init__(self):
        pass

    def tuple_operations(self):
        # Tuple demonstration
        my_tuple = (3, 1, 5, 2, 4)
        sorted_tuple = sorted(my_tuple)
        print("Sorted Tuple:", sorted_tuple)

    def list_operations(self):
        # List demonstration
        my_list = [3, 1, 5, 2, 4]
        my_list.append(6)
        print("Appended List:", my_list)
        my_list.sort()
        print("Sorted List:", my_list)

    def dictionary_operations(self):
        # Dictionary demonstration
        my_dict = {'a': 1, 'b': 2, 'c': 3}
        my_dict['d'] = 4  # Adding a new key-value pair
        print("Updated Dictionary:", my_dict)
        del my_dict['b']  # Removing a key-value pair
        print("Dictionary after removing 'b':", my_dict)

    def set_operations(self):
        # Set demonstration
        my_set = {3, 1, 5, 2, 4}
        my_set.add(6)  # Adding an element to the set
        print("Updated Set:", my_set)
        my_set.remove(3)  # Removing an element from the set
        print("Set after removing 3:", my_set)

# Test the functionality
if __name__ == "__main__":
    processor = DataProcessor()
    processor.tuple_operations()
    processor.list_operations()
    processor.dictionary_operations()
    processor.set_operations()