#IPRB
def dominant_allele_probability(k, m, n):
    total_population = k + m + n
    AAAA = (k / total_population) * ((k - 1) / (total_population - 1))
    AAAa = (k / total_population) * (m / (total_population - 1)) + (m / total_population) * (k / (total_population - 1))
    AAaa = (k / total_population) * (n / (total_population - 1)) + (n / total_population) * (k / (total_population - 1))
    AaAa = (m / total_population) * ((m - 1) / (total_population - 1)) * 0.75
    Aaaa = (m / total_population) * (n / (total_population - 1)) * 0.5 + (n / total_population) * (m / (total_population - 1)) * 0.5

    # no dominant phenotype for aa x aa
    aaaa = 0

    dominant_probability = AAAA + AAAa + AAaa + AaAa + Aaaa + aaaa
    return dominant_probability

print(dominant_allele_probability(18,28,29))
