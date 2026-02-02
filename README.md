```markdown
# XML Validator

A lightweight Python script that validates XML structure by checking for proper tag matching, nesting, and attribute handling without using external libraries.

## Features

- ✅ **No dependencies** - Pure Python, no external libraries
- 🔍 **Attribute-aware** - Handles quoted attributes with special characters
- 📏 **Stack-based validation** - Ensures proper tag nesting
- ⚡ **Fast** - Simple string parsing algorithm
- 🛡️ **Error detection** - Identifies mismatched or unclosed tags

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/xml-validator.git
cd xml-validator

# No installation required - just run the script
```

## Usage

### Command Line
```bash
# Basic validation
python validator.py "<root><tag>content</tag></root>"

# With attributes
python validator.py '<note to="john"><message>hello</message></note>'
```

### Python Module
```python
from validator import determine_xml

# Validate XML string
xml_string = '<root><item>test</item></root>'
if determine_xml(xml_string):
    print("Valid XML")
else:
    print("Invalid XML")
```

## Examples

| XML Input | Result | Reason |
|-----------|--------|--------|
| `<root><tag>text</tag></root>` | ✅ **Valid** | Proper nesting |
| `<open><mismatch></different>` | ❌ **Invalid** | Tag mismatch |
| `<tag attr=">">text</tag attr=">">` | ✅ **Valid** | Matching attributes |
| `<tag attr=">">text</tag attr="<">` | ❌ **Invalid** | Attribute mismatch |
| `<root>text only</root>` | ✅ **Valid** | Text content |
| `<unclosed>` | ❌ **Invalid** | Missing closing tag |

## How It Works

The validator uses a simple stack-based algorithm:

1. **Parse**: Find each `<` and `>` pair while skipping quoted content
2. **Extract**: Get tag content between `<` and `>`
3. **Validate**: Push opening tags onto stack, pop when closing tag matches
4. **Check**: Ensure stack is empty at the end

### Key Logic
```python
# Handle quoted attributes (critical for XML validation)
if c in ['"', "'"]:
    quote = c
    in_quote = True
elif c == '>' and not in_quote:
    break  # Found end of tag
```

## Limitations

- ❌ No XML declaration support (`<?xml?>`)
- ❌ No comment handling (`<!-- comment -->`)
- ❌ No CDATA sections
- ❌ No entity references (`&amp;`, `&lt;`, etc.)
- ❌ Self-closing tags (`<tag/>`) require closing tag

## Testing

Run the included test suite:
```bash
python test_validator.py
```

Or test manually:
```bash
python validator.py "<root><child>test</child></root>"
# Output: Valid
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## License

MIT License - See LICENSE file for details.
```
