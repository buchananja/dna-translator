class DNATranslator:
    '''a class that translates dna into mrna'''

    def translate_dna_sequence(sequence):
        '''a function that translates dna into mrna using a dictionary'''

        mrna_sequence = str()
        dna_to_mrna = {'a': 'u', 't': 'a', 'g': 'c', 'c': 'g'}
        for base in sequence:
            if base.lower() in dna_to_mrna.keys():
                mrna_sequence += dna_to_mrna[base.lower()]
            else:
                mrna_sequence += '#'
        return mrna_sequence

    def get_valid_bases(sequence):
        '''a function that returns a list of valid bases in a sequence'''

        valid_bases = list()
        for base in sequence:
            if base.lower() in 'augc':
                valid_bases.append(base)
        return valid_bases