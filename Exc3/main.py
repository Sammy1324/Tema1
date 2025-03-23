from Common_words import Words

text1 = ["hello", "world", "hello", "python"]
text2 = ["hello", "goodbye", "apple", "world"]

def main():
    words1 = Words(text1)
    words2 = Words(text2)
    common = words1.common_words(words2)
    print(common)

if __name__ == "__main__":
    main()