import re


CODE_PATTERN = re.compile(r"(?<=(?:[ |,|.|:|;|\n|\t|<p>]))`(?=\S)(.+?)(?<=\S)`(?=(?:[ ,.:;\n\t<\/p>]|$))")
BOLD_PATTERN = re.compile(r"(?<=(?:[ |,|.|:|;|\n|\t|<p>|]))\*\*(?=\S)(.+?)(?<=\S)\*\*(?=(?:[ ,.:;\n\t<\/p>]|$))")
ITALIC_PATTERN = re.compile(r"(?<=(?:[ |,|.|:|;|\n|\t|<p>]))_(?=\S)(.+?)(?<=\S)_(?=(?:[ ,.:;\n\t<\/p>]|$))")

CODE_PATTERN_START_OF_LINE = re.compile(r"^`(?=\S)(.+?)(?<=\S)`(?=(?:[ ,.:;\n\t<\/p>]|$))")
BOLD_PATTERN_START_OF_LINE = re.compile(r"^(\*\*)(?=\S)(.+?)(?<=\S)\*\*(?=(?:[ ,.:;\n\t<\/p>]|$))")
ITALIC_PATTERN_START_OF_LINE = re.compile(r"^_(?=\S)(.+?)(?<=\S)_(?=(?:[ ,.:;\n\t<\/p>]|$))")

OPENING_STARS_PATTERN = re.compile(r"(?<=(?:[ |,|.|:|;|\n|\t]))\*\*(?=\S)(.+?)(?=(?:[ ,.:;\n\t<\/p>]|$))")
CLOSED_STARS_PATTERN = re.compile(r"(?<=(?:[ |,|.|:|;|\n|\t|<p>]))(.+?)(?<=\S)\*\*(?=(?:[ ,.:;\n\t<\/p>]|$))")

OPENING_UNDERSCORE_PATTERN = re.compile(r"(?<=(?:[ |,|.|:|;|\n|\t]))_(?=\S)(.+?)(?=(?:[ ,.:;\n\t<\/p>]|$))")
CLOSED_UNDERSCORE_PATTERN = re.compile(r"(?<=(?:[ |,|.|:|;|\n|\t|<p>]))(.+?)(?<=\S)_(?=(?:[ ,.:;\n\t<\/p>]|$))")

OPENING_BACKTICK_PATTERN = re.compile(r"(?<=(?:[ |,|.|:|;|\n|\t]))`(?=\S)(.+?)(?=(?:[ ,.:;\n\t<\/p>]|$))")
CLOSED_BACKTICK_PATTERN = re.compile(r"(?<=(?:[ |,|.|:|;|\n|\t|<p>]))(.+?)(?<=\S)`(?=(?:[ ,.:;\n\t<\/p>]|$))")

EMPTY_PARAGRAPH_PATTERN = re.compile(r'<p>\s*</p>')
