import sublime
import sublime_plugin

import re
from .lib.anytree import Node, RenderTree

def render_tree(text):
    lines = text.strip().splitlines()
    if len(lines) < 2:
        print('Error: tree must have at least 2 lines')
        return
    # Find string of characters used to represent an indent level
    m = re.search(r'^\s+', lines[1])
    if not m:
        print('Error: second line of tree must be indented')
        return
    indent_string = m.group(0)
    print('Info: using string', repr(indent_string), 'for each indent level')
    # Add each line to tree
    branch = [0]
    prev_depth = 0
    label = lines[0].strip()
    nodes = {0: Node(label)}
    for i, line in enumerate(lines):
        if i == 0:
            continue
        m = re.search('^((' + indent_string + ')+)(.*)', line)
        if not m:
            print('Error: no indent on line', repr(line))
            return
        indents = m.group(1)
        depth = indents.count(indent_string)
        if depth > prev_depth + 1:
            print('Error: extra indent level(s) on line', repr(line))
            return
        label = m.group(3).strip()
        nodes[i] = Node(label)
        if depth > prev_depth:
            branch.append(i)
        elif depth == prev_depth:
            branch[depth] = i
        else:
            branch = branch[:depth] + [i]
        if len(branch) >= 2:
            parent, child = branch[-2:]
            nodes[child].parent = nodes[parent]
        prev_depth = depth

    output = '\n'
    for pre, _, node in RenderTree(nodes[child].root):
        output += '%s%s' % (pre, node.name) + '\n'
    output += '\n'
    return output


class IndentedLinesToTreeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = self.view.substr(self.view.sel()[0])
        output = render_tree(text)
        if output:
            self.view.insert(edit, self.view.sel()[0].end(), output)
