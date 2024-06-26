# Markdown Parser


This console application parse markdown into html.
The output can either be displayed in the console or saved to a file.

### How to set up it?

Clone this repo:

```bash
 git clone https://github.com/OlhaMish/software-development-lab-1 
 ```

[Then install poetry following official instruction](https://python-poetry.org/docs/) 


### Run application:

```bash
poetry run python markdown2html.py <path/to/your/input/file> 
```

Explore commands:

```bash
poetry run python markdown2html.py --help
```

```bash
usage: markdown2html.py [-h] [--output OUTPUT] input_file

Convert Markdown to HTML.

positional arguments:
  input_file            Path to the input Markdown file

options:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Path to the output HTML file
  -format, -f
                        choices: ['ansi', 'html']
```

### Run tests

To run tests you need to [install poetry](https://python-poetry.org/docs/), then run tests by: 
```bash
  poetry run pytest
```

### Example

```markdown
Alice's Adventures in Wonderland by Lewis Carroll


This novel follows the story of a young girl named _Alice_ who falls down a rabbit hole into a **fantastical world full of peculiar creatures** and bizarre experiences. 
As she navigates through this `strange land`, she encounters a series of nonsensical events, including a tea party with a _Mad Hatter_, a pool of tears, and a trial over stolen tarts. 

```The book is renowned for its playful use of language, logic, and its **exploration** of the boundaries of reality.```
```

### Parse it as html:

```bash
poetry run python markdown2html.py input.md -o output.html 
```


output.html:

```html
<p>Alice's Adventures in Wonderland by Lewis Carroll</p>
<p> This novel follows the story of a young girl named <i>Alice</i> who falls down a rabbit hole into a <b>fantastical world full of peculiar creatures</b> and bizarre experiences. 
As she navigates through this <tt>strange land</tt>, she encounters a series of nonsensical events, including a tea party with a <i>Mad Hatter</i>, a pool of tears, and a trial over stolen tarts.</p>
<p><pre>The book is renowned for its playful use of language, logic, and its **exploration** of the boundaries of reality.</pre></p>
```

### Parse it as ansi:

```bash
poetry run python markdown2html.py -o output.html -f ansi input.md 
```
output.ansi:

![image](https://github.com/OlhaMish/software-development-lab-2/blob/master/docs/img.png)

### Revert commit
[link](https://github.com/OlhaMish/software-development-lab-1/commit/ea82720f5675d9c93b87cf83f3bde17e197f277d)

### Dropped tests
[link](https://github.com/OlhaMish/software-development-lab-2/commit/1f76ec9fb14190358e18b2bf2dd16688b0f6b862)

### Conclusions
From my experience, writing unit tests before coding might not seem appealing, but doing so can save considerable time.