from translation import DNATranslator


# creates translator instance
tran = DNATranslator()

# defines sequences
target_sequence = 'AAAaatttgccggc********CCgCgaTTTatac087/vdsjc;osakjc;97gcgcg'
mrna_sequence = tran.translate_dna_sequence(target_sequence)

# prints count of valid bases
print(f'mRNA [No. Valid Bases {len(tran.get_valid_bases(mrna_sequence))}]')