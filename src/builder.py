ListErrors=(400,401,402,403,404,405,500,502,503,504,505,526)

for i in ListErrors:
    with open("template.html", "r") as f:
        t = f.read()

    t = t.replace("{$TITLE$}", "Error " + str(i))
    t = t.replace("{$ERROR$}", "" + str(i))

    with open("../builded/"+str(i)+".html","w") as f:
        f.write(t)

print("Done!")