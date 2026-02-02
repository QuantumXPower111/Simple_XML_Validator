import sys

def determine_xml(xml):
    openings = []
    pos = 0
    while pos < len(xml):
        start = xml.find('<', pos)
        if start == -1:
            break  # No more tags
        # Find the closing '>' while handling quoted strings
        i = start + 1
        quote = None
        in_quote = False
        while i < len(xml):
            c = xml[i]
            if in_quote:
                if c == quote:
                    in_quote = False
            else:
                if c in ['"', "'"]:
                    quote = c
                    in_quote = True
                elif c == '>':
                    break
            i += 1
        if i >= len(xml) or xml[i] != '>':
            return False  # Unclosed tag
        end = i
        tag = xml[start + 1:end]  # Content between < and >
        is_closing = False
        if tag and tag[0] == '/':
            is_closing = True
            tag_name = tag[1:]
        else:
            tag_name = tag
        if is_closing:
            if not openings:
                return False  # No matching opening
            expected = openings.pop()
            if expected != tag_name:
                return False  # Mismatch
        else:
            openings.append(tag_name)
        pos = end + 1
    return len(openings) == 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid")
        sys.exit(1)
    xml = sys.argv[1]
    if determine_xml(xml):
        print("Valid")
    else:
        print("Invalid")