import os
import re
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val})'

def generateLinkedList(array):
    if not array:
        return []
    head = ListNode(array[0])
    current = head
    for i in range(1, len(array)):
        current.next = ListNode(array[i])
        current = current.next
    return head

def displayLinkedList(head):
    if not head:
        print('None')
        return
    node = head
    ll = f'{node.val}'

    while node.next:
        node = node.next
        ll += f' --> {node.val}'
    print(ll)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
            for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

def generate_readmes(directory):
    '''
    Generate READMEs.md in each directory
    '''
    for _, dirs, _ in os.walk(directory):
        unitDirs = [dir for dir in dirs if re.match(r"\d+", dir[0])]

        for dir in unitDirs:
            with open(f"{dir}/README.md", "w+") as file:
                header = dir.split("-")
                formatted_header = f"Unit {header[0]}:"
                for word in header[1:]:
                    spacedWord = re.sub(r"([A-Z]{1,2})", " \\1", word).strip()
                    formatted_header += f" {spacedWord}"

                file.write(f"# {formatted_header}\n")
                file.write(f"## TODO\n")
                file.write(f"- [ ] PreWork\n")
                file.write(f"- [ ] Session #1\n")
                file.write(f"- [ ] Session #2\n")
                file.write(f"- [ ] HackerRank\n")
                file.write(f"- [ ] Additional Exercises")

if __name__ == "__main__":
    generate_readmes(".")
