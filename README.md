# Plain text Lewis & Short CSV

## What?

Two plain text versions of *A Latin Dictionary* edited by Charlton T. Lewis and Charles Short. These files are based on the XML version that [the Perseus Digital Library][perseus] has [made available under a Creative-Commons license][lexica]. The only difference between the two files is that one replaces straight quotes with curly quotes. (The text already contains other unicode features, so it seemed worth doing.)

[perseus]: http://www.perseus.tufts.edu/hopper/
[lexica]: https://github.com/PerseusDL/lexica/tree/master/CTS_XML_TEI/perseus/pdllex/lat/ls

## Why?

This dictionary is widely available online in various ebook formats and as XML, but not as plain text as far as I know. Plain text is much easier to work with than these other formats. In addition, the PerseusDL XML file leaves the Greek in [beta code][beta] format.

[beta]: https://en.wikipedia.org/wiki/Beta_Code

My motivation is to use this version of Lewis and Short to create tools to help myself and other teachers create glossaries for students. (As those tools develop, I'll put a link here.) However, I hope that other people find these files useful for lots of other projects. See below for license.

## How?

I used [a tool provided by PerseusDL][tei-conversion-tools] to transform the beta code in the XML file into unicode Greek and a small set of `sed` commands to transform all of the remaining character entities into unicode. (E.g., `&amacr;` becomes 'ā'.) Finally a Python script extracted the content from the XML. (I've included the `sed` and Python scripts in case anyone wants to adapt or improve those.)

[tei-conversion-tools]: https://github.com/PerseusDL/tei-conversion-tools

## Credits

Text provided by Perseus Digital Library, with funding from The National Endowment for the Humanities. 

Original version available for viewing and download at http://www.perseus.tufts.edu/

## License

The two Lewis and Short text files are licensed under [the CC BY-SA 3.0 license][cc]. The Python script and `sed` commands are licensed under [the BSD 3-Clause license][bsd]

[cc]: https://creativecommons.org/licenses/by-sa/3.0/us/
[bsd]: https://opensource.org/licenses/BSD-3-Clause
