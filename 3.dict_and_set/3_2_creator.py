def get_creators(record: dict) -> list:
    match record:
        case {'type': "book", 'api' : 2, 'authors': [*names]}:
            return names
        case {'type': "book", 'api' : 1, 'author': name}:
            return [name]
        case {'type': "book"}:
            raise ValueError(f'Invalid book record: {record}')
        case {'type': "movie", 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid book record: {record!r}')    
        
        
        
b1 = dict(type="book", api=2, authors=["name1", "name2"])
print(get_creators(b1))
b2 = dict(type="book", api=1, author="name1")
print(get_creators(b2))
b3 = dict(type="book")
# print(get_creators(b3))
m1 = dict(type="movie", director="name3")
print(get_creators(m1))
# print(get_creators(dict(type="movie")))