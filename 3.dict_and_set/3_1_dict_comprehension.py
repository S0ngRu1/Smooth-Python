dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (1, 'United States'),
    (64, 'New Zealand'),
    (7, 'Russia'),
    (27, 'South Africa'),
]

country_dial = {country: code for code, country in dial_codes}
print(country_dial)

country_dial1 = {code : country.upper() for code, country in dial_codes}
print(country_dial1)

country_dial2 = {code : country.upper() for code, country in sorted(dial_codes) if code < 70}
print(country_dial2)