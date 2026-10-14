ontology={
    "Animal":["Dog","Cat"],
    "Dog":["Labrador"],
    "Cat":["Persian"]
}
relationships=[
    ("Dog","is_a","Animal"),
    ("Cat","is_a","Animal"),
    ("Labrador","is_a","Dog"),
    ("Persian","is_a","Cat")
]

for cls,subclasses in ontology.items():
    print(cls,":",subclasses)
for a,relation,b in relationships:
    print(a,relation,b)


"""
Classes: Animal, Dog, Cat
Subclasses: Labrador, Persian
Relationships: is_a
"""