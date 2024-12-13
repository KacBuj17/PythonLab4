from collections import OrderedDict

ordered_dict = OrderedDict()

ordered_dict['a'] = 1
ordered_dict['c'] = 2
ordered_dict['b'] = 3
ordered_dict['d'] = 4

print("OrderedDict:")
for key, value in ordered_dict.items():
    print(f"{key}: {value}")

print("\nReversed OrderedDict:")
for key, value in reversed(ordered_dict.items()):
    print(f"{key}: {value}")
