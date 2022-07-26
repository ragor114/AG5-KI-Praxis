# Deep Neural Networks
In dieser Session wurden Vorteile und Probleme von tiefen Neuronalen Netzen behandelt, sowie erste komplexere Architekturen eingeführt.

Im Rahmen der Session wurde ein [Jupyter Notebook](/04_Deep%20Neural%20Networks/Q_&_A_Deep_Neural_Networks.ipynb) entwickelt, mit dem die Functional API, ResNets und Skip-Connections, BatchNormalization, Optimizer, Lernratenoptimierung und Autoencoder behandelt wurden.

# Material
Das folgende Material kann verwendet werden, um sich die Inhalte selbst anzueignen:

## Tensorflow Functional API
Die Tensorflow Functional API erlaubt es Netzarchitekturen flexibler, als Reihe von Funktionsaufrufen, zu definieren.

- Ein Einsteigstutorial findet sich [hier](https://keras.io/guides/functional_api/)
- Alternativ findet sich [hier ein kurzes Tutorial](https://machinelearningmastery.com/keras-functional-api-deep-learning/)

## Vanishing and Exploding Gradients
Fehler werden beim Lernen durch die Schichten zurückgegeben und multipliziert. Wenn man viele Schichten hat, bedeutet das, bei einem Fehler der oft größer 1 ist, einen exponentiellen Anstieg. Bei einem Fehler der kleiner 1 ist bedeutet das einen exponentiellen Abstieg. Da Computer keine unendliche Genauigkeit haben kann es sein, dass dann 0 oder unendlich propagiert werden, damit lernt (und rechnet) es sich aber schlecht.

- Eine Erklärung gibt es [hier](https://programmathically.com/understanding-the-exploding-and-vanishing-gradients-problem/)
- Das Problem und mögliche Lösungen werden [hier](https://www.analyticsvidhya.com/blog/2021/06/the-challenge-of-vanishing-exploding-gradients-in-deep-neural-networks/) beschrieben

## Skip Connections
Eine mögliche Lösung ist es, dem Netz Umwege anzubieten, so dass Layer ausgelassen werden können, wenn sie nicht gebraucht werden.

- [hier](https://arxiv.org/pdf/1512.03385.pdf) findet sich das Original Paper zu solchen Netzen
- eine Implementierung in keras wird in [diesem Tutorial gezeigt](https://medium.com/analytics-vidhya/understanding-and-implementation-of-residual-networks-resnets-b80f9a507b9c)
- noch etwas praktischer (und weiter weg von der Theorie) ist [dieser Guide](https://towardsdatascience.com/building-a-resnet-in-keras-e8f1322a49ba)

## BatchNormalization
Um das Lernen zu stabilieren, hilft BatchNormalization. Dabei wird der mittlere Output eines Layers für den aktuellen Batch auf eine Normalverteilung transformiert, auf einen lernbaren Mittelwert verschoben und auf eine lernbare Varianz skaliert.

- [das hier ist ein guter Start](https://towardsdatascience.com/batch-norm-explained-visually-how-it-works-and-why-neural-networks-need-it-b18919692739), um BatchNormalization zu verstehen
- [dieser Guide](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338), geht mehr ins Detail und ist wirklich Gold wert

## Optimizer
Zusätzlich dazu lernen tiefere Netze langsamer. Wir wollen daher den Trainingsprozess beschleunigen. Dazu verändern wir die Optimierung.

- eine mathematische Erklärung der wichtigsten Optimierungsverfahren gibt es in [diesem Video](https://www.youtube.com/watch?v=Tyob6iDNmVg)
- deutlich kompakter ist [diese kurze Erklärung](https://towardsdatascience.com/optimizers-for-training-neural-network-59450d71caf6) aller wichtigen Verfahren
- etwas ausführlicher aber weniger mathematisch ist [dieser Guide](https://www.analyticsvidhya.com/blog/2021/10/a-comprehensive-guide-on-deep-learning-optimizers/)

## Learningrate Trick
Dooferweise bleibt die initiale Lernrate ein Hyperparameter, den wir tunen müssen. Dieser beeinflusst die Zeit, die wir zum lernen brauchen und die Qualität des Ergebnisses. Glücklicherweise gibt es einen Trick, schnell eine gute Lernrate zu finden.

- wie dieser zu implementieren ist, wird [hier](https://towardsdatascience.com/estimating-optimal-learning-rate-for-a-deep-neural-network-ce32f2556ce0) beschrieben
- warum er funktioniert wird (ansatzweise) im ursprünglichen [Paper](https://arxiv.org/abs/1506.01186) dazu behandelt

## Autoencoder
Autoencoder lernen den eigenen Input zu rekonstruieren. Das können wir nutzen um eine Zerlegung in prinzipale Komponenten vorzunehmen, Outlier zu erkennen, One-Hot-Vektoren zu erzeugen und Rauschen zu reduzieren.

- [dieses Buchkapitel](https://www.deeplearningbook.org/contents/autoencoders.html) beschreibt Autoencoder ausführlich
- für visuelle Menschen ist [dieses Video](https://www.youtube.com/watch?v=1xVgIkAR398) (auf deutsch) zu empfehlen
- aber auch Tensorflow hat [ein Tutorial](https://www.tensorflow.org/tutorials/generative/autoencoder) wie ein Autoencoder zu implementieren ist
