from datasets import load_dataset

ds = load_dataset("wldnjs057/diary_entry")
print(ds['test']['diary_entry'][:5])

for line in ds['test']['diary_entry']:
    print(f"\n{line}")