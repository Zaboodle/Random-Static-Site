import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)
		self.assertNotEqual(node, node2)
		self.noURL(node, node2)
		self.EqTextType(node, node2)

	def assertEqual(self, node, node2):
		return node.text == node2.text and node.text_type == node2.text_type and node.url == node2.url

	def assertNotEqual(self, node, node2):
		return node.text != node2.text and node.text_type != node2.text_type and node.url != node2.url

	def noURL(self, node, node2):
		return f'node 1 url: {node.url}, node 2 url: {node2.url}'

	def EqTextType(self, node, node2):
		return node.text_type == node2.text_type

if __name__ == "__main__":
	unittest.main()
