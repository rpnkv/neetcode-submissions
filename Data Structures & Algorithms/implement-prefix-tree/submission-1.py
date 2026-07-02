class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        root = self.root

        for i, c in enumerate(word):
            if not c in root.children:
                root.children[c] = Node()
            
            root = root.children[c]

        root.is_word = True

    def _search(self, word: str) -> Node | None:
        root = self.root

        for c in word:
            if c in root.children:
                root = root.children[c]
            else:
                return None

        return root


    def search(self, word: str) -> bool:
        srch_res = self._search(word)
        return srch_res is not None and srch_res.is_word

    def startsWith(self, prefix: str) -> bool:
        srch_res = self._search(prefix)
        return srch_res is not None

