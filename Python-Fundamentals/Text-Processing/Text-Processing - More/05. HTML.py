title = input()
print("<h1>")
print(f"    {title}")
print("</h1>")
article = input()
print("<article>")
print(f"    {article}")
print("</article>")

text = input()

while text != "end of comments":

    print("<div>")
    print(f"    {text}")
    print("</div>")

    text = input()