# RenderTree

Sublime Text 3 plugin to render tree structures as text. Uses the
excellent [anytree](https://github.com/c0fec0de/anytree) library.

## Usage

### Convert indented lines to tree

Type your tree structure using indented lines to represent the levels of the
tree. You can use any sequence of whitespace to represent an indention level
but it must be consistent across all lines. The indentation sequence is
inferred from the second line of the tree, since by definition that must be
indented. In the example below each level is indented by four spaces but you
could just as easily use three spaces, or even a mixture of tabs and spaces,
as long as the same string is used on all lines.

There must always be a single root node that has no identation ("Alpha" in the
example below).

```text
Alpha
    Bravo
    Charlie
        Delta
        Echo
    Foxtrot
    Golf
        Hotel
            India
```

Select all the lines containing your indented text then open the
command pallete and choose "Render Tree: Convert indented lines to tree".
The tree structure will be inserted after your selected text.

```text
Alpha
├── Bravo
├── Charlie
│   ├── Delta
│   └── Echo
├── Foxtrot
└── Golf
    └── Hotel
        └── India
```

Error messages and informational messages are printed to the Sublime Text
console.

## Install

- Via Package Control: search for `Render Tree`.
- Manual: clone this repo into your Sublime text 3 `Packages` folder.
