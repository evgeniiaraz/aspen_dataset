## ASPEN Dataset

We present a dataset for plan-based cross-lingual story generation. 

To load the dataset for a certain language/plan, you can use `load_dataset.py` script.

You can use it as follows:

```
load_dataset.py:
    --lang:
        'prs' : Dari
        'bn' : Bengali
        'my' : Burmese
        'ca' : Catalan
        'rki' : Rakhine
        'ar'  : Arabic
        'ru' : Russian
        'hi' : Hindi
        'ht' : Haitian Creole
        'it' : Italian
        'el' : Greek, Modern
        'nb' : Norwegian Bokmål
        'pl' : Polish
        'adx' : Tibetan, Amdo
        'aeb' : Arabic, Tunisian
        'bo' : Tibetan
        'es' : Spanish
        'ja' : Japanese
        'nl' : Dutch
        'ur' : Urdu
        'gu' : Gujarati
        'ko' : Korean
        'ckb' : Central Kurdish
        'eo' : Esperanto
        'vi' : Vietnamese
        'fa' : Persian
        'ro' : Romanian
        'uk' : Ukrainian
        'tl' : Tagalog
        'hu' : Hungarian
        'yue' : Cantonese
        'pa' : Panjabi
        'ne' : Nepali
        'mfe' : Mauritian Creole
        'khg' : Khams Tibeta
        'da' : Danish
        'sv' : Swedish
        'tr' : Turkish
        'mnw' : Mon
        'tet' : Tetum (Timor)
        'ps' : Pushto
        'lt' : Lithuanian
        'de' : German 
        'zh' : Chinese
        'nn' : Norwegian Nynorsk
        'km' : Central Khmer

    --plan:
        first_sents : Story Completion
        only_entities : Entities
        summary : Plot Outline
        triangle_qa : Three-act Structure


```
