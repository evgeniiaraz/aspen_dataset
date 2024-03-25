import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument('--lang', type=str, default="it", help = "Language code")
parser.add_argument('--plan', type=str, default="summary", help = "Plan type. Options: [summary, only_entitities, first_sents, coarse_qa, triangle_qa]")
args = parser.parse_args()

plan = args.plan
lang = args.lang

df_dataset = pd.read_excel("aspen_dataset.xlsx")
df_subset = df_dataset[["story_id", plan, lang]]
df_nonempty = df_subset.loc[df_subset[lang]!="--"]
df.to_excel("output_dataset.xlsx")
