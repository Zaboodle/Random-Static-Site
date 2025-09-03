from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
	TEXT = "text"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		return (
			self.text_type == other.text_type
			and self.text == other.text
			and self.url == other.url
		)

	def __repr__(self):
		return f'TextNode({self.text}, {self.text_type.value}, {self.url})'

def text_node_to_html(node):
        if node.text_type is TextType.TEXT:
                return LeafNode(None, node.text, None)
        if node.text_type is TextType.BOLD:
                return LeafNode('b', node.text, None)
        if node.text_type is TextType.ITALIC:
                return LeafNode('i', node.text, None)
        if node.text_type is TextType.CODE:
                return LeafNode('code', node.text, None)
        if node.text_type is TextType.LINK:
                return LeafNode('a', node.text, 'href')
        if node.text_type is TextType.IMAGE:
                return LeafNode('img', "", {'src': node.url, 'alt': node.text})
        raise ValueError(f'invalid text type: {node.text_type}')
