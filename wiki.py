import wikipedia #install wikipedia module first using "pip install wikipedia"
page_content = wikipedia.page(input("Enter a page you want to search on wikipedia: ")).content
print(page_content)