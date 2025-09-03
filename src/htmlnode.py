

class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError('to_html no implemented')

	def props_to_html(self):
		if self.props is None:
			return ""
		props_html = ""
		for prop in self.props:
			props_html += f' {prop}="{self.props[prop]}"'
		return props_html

	def __repr__(self):
		return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'

	def __eq__(self, other):
		return (
			self.tag == other.tag and self.value == other.value and
			self.children == other.children and self.props == other.props
		)


class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if not self.value:
			raise ValueError('HTML has no value')
		if self.tag == None:
			return self.value
		return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

	def __repr__(self):
		return f'Leafnode({self.tag}, {self.value}, {self.props})'

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)

	def to_html(self):
		if not self.tag:
			raise ValueError('node has no tag')
		if not self.children:
			raise ValueError('child node is missing')
		children_html = ""
		for child in self.children:
			children_html += child.to_html()
		return f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'

	def __repr__(self):
		return f'ParentNode({self.tag}, children: {self.children}, {self.props})'
