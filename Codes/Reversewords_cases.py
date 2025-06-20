"Program to Reverse Words and Swap Cases"

def reverse_words_swap_case(sentence):
    words = sentence.split()
    result = []

    for word in words:
        reversed_word = word[::-1]
        swapped_case_word = reversed_word.swapcase()
        result.append(swapped_case_word)

    return " ".join(result)

# Example usage
sentence = input("Enter a sentence: ")
print("Modified sentence:", reverse_words_swap_case(sentence))