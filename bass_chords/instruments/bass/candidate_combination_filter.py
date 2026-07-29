class CandidateCombinationFilter:

    def filter(self, combinations):

        return tuple(
            combination
            for combination in combinations
        )