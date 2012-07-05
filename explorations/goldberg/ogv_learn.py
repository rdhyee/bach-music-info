from music21 import *

aria = converter.parse('ogv-aria.xml')

# goldberg base line
tinyNotation.TinyNotationStream("G4 F# E D  BB C D GG  G F# E A   F# G A D  d B c B  G A B E  C BB AA D  GG C D GG ", "2/4").show()