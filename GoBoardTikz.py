class GoBoard:
	def __init__(self, size, left=True, top=True, right=True, bottom=True):
		self.size = size
		self.i = self.size[0]
		self.j = self.size[1]
		self.left = left
		self.top = top
		self.right = right
		self.bottom = bottom
		self.i_range = range(self.i)
		self.j_range = range(self.j)

	def _board(self):
		s = r"""\draw [very thick, draw=black, fill=brown!60!yellow!80!red!80!black] rectangle ({}, {}) ++ (0, 0);
""".format(self.i+1, self.j+1)
		i_start = 1 if self.bottom else 0
		i_stop = (0 if self.top else 1) + self.j
		j_start = 1 if self.left else 0
		j_stop = (0 if self.right else 1) + self.i
		for i in self.i_range:
			s += r"""\draw [very thick, black] ({0},{1}) -- ({0},{2});
""".format(i + 1, i_start, i_stop)
		for j in self.j_range:
			s += r"""\draw [very thick, black] ({1},{0}) -- ({2},{0});
""".format(j + 1, j_start, j_stop)
		return s

	def make(self, white=[], black=[], marked=[], number=[], circle=[], **kwargs):
		s = r"""\begin{tikzpicture}
"""
		s += self._board()
		for i, j in white:
			s += r"""\draw [very thick, draw=black, fill=white] ({0}, {1}) circle (0.475);
""".format(i, j)
		for i, j in black:
			s += r"""\draw [very thick, draw=black, fill=black!95!white] ({0}, {1}) circle (0.475);
""".format(i, j)
		for i, j in marked:
			if (i, j) in black:
				s += r"\draw [white] (" + str(i) + ", " + str(j) + r") node {\scalebox{1.75}{$\boldsymbol{\bigtriangleup}$}};" + "\n"
			elif (i, j) in white:
				s += r"\draw [black] (" + str(i) + ", " + str(j) + r") node {\scalebox{1.75}{$\boldsymbol{\bigtriangleup}$}};" + "\n"
			else:
				s += r"\draw [draw=brown!60!yellow!80!red!80!black ,fill=brown!60!yellow!80!red!80!black] (" + str(i) + ", " + str(j) + r") circle (0.4);"
				s += r"\draw [draw=black] (" + str(i) + ", " + str(j) + r") node {\scalebox{1.75}{$\boldsymbol{\bigtriangleup}$}};" + "\n"
		for i, j in circle:
			if (i, j) in black:
				s += r"\draw [white] (" + str(i) + ", " + str(j) + r") node {\scalebox{1.75}{$\boldsymbol{\bigcirc }$}};" + "\n"
			elif (i, j) in white:
				s += r"\draw [black] (" + str(i) + ", " + str(j) + r") node {\scalebox{1.75}{$\boldsymbol{\bigcirc }$}};" + "\n"
			else:
				s += r"\draw [draw=brown!60!yellow!80!red!80!black ,fill=brown!60!yellow!80!red!80!black] (" + str(i) + ", " + str(j) + r") circle (0.4);"
				s += r"\draw [draw=black] (" + str(i) + ", " + str(j) + r") node {\scalebox{1.75}{$\boldsymbol{\bigcirc }$}};" + "\n"
		for idx, v in enumerate(number):
			i, j = v
			if (i, j) in black:
				s += r"\draw [white] (" + str(i) + ", " + str(j) + r") node {\scalebox{1.75}{\textbf{" + str(idx+1) + "}}};" + "\n"
			elif (i, j) in white:
				s += r"\draw [black] (" + str(i) + ", " + str(j) + r") node {\scalebox{1.75}{\textbf{" + str(idx+1) + "}}};" + "\n"
			else:
				s += r"\draw [draw=brown!60!yellow!80!red!80!black ,fill=brown!60!yellow!80!red!80!black] (" + str(i) + ", " + str(j) + r") circle (0.4);"
				s += r"\draw [draw=black] (" + str(i) + ", " + str(j) + r") node {\scalebox{1.75}{\textbf{" + str(idx+1) + "}}};" + "\n"
		for k, v in kwargs.items():
			for i, j in v:
				if (i, j) in black:
					s += r"\draw [white] (" + str(i) + ", " + str(j) + r") node {\scalebox{1.75}{\textbf{" + k + "}}};" + "\n"
				elif (i, j) in white:
					s += r"\draw [black] (" + str(i) + ", " + str(j) + r") node {\scalebox{1.75}{\textbf{" + k + "}}};" + "\n"
				else:
					s += r"\draw [draw=brown!60!yellow!80!red!80!black ,fill=brown!60!yellow!80!red!80!black] (" + str(i) + ", " + str(j) + r") circle (0.4);"
					s += r"\draw [draw=black] (" + str(i) + ", " + str(j) + r") node {\scalebox{1.75}{\textbf{" + k + "}}};" + "\n"
		s += r"""\end{tikzpicture}"""
		return s

dims = (6,6)

brett = GoBoard(dims, left=False, top=False)

b = [(3, 4), (4, 4), (2, 3), (1, 3), (5, 5), (4, 6)]
w = [(4, 3), (3, 3), (2, 2), (5, 4), (5, 3)]
c = [(3, 4)]
m = [(4, 3)]
n = [(4, 4), (3, 3), (2, 3), (2, 2), (1, 3), (5, 4), (5, 5), (4, 6), (5, 3)]

tikz = brett.make(white=w, black=b, circle=c, marked=m, number=n, A=[(1, 2)], B=[(3, 2)])

print(tikz)