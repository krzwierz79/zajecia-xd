# .title() is naive
# titlecase seems better but not perfect
# (considering in-company style guide variety) it's good enough

# pip instal titlecase (https://pypi.org/project/titlecase/)
from titlecase import titlecase
punct = "it's an auth'ring 'aight-mare: a f**ked-up s**tstorm!"
titled = punct.title()
print(titled)  # It'S An Auth'Ring 'Aight-Mare: A F**Ked-Up S**Tstorm!
titlecased = titlecase(punct)
print(titlecased)  # It's an Auth'ring 'Aight-Mare: A F**ked-Up S**tstorm!
# better: It's an Auth'ring 'Aight-Mare: A F**ked-up S**tstorm!
