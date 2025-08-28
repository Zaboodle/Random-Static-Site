from textnode import TextNode, TextType

def main():
	node = TextNode('this guy, amiright?', TextType.LINK, 'https://www.google.com')
	print(node)


main()
