# Regular Expressions

`import re`

**Pattern** 
- is a raw string so it can not include special chars
- but can include the regex special chars

The _pattern_ is compiled by `re`

    pattern = re.compile(r'^#')
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)

`match` is a match object
You can get the re `group` by its index

    print(match.group(0))

Where 0 is the entire match
if the re has other groups defined by parens () then each group is the next index

    text = "The IP address is 192.168.1.3.
    pattern = re.compile(r'(\d+)\.(\d+)\.(\d+)\.(\d+)')
    matches = pattern.finditer(text)
    for m in matches:
        print(m.group(0))
        print(m.group(1))
        print(m.group(2))

    192.168.1.3
    192
    168

Or just get all the matches as a list

    matches = pattern.findall(text)

Get first match

    matches = pattern.search(text)

Ignore case

    pattern = re.compile(r'Start', re.IGNORECASE)
    pattern = re.compile(r'Start', re.I)
