def calculate_physical_address(page_number, page_size, offset):
    return (page_number * page_size) + offset


physical_address = calculate_physical_address(3, 2, 8)
print(physical_address)