
#!/usr/bin/env python
import numpy as np
def match_sequence(seq,dataset):
    """
    Return match sequence start,end positions in a dataset
    
    Parameters
    ----------
    seq : list
        sequence
    dataset : list
        dataset
    
    """
    N = len(seq)
    if N < 1:
        raise ValueError("Sequence is empty !")

    
    if isinstance(dataset,list):
        dataset=np.asarray(dataset)
    if isinstance(seq,list):
        seq=np.asarray(seq,dtype=dataset.dtype)
    print(seq,dataset)
    prefix_ind=np.where(dataset == seq[0])[0]
    results=[]
    for idx in prefix_ind:
        start,end=idx,idx+N
        if (dataset[start:end].tolist() == seq.tolist()):
            results.append([seq,start,end])
    return results

if __name__ == "__main__":
    import spacy
    from spacy.matcher import PhraseMatcher
    nlp = spacy.load("fr")

    def match_syntagm_text_spacy(syntagm,text,matcher):
        return matcher(nlp(text))

    def match_syntagm_text_text_blob(syntagm,text):
        from textblob import TextBlob
        from textblob_fr import PatternTagger, PatternAnalyzer
        blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        return match_sequence(syntagm,list(blob.tokenize()))
    text= """Quel sera le sort des centaines d’anciens djihadistes européens partis combattre en Syrie au cours des dernières années ? Alors que l’organisation Etat islamique (EI) perd de plus en plus de terrain, le président américain, Donald Trump, a exhorté, dimanche 17 février, les Européens à rapatrier leurs ressortissants, retenus en Syrie après avoir rallié le groupe islamiste. « Il n’y a pas d’alternative, car nous serions forcés de les libérer », a mis en garde le président américain, s’adressant particulièrement à la Grande-Bretagne, la France, et l’Allemagne.\nDes représentants des autorités du nord-est de la Syrie qui détiennent ces djihadistes étrangers ont, pour leur part, nuancé la portée des déclarations du président des Etats-Unis. « Nous ne les relâcherons pas. Jamais nous ne pourrions faire cela », a affirmé le coresponsable des relations internationales dans la région, M. Abdulkarim Omar. Ce dernier a toutefois averti les gouvernements européens que ces djihadistes constituaient des « bombes à retardement ». Il a exhorté leurs pays d’origine à assumer leurs responsabilités, soulignant des risques d’évasion à la faveur d’une éventuelle attaque de la Turquie sur le territoire, rendue possible par le retrait américain. Il a aussi précisé que les forces locales détenaient 800 hommes étrangers et retenaient 700 femmes et 1 500 enfants dans des camps de déplacés.\nLundi 18 février, les gouvernements européens qui avaient déjà engagé des discussions avec Washington au sujet du sort de leurs ressortissants ont été contraints de réagir dans l’urgence aux déclarations de Donald Trump."""
    match_syntagm_text_spacy("Donald Trump",text,matcher)
    match_syntagm_text_text_blob("Donald Trump".split(),text)