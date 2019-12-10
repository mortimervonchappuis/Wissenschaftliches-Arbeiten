# Wissenschaftliches-Arbeiten

### Klasse
Die Klasse `GoBoard` erstellt TikZ-Pictures von verschiedenen Go Stellungen.

Die initiallisierung erfolgt über den Aufruf des Konstruktors.

~~~python
dimensions = (9, 9)
brett = GoBoard(dimensions, left=False, top=False)
~~~

Dem Konstruktor muss eine `size` übergeben werden (im Beispiel das Tuple 'dimensions'). Diese gibt die Zeilen- und Spaltenanzahl des Bretts an. Des Weiteren können die attribute `left`, `top`, `right`, `bottom` mit dem Wert `False` überschrieben werden, um den jeweiligen Rand des Bretts verschwinden zu lassen.

### Erstellung des TikZ Codes
Der Aufruf der methode `make` erstellt den LaTex TikZ Picture Code.
~~~python
brett.make()
~~~
Erzeugt den folgenden Code:
~~~
\begin{tikzpicture}
\draw [very thick, draw=black, fill=brown!60!yellow!80!red!80!black] rectangle (6, 6) ++ (0, 0);
\draw [very thick, black] (1,1) -- (1,6);
\draw [very thick, black] (2,1) -- (2,6);
\draw [very thick, black] (3,1) -- (3,6);
\draw [very thick, black] (4,1) -- (4,6);
\draw [very thick, black] (5,1) -- (5,6);
\draw [very thick, black] (0,1) -- (5,1);
\draw [very thick, black] (0,2) -- (5,2);
\draw [very thick, black] (0,3) -- (5,3);
\draw [very thick, black] (0,4) -- (5,4);
\draw [very thick, black] (0,5) -- (5,5);
\end{tikzpicture}
~~~
![alt text](demo_1.pdf)
