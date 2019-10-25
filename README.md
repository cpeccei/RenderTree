# RenderTree

Sublime Text 3 plugin to render trees as text.

## Usage

## Convert indented lines to tree

Type your tree structure using indented lines to represent the levels
of the tree. Each new level must be indented using **four spaces**. There
must always be a single root node that has no identation ("Alpha" in
the example below).

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
