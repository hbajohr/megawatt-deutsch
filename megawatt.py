#!/usr/bin/python
# coding: utf-8
#
# Megawatt, copyright (c) 2014, 2018 Nick Montfort <nickm@nickm.com>
#
# Copying and distribution of this file, with or without modification, are
# permitted in any medium without royalty provided the copyright notice and
# this notice are preserved. This file is offered as-is, without any warranty.
#
# Updated 31 May 2018, changed "print" and "/" for Python 2 & 3 compatibility
# Updated 26 November 2018, substituted a shorter all-permissive license
# Written 29 November 2014


"""_Megawatt_ ist der Titel eines Computerprogramms, dessen Quellcode
Sie womöglich gerade lesen, und des Outputs dieses Programms, der
in vielerlei Hinsicht ein konventioneller Roman ist, und den Sie 
womöglich stattdessen lesen. 
Dieser Hinweis erscheint am Anfang beider.

Das Programm _Megawatt_ basiert auf Passagen aus Samuel Becketts Roman
_Watt_, der 1953 veröffentlicht, aber sehr viel früher geschrieben 
wurde, als Beckett während des Zweiten Weltkrieges die Résistance
unterstützte. 

Der Roman _Megawatt_ lässt das meiste der eher verständlichen Teile
von Becketts Roman beiseite und konzentriert sich stattdessen auf 
das, was an ihm am durchgängigsten systematisch und rätselhaft ist. 
Er baut diese Romanpassagen nicht einfach nach, obwohl _Megawatt_ 
mit nur wenigen Veränderungen sehr wohl in der Lage wäre, genau dies 
zu tun. Stattdessen werden sie im neuen Roman durch Textgenerierung 
intensiviert, wobei dieselben Methoden zum Einsatz kommen, die Beckett 
verwandte, und bedeutend mehr Text entsteht als im ohnehin bereits 
exzessiven _Watt_ zu finden ist.

Um den Roman im Markdown-Format zu kompilieren, führen Sie megawatt.py 
(ein Python 2-Programm) bei installiertem TextBlob aus (einer Text-
verarbeitungsbibliothek).

    % python megawatt.py > megawatt.text

Um PDF- und epub-Dokumente zu erstellen, verwenden Sie pandoc:

    % pandoc -V geometry:paperwidth=5.8268in \ 
        -V geometry:paperheight=8,2677in \ 
        -V geometry:margin=.7in -o megawatt.pdf \ 
        megawatt.text
    % echo '% Megawatt' > info.txt
    % echo '% Nick Montfort' >> info.txt
    % pandoc -o megawatt.epub info.txt megawatt.text

_Megawatt_ wurde für den zweiten NaNoGenMo (National Novel Generation
Month/Nationalen Romangenerierungsmonat) im November 2014 geschrieben/
generiert und ist eine freie Software.
Hannes Bajohr hat das Buch – im Code, nicht im Output – übersetzt. 
Es erscheint mit freundlicher Genehmigung des Autors bei 0x0a."""

__author__ = 'Nick Montfort'
__translator__ = 'Hannes Bajohr'
__license__ = 'ISC'
__version__ = '1.0'


#### ALLGEMEINES
import urllib3
import xml.etree.ElementTree as ET
from textblob import Word, TextBlob
urllib3.disable_warnings()

def folgender_abschnitt(num):
    text.append('\n\\newpage')
    text.append('\n# ' + num + '\n\n')

text = []
ausbuchstabiert = {
    0: 'null',
    1: 'eins',
    2: 'zwei',
    3: 'drei',
    4: 'vier',
    5: 'fünf',
    6: 'sechs',
    7: 'sieben',
    8: 'acht',
    9: 'neun',
    10: 'zehn',
    11: 'elf',
    12: 'zwölf',
    13: 'dreizehn',
    14: 'vierzehn',
    15: 'fünfzehn',
    16: 'sechzehn',
    17: 'siebzehn',
    18: 'achtzehn',
    19: 'neunzehn',
    20: 'zwanzig'
}


#### DIE STIMMEN

text.append('\n# I\n\n')
def kombiniere(num, worte):
    schluss = []
    if num > 0 and len(worte) >= num:
        if num == 1:
            schluss = schluss + [[worte[0]]]
        else:
            schluss = schluss + [[worte[0]] +
                    c for c in kombiniere(num - 1, worte[1:])]
        schluss = schluss + kombiniere(num, worte[1:])
    return schluss

## In 'Watt' gibt es Stimmen = ['sangen', 'schrien', 'erklärten', 
## 'murmelten']
## Und Watt versteht = ['alles', 'viel', 'wenig', 'nichts']
## Hier sprechen die Stimmen auf acht Weisen und es gibt acht 
## Verständnisstufen:
Stimmen = ['sangen', 'schrieen', 'erklärten', 'murmelten', 'schwatzten', 
		'plauderten', 'schimpften', 'flüsterten']
versteht = ['alles', 'viel', 'einiges', 'die Hälfte', 'wenig', 'weniger', 
			'Teile', 'nichts']
absatz = ''
vorwort = ' und manchmal '

for num in range(len(Stimmen)):
    for wortliste in kombiniere(num + 1, Stimmen):
        absatz = absatz.replace(", und ", " und ") + vorwort + ' und '.join(wortliste)
        if len(wortliste) == 1:
            absatz = absatz + ' sie nur'
absatz = ('Watt hörte Stimmen. Nun, ' + absatz[5:] + 
    ' die Stimmen, alle zusammen, zur selben Zeit, wie jetzt, um nur ' + 
    'die Stimmen zu erwähnen, die ' + ausbuchstabiert[len(Stimmen)] + 
    ', denn es gab noch andere. Und manchmal verstand Watt ' + 
    ' und manchmal verstand er '.join(versteht) + ', so wie jetzt.')
text.append(absatz)


#### BEWEGUNGSARTEN

folgender_abschnitt('II')
## In 'Watt' gibt es nur eine Richtung, kompass = ['nach Osten']
## Auch kommt der Ausdruck 'zum Beispiel' im Text vor; ich habe ihn
## fortgelassen, da mir der neue Text erschöpfend zu sein scheint. 
kompass = ['nach Osten', 'nach Südosten', 'nach Süden', 
		   'nach Südwesten', 'nach Westen', 'nach Nordwesten', 
		   'nach Norden', 'nach Nordosten']
bein = ['rechtes', 'linkes']
j = 0
rl = 0
for i in range(len(kompass)):
    absatz = (['Watts', 'Sein'][i > 0] + ' Gewohnheit, geradewegs ' +
           kompass[0]  + ' zu gehen, bestand darin, daß er')
    for j in range(8):
        absatz = absatz + (' seinen Oberkörper so weit wie möglich ' +
        kompass[[6, 2][rl]] + ' drehte und gleichzeitig sein ' + 
        bein[rl] + ' Bein so weit wie möglich ' + kompass[[2, 6][rl]] +
        ' schleuderte, dann')
        rl = [1, 0][rl]
        absatz = absatz + ['', ' wieder', ' noch einmal', ' erneut'][j/2]
    absatz = (absatz[:-12] + ' und so weiter, immer und immer wieder, ' +
            'viele, viele Male, bis er sein Ziel erreicht hatte und ' +
            'sich hinsetzen konnte.')
    
    text.append(absatz.replace(", und ", " und "))
    kompass = kompass[1:] + kompass[:1]


#### HAUSBESUCH

folgender_abschnitt('III')
text.append('Das Haus lag im Dunkeln.')
## In 'Watt' gibt es zwei Türen = ['Vorder', 'Hinter']
## Watt geht zu ihnen und kehrt zurück, ging = 
## ['ging er', 'kehrte er zurück']
## Hier gibt es nun vier Türen und Watt sucht sie doppel so oft auf.
tueren = ['Vorder', 'Hinter', 'Seiten', 'Fall']
ging = ['ging er', 'kehrte er zurück', 'ging er erneut zurück', 
		'lief er abermals']

for i in range(len(tueren) * 4):
    absatz = ('Da Watt die ' + tueren[0] + 'tür verschlossen fand, ' +
            ging[i / len(tueren)] + ' zur ')
    tueren = tueren[1:] + tueren[:1]
    absatz = absatz + (tueren[0] + 'tür.')
    text.append(absatz)

text[-1] = (text[-2][:-50] + ' jetzt offen fand, oh, nicht ' + 
				'sperrangelweit offen, sondern aufgeklinkt, wie man ' +
				'sagt, konnte er das Haus betreten.')


#### DIE KURZE ERKLÄRUNG

folgender_abschnitt('IV')
text.append('Drinnen befanden sich Mr. Knott und Erskine und noch ' +
			'jemand. Bevor er ging, machte dieser Gentleman die ' +
			'folgende kurze Erklärung:')

absatz = ('Und die arme alte, lausige Erde, die meine und die ' +
			'meines Vaters und meiner Mutter und')

def vorfahren(erste_liste, zweite_liste, tiefe):
    if tiefe < 1: 
        return
    nl1 = []
    for e in erste_liste:
        for f in zweite_liste:
             nl1.append(f+e)
             yield nl1[-1]
    yield ' und'.join(vorfahren(nl1,zweite_liste,tiefe-1))

## Ursprünglich wird die folgende Operation für drei Generationen 
## durchgeführt, also:
#   for x in vorfahren([' meiner Mutter', ' meines Vaters'], 
#   [' der Mutter', ' des Vaters'],2):
## Hier ist die Anzahl an Generationen doppelt so groß,
## es gibt sechs:
for x in vorfahren([' meiner Mutter', ' meines Vaters'], [' der Mutter', ' des Vaters'],5):
    absatz = absatz + x + ' und'
absatz = absatz[:-4] + ' der Väter und Mütter anderer Unseligen und'
for x in vorfahren([' ihrer Mütter', ' ihrer Väter'], [' der Mutter', ' des Vaters'],5):
    absatz = absatz + x + ' und'
absatz = "".join(absatz[:-8]) + '.'
text.append(absatz)

#### DIE ZUSAMMENSETZUNG DES GERICHTS

## Da es keine deutsche Synonym-API gibt, die frei und ohne
## Anmeldung zugänglich ist, war dieser Abschnitt nur über
## den Umweg zu übersetzen, dass die Synonyme auf Englisch
## generiert und schließlich über TextBlob ins Deutsche 
## übertragen wurden. Bei der Übersetzung entstehende Dopp-
## lungen wurden anschließend entfernt. [A.d.Ü]

folgender_abschnitt('V')

nahrungsmittel = []

def uebersetze(liste):
    neue_liste = []
    liste = ', '.join(liste).encode("utf-8")
    liste = str(TextBlob(liste).translate(to="de"))
    liste = liste.split(", ")
    for element in liste:
        if element not in neue_liste:
            neue_liste.append(element)
    return ', '.join(neue_liste)

def verschiene_arten(wort, sinn, dt_wort, plural=False):
    bestandteile = []
    for synset in Word(wort).synsets[sinn - 1].hyponyms():
        next_name = synset.lemma_names()[0].replace('_', ' ')
        if plural:
            bestandteile.append(Word(next_name).pluralize())
        else:
            bestandteile.append(next_name)
    liste = uebersetze(bestandteile)
    return (liste + ' und andere' + dt_wort +
            ' verschiedener Art, ')
            
text.append('Samstagabends wurde eine Menge Nahrung zubereitet und gekocht, ' +
               'die genügte, um Mr. Knott eine Woche lang durchzubringen. ')
absatz = 'Dieses Gericht enthielt Nahrungsmittel verschiedener Art, '
## Das Original beginnt: 'wie Suppen verschiedener Art, Fisch, Eier, Wild,
## Geflügel, Fleisch, Käse, Obst, alles verschiedener Art...'
nahrungsmittel.append(verschiene_arten('soup', 1, ' Suppen'))
nahrungsmittel.append(verschiene_arten('fish', 2, 'n Fisch'))
nahrungsmittel.append(verschiene_arten('game', 4, 's Wild'))
nahrungsmittel.append(verschiene_arten('poultry', 1, 's Geflügel'))
nahrungsmittel.append(verschiene_arten('meat', 1, 's Fleisch'))
nahrungsmittel.append(verschiene_arten('cheese', 1, ' Milchprodukte'))
nahrungsmittel.append(verschiene_arten('fruit', 1, 's Obst'))
nahrungsmittel.append(verschiene_arten('bread', 1, 's Brot'))
nahrungsmittel.append(verschiene_arten('butter', 1, ' Butter'))
nahrungsmittel.append(verschiene_arten('tea', 1, 'n Tee'))
nahrungsmittel.append(verschiene_arten('coffee', 1, 'n Kaffee'))
nahrungsmittel.append(verschiene_arten('milk', 1, ' Milch'))
nahrungsmittel.append(verschiene_arten('beer', 1, 's Bier'))
nahrungsmittel.append(verschiene_arten('wine', 1, 'n Wein'))
nahrungsmittel.append(verschiene_arten('medicine', 2, ' Medizin', plural=True))
nahrungsmittel.insert(2,'und Eier verschiedener Art, ')
nahrungsmittel.insert(10,'und Absinth, Mineralwasser, ')
nahrungsmittel.insert(15, 'Whiskey, Brandy, ')
nahrungsmittel.insert(17, 'und Wasser und es enthielt außerdem viele Dinge, ' +
              'die gut für die Gesundheit sind, wie etwa Insiulin, Digitalin, ' +
              'Kalomel, Job, Laudanum, Quecksilber, Kohle, Eisen, ' +
              'Kamille, Wurmpulver, ')
nahrungsmittel.insert(19,'und freilich Salz und Senf, Pfeffer und Zucker, und ' +
               'freilich ein Tröpfchen Salizylsäure gegen die Gärung.')
for element in nahrungsmittel:
    absatz = absatz + element
text.append(str(absatz.replace(", und ", " und ")))

#### DIE TEILE DES VERSPEISTEN GERICHTS

folgender_abschnitt('VI')
## In Watt wird nur 'die Hälfte' (hier: zehn Zwanzigstel) erwähnt.
absatz = ('Man hörte Mr. Knott nie über seine Nahrung klagen, obgleich ' +
		'er sie nicht immer aß. Manchmal leerte er den Napf, und kratzte ' +
		'mit dem Schäufelchen an der Innenwand und über den Boden, bis ' +
		'sie blank waren, und manchmal ließ er ein Zwanzigstel ')
for numerator in range(2,20):
    absatz = absatz + ' oder ' + ausbuchstabiert[numerator] + ' Zwanzigstel'
absatz = absatz + (' oder irgendeinen anderen Bruchteil stehen, und ' + 
				'manchmal ließ er alles stehen.')
text.append(absatz)


#### SO WENIGSTENS

folgender_abschnitt('VII')
## In Watt gibt es drei Empfindungen:
# empfindungen = ['ruhig', 'frei', 'froh']
## Hier sind sie auf sechs erweitert:
empfindungen = ['ruhig', 'frei', 'froh', 'ganz', 'gut', 'richtig']
absatz = ('Vielmehr unter dem Druck… Nicht daß Watt sich ' + 
		' und '.join(empfindungen) + ' fühlte, oder je gefühlt' +
		' hatte, durchaus nicht. Aber er dachte, daß er sich vielleicht ')
for i in range(6, 0, -1):
    folgende_empfindungen = ''
    for c in kombiniere(i, empfindungen):
        folgende_empfindungen = folgende_empfindungen + ' und '.join(c) + ' oder '
    absatz = (absatz + folgende_empfindungen + 'wenn nicht ' + 
    		folgende_empfindungen[:-6] + ' so wenigstens ')
absatz = absatz[:-14] + 'fühlte, ohne es zu wissen.'
text.append(absatz)


#### MR. KNOTTS Schuhwerk
## 'Was seine Füße betraf, so trug er manchmal an jedem eine Socke…'
## Nicht erweitert. ppg256-7 basiert auf dieser Passage:
## http://nickm.com/poems/ppg256.html

#### MR. KNOTTS BEWEGUNGEN
## '…von der Tür zum Fenster, vom Fenster zur Tür,…'
## Nicht erweitert. Nanowatt generiert die Passage 
## auf Englisch und Französisch:
## http://nickm.com/post/2013/11/nanowatt/

#### DIE ANORDNUNG VON MR. KNOTTS MÖBELN
## 'So befanden sich nicht selten sonntags: die Kommode auf
## den Füßen am Kamin und der Toilettentisch auf dem Kopf…'
## Nicht erweitert. Nanowatt generiert die Passage 
## auf Englisch und Französisch:
## http://nickm.com/post/2013/11/nanowatt/


#### MR. KNOTTS ÄUSSERE ERSCHEINUNG

folgender_abschnitt('VIII')
## Nur die ersten vier erscheinen im Original.
attribute = [
    ['dünn', 'stämmig', 'dick'],
    ['klein', 'mittelgroß', 'groß'],
    ['blaß', 'gelb', 'rosig'],
    ['schwarz', 'rot', 'blond'],
    ['braunäugig', 'blauäugig', 'grünäugig'],
    ['ektomorph', 'mesomorph', 'endomorph'],
    ['glattrasiert', 'vollbärtig', 'schnurrbärtig'],
    ['aufrecht', 'gebeugt', 'lehnend']
]
def permutiere(liste_der_listen):
    if len(liste_der_listen) == 1:
        for i in liste_der_listen[0]:
            yield 'und ' + i
    else:
        for i in liste_der_listen[0]:
            for j in permutiere(liste_der_listen[1:]):
                yield i + ', ' + j
absatz = ('Was den so wichtigen physischen Aspekt Mr. Knotts betraf, so ' +
        'hatte Watt dazu leider wenig oder nichts zu sagen. ' +
        'Denn an einem Tag konnte Mr. Knott ')
absatz = absatz + ' sein, und am nächsten '.join(list(permutiere(attribute)))
absatz = (absatz + ', jedenfalls schien es Watt so, um nur den Wuchs ' +
        'die Gestalt, die Haut, das Haar, die Augenfarbe, den Körpertyp, ' +
        'die Gesichtsbehaarung und die Haltung zu erwähnen.')
text.append(absatz.replace(", und ", " und "))

#### ENDE

folgender_abschnitt('IX')
text.append(('&nbsp;' * 16) + '?') # Solche Auslassungen kommen in Watt oft vor.
text.append('Sie gingen auseinander.')
text.append(('&nbsp;' * 32) + '?')

####  ALLES NACH STDOUT AUSGEBEN

leere_seite = '\\thispagestyle{empty}\n\n\\newpage\n\n&nbsp;\n\n'
schmutztitel = ('&nbsp;\n\n&nbsp;\n\n&nbsp;\n\n# Megawatt\n\n' + (leere_seite * 2))
titel = ('&nbsp;\n\n&nbsp;\n\n&nbsp;\n\n# Nick Montfort\n\n' +
         '## Megawatt\n' +
         '\n&nbsp;\n&nbsp;\n&nbsp;\n\n_Ein deterministisch-computergenerierter Roman,_  \n' + 
         '_Passagen aus Samuel Becketts *Watt* erweiternd_\n' +
         '\n\n' +
         '_Übersetzt von Hannes Bajohr auf Grundlage_ \n' + 
         '_der deutschen Erstübersetzung von Elmar Tophoven\n_' +
         '\n&nbsp;\n&nbsp;\n&nbsp;\n' +
         '&nbsp;\n\n&nbsp;\n\n&nbsp;\n' + 
         '__0x0a__\n' +
         (leere_seite * 2))
vorwort = '# Vorwort\n\n' + __doc__ + (leere_seite * 2)
print(schmutztitel + titel + vorwort)
print('\\setcounter{page}{1}\n\n' + '\n\n'.join(text))
this_file = open('megawatt.py')
print('\n\\newpage\n\n')
print('# Addenda\n\n\n\\scriptsize\n\n')
print('    ' + '    '.join(list(this_file)))