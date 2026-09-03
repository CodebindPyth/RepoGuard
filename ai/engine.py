from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

my_list2 = []
my_list1 = []

with open("dataset/example.csv") as file:
    read = file.readlines()
    for line in read[1:]:
        code, label = line.split(",")
        label = label.strip()
        my_list1.append(code)
        my_list2.append(label)
vectorizer.fit(my_list1)
x = vectorizer.transform(my_list1)
print(vectorizer.get_feature_names_out())
