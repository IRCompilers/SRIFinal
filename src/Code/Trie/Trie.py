from collections import defaultdict


class TrieNode:
    def __init__(self, char: str = '', word: str = '', count: int = 0):
        self.char = char
        self.children = defaultdict(TrieNode)
        self.count = 0
        self.mcs = word
        self.mcs_count = count


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def Insert(self, word):
        node = self.root
        nodes = [node]
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
            nodes.append(node)
        node.count = node.count + 1
        count = node.count

        i = 0
        for path_node in nodes:
            if path_node.mcs_count < count:
                path_node.mcs_count = count
                path_node.mcs = word[i:]

            i += 1

    def MostCommon(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return ""
            node = node.children[char]
        return node.mcs

    def to_dict(self, node=None):
        if node is None:
            node = self.root
        trie_dict = {node.char: {'mcs': node.mcs, 'children': {}}}
        for char, child_node in node.children.items():
            trie_dict[node.char]['children'].update(self.to_dict(child_node))
        return trie_dict

    def from_dict(self, trie_dict, node=None):
        if node is None:
            node = self.root
        for key, value in trie_dict.items():
            node.char = key
            node.mcs = value['mcs']
            for child_key, child_value in value['children'].items():
                node.children[child_key] = TrieNode()
                self.from_dict({child_key: child_value}, node.children[child_key])

        return node