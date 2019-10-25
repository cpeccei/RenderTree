import sublime
import sublime_plugin

import re
from .lib.anytree import Node, RenderTree

class IndentedLinesToTreeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = self.view.substr(self.view.sel()[0])
        lines = text.strip().splitlines()
        branch = []
        prev_depth = -1
        nodes = {}
        for i, line in enumerate(lines):
            m = re.search('^ *', line)
            num_initial_spaces = len(m.group(0))
            depth, remainder = divmod(num_initial_spaces, 4)
            if remainder:
                print('Error: indentation must use multiples of 4 spaces')
                return
            label = line.strip()
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
        self.view.insert(edit, self.view.sel()[0].end(), output)
