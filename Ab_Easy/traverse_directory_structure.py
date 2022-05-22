
RED = "\u001b[31m"
GREEN = "\u001b[32m"
END = "\u001b[0m"
# Write a program that traverses directory structure.

directory = {"fold_a": ["fold_b", "fold_c", "fold_d", "file_a"],
             "fold_b": ["file_c", "file_d", "file_e"],
             "fold_c": ["fold_d", "fold_e", "file_f"],
             "fold_d": ["file_i"],
             "fold_e": ["file_p", "file_q"]}


def traverse(fold, indent=""):
    color = RED if fold in directory else GREEN
    print(color + indent + fold + END)
    if fold not in directory:
        return
    for f in directory[fold]:
        traverse(f, indent + '\t')


traverse("fold_a")
