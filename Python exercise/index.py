#index operator [] = access to the sequence of elements it can be( string, list and tuples)
name="nool angelo"

if (name[0].islower() or name[6].islower()):
    name = name.capitalize()

last_name =name[:4].upper()
first_name = name[5:].upper()
full_name = first_name +" " + last_name

print(full_name)