from __future__ import print_function

import json
import sys
import codecs

filename = sys.argv[1]
with codecs.open(filename=filename, encoding='utf-8') as infile:
    json = json.load(infile)
    with codecs.open('recipes.txt', 'w', encoding='utf-8') as outfile:
        for recipe in json:
            try:
                outfile.write(recipe['title'].lower())
                outfile.write(u' <eos> ')
                outfile.write(u'Ingredients <eos> ')
                for ingredient in recipe['ingredients']:
                    ingredient = ingredient.replace('.', ' .')
                    ingredient = ingredient.replace(',', ' ,')
                    ingredient = ingredient.replace(':', ' :')
                    ingredient = ingredient.replace('(', '( ')
                    ingredient = ingredient.replace(')', ' )')
                    ingredient = ingredient.replace(';', ' ;')
                    outfile.write(ingredient.lower())
                    outfile.write(u' <eos> ')
                outfile.write(u'Directions <eos> ')
                for direction in recipe['directions']:
                    direction = direction.replace('.', ' .')
                    direction = direction.replace(',', ' ,')
                    direction = direction.replace(':', ' :')
                    direction = direction.replace('(', '( ')
                    direction = direction.replace(')', ' )')
                    direction = direction.replace(';', ' ;')
                    outfile.write(direction.lower())
                    outfile.write(u' <eos> ')
                outfile.write(u'Categories <eos> ')
                for category in recipe['categories']:
                    outfile.write(category.lower())
                    outfile.write(u' <eos> ')
            except KeyError:
                pass
            outfile.write("\n")
